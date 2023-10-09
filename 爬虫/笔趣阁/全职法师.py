import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
        'Safari/537.36'
}


def get_main(url):
    response = requests.get(url=url, headers=headers).text

    soup = BeautifulSoup(response, 'html.parser')

    title = soup.find('span', attrs={'class': 'title'}).text

    article = soup.findAll('div', attrs={'id': 'chaptercontent'})

    for i in article:
        text = i.text
        if '请收藏本站' in text:
            text = text.replace('请收藏本站：https://www.bqg70.com。笔趣阁手机版：https://m.bqg70.com ', '')
        if '『点此报错』『加入书签』' in text:
            text = text.replace('『点此报错』『加入书签』', '')
        art_list = re.split('\s', text)
        with open(f'./全职法师/{title}.txt', 'w', encoding='utf-8-sig') as f:
            for j in art_list:
                f.writelines(j + '\n')


with ThreadPoolExecutor(max_workers=32) as k:
    for page in range(1,3233):
        url = 'https://www.bqg70.com/book/662/'+str(page)+'.html'
        try:
            k.submit(get_main, url)
            print(f'{page}章已经爬取完毕')
        except Exception as e:
            print(e)


