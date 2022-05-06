import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def download_image(url, filename):
    """Скачать картинку"""
    response = requests.get(url)
    response.raise_for_status()
    with open(Path(filename), 'wb') as file:
        file.write(response.content)


def get_extension_from_url(url):
    """Получить расширение файла"""
    url_split = urlsplit(url)
    return os.path.splitext(unquote(url_split.path))[1]
