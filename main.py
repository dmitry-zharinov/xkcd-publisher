import os

from dotenv import load_dotenv

from utils import download_image, get_extension_from_url, remove_image
from vk import upload_photo, wall_post
from xkcd import fetch_random_comic

IMG_FOLDER_NAME = 'images'


def main():
    load_dotenv()

    # Path(IMG_FOLDER_NAME).mkdir(parents=True, exist_ok=True)

    xkcd = fetch_random_comic()

    message = xkcd['alt']
    img_url = xkcd['img']
    filename = f'xkcd{get_extension_from_url(img_url)}'
    download_image(img_url,
                   filename,
                   '')

    group_id = os.environ['VK_GROUP_ID']
    photo = upload_photo(group_id, filename)
    wall_post(group_id, photo, message)

    remove_image(filename)


if __name__ == '__main__':
    main()
