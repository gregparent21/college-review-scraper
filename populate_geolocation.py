import argparse
import logging
import os
import sqlite3
import time
from contextlib import contextmanager
from typing import Iterable, Optional, Tuple

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# API Configuration
GOOGLE_PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
REQUEST_DELAY_SECONDS = 0.5  # Be respectful to API


@contextmanager
def sqlite_conn(db_path: str) -> Iterable[sqlite3.Connection]:
    """Context manager for SQLite database connections."""
    conn = sqlite3.connect(db_path)
    try:
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()


def get_api_key() -> str:
    """Get Google Places API key from environment variable."""
    api_key = os.environ.get("GOOGLE_PLACES_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_PLACES_API_KEY environment variable not set. "
            "Please set it before running this script."
        )
    return api_key


def search_school_location(school_name: str, api_key: str) -> Optional[dict]:
    """
    Search for a school's location using Google Places API.
    
    Returns: dict with keys 'city', 'state', 'latitude', 'longitude' or None if not found
    """
    time.sleep(REQUEST_DELAY_SECONDS)  # Rate limiting
    
    try:
        params = {
            "query": f"{school_name} college university",
            "key": api_key,
            "type": "university"
        }
        
        response = requests.get(GOOGLE_PLACES_API_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("status") != "OK" or not data.get("results"):
            logger.warning(f"No results found for {school_name}")
            return None
        
        # Use the first result
        result = data["results"][0]
        location = result.get("geometry", {}).get("location", {})
        formatted_address = result.get("formatted_address", "")
        
        # Parse address components to extract city and state
        address_components = parse_address(formatted_address)
        
        return {
            "city": address_components.get("city", ""),
            "state": address_components.get("state", ""),
            "latitude": location.get("lat"),
            "longitude": location.get("lng")
        }
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error for {school_name}: {e}")
        return None
    except Exception as e:
        logger.error(f"Error searching location for {school_name}: {e}")
        return None


def parse_address(formatted_address: str) -> dict:
    """
    Parse formatted address to extract city and state.
    Handles US addresses in the format: Street, City, State ZIP
    """
    parts = [p.strip() for p in formatted_address.split(",")]
    
    city = ""
    state = ""
    
    if len(parts) >= 3:
        # Typically: [Street, City, State ZIP]
        city = parts[-2]
        
        # State and ZIP are often together, extract state (2 letters)
        last_part = parts[-1].strip()
        state_zip_parts = last_part.split()
        if len(state_zip_parts) >= 1:
            # Usually the first part is the 2-letter state code
            state = state_zip_parts[0]
    elif len(parts) >= 2:
        city = parts[-2]
        state = parts[-1]
    
    return {"city": city, "state": state}


def update_school_location(
    conn: sqlite3.Connection,
    school_id: int,
    location_data: dict
) -> bool:
    """Update school location data in database."""
    try:
        conn.execute(
            """
            UPDATE schools
            SET city = ?, state = ?, latitude = ?, longitude = ?
            WHERE id = ?
            """,
            (
                location_data.get("city"),
                location_data.get("state"),
                location_data.get("latitude"),
                location_data.get("longitude"),
                school_id
            )
        )
        conn.commit()
        return True
    except Exception as e:
        logger.error(f"Error updating school {school_id}: {e}")
        return False


def populate_geolocation(
    db_path: str,
    api_key: str,
    dry_run: bool = False,
    skip_existing: bool = True,
    limit: Optional[int] = None
) -> None:
    """
    Populate city, state, latitude, longitude for all schools.
    
    Args:
        db_path: Path to SQLite database
        api_key: Google Places API key
        dry_run: If True, don't actually update database
        skip_existing: If True, skip schools that already have location data
        limit: If set, only process this many schools (useful for testing)
    """
    with sqlite_conn(db_path) as conn:
        # Get schools to process
        if skip_existing:
            query = """
                SELECT id, school_name
                FROM schools
                WHERE city IS NULL OR city = '' OR latitude IS NULL
                ORDER BY id
            """
        else:
            query = "SELECT id, school_name FROM schools ORDER BY id"
        
        if limit:
            query += f" LIMIT {limit}"
        
        cursor = conn.execute(query)
        schools = cursor.fetchall()
        
        logger.info(f"Found {len(schools)} schools to process")
        
        updated_count = 0
        for idx, school in enumerate(schools, 1):
            school_id = school["id"]
            school_name = school["school_name"]
            
            logger.info(f"[{idx}/{len(schools)}] Processing: {school_name}")
            
            location_data = search_school_location(school_name, api_key)
            
            if location_data:
                logger.info(
                    f"  Found: {location_data['city']}, {location_data['state']} "
                    f"({location_data['latitude']}, {location_data['longitude']})"
                )
                
                if not dry_run:
                    if update_school_location(conn, school_id, location_data):
                        updated_count += 1
                else:
                    updated_count += 1
            else:
                logger.warning(f"  No location found")
        
        logger.info(f"Successfully updated {updated_count}/{len(schools)} schools")


def main():
    parser = argparse.ArgumentParser(
        description="Populate school geolocation data using Google Places API"
    )
    parser.add_argument(
        "--db",
        default="niche_reviews.sqlite",
        help="Path to SQLite database (default: niche_reviews.sqlite)"
    )
    parser.add_argument(
        "--api-key",
        help="Google Places API key (uses GOOGLE_PLACES_API_KEY env var if not provided)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be updated without actually updating the database"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Update all schools, even if they already have location data"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Only process this many schools (useful for testing)"
    )
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or get_api_key()
    
    db_path = args.db
    if not os.path.exists(db_path):
        logger.error(f"Database not found: {db_path}")
        return
    
    logger.info(f"Using database: {db_path}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Skip existing: {not args.all}")
    if args.limit:
        logger.info(f"Limit: {args.limit} schools")
    
    populate_geolocation(
        db_path=db_path,
        api_key=api_key,
        dry_run=args.dry_run,
        skip_existing=not args.all,
        limit=args.limit
    )


if __name__ == "__main__":
    main()
