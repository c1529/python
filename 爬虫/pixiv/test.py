import requests
import re
import json

headers = {
    'Referer':
        'https://www.pixiv.net/',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
        'Safari/537.36'
}


def save_img(url_img):
    name = re.split('/', url_img)[-1]
    with open(f'图片/{name}', 'wb') as f:
        img = requests.get(url=url_img, headers=headers).content
        f.write(img)
    print(name+'已经保存完毕')


def main(illust_id):
    p_url = f'https://www.pixiv.net/ajax/illust/{illust_id}/pages?lang=zh&version=d7bfbb7567158dd28a7a3fbb8345607fdf33d327'
    response = requests.get(url=p_url, headers=headers)
    result = json.loads(response.text)
    result = result['body']
    for i in result:
        url = i['urls']['original']
        save_img(url)
