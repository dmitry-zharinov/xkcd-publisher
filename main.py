from pathlib import Path

import requests

from utils import download_image, get_extension_from_url

IMG_FOLDER_NAME = 'images'




def main():

    Path(IMG_FOLDER_NAME).mkdir(parents=True, exist_ok=True)

    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    xkcd = response.json()
    
    print(xkcd['alt'])
    img_url = xkcd['img']
    download_image(img_url,
                   f'xkcd{get_extension_from_url(img_url)}',
                   IMG_FOLDER_NAME,
                   '')

if __name__ == '__main__':
    main()
