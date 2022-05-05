from pathlib import Path

import requests

from utils import download_image, get_extension_from_url
from publish_vk import upload_photo, wall_post
IMG_FOLDER_NAME = 'images'




def main():

    Path(IMG_FOLDER_NAME).mkdir(parents=True, exist_ok=True)

    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    xkcd = response.json()
    
    message = xkcd['alt']
    img_url = xkcd['img']
    filename = f'xkcd{get_extension_from_url(img_url)}'
    download_image(img_url,
                   filename,
                   IMG_FOLDER_NAME,
                   '')

    VK_GROUP_ID = '213092935'
    photo = upload_photo(VK_GROUP_ID, IMG_FOLDER_NAME, filename)
    print(photo)
    wall_post(VK_GROUP_ID, photo, message)
    
    
if __name__ == '__main__':
    main()
