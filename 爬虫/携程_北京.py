import time

import requests
import re
from threading import Thread
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 Edg/113.0.1774.42'
}

o_url = 'https://vacations.ctrip.com/list/whole/sc6.html?startcity=6&sv=%E5%8C%97%E4%BA%AC&st=%E5%8C%97%E4%BA%AC&p='


def get_url(o_page):
    return o_url + str(o_page)


# for page in range(0, 101):
#     a = get_url(page)
#     print(a)

# 获取id

object1 = re.compile(r'data-track-product-id="(?P<pp_iid>.*?)" data-track-is-recommend', re.S)


# 获取每个详情


def get_uurl(pp_id):
    return 'https://vacations.ctrip.com/travel/detail/p' + str(pp_id) + '/?city=6'


# a = get_url(2)
#
# res = requests.get(a)
#
# res = res.text
#
# b = object1.finditer(res)
#
# for i in b:
#     c = i.group('pp_id')
#     print(get_uurl(c))

object2 = re.compile(r'id="js_DetailHeader"><div class="detail_summary"><h1>(?P<name>.*?)'
                     r'<div style="display:inline-block"><div'
                     r'.*?<dfn>¥</dfn><em>(?P<price>.*?)</em>/人起</span><div style="'
                     r'.*?class="score_inf"><span>(?P<people>.*?)<!-- -->人出游'
                     r'.*?卖点</dt><dd class="pm_rec"><ul><li>(?P<maidian>.*?)'
                     r'</li></ul></dd></dl></div>')


def ppint(num_1, num_2):
    for i in range(num_1, num_2 + 1):
        time.sleep(1)
        u1 = get_url(i)
        response = requests.get(url=u1, headers=headers).text
        id_list = object1.finditer(response)
        for j in id_list:
            iid = j.group('pp_iid')
            u2 = get_uurl(iid)
            txt1 = requests.get(url=u2, headers=headers).text
            c = object2.finditer(txt1)
            for c1 in c:
                print(c1.group('name'))
                print(c1.group('price'))
                print(c1.group('people') + '人')
                print(c1.group('maidian'))


tt1 = Thread(target=ppint, args=(1, 10))
tt2 = Thread(target=ppint, args=(11, 20))
tt3 = Thread(target=ppint, args=(21, 30))
tt4 = Thread(target=ppint, args=(31, 40))
tt5 = Thread(target=ppint, args=(41, 50))
tt6 = Thread(target=ppint, args=(51, 60))
tt7 = Thread(target=ppint, args=(61, 70))
tt8 = Thread(target=ppint, args=(71, 80))
tt9 = Thread(target=ppint, args=(81, 90))
tt10 = Thread(target=ppint, args=(91, 100))

tt1.start()
tt2.start()
tt3.start()
tt4.start()
tt5.start()
tt6.start()
tt7.start()
tt8.start()
tt9.start()
tt10.start()

