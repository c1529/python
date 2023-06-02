import requests
import re
from concurrent.futures import ThreadPoolExecutor

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

object1 = re.compile(r'<div class="main"><div align="center"><a href="(?P<url>.*?)" title="(?P<name>.*?)"', re.S)


def get_start_url(page):
    return 'http://blog.getchu.com/?p=' + str(page)


def save_img(img_url, img_name):
    with open(f"D://动漫图片/" + img_name + ".jpg", mode="wb") as f:
        f.write(img_url)


def get_img(url):
    response = requests.get(url=url, headers=headers)
    result = response.text
    re_list = object1.finditer(result)
    for i in re_list:
        c = requests.get(url=i.group('url'), headers=headers).content
        save_img(c, i.group('name'))


def main(page):
    start_url = get_start_url(page)
    get_img(start_url)
    print(f"已经爬取完第{page}页")


with ThreadPoolExecutor(max_workers=10) as executor:
    # 提交任务给线程池执行
    for j in range(0, 1425):
        executor.submit(main, j)
