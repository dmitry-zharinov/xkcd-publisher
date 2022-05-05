from tokenize import group
from dotenv import load_dotenv
import requests
import os
from pathlib import Path

load_dotenv()
TOKEN = os.environ['VK_ACCESS_TOKEN']
CLIENT_ID = os.environ['VK_CLIENT_ID']
API_VERSION = '5.131'

def get_vk_upload_url(group_id):
    """Получить адрес для загрузки фото"""
    params = {
        'access_token': TOKEN,
        'v': API_VERSION,
        'group_id': group_id
    }
    response = requests.get(
        'https://api.vk.com/method/photos.getWallUploadServer',
        params=params
    )
    response.raise_for_status()
    return response.json()['response']['upload_url']
    
def upload_photo(group_id, filepath, filename):
    """Загрузить фото на сервер"""
    url = get_vk_upload_url(group_id)
    photo_path = Path(filepath) / filename
    files = {
        'photo': (filename, open(photo_path, 'rb'))
    }
    response_post = requests.post(url, files=files)
    response_post.raise_for_status()
    
    photo_upload = response_post.json()
    params = {
        'access_token': TOKEN,
        'v': API_VERSION,
        'group_id': group_id,
        'photo': photo_upload['photo'],
        'server': photo_upload['server'],
        'hash': photo_upload['hash'],
    }
    response = requests.get(
        'https://api.vk.com/method/photos.saveWallPhoto',
        params=params
    )
    response.raise_for_status()

    return response.json()['response']


def wall_post(group_id, photo, message):
    photo = photo[0]
    photo = 'photo'+ '-' + str(photo['owner_id']) + '_' + str(photo['id'])
    params = {
        'access_token': TOKEN,
        'v': API_VERSION,
        'attachments': photo,
        'message': message,
        'owner_id': '-' + group_id,
        'from_group': '1'
    }
    response = requests.get(
        'https://api.vk.com/method/wall.post',
        params=params
    )
    response.raise_for_status()

# test = publish_to_vk_group('213092935')
# print(test)