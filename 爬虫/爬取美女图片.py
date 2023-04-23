import requests
import re
import threading
from threading import Thread

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

ua = 'https://pic.netbian.com/4kmeinv/index_'


def geturl(k):
    uu = ua + str(k) + '.html'
    return uu


# def fun(start, end, k):
#     url = geturl(k)
#     res = requests.get(url=url, headers=headers)
#     res.encoding = 'gbk'
#     text = res.text
#     obj = re.compile(r'<img src="(?P<url_img>.*?)" alt', re.S)
#     s = 'https://pic.netbian.com'
#     a = obj.finditer(text)
#     for i in a:
#         name = s + i.group('url_img')
#         response = requests.get(name)
#         with open(f"./美女/{name}.jpg", mode="wb") as f:
#             f.write(response.content)


def fun(start, end, k):
    for num in range(start, end + 1):
        url = geturl(num)
        res = requests.get(url=url, headers=headers)
        res.encoding = 'gbk'
        text = res.text
        obj = re.compile(r'<img src="(?P<url_img>.*?)" alt', re.S)
        s = 'https://pic.netbian.com'
        a = obj.finditer(text)
        x = 0
        for i in a:
            x = x + 1
            name = s + i.group('url_img')
            response = requests.get(name)
            xx = k + str(x)+str(num)
            with open(f"./美女/{xx}.jpg", mode="wb") as f:
                f.write(response.content)


# 创建线程
t1 = Thread(target=fun, args=(1, 6, 'aaa'))
t2 = Thread(target=fun, args=(7, 12, 'bbb'))
t3 = Thread(target=fun, args=(13, 20, 'ccc'))
t4 = Thread(target=fun, args=(21, 28, 'ddd'))
t5 = Thread(target=fun, args=(29, 36, 'eee'))
t6 = Thread(target=fun, args=(37, 42, 'fff'))
t7 = Thread(target=fun, args=(43, 50, 'ggg'))
t8 = Thread(target=fun, args=(51, 56, 'hhh'))
t9 = Thread(target=fun, args=(57, 61, 'iii'))
t10 = Thread(target=fun, args=(62, 66, 'kkk'))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
