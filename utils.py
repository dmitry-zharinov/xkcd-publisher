import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests



def download_image(url, filename, img_folder, payload):
    response = requests.get(url, payload)
    response.raise_for_status()
    with open(Path(img_folder) / filename, 'wb') as file:
        file.write(response.content)

        
def get_extension_from_url(url):
    url_split = urlsplit(url)
    return os.path.splitext(unquote(url_split.path))[1]
