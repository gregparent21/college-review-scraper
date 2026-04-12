# Populate School Geolocation Data

This script uses the **Google Places API** to populate the `city`, `state`, `latitude`, and `longitude` columns in your schools database.

## Setup

### 1. Get a Google Places API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Places API** (and optionally the **Maps JavaScript API** for reference)
4. Create an API key in the Credentials section
5. Set up billing (required for Google Places API usage)

> **Note:** The Places API has a free tier with monthly credits. Typical queries cost $0.017-$0.0175 per request.

### 2. Set Environment Variable

Set your API key as an environment variable before running the script:

```bash
export GOOGLE_PLACES_API_KEY="your-api-key-here"
```

Or on Windows (PowerShell):

```powershell
$env:GOOGLE_PLACES_API_KEY="your-api-key-here"
```

## Usage

### Basic Usage

```bash
python populate_geolocation.py
```

This will:

- Search for all schools in your database that don't already have location data
- Skip schools that already have city/state/latitude/longitude populated
- Update the database with found location information

## Testing on a Subset

Before running on your entire database, test on a few schools first to verify the results:

```bash
# Test on just 5 schools with dry-run (shows results without updating)
python populate_geolocation.py --limit 5 --dry-run

# Test on 10 schools and actually update (good safeguard)
python populate_geolocation.py --limit 10

# Test with highest-priority schools, then expand
python populate_geolocation.py --limit 20 --dry-run
```

This approach lets you:

- Verify the API results look correct before full run
- Estimate API costs ($0.017 per query × number of schools)
- Catch any issues with database schema or API key early

### Command Line Options

```bash
# Use a specific database
python populate_geolocation.py --db path/to/database.sqlite

# Provide API key directly (instead of using env var)
python populate_geolocation.py --api-key "your-api-key"

# Dry run: see what would be updated without modifying database
python populate_geolocation.py --dry-run

# Force update all schools, even if they already have location data
python populate_geolocation.py --all

# Process only N schools (great for testing)
python populate_geolocation.py --limit 10

# Combine options
python populate_geolocation.py --db niche_reviews.sqlite --dry-run --all --limit 25
```

## What the Script Does

1. **Connects to the database** and retrieves schools that need geolocation data
2. **Searches Google Places API** for each school using the school name
3. **Parses the address** to extract city and state
4. **Extracts coordinates** (latitude/longitude) from the API response
5. **Updates the database** with the geolocation information
6. **Logs all operations** with detailed status information

## Example Output

```
2025-04-12 10:30:45,123 - INFO - Using database: niche_reviews.sqlite
2025-04-12 10:30:45,124 - INFO - Dry run: False
2025-04-12 10:30:45,125 - INFO - Skip existing: True
2025-04-12 10:30:45,126 - INFO - Found 150 schools to process
2025-04-12 10:30:46,345 - INFO - [1/150] Processing: Harvard University
2025-04-12 10:30:47,567 - INFO -   Found: Cambridge, MA (42.3601, -71.1089)
2025-04-12 10:30:47,891 - INFO - [2/150] Processing: Yale University
2025-04-12 10:30:49,012 - INFO -   Found: New Haven, CT (41.3083, -72.9279)
...
```

## Tips

- **Start with a dry run** (`--dry-run`) to verify results before updating
- **Run incrementally** on a subset first to test before processing all schools
- **Rate limiting** is built in (0.5s delay between requests) to avoid API throttling
- **Monitor your API usage** in Google Cloud Console to control costs

## Troubleshooting

### "GOOGLE_PLACES_API_KEY environment variable not set"

- Use `export GOOGLE_PLACES_API_KEY="..."` (bash) or `$env:GOOGLE_PLACES_API_KEY="..."` (PowerShell)
- Or pass it directly: `python populate_geolocation.py --api-key "your-key"`

### "Invalid API key" or 403 errors

- Verify your API key is correct
- Ensure Places API is enabled in Google Cloud Console
- Check that billing is set up for your project

### "No results found" for some schools

- Check the school name in your database
- Try with full location information (school name + city) by modifying the search query
- Some smaller schools may not have Places API results

## Database Requirements

Your database must already have these columns in the `schools` table:

- `city` (TEXT)
- `state` (TEXT)
- `latitude` (REAL)
- `longitude` (REAL)

If you haven't added these columns yet, run:

```sql
ALTER TABLE schools ADD COLUMN city TEXT;
ALTER TABLE schools ADD COLUMN state TEXT;
ALTER TABLE schools ADD COLUMN latitude REAL;
ALTER TABLE schools ADD COLUMN longitude REAL;
```
