import requests
# 不得不承认这里用bs4确实方便
from bs4 import BeautifulSoup

# 直接在要爬取的视频网站前bilibili加上i
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=908204446'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

res = requests.get(url=url, headers=headers)
res.encoding = 'utf-8'
text = res.text

# 指定解析器
soup = BeautifulSoup(text, 'html.parser')

a = soup.findAll('d')

for i in a:
    print(i.text)












