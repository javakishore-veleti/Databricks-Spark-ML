# import urllib3
import shutil
import os
import logging
import requests

def download_url_file(file_url: str, local_file_name_with_path: str):
    print(f"Enter [file_url: {file_url}] [local_file_name_with_path: {local_file_name_with_path}]")
    logging.debug(f"Enter [file_url: {file_url}] [local_file_name_with_path: {local_file_name_with_path}]")

    if not os.path.exists(local_file_name_with_path):
        logging.debug(f"Downloading the file {file_url}")
        # http = urllib3.PoolManager()

        with open(local_file_name_with_path, 'wb') as out:
            r = requests.get(file_url, allow_redirects=True)
            out.write(r.content)
            # r = http.request('GET', file_url, preload_content=False)
            # shutil.copyfileobj(r, out)

    logging.debug(f"Exit")
    return
