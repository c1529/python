import re
import json

import requests

url = 'https://www.bilibili.com/video/BV1rT411h764/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source' \
      '=606f61eee9182a64593df0b2579f4d79'

# 防盗链
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36',
    'referer': 'https://www.bilibili.com/video/BV11S4y1G7X3/?spm_id_from=333.337.search-card.all.click&vd_source'
               '=606f61eee9182a64593df0b2579f4d79'
}

res = requests.get(url=url, headers=headers)

text = res.text

# object2 = re.compile(r'<script>window.__playinfo__=(?P<title>.*?)</script>', re.S)
#
# a = object2.finditer(text)
'''
<h1 title="《起风了》[我曾难自拔于世间之大，也沉溺于其中梦话]" class="video-title tit">《起风了》[我曾难自拔于世间之大，也沉溺于其中梦话]</h1>
'''

# for i in a:
#     print(i.group('title'))
#     b = i.group('title')
#     print(type(b))
#     c = json.loads(b)
#     print(type(c))

a = re.findall(r'<script>window.__playinfo__=(.*?)</script>', text)

b = json.loads(a[0])

audio = b['data']['dash']['audio'][0]['baseUrl']

video = b['data']['dash']['video'][0]['baseUrl']

name = re.findall(r'property="og:title" content="(.*?)_哔哩哔哩_bilibili', text)[0]

res_audio = requests.get(url=audio, headers=headers).content

res_video = requests.get(url=video, headers=headers).content

with open(name+'.mp3',mode='wb') as f:
    f.write(res_audio)

with open(name+'.mp4', mode='wb') as f:
    f.write(res_video)


