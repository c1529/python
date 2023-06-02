import requests
import json
from threading import Thread

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

start_url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset=0&period=hour'

response = requests.get(url=start_url, headers=headers)

res = response.text

data = json.loads(res)

num = data['paging']['totals']


def get_url(page):
    return 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset=' + str(page * 20) + '&period=hour'


total = int((num - 19) / 20) + 1


def get_hot(url):
    response_hot = requests.get(url=url, headers=headers)
    data_hot = json.loads(response_hot.text)['data']
    for i in data_hot:
        print(i['question']['title'])


def get_title(page1, page2):
    for number in range(page1, page2):
        try:
            url = get_url(number)
            get_hot(url)
        except Exception as e:
            print(e)


# try:
#     get_title(0, total)
# except Exception as e:
#     print("程序异常", e)

t1 = Thread(target=get_title, args=(0, 30))
t2 = Thread(target=get_title, args=(31, 60))
t3 = Thread(target=get_title, args=(61, 90))
t4 = Thread(target=get_title, args=(91, 120))
t5 = Thread(target=get_title, args=(121, 150))
t6 = Thread(target=get_title, args=(151, 180))
t7 = Thread(target=get_title, args=(181, 210))
t8 = Thread(target=get_title, args=(211, 240))
t9 = Thread(target=get_title, args=(241, 270))
t10 = Thread(target=get_title, args=(271, 300))


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

