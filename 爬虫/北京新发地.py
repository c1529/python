import requests
import re

url = 'http://www.xinfadi.com.cn/getCat.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

data = {
    'prodCatid': '1186'
}

res = requests.post(url=url, headers=headers, data=data)

text = res.text

# print(text)

obj = re.compile(r'"prodName":"(?P<name>.*?)","'
                 r'.*?"prodCat":"(?P<kind>.*?)","'
                 r'.*?"lowPrice":"(?P<low>.*?)","highPrice":"'
                 r'(?P<high>.*?)","avgPrice":"(?P<avg>.*?)'
                 r'","place":"(?P<place>.*?)",".*?'
                 r'"pubDate":"(?P<data>.*?)","status', re.S)

list1 = obj.finditer(text)

for i in list1:
    print(i.group('name'),
          i.group('kind'),
          i.group('low'),
          i.group('high'),
          i.group('avg'),
          i.group('place'),
          i.group('data'))
