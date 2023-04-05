import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/chart'
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36'
}

response = requests.get(url=url, headers=head)

print(response.status_code)

content = response.text

# html.parser是指定解释器
soup = BeautifulSoup(content, 'html.parser')

# html里第一个<p>标签
# print(soup.p)

a = soup.findAll('table', attrs={"width": "100%"})

# print(a)

'''
j = []
for i in a:
    j.append(soup.findAll('a', attrs={'class': 'nbg'}))
'''

j = soup.findAll('a', attrs={'class': 'nbg'})
print(type(j))

for aa in j:
    print(aa['title'])







