import random

import requests


def fetch_latest_comic():
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    return response.json()


def fetch_random_comic():
    num = fetch_latest_comic()['num']
    random_num = random.randint(1, num)

    response = requests.get(
        f'https://xkcd.com/{random_num}/info.0.json'
    )
    response.raise_for_status()
    return response.json()
    # https://xkcd.com/1/info.0.json (comic #614)
