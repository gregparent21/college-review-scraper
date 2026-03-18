import argparse
import json
import logging
import sqlite3
import time
from contextlib import contextmanager
from dataclasses import asdict
from typing import Any, Dict, Iterable, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup

# Reuse the HTML fetching + parsing logic from the JSON scraper.
from scrape_niche import (  # type: ignore
    BASE_HEADERS,
    REQUEST_DELAY_SECONDS,
    SchoolData,
    Review,
    build_school_list,
    extract_ai_summary,
    extract_rating_breakdown_from_reviews_page,
    extract_recent_reviews,
    extract_total_review_count_from_reviews_page,
    fetch_html,
    parse_school_page,
)


SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS schools (
  id INTEGER PRIMARY KEY,
  school_name TEXT NOT NULL,
  school_url TEXT NOT NULL UNIQUE,
  ai_summary TEXT,
  total_review_count INTEGER,
  rating_breakdown_json TEXT,
  last_scraped_at TEXT
);

CREATE TABLE IF NOT EXISTS reviews (
  id INTEGER PRIMARY KEY,
  school_id INTEGER NOT NULL,
  text TEXT NOT NULL,
  rating REAL,
  date TEXT,
  reviewer_type TEXT,
  scraped_at TEXT,
  FOREIGN KEY (school_id) REFERENCES schools(id) ON DELETE CASCADE
);

-- Prevent obvious duplicates across runs (same school + same content).
CREATE UNIQUE INDEX IF NOT EXISTS idx_reviews_dedupe
ON reviews (school_id, text, IFNULL(date, ''), IFNULL(reviewer_type, ''), IFNULL(rating, -1));
"""


@contextmanager
def sqlite_conn(db_path: str) -> Iterable[sqlite3.Connection]:
    conn = sqlite3.connect(db_path)
    try:
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_SQL)
    conn.commit()


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def upsert_school(
    conn: sqlite3.Connection,
    *,
    school_name: str,
    school_url: str,
    ai_summary: Optional[str],
    total_review_count: Optional[int],
    rating_breakdown: Dict[str, Optional[int]],
) -> int:
    rating_breakdown_json = json.dumps(rating_breakdown, ensure_ascii=False, sort_keys=True)
    conn.execute(
        """
        INSERT INTO schools (school_name, school_url, ai_summary, total_review_count, rating_breakdown_json, last_scraped_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(school_url) DO UPDATE SET
          school_name=excluded.school_name,
          ai_summary=excluded.ai_summary,
          total_review_count=excluded.total_review_count,
          rating_breakdown_json=excluded.rating_breakdown_json,
          last_scraped_at=excluded.last_scraped_at
        """,
        (school_name, school_url, ai_summary, total_review_count, rating_breakdown_json, now_iso()),
    )
    row = conn.execute("SELECT id FROM schools WHERE school_url = ?", (school_url,)).fetchone()
    if not row:
        raise RuntimeError("Failed to load school id after upsert")
    return int(row["id"])


def insert_reviews(conn: sqlite3.Connection, *, school_id: int, reviews: List[Review]) -> Tuple[int, int]:
    inserted = 0
    skipped = 0
    for r in reviews:
        try:
            conn.execute(
                """
                INSERT OR IGNORE INTO reviews (school_id, text, rating, date, reviewer_type, scraped_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (school_id, r.text, r.rating, r.date, r.reviewer_type, now_iso()),
            )
            if conn.total_changes > 0:
                inserted += 1
            else:
                skipped += 1
        except sqlite3.Error as exc:
            logging.warning("Failed inserting review for school_id=%s: %s", school_id, exc)
            skipped += 1
    return inserted, skipped


def scrape_school_to_sqlite(
    conn: sqlite3.Connection,
    session: requests.Session,
    *,
    school_name: str,
    school_url: str,
    review_limit: int = 15,
) -> Optional[SchoolData]:
    logging.info("Scraping %s", school_name)

    main_html = fetch_html(school_url, session=session)
    if not main_html:
        logging.error("Failed to fetch main page for %s", school_name)
        return None

    main_data = parse_school_page(main_html, school_url)

    reviews_url = main_data.get("reviews_url") or school_url.rstrip("/") + "/reviews/"
    reviews_html = fetch_html(reviews_url, session=session)
    reviews: List[Review] = []

    if reviews_html:
        reviews_soup = BeautifulSoup(reviews_html, "html.parser")
        reviews = extract_recent_reviews(reviews_soup, limit=review_limit)

        # Prefer reviews-page metadata when available.
        if not main_data.get("ai_summary"):
            main_data["ai_summary"] = extract_ai_summary(reviews_soup)

        total_from_reviews = extract_total_review_count_from_reviews_page(reviews_soup)
        if total_from_reviews is not None:
            main_data["total_review_count"] = total_from_reviews

        breakdown_from_reviews = extract_rating_breakdown_from_reviews_page(reviews_soup)
        if any(v is not None for v in breakdown_from_reviews.values()):
            main_data["rating_breakdown"] = breakdown_from_reviews
    else:
        logging.error("Failed to fetch reviews page for %s", school_name)

    school_id = upsert_school(
        conn,
        school_name=school_name,
        school_url=school_url,
        ai_summary=main_data.get("ai_summary"),
        total_review_count=main_data.get("total_review_count"),
        rating_breakdown=main_data.get("rating_breakdown") or {str(i): None for i in range(1, 6)},
    )
    inserted, skipped = insert_reviews(conn, school_id=school_id, reviews=reviews)
    conn.commit()
    logging.info("Saved %s: %d inserted, %d skipped reviews", school_name, inserted, skipped)

    return SchoolData(
        school_name=school_name,
        school_url=school_url,
        ai_summary=main_data.get("ai_summary"),
        total_review_count=main_data.get("total_review_count"),
        rating_breakdown=main_data.get("rating_breakdown") or {str(i): None for i in range(1, 6)},
        reviews=reviews,
    )


def seed_schools(conn: sqlite3.Connection, schools: List[Dict[str, str]]) -> None:
    """
    Populate or update the schools table without touching reviews.

    This lets you load hundreds of schools up-front (from build_school_list,
    a CSV, or some other source) and then backfill reviews separately.
    """
    for s in schools:
        conn.execute(
            """
            INSERT INTO schools (school_name, school_url, last_scraped_at)
            VALUES (?, ?, NULL)
            ON CONFLICT(school_url) DO UPDATE SET
              school_name=excluded.school_name
            """,
            (s["name"], s["url"]),
        )
    conn.commit()


def get_schools_missing_reviews(conn: sqlite3.Connection, *, limit: Optional[int] = None) -> List[sqlite3.Row]:
    """
    Return schools that currently have no reviews in the reviews table.
    """
    sql = """
        SELECT s.id, s.school_name, s.school_url
        FROM schools s
        LEFT JOIN reviews r ON r.school_id = s.id
        WHERE r.id IS NULL
        GROUP BY s.id
        ORDER BY s.id
    """
    if limit is not None:
        sql += " LIMIT ?"
        return list(conn.execute(sql, (limit,)))
    return list(conn.execute(sql))


def backfill_reviews(db_path: str, review_limit: int = 15, batch_size: Optional[int] = None) -> None:
    """
    Iterate over schools that don't yet have reviews and scrape them.

    Safe to re-run: schools with existing reviews will be skipped by default.
    """
    session = requests.Session()
    session.headers.update(BASE_HEADERS)

    with sqlite_conn(db_path) as conn:
        init_db(conn)

        while True:
            pending = get_schools_missing_reviews(conn, limit=batch_size)
            if not pending:
                logging.info("No schools without reviews remain.")
                break

            logging.info("Backfilling %d school(s) without reviews", len(pending))
            for row in pending:
                try:
                    scrape_school_to_sqlite(
                        conn,
                        session,
                        school_name=row["school_name"],
                        school_url=row["school_url"],
                        review_limit=review_limit,
                    )
                except Exception as exc:
                    logging.exception("Unexpected error while scraping %s: %s", row["school_name"], exc)


def export_schools_to_json(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    schools = conn.execute(
        "SELECT id, school_name, school_url, ai_summary, total_review_count, rating_breakdown_json FROM schools ORDER BY school_name"
    ).fetchall()
    out: List[Dict[str, Any]] = []
    for s in schools:
        school_id = int(s["id"])
        reviews_rows = conn.execute(
            """
            SELECT text, rating, date, reviewer_type
            FROM reviews
            WHERE school_id = ?
            ORDER BY COALESCE(date, '') DESC, id DESC
            """,
            (school_id,),
        ).fetchall()
        out.append(
            {
                "school_name": s["school_name"],
                "school_url": s["school_url"],
                "ai_summary": s["ai_summary"],
                "total_review_count": s["total_review_count"],
                "rating_breakdown": json.loads(s["rating_breakdown_json"]) if s["rating_breakdown_json"] else {str(i): None for i in range(1, 6)},
                "reviews": [
                    {
                        "text": r["text"],
                        "rating": r["rating"],
                        "date": r["date"],
                        "reviewer_type": r["reviewer_type"],
                    }
                    for r in reviews_rows
                ],
            }
        )
    return out


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    parser = argparse.ArgumentParser(description="Scrape Niche reviews into SQLite.")
    parser.add_argument("--db", default="niche_reviews.sqlite", help="SQLite database filepath.")
    parser.add_argument("--limit", type=int, default=15, help="Number of most recent reviews per school.")
    parser.add_argument(
        "--mode",
        choices=["seed-schools", "backfill-reviews"],
        default="backfill-reviews",
        help="Operation mode: seed only schools or backfill missing reviews.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=None,
        help="Max number of schools to backfill per run (for long lists).",
    )
    parser.add_argument(
        "--export-json",
        default=None,
        help="Export all schools+reviews from the DB to this JSON filepath.",
    )
    args = parser.parse_args()

    if args.export_json:
        with sqlite_conn(args.db) as conn:
            init_db(conn)
            payload = export_schools_to_json(conn)
        with open(args.export_json, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        logging.info("Exported %d schools to %s", len(payload), args.export_json)
    elif args.mode == "seed-schools":
        with sqlite_conn(args.db) as conn:
            init_db(conn)
            seed_schools(conn, build_school_list())
        logging.info("Seeded/updated %d schools", len(build_school_list()))
    else:  # backfill-reviews
        backfill_reviews(db_path=args.db, review_limit=args.limit, batch_size=args.batch_size)

