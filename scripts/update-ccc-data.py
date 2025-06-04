import logging
import datetime as dt
import os
import re
import requests
import hashlib
import tempfile

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

base_dir = os.path.dirname(os.path.dirname(__file__))
public_dir = os.path.join(base_dir, 'public')

# see https://doi.org/10.7910/DVN/RI9JFU
FILE_ID = '11584216'
DOWNLOAD_URL = f"https://dataverse.harvard.edu/api/access/datafile/{FILE_ID}"

def download_file(url: str, local_path: str) -> None:
    """Download a file from a given URL and save it to a local path."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        logger.info(f"  Fetched from dataverse to {local_path}")
    else:
        raise Exception(f"  Failed to download file from {url}. Status code: {response.status_code}")


def update_json(new_filename: str, py_file_path: str) -> str:
    # update the JSON file that feeds the interactive to point at the newly named file (hack)
    # return the filename to delete from public
    last_filename = None
    with open(py_file_path, 'r') as file:
        content = file.readlines()
    for i, line in enumerate(content):
        if 'export const CCC_URL =' in line:
            match = re.search(r'export const CCC_URL = "([^"]+)"', line)
            last_filename = match.group(1) if match and (match.group(1) != new_filename) else None
            content[i] = f'export const CCC_URL = "{new_filename}";\n'
            break
    with open(py_file_path, 'w') as file:
        file.writelines(content)
    logger.debug(f"  Successfully updated {py_file_path} with new filename: {new_filename}")
    return last_filename


def current_ccc_file_path() -> str:
    files = [f for f in os.listdir(public_dir) if f.startswith('ccc-') and f.endswith('.csv')]
    ccc_data_filepath = os.path.join(public_dir, files[0])
    return ccc_data_filepath
    
def hash_of_file(path: str) -> str:
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


if __name__ == "__main__":
    try:
        
        # get hash of current file to check if we need to update
        current_file = current_ccc_file_path()
        current_hash = hash_of_file(current_file)
        logger.info(f"Current data: ")
        logger.info(f"  {current_file}")
        logger.info(f"  -> {current_hash}")
        
        # grab latest data from dataverse to a temp file
        logger.info("New data:")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
            tmp_csv_path = tmp_file.name
        download_file(DOWNLOAD_URL, tmp_csv_path)
        # convert to a CSV file from a TSV file
        with open(tmp_csv_path, 'r', encoding='utf-8') as tsv_file:
            with open(tmp_csv_path.replace('.csv', '.tmp.csv'), 'w', encoding='utf-8') as csv_file:
                for line in tsv_file:
                    csv_file.write(line.replace('\t', ','))
        os.remove(tmp_csv_path)  # remove the original TSV file
        tmp_csv_path = tmp_csv_path.replace('.csv', '.tmp.csv')
        new_hash = hash_of_file(tmp_csv_path)
        logger.info(f"  -> {new_hash}")
        
        # if hashes differ then delete current file, name new one, return status
        new_data = current_hash != new_hash
        new_filename = f"ccc-{dt.datetime.now().strftime('%Y-%m-%d')}.csv"

        if new_data:
            # save new data to public dir
            logger.info(f"  copying to: {new_filename}")
            os.rename(tmp_csv_path, os.path.join(public_dir, new_filename))
            # update the JSON to point at this new file (kind of a hack)
            json_filename = 'data.js'
            last_filename = update_json(new_filename,
                                        os.path.join(base_dir, 'src', 'lib', 'util', json_filename))
            logger.info(f"  Updated {json_filename} to point to {new_filename}")
            # delete the old file from public
            os.remove(current_file)
        else:
            logger.info("  Data is up to date, no changes made.")

        exit(0)  # even if data not updated that isn't an error
    except Exception as e:
        logger.error(f"Error: {e}")
        exit(1)
