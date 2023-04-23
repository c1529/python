import requests
import re
import csv
import threading
from threading import Thread

url = 'https://vacations.ctrip.com/list/whole/sc2.html?st=%E6%B8%A9%E6%B3%89&startcity=2&sv=%E6%B8%A9%E6%B3%89&p='

cookies = {
    'cookie': 'GUID=09031172318583808785; MKT_CKID=1682229026870.ig7r4.lj9i; MKT_CKID_LMT=1682229026870; '
              '_RF1=2408%3A8431%3A1f00%3A3264%3A4987%3Ad0e5%3A7d70%3Ac39f; _RSG=5K4CNlxmb74nQa6DaszHe9; '
              '_RDG=282ea5766e23f52f200a6d17de14fd8896; _RGUID=41e5c3bb-d730-4505-9a11-f7690d1a46b1; MKT_Pagesource=PC; '
              '_bfaStatusPVSend=1; SearchHistoryWord=%u6240%u6709%u6E29%u6CC9%u65C5%u6E38%u7EBF%u8DEF%23--%20%23%3D'
              '%3Dhttp%3A//vacations.ctrip.com/whole-2B126/%3FsearchValue%3D%25E6%25B8%25A9%25E6%25B3%2589%26searchText'
              '%3D%25E6%25B8%25A9%25E6%25B3%2589%26from%3Ddo; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; '
              'nfes_isSupportWebP=1; StartCity_Pkg=PkgStartCity=2; '
              'Union=OUID=index.robots.txt&AllianceID=4897&SID=155952&SourceID=&createtime=1682232547&Expires'
              '=1682837346971; MKT_OrderClick=ASID=4897155952&AID=4897&CSID=155952&OUID=index.robots.txt&CT=1682232546972'
              '&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex.robots.txt&VAL={}; '
              '_jzqco=%7C%7C%7C%7C1682229027141%7C1.1159160578.1682229026866.1682232534669.1682232546991.1682232534669'
              '.1682232546991.undefined.0.0.9.9; __zpspc=9.3.1682232534.1682232546.2%232%7Cwww.baidu.com%7C%7C%7C%25E6'
              '%2590%25BA%25E7%25A8%258B%7C%23; '
              'ABTESTTRACE'
              '=42C1AF6C83753C4B0741608D0771DAD1AD62431EC1154AA4E40F8066984B5EEAE5FED4D9630E93BA550CA866E3563FE7; '
              '_bfa=1.1682229026454.3tw0ma.1.1682229026454.1682229026454.1.39.1; _bfs=1.39; '
              '_ubtstatus=%7B%22vid%22%3A%221682229026454.3tw0ma%22%2C%22sid%22%3A1%2C%22pvid%22%3A39%2C%22pid%22%3A0%7D; '
              '_bfi=p1%3D104317%26p2%3D104317%26v1%3D39%26v2%3D38; _bfaStatus=success'
}


def geturl(url, page):
    gurl = url + page
    return gurl


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

# print(res.text)

obj = re.compile(r'p class="list_product_title" title="(?P<name>.*?)"><span>', re.S)


# for page in range(1, 10):
#     page = str(page)
#     url1 = geturl(url, page)
#     res = requests.get(url=url1, headers=headers)
#     text = obj.finditer(res.text)
#     for i in text:
#         print(i.group('name'))


# 创建任务
def aa(a, b):
    for page in range(a, b):
        page = str(page)
        url1 = geturl(url, page)
        res = requests.get(url=url1, headers=headers, cookies=cookies)
        text = obj.finditer(res.text)
        # print(res.status_code)
        for i in text:
            print(i.group('name'))


# 创建多线程
t1 = Thread(target=aa, args=(1, 11))
t2 = Thread(target=aa, args=(11, 21))
t3 = Thread(target=aa, args=(21, 31))
t4 = Thread(target=aa, args=(31, 41))
t5 = Thread(target=aa, args=(41, 51))
t6 = Thread(target=aa, args=(51, 61))
t7 = Thread(target=aa, args=(61, 71))
t8 = Thread(target=aa, args=(71, 81))
t9 = Thread(target=aa, args=(81, 91))
t10 = Thread(target=aa, args=(91, 101))

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
