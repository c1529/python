import requests
import re
import test1
from concurrent.futures import ThreadPoolExecutor

aa = 'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1685974983930&loginType=3&uuid=122270672.284582141.1683972867.1685962697.1685972224.13&productId='

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

start_url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&wq=%E7%AC%94%E8%AE%B0' \
            '%E6%9C%AC%E7%94%B5%E8%84%91&pvid=fc06b54e75404cc89893dde6b48dc293&page='

object1 = re.compile(r'gl-i-wrap.*?href="//item.jd.com/(?P<id>.*?).html', re.S)


def get_url1(page):
    return start_url + str(page) + '3&s=56&click=0'


cc = '&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='


def get_url(p_url):
    res = requests.get(url=p_url, headers=headers).text
    result = object1.finditer(res)
    for i in result:
        s_id = i.group('id')
        x_url = aa + str(s_id) + '&score=0&sortType=5&page='
        for m in range(1, 100):
            x_url = x_url + str(m) + '&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='
            response = requests.get(url=x_url, headers=headers).text
            test1.parse_html(response)


def main(num):
    get_url(get_url1(num))


with ThreadPoolExecutor(max_workers=8) as k1,\
        ThreadPoolExecutor(max_workers=8) as k2:
    for j in range(21, 30):
        k1.submit(main, 2*j-1)
    for jj in range(31, 40):
        k2.submit(main, jj*2-1)
