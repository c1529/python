import requests
import test
import json
import time

headers = {
    'Referer':
        'https://www.pixiv.net/ranking.php',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
        'Safari/537.36'
}


def main(page):
    url = f'https://www.pixiv.net/ranking.php?p={page}&format=json'
    response = requests.get(url=url, headers=headers)
    result = json.loads(response.text)['contents']
    for i in result:
        time.sleep(0.8)
        illust_id = i['illust_id']
        test.main(illust_id)
