import requests

API_VERSION = '5.131'


def get_upload_url(token, group_id):
    """Получить адрес для загрузки фото"""
    params = {
        'access_token': token,
        'v': API_VERSION,
        'group_id': group_id
    }
    response = requests.get(
        'https://api.vk.com/method/photos.getWallUploadServer',
        params=params
    )
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_photo(token, group_id, filename):
    """Загрузить фото на сервер"""
    url = get_upload_url(token, group_id)
    files = {
        'photo': (filename, open(filename, 'rb'))
    }
    response_post = requests.post(url, files=files)
    response_post.raise_for_status()

    photo_upload = response_post.json()
    params = {
        'access_token': token,
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


def wall_post(token, group_id, photo, message):
    photo = photo[0]
    photo_id = f'photo{photo["owner_id"]}_{photo["id"]}'
    params = {
        'access_token': token,
        'v': API_VERSION,
        'attachments': photo_id,
        'message': message,
        'owner_id': f'-{group_id}',
        'from_group': '1'
    }
    response = requests.get(
        'https://api.vk.com/method/wall.post',
        params=params
    )
    response.raise_for_status()
