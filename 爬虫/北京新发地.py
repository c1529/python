import requests
import re
import csv

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

# for i in list1:
#     print(i.group('name'),
#           i.group('kind'),
#           i.group('low'),
#           i.group('high'),
#           i.group('avg'),
#           i.group('place'),
#           i.group('data'))

head = ['名字', '种类', '最低价', '最高价', '平均价', '产地', '时间']

with open("text.csv", "w", encoding='gbk', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(head)
    for i in list1:
        writer.writerow([i.group('name'),
                        i.group('kind'),
                        i.group('low'),
                        i.group('high'),
                        i.group('avg'),
                        i.group('place'),
                        i.group('data')])
