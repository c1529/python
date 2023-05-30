# 新的爬取，跟之前相比，添加了一次字符串切割

import requests
import re
from threading import Thread

o_url = 'https://pic.netbian.com/4kmeinv/index_'

st = 'https://pic.netbian.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

object1 = re.compile(r'<li><a href="(?P<url>.*?)" target="_blank"><img src="/upload', re.S)


def get_url(page):
    return o_url + str(page) + '.html'


def get_img(url_img):
    res_img = requests.get(url=url_img, headers=headers)
    res_img.encoding = 'gbk'
    img_url = re.findall(r'<img src="(.*?)" data-pic=', res_img.text)[0]
    img_url = st + img_url
    img = requests.get(url=img_url, headers=headers)
    img.encoding = 'gbk'
    return img.content


def get_f(e, b, k):
    for page in range(e, b + 1):
        url = get_url(page)
        res_uurl = requests.get(url=url, headers=headers)
        res_uurl = re.split(r'<ul class="clearfix">', res_uurl.text)[-1]
        a = object1.finditer(res_uurl)
        x = 0
        for j in a:
            x = x + 1
            z = st + j.group('url')
            img = get_img(z)
            xx = k + str(x) + str(page)
            with open(f'./美女/{xx}.jpg', mode='wb') as f:
                f.write(img)


# 创建线程

t1 = Thread(target=get_f, args=(1, 10, 'a'))
t2 = Thread(target=get_f, args=(11, 20, 'b'))
t3 = Thread(target=get_f, args=(21, 30, 'c'))
t4 = Thread(target=get_f, args=(31, 40, 'd'))
t5 = Thread(target=get_f, args=(41, 50, 'e'))
t6 = Thread(target=get_f, args=(51, 60, 'f'))
t7 = Thread(target=get_f, args=(61, 68, 'g'))

# 启动线程
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
