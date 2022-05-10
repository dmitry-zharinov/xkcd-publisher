import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from utils import download_image, get_extension_from_url
from vk import upload_photo, wall_post
from xkcd import fetch_random_comic

IMG_FOLDER_NAME = 'images'


def main():
    load_dotenv()
    token = os.environ['VK_ACCESS_TOKEN']

    try:
        xkcd = fetch_random_comic()
        message = xkcd['alt']
        img_url = xkcd['img']
        filename = f'xkcd{get_extension_from_url(img_url)}'
        download_image(img_url, filename)

        group_id = os.environ['VK_GROUP_ID']
        photo = upload_photo(token, group_id, filename)
        wall_post(token, group_id, photo, message)

    except requests.HTTPError as err:
        print(f'Ошибка {err}')
    finally:
        Path(filename).unlink()


if __name__ == '__main__':
    main()
