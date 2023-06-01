import requests
import json
import re
from threading import Thread
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36',
    'referer': 'https://www.bilibili.com/video/BV11S4y1G7X3/?spm_id_from=333.337.search-card.all.click&vd_source'
               '=606f61eee9182a64593df0b2579f4d79'
}


# url = 'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1' \
#       '&new_web_tag=1&order=click&cate_id=24&page=1&pagesize=30&time_from=20230525&time_to=20230601'
#
# res = requests.get(url=url, headers=headers)
#
# # print(res.text)
#
# res = json.loads(res.text)
#
# result = res['result']
#
# for i in result:
#     print(i['arcurl'])


def get_video(url_v):
    text = requests.get(url=url_v, headers=headers).text
    a = re.findall(r'<script>window.__playinfo__=(.*?)</script>', text)
    b = json.loads(a[0])
    # audio = b['data']['dash']['audio'][0]['baseUrl']
    video = b['data']['dash']['video'][0]['baseUrl']
    name = re.findall(r'property="og:title" content="(.*?)_哔哩哔哩_bilibili', text)[0]
    # res_audio = requests.get(url=audio, headers=headers).content
    res_video = requests.get(url=video, headers=headers).content
    try:
        with open(f"./bilibili动漫视频/{name}.mp4", mode='wb') as f:
            f.write(res_video)
            print(name + "保存完毕")
            time.sleep(1)
    except Exception as e:
        print(name + "保存失败")
        print(e)


# for page in range(1, 31):
#     url = f'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1' \
#           '&new_web_tag=1&order=click&cate_id=24&page=' + str(page) + '&pagesize=30&time_from=20230525&time_to=20230601'
#     res = requests.get(url=url, headers=headers)
#     res = json.loads(res.text)
#     result = res['result']
#     for i in result:
#         v_url = i['arcurl']
#         get_video(v_url)

def main(y, z):
    for page in range(y, z + 1):
        url = f'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1' \
              '&new_web_tag=1&order=click&cate_id=24&page=' + str(
            page) + '&pagesize=30&time_from=20230525&time_to=20230601'
        res = requests.get(url=url, headers=headers)
        res = json.loads(res.text)
        result = res['result']
        for i in result:
            v_url = i['arcurl']
            get_video(v_url)
        print(f"你已经爬取完{page}页视频")


t1 = Thread(target=main, args=(1, 3))
t2 = Thread(target=main, args=(4, 6))
t3 = Thread(target=main, args=(7, 9))
t4 = Thread(target=main, args=(10, 12))
t5 = Thread(target=main, args=(13, 15))
t6 = Thread(target=main, args=(16, 18))
t7 = Thread(target=main, args=(19, 21))
t8 = Thread(target=main, args=(22, 24))
t9 = Thread(target=main, args=(24, 26))
t10 = Thread(target=main, args=(27, 30))

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


