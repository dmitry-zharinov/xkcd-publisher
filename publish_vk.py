from tokenize import group
from dotenv import load_dotenv
import requests
import os

load_dotenv()
TOKEN = os.environ['VK_ACCESS_TOKEN']
CLIENT_ID = os.environ['VK_CLIENT_ID']
API_VERSION = '5.131'

def get_vk_upload_server(group_id):
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
    return response.json()
    
def publish_to_vk_group():
    pass


test = get_vk_upload_server('213092935')
print(test)