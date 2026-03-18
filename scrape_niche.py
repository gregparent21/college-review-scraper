import argparse
import json
import logging
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from bs4 import BeautifulSoup, Tag

from school_list import get_school_list


BASE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

REQUEST_DELAY_SECONDS = 2.0


@dataclass
class Review:
    text: str
    rating: Optional[float]
    date: Optional[str]
    reviewer_type: Optional[str]


@dataclass
class SchoolData:
    school_name: str
    school_url: str
    ai_summary: Optional[str]
    total_review_count: Optional[int]
    rating_breakdown: Dict[str, Optional[int]]
    reviews: List[Review]


def fetch_html(url: str, *, session: Optional[requests.Session] = None) -> Optional[str]:
    """
    Fetch the raw HTML for a URL using requests.
    Returns HTML text or None if the request fails.
    """
    s = session or requests.Session()
    try:
        logging.info("Fetching %s", url)
        resp = s.get(url, headers=BASE_HEADERS, timeout=20)
        if resp.status_code != 200:
            logging.warning("Non-200 status for %s: %s", url, resp.status_code)
            return None
        return resp.text
    except requests.RequestException as exc:
        logging.error("Request error for %s: %s", url, exc)
        return None
    finally:
        # Be polite between requests
        time.sleep(REQUEST_DELAY_SECONDS)


def clean_text(text: str) -> str:
    """Normalize whitespace in extracted text."""
    return " ".join(text.split()).strip()


def parse_int_safe(value: str) -> Optional[int]:
    """Best-effort integer parsing that ignores commas and failures."""
    digits = "".join(ch for ch in value if ch.isdigit())
    if not digits:
        return None
    try:
        return int(digits)
    except ValueError:
        return None


def extract_ai_summary(soup: BeautifulSoup) -> Optional[str]:
    """
    Extract the 'What Students Say' AI summary block from the school page.

    This relies on a heading containing that exact phrase and then takes
    the following paragraph-like sibling's text.
    """
    heading = soup.find(["h2", "h3"], string=lambda t: t and "What Students Say" in t)
    if heading:
        # Look for the next sibling that has substantial text.
        current: Optional[Tag] = heading.find_next_sibling()
        while current is not None and isinstance(current, Tag):
            text = clean_text(current.get_text(" ", strip=True))
            if text:
                return text
            current = current.find_next_sibling()

    # Fallback: some pages only mark the summary with the summary-specific class.
    summary_span = soup.select_one("span.review__text--summary, span.review__text.review__text--summary")
    if summary_span:
        text = clean_text(summary_span.get_text(" ", strip=True))
        if text:
            return text

    logging.info("AI summary text not found")
    return None


def extract_total_review_count_and_distribution(
    soup: BeautifulSoup,
) -> (Optional[int], Dict[str, Optional[int]]):
    """
    Extract total number of reviews and a star rating distribution from the
    school page.

    The exact markup can change; this function is isolated so selectors can be
    updated easily if needed.
    """
    rating_breakdown: Dict[str, Optional[int]] = {str(i): None for i in range(1, 6)}
    total_reviews: Optional[int] = None

    # Heuristic: look for a heading with 'Reviews' plus a nearby count like '1,119 reviews'
    reviews_heading = soup.find(["h2", "h3"], string=lambda t: t and "Reviews" in t)
    if reviews_heading:
        count_tag = reviews_heading.find_next(string=lambda t: t and "review" in t.lower())
        if count_tag:
            total_reviews = parse_int_safe(str(count_tag))

    # Heuristic for star distribution: look for elements that contain patterns
    # like '5', '4', ..., and counts near them. If this fails, we keep None.
    # This is intentionally conservative to avoid brittle selectors.
    try:
        distribution_container = None
        for candidate in soup.find_all(["ul", "div"]):
            text = candidate.get_text(" ", strip=True)
            if all(str(i) in text for i in range(1, 6)) and "overall star rating" in text.lower():
                distribution_container = candidate
                break

        if distribution_container:
            # Very heuristic: extract sequences of digits from the container text;
            # then map from 5->1 stars in order.
            text = distribution_container.get_text(" ", strip=True)
            numbers: List[int] = []
            buf = ""
            for ch in text:
                if ch.isdigit():
                    buf += ch
                else:
                    if buf:
                        try:
                            numbers.append(int(buf))
                        except ValueError:
                            pass
                        buf = ""
            if buf:
                try:
                    numbers.append(int(buf))
                except ValueError:
                    pass

            # Best guess: the last count is the total review count; the 5 prior
            # are star buckets 5..1.
            if len(numbers) >= 6:
                bucket_counts = numbers[-6:-1]
                for idx, star in enumerate(range(5, 0, -1)):
                    rating_breakdown[str(star)] = bucket_counts[idx]
                if total_reviews is None:
                    total_reviews = numbers[-1]
    except Exception as exc:
        logging.info("Failed to parse rating breakdown heuristically: %s", exc)

    return total_reviews, rating_breakdown


def find_reviews_page_url(soup: BeautifulSoup, base_url: str) -> str:
    """
    Locate the reviews page URL from the school page.
    Falls back to a convention-based '/reviews/' URL if a direct link isn't found.
    """
    link = soup.find("a", string=lambda t: t and "Read More Reviews" in t)
    if link and link.has_attr("href"):
        href = link["href"]
        if href.startswith("http"):
            return href
        # Niche tends to use absolute paths.
        if href.startswith("/"):
            return f"https://www.niche.com{href}"

    # Fallback convention: append 'reviews/' if not already present.
    if base_url.rstrip("/").endswith("/reviews"):
        return base_url
    return base_url.rstrip("/") + "/reviews/"


def extract_review_card_data(card: Tag) -> Optional[Review]:
    """
    Extract a single review's data from a card element on the reviews page.

    Niche review cards include schema.org-style microdata. We prefer those
    attributes (e.g., itemprop="reviewBody") because they're typically more
    stable than generated class names.
    """
    if not isinstance(card, Tag):
        return None

    # Cards often contain a nested element with schema.org Review.
    review_root = card.find(attrs={"data-testid": "review"}) or card

    # Review body (main text).
    body = review_root.find(attrs={"itemprop": "reviewBody"})
    if not body:
        return None
    review_text_raw = body.get_text("\n", strip=True)
    review_text_lines = [clean_text(ln) for ln in review_text_raw.splitlines() if clean_text(ln)]
    review_text = "\n".join(review_text_lines).strip()
    if not review_text:
        return None

    # Rating value (schema.org Rating).
    rating: Optional[float] = None
    rating_container = review_root.find(attrs={"itemprop": "reviewRating"})
    if rating_container:
        rating_meta = rating_container.find("meta", attrs={"itemprop": "ratingValue"})
        if rating_meta and rating_meta.has_attr("content"):
            try:
                rating = float(str(rating_meta["content"]).strip())
            except ValueError:
                rating = None

    # Tagline: reviewer type + date (ISO and/or relative label).
    reviewer_type: Optional[str] = None
    date: Optional[str] = None
    tagline = review_root.find("ul", attrs={"data-testid": "review-tagline"})
    if tagline:
        author_name = tagline.find(attrs={"itemprop": "name"})
        if author_name:
            reviewer_type = clean_text(author_name.get_text(" ", strip=True)) or None

        date_meta = tagline.find("meta", attrs={"itemprop": "datePublished"})
        if date_meta and date_meta.has_attr("content"):
            date = str(date_meta["content"]).strip() or None
        else:
            # Fall back to the visible relative date, e.g. "18 days ago"
            date_li = None
            for li in tagline.find_all("li"):
                txt = clean_text(li.get_text(" ", strip=True))
                if "ago" in txt.lower():
                    date_li = txt
                    break
            date = date_li or None

    return Review(
        text=review_text,
        rating=rating,
        date=date,
        reviewer_type=reviewer_type,
    )


def extract_recent_reviews(soup: BeautifulSoup, limit: int = 15) -> List[Review]:
    """
    Extract up to `limit` most recent reviews from the reviews page soup.

    The function assumes the page is already sorted by recency, as Niche
    typically shows, and simply walks the card elements in order.
    """
    reviews: List[Review] = []

    # Prefer stable containers found in the provided Niche HTML:
    # - div.review-card[aria-label="review"] (card wrapper)
    # - elements with data-testid="review" (schema.org Review root)
    card_candidates: List[Tag] = soup.select('div.review-card[aria-label="review"]')
    if not card_candidates:
        card_candidates = [t for t in soup.find_all(attrs={"data-testid": "review"}) if isinstance(t, Tag)]

    for card in card_candidates:
        if len(reviews) >= limit:
            break
        review = extract_review_card_data(card)
        if review:
            reviews.append(review)

    # Deduplicate by text while preserving order.
    seen_texts = set()
    unique_reviews: List[Review] = []
    for r in reviews:
        if r.text in seen_texts:
            continue
        seen_texts.add(r.text)
        unique_reviews.append(r)

    return unique_reviews[:limit]


def extract_total_review_count_from_reviews_page(soup: BeautifulSoup) -> Optional[int]:
    """
    Extract total review count from the reviews page.

    Two reliable-ish sources:
    - meta property="og:description" like "Read 494 reviews for ..."
    - visible text like "512 reviews"
    """
    og = soup.find("meta", attrs={"property": "og:description"})
    if og and og.has_attr("content"):
        count = parse_int_safe(str(og["content"]))
        if count is not None:
            return count

    for txt in soup.find_all(string=True):
        s = clean_text(str(txt))
        if s.lower().endswith("reviews") and any(ch.isdigit() for ch in s):
            count = parse_int_safe(s)
            if count is not None:
                return count

    return None


def extract_rating_breakdown_from_reviews_page(soup: BeautifulSoup) -> Dict[str, Optional[int]]:
    """
    Extract the visible 1-5 star distribution from the reviews page, if present.

    In the provided HTML this appears under:
    - ul.review__chart
      - span.review__chart__item__label: star number
      - span.review__chart__item__label--total: count
    """
    breakdown: Dict[str, Optional[int]] = {str(i): None for i in range(1, 6)}
    chart = soup.select_one("ul.review__chart")
    if not chart:
        return breakdown

    for item in chart.select("li.review__chart__item"):
        star_span = item.select_one("span.review__chart__item__label")
        total_span = item.select_one("span.review__chart__item__label--total")
        if not star_span or not total_span:
            continue
        star = clean_text(star_span.get_text(" ", strip=True))
        total = parse_int_safe(total_span.get_text(" ", strip=True))
        if star in breakdown:
            breakdown[star] = total

    return breakdown


def parse_school_page(html: str, base_url: str) -> Dict[str, Any]:
    """
    Parse the main school page HTML for AI summary, review counts,
    rating distribution, and a link to the reviews page.
    """
    soup = BeautifulSoup(html, "html.parser")

    ai_summary = extract_ai_summary(soup)
    total_reviews, rating_breakdown = extract_total_review_count_and_distribution(soup)
    reviews_url = find_reviews_page_url(soup, base_url)

    return {
        "ai_summary": ai_summary,
        "total_review_count": total_reviews,
        "rating_breakdown": rating_breakdown,
        "reviews_url": reviews_url,
    }


def parse_reviews_page(html: str, limit: int = 15) -> List[Review]:
    """
    Parse the reviews page HTML and return up to `limit` recent reviews.
    """
    soup = BeautifulSoup(html, "html.parser")
    return extract_recent_reviews(soup, limit=limit)


def save_results(data: List[SchoolData], filepath: str) -> None:
    """
    Save a list of SchoolData objects as JSON.
    """
    serializable: List[Dict[str, Any]] = []
    for school in data:
        serializable.append(
            {
                "school_name": school.school_name,
                "school_url": school.school_url,
                "ai_summary": school.ai_summary,
                "total_review_count": school.total_review_count,
                "rating_breakdown": school.rating_breakdown,
                "reviews": [asdict(r) for r in school.reviews],
            }
        )

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)


def build_school_list() -> List[Dict[str, str]]:
    """
    Wrapper around the shared school list in `school_list.py`.

    Edit `get_school_list()` in `school_list.py` to change which
    schools are scraped.
    """
    return get_school_list()


def scrape_school(session: requests.Session, name: str, url: str, review_limit: int = 15) -> Optional[SchoolData]:
    """
    Scrape a single school's main page and reviews page.
    """
    logging.info("Scraping %s", name)

    main_html = fetch_html(url, session=session)
    if not main_html:
        logging.error("Failed to fetch main page for %s", name)
        return None

    main_data = parse_school_page(main_html, url)

    reviews_url = main_data.get("reviews_url") or url
    reviews_html = fetch_html(reviews_url, session=session)
    if not reviews_html:
        logging.error("Failed to fetch reviews page for %s", name)
        reviews: List[Review] = []
    else:
        reviews_soup = BeautifulSoup(reviews_html, "html.parser")
        reviews = extract_recent_reviews(reviews_soup, limit=review_limit)

        # Reviews page tends to have the most consistent review-specific metadata.
        if not main_data.get("ai_summary"):
            main_data["ai_summary"] = extract_ai_summary(reviews_soup)

        total_from_reviews = extract_total_review_count_from_reviews_page(reviews_soup)
        if total_from_reviews is not None:
            main_data["total_review_count"] = total_from_reviews

        breakdown_from_reviews = extract_rating_breakdown_from_reviews_page(reviews_soup)
        if any(v is not None for v in breakdown_from_reviews.values()):
            main_data["rating_breakdown"] = breakdown_from_reviews

    school_data = SchoolData(
        school_name=name,
        school_url=url,
        ai_summary=main_data.get("ai_summary"),
        total_review_count=main_data.get("total_review_count"),
        rating_breakdown=main_data.get("rating_breakdown") or {str(i): None for i in range(1, 6)},
        reviews=reviews,
    )

    return school_data


def run_scraper(output_path: str = "niche_ivy_reviews.json", review_limit: int = 15) -> None:
    """
    Main scraper runner for all 8 Ivy League schools.
    """
    session = requests.Session()
    results: List[SchoolData] = []

    for school in build_school_list():
        name = school["name"]
        url = school["url"]
        try:
            school_data = scrape_school(session, name, url, review_limit=review_limit)
            if school_data is None:
                logging.warning("Skipping %s due to previous errors", name)
                continue
            results.append(school_data)
        except Exception as exc:
            logging.exception("Unexpected error while scraping %s: %s", name, exc)

    if not results:
        logging.error("No school data scraped; not writing output file.")
        return

    save_results(results, output_path)
    logging.info("Saved results for %d schools to %s", len(results), output_path)


def parse_reviews_html_file(input_path: str, *, limit: int = 15) -> Dict[str, Any]:
    """
    Utility for parsing a saved Niche reviews HTML file (offline).
    Useful for verifying selectors when network access is restricted.
    """
    html = Path(input_path).read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    return {
        "total_review_count": extract_total_review_count_from_reviews_page(soup),
        "rating_breakdown": extract_rating_breakdown_from_reviews_page(soup),
        "reviews": [asdict(r) for r in extract_recent_reviews(soup, limit=limit)],
    }


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    parser = argparse.ArgumentParser(description="Scrape Niche Ivy League college reviews.")
    parser.add_argument("--output", default="niche_ivy_reviews.json", help="Output JSON filepath.")
    parser.add_argument("--limit", type=int, default=15, help="Number of most recent reviews per school.")
    parser.add_argument(
        "--parse-reviews-html",
        dest="parse_reviews_html",
        default=None,
        help="Parse a saved Niche reviews HTML file offline and print JSON to stdout.",
    )
    args = parser.parse_args()

    if args.parse_reviews_html:
        print(json.dumps(parse_reviews_html_file(args.parse_reviews_html, limit=args.limit), ensure_ascii=False, indent=2))
    else:
        run_scraper(output_path=args.output, review_limit=args.limit)

