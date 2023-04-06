import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36'
}

for a in range(10):
    a = a * 25
    a = str(a)
    url = 'https://movie.douban.com/top250?start=' + a + '&filter='
    responses = requests.get(url=url, headers=headers)

    text = responses.text

    # 编写正则
    # re.S可以让正则中的.匹配到换行符
    obj1 = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                      r'<p class="">.*?导演: (?P<daoyan>.*?)&nbsp'
                      r'.*?主演: (?P<zhuyan>.*?)\s(.*?)<br>\n\s{28}(?P<year>.*?)&nbsp'
                      r';/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;'
                      r'(?P<leixing>.*?)\n'
                      r'.*?property="v:average">(?P<pingfen>.*?)</span>'
                      r'.*?<span>(?P<renshu>.*?)人评价</span>', re.S)

    a = obj1.finditer(text)
    for i in a:
        print(i.group('name'))
        print(i.group('daoyan'))
        print(i.group('zhuyan'))
        print(i.group('year'))
        print(i.group('country'))
        print(i.group('leixing'))
        print(i.group('pingfen'))
        print(i.group('renshu'))






