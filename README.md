## College Review Scraper

Python scraper for review-based college profile data from Niche, with both JSON and SQLite outputs and support for resuming long runs.

### Requirements

- Python 3.9+
- `pip install -r requirements.txt`

### Files

- `scrape_niche.py` – scrapes schools into a single JSON file (supports multiple school lists).
- `scrape_niche_sqlite.py` – scrapes schools into a SQLite database (supports multiple school lists).
- `school_list.py` – primary list of ~436 schools to scrape.
- `liberal_arts_colleges_list.py` – list of ~201 U.S. News National Liberal Arts Colleges.
- `niche_ivy_reviews.json` – example JSON output (optional, can be regenerated).
- `requirements.txt` – Python dependencies.

### Available School Lists

Two school lists are available, and you can easily add more:

1. **`schools`** (default) – ~436 schools from `school_list.py`
2. **`liberal-arts`** – ~201 U.S. News National Liberal Arts Colleges from `liberal_arts_colleges_list.py`

Each list file exports a `get_school_list()` function that returns a list of `{"name": "...", "url": "..."}` entries.

### Working with Different School Lists

All scraping commands support the `--school-list` parameter to choose which list to use:

```bash
# Default (primary schools list)
python scrape_niche.py
python scrape_niche_sqlite.py --mode seed-schools --db niche_reviews.sqlite

# Liberal arts colleges
python scrape_niche.py --school-list liberal-arts
python scrape_niche_sqlite.py --mode seed-schools --db liberal_arts.sqlite --school-list liberal-arts
```

#### Creating New School Lists

To add a new school list:

1. Create a new Python file (e.g., `my_schools_list.py`)
2. Define a `get_school_list()` function that returns a list of `{"name": "...", "url": "..."}` dicts
3. Import it in `scrape_niche.py` and add a wrapper function (e.g., `build_my_schools_list()`)
4. Update `scrape_niche_sqlite.py`'s `get_school_list_for_mode()` function to handle the new list
5. Add a choice to the `--school-list` argument in both scripts

#### Recommended Database Strategy

Keep separate databases for different school lists to avoid mixing data:

```bash
# Original schools list
python scrape_niche_sqlite.py --mode seed-schools --db niche_reviews.sqlite

# Liberal arts colleges
python scrape_niche_sqlite.py --mode seed-schools --db liberal_arts.sqlite --school-list liberal-arts
```

### School list (where to add schools)

The seed list of schools lives in `scrape_niche.py` inside `build_school_list()`:

- Each entry has:
  - `name`: human-readable school name
  - `url`: Niche college URL, e.g. `https://www.niche.com/colleges/princeton-university/`
- `scrape_niche_sqlite.py` reuses this same list when seeding the SQLite DB.

To add more schools:

1. Open `scrape_niche.py`.
2. Edit `build_school_list()` and append new `{"name": "...", "url": "..."}` entries.
3. Re-run the seed / scraper commands below.

### JSON scraper usage

From the project root:

```bash
python scrape_niche.py
```

This will:

- Loop over all schools in `build_school_list()`.
- Fetch each school’s main page and reviews page.
- Extract:
  - `school_name`, `school_url`
  - AI “What Students Say” summary (if present)
  - Total review count and star rating breakdown (1–5)
  - Up to 15 most recent reviews, with text, rating, date, reviewer_type
- Write an array of school objects to `niche_ivy_reviews.json`.

Options:

- Change number of recent reviews per school:

```bash
python scrape_niche.py --limit 20
```

- Change output file:

```bash
python scrape_niche.py --output my_schools.json
```

### SQLite scraper workflow (recommended for many schools)

The SQLite-based workflow separates **school seeding** from **review scraping** so you can resume easily.

#### 1. Seed the `schools` table (no network)

This only populates/updates the `schools` table; it does **not** fetch reviews:

```bash
python scrape_niche_sqlite.py --mode seed-schools --db niche_reviews.sqlite
```

This uses `build_school_list()` as the source of schools. After editing that function, re-run this command to add more schools.

#### 2. Backfill reviews for schools missing them (resumable)

This scans `schools` and scrapes reviews only for schools that currently have **no rows in `reviews`**:

```bash
python scrape_niche_sqlite.py --mode backfill-reviews --db niche_reviews.sqlite --limit 15
```

Notes:

- Safe to run multiple times; schools with existing reviews will be skipped.
- You can process in batches to avoid very long runs:

```bash
python scrape_niche_sqlite.py --mode backfill-reviews --db niche_reviews.sqlite --limit 15 --batch-size 25
```

#### 3. Export from SQLite back to JSON

At any time, you can export the current DB contents to a JSON file with the same overall schema as `scrape_niche.py`:

```bash
python scrape_niche_sqlite.py --db niche_reviews.sqlite --export-json niche_ivy_reviews.json
```

### Offline HTML parsing (for debugging selectors)

If you save a Niche reviews HTML page (e.g., `Princeton University Reviews - Niche.html`), you can run:

```bash
python scrape_niche.py --parse-reviews-html "Princeton University Reviews - Niche.html" --limit 15
```

This prints a JSON object with:

- `total_review_count`
- `rating_breakdown`
- `reviews` (list of recent reviews with metadata)

Useful when network access is restricted or to fine‑tune selectors.

### Notes and caveats

- The scraper uses polite request headers and a small delay between requests, but you should still avoid hammering Niche.
- HTML structure can change; most selectors are isolated in helper functions so you can adjust them in one place if needed.
- For large school lists, prefer the SQLite workflow to avoid re‑scraping everything from scratch on each run.
