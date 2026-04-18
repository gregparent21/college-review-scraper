# Liberal Arts Colleges Scraping

This document explains how to scrape and manage data for the U.S. News National Liberal Arts Colleges using the parallel school list system.

## Quick Start

### Seed the liberal arts colleges database

```bash
python scrape_niche_sqlite.py --mode seed-schools --db liberal_arts.sqlite --school-list liberal-arts
```

This creates/updates a SQLite database with ~201 liberal arts colleges from `liberal_arts_colleges_list.py`.

### Backfill reviews

```bash
python scrape_niche_sqlite.py --mode backfill-reviews --db liberal_arts.sqlite --limit 15
```

### Backfill reviews in batches (recommended for large lists)

```bash
python scrape_niche_sqlite.py --mode backfill-reviews --db liberal_arts.sqlite --limit 15 --batch-size 25
```

### Add geolocation data

```bash
python populate_geolocation.py --db liberal_arts.sqlite --api-key YOUR_API_KEY
```

### Export to JSON

```bash
python scrape_niche_sqlite.py --export-json liberal_arts_reviews.json --db liberal_arts.sqlite
```

## Full Workflow Example

Complete workflow from schools list to JSON export:

```bash
# 1. Initialize the database with schools
python scrape_niche_sqlite.py --mode seed-schools --db liberal_arts.sqlite --school-list liberal-arts

# 2. Scrape reviews (in batches if needed)
python scrape_niche_sqlite.py --mode backfill-reviews --db liberal_arts.sqlite --limit 15 --batch-size 50

# 3. Add geolocation data (requires API key)
export GOOGLE_PLACES_API_KEY="your-key-here"
python populate_geolocation.py --db liberal_arts.sqlite

# 4. Export final results
python scrape_niche_sqlite.py --export-json liberal_arts_reviews.json --db liberal_arts.sqlite
```

## Database Schema

Both the original schools database and liberal arts database use the same schema:

### `schools` table

- `id` - Primary key
- `school_name` - Name of the school
- `school_url` - Niche URL
- `ai_summary` - AI-generated summary text
- `total_review_count` - Total number of reviews on Niche
- `rating_breakdown_json` - JSON with 1-5 star rating distribution
- `city` - City (added by `populate_geolocation.py`)
- `state` - State (added by `populate_geolocation.py`)
- `latitude` - Latitude coordinate
- `longitude` - Longitude coordinate
- `last_scraped_at` - Timestamp of last update

### `reviews` table

- `id` - Primary key
- `school_id` - Foreign key to `schools`
- `text` - Review text
- `rating` - Numeric rating (1-5)
- `date` - Review date
- `reviewer_type` - Type of reviewer (student, parent, etc.)
- `scraped_at` - When this review was scraped

## Recommended Setup

Keep separate databases for different school lists to avoid mixing data:

```bash
# Original school list database
niche_reviews.sqlite

# Liberal arts colleges database
liberal_arts.sqlite
```

This separation makes it easier to:

- Run different workflows independently
- Resume interrupted scrapes without affecting the other database
- Export separate JSON files for different analyses

## School List Source

The liberal arts colleges list comes from:

- **File**: `liberal_arts_colleges_list.py`
- **Source**: U.S. News & World Report National Liberal Arts Colleges rankings (2026 rankings)
- **Count**: ~201 schools

To modify which schools are included, edit `liberal_arts_colleges_list.py` and re-run the `seed-schools` command.

## Using Different School Lists in Parallel

You can work with multiple school lists simultaneously by using different database files and the `--school-list` parameter:

```bash
# Original schools
python scrape_niche_sqlite.py --db niche_reviews.sqlite --mode seed-schools

# Liberal arts colleges
python scrape_niche_sqlite.py --db liberal_arts.sqlite --mode seed-schools --school-list liberal-arts

# Both can now be scraped, geocoded, and exported independently
```

## Common Workflows

### Start from scratch with liberal arts colleges

```bash
rm liberal_arts.sqlite*  # Remove old database if exists
python scrape_niche_sqlite.py --db liberal_arts.sqlite --mode seed-schools --school-list liberal-arts
python scrape_niche_sqlite.py --db liberal_arts.sqlite --mode backfill-reviews --limit 20
```

### Update an existing liberal arts database with new schools

If you edited `liberal_arts_colleges_list.py`:

```bash
python scrape_niche_sqlite.py --db liberal_arts.sqlite --mode seed-schools --school-list liberal-arts
python scrape_niche_sqlite.py --db liberal_arts.sqlite --mode backfill-reviews --batch-size 25
```

### Skip already-reviewed schools

The backfill process automatically skips schools that already have reviews, so it's safe to re-run:

```bash
# This will only scrape schools without reviews
python scrape_niche_sqlite.py --db liberal_arts.sqlite --mode backfill-reviews --limit 15
```

### Dry run for geolocation

Preview what would be updated without making changes:

```bash
python populate_geolocation.py --db liberal_arts.sqlite --dry-run --limit 5
```

### Check database status

```bash
# Total schools
sqlite3 liberal_arts.sqlite "SELECT COUNT(*) FROM schools;"

# Schools with reviews
sqlite3 liberal_arts.sqlite "SELECT COUNT(DISTINCT school_id) FROM reviews;"

# Schools with geolocation data
sqlite3 liberal_arts.sqlite "SELECT COUNT(*) FROM schools WHERE city != '' AND latitude IS NOT NULL;"
```

## Extensibility

The system is designed to support additional school lists. To add a new school list:

1. Create a new file (e.g., `ivy_league_list.py`)
2. Implement a `get_school_list()` function
3. In `scrape_niche.py`, import and add a wrapper function
4. In `scrape_niche_sqlite.py`, update `get_school_list_for_mode()`
5. Add a choice to the `--school-list` argument in both scripts

See the existing implementations for reference.
