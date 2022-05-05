import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def download_image(url, filename, payload):
    """Скачать картинку"""
    response = requests.get(url, payload)
    response.raise_for_status()
    with open(Path(filename), 'wb') as file:
        file.write(response.content)


def get_extension_from_url(url):
    """Получить расширение файла"""
    url_split = urlsplit(url)
    return os.path.splitext(unquote(url_split.path))[1]


def remove_image(filename):
    file_to_remove = Path(filename)
    file_to_remove.unlink()
