import logging
import datetime as dt
import os
import csv
from dotenv import load_dotenv
import requests
from typing import List, Dict

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

ACLED_READ_URL = "https://api.acleddata.com/acled/read"

us_protest_filters: Dict[str, int | str] = {
    'limit': 10,
    'event_date': f'2025-01-01|{dt.datetime.now().strftime("%Y-%m-%d")}',
    'event_date_where': 'BETWEEN',
    'event_type': 'Protests',
    'region': 18,  # Region ID for the North America
    'country': 'United States'
}

def likely_update_date() -> str:
    # the ACLED documentation says data is updated every monday, so find latest monday (including today)
    today = dt.datetime.now()
    days_since_monday = today.weekday()
    if days_since_monday == 0:
        most_recent_monday = today
    else:
        most_recent_monday = today - dt.timedelta(days=days_since_monday)
    return most_recent_monday.strftime('%Y-%m-%d')

def update_json(new_filename: str, py_file_path: str) -> None:
    # update the JSON file that feeds the interactive to point at the newly named file (hack)
    with open(py_file_path, 'r') as file:
        content = file.readlines()
    found = False
    for i, line in enumerate(content):
        if 'export const ACLED_URL =' in line:
            content[i] = f'export const ACLED_URL = "{new_filename}";\n'
            found = True
            break
    with open(py_file_path, 'w') as file:
        file.writelines(content)
    logger.debug(f"Successfully updated {py_file_path} with new filename: {new_filename}")

def fetch_results(page=1) -> List[Dict]:
    # fetch a page of results from ACLED API
    params = us_protest_filters.copy()
    params['key'] = os.getenv('ACLED_API_KEY')
    params['email'] = os.getenv('ACLED_EMAIL')
    params['page'] = page
    #logger.info(f"{ACLED_READ_URL}?{requests.compat.urlencode(params)}")
    return requests.get(ACLED_READ_URL, params=params).json()

def get_latest_data() -> List[Dict]:
    # grab all the data from ACLED
    logger.info("Updating ACLED data...")
    page = 1
    data = []
    while True:
        results = fetch_results(page) 
        logger.info(f"  page {page}: {len(results['data'])}")
        if results['count'] == 0:
            break
        data.extend(results['data'])
        page += 1
    #print(json.dumps(results, indent=4))
    logger.info(f"Fetched {results['count']} results.")
    return data

if __name__ == "__main__":
    load_dotenv()  # take environment variables
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    # fetch the latest data from ACLED
    data = get_latest_data()
    csv_filename = f'acled-{likely_update_date()}.csv'
    csv_filepath = os.path.join(base_dir, 'public', csv_filename)
    
    # save the latest data to a CSV file
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    logger.info(f"Saved data to {csv_filename}")

    # now update the JSON to point at this new file (kind of a hack)
    json_filename = 'data.js'
    update_json(csv_filename, os.path.join(base_dir, 'src', 'lib', 'util', json_filename))
    logger.info(f"Updated {json_filename} to point to {csv_filename}")
