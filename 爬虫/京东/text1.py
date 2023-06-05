import requests
import json
import time
import csv
from concurrent.futures import ThreadPoolExecutor

start_time = time.time()

# start_url = 'https://api.m.jd.com/?appid=item-v3&functionId=getQuestionAnswerList&client=pc&clientVersion=1.0.0&t' \
#       '=1685945981700&loginType=3&uuid=122270672.284582141.1683972867.1685934758.1685945052.6&page='+'&productId=1205289'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}


def get_url(page):
    return f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0' \
           f'&t=1685973020122&loginType=3&uuid=122270672.284582141.1683972867.1685962697.1685972224.13&productId' \
           f'=100021207879&score=0&sortType=5&page=' + str(page) + '&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='


def parse_html(response):
    txt = json.loads(response)
    result = txt['comments']
    for i in result:
        username = i['nickname']
        content = i['content']
        score = i['score']
        if score <= 3:
            feel = '差评'
        else:
            feel = '好评'
        print(username)
        print(content)
        print(feel)
        with open('评论.csv', 'a', encoding='utf-8-sig', newline='') as f1:
            write1 = csv.writer(f1)
            write1.writerow([username, content, feel])


def main_1(a):
    url = get_url(a)
    res = requests.get(url=url, headers=headers).text
    parse_html(res)
    time.sleep(1)


# head = ['用户名', '评论', '态度']
#
# with open('评论.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     write = csv.writer(f)
#     write.writerow(head)

def main():
    try:
        with ThreadPoolExecutor(max_workers=16) as k:
            for j in range(1, 100):
                k.submit(main_1, j)
    except Exception as e:
        print(e)


end_time = time.time()

print("您一共用时：" + str(end_time - start_time))
