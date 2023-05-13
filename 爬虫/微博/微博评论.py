# 爬取的是天气之子首条置顶评论
import requests
import json

o_url = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4529159030703841&is_show_bulletin=2&is_mix=0' \
        '&count=10&uid=6885069945&fetch_level=0'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36',
    'referer': 'https://weibo.com/6885069945/JceyH2X6h',
    'cookie': 'SINAGLOBAL=5025427609804.329.1683282069712; ULV=1683282069714:1:1:1:5025427609804.329.1683282069712:; '
              'XSRF-TOKEN=dt71FTH3mssV--ja1-9fxA_O; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5CoEv9H6YlGr0n4_-WI5Z85JpX5KMhUgL'
              '.FoMN1KB41KzNehz2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0.X1K.ES05E; ALF=1686543799; SSOLoginState=1683951799;'
              'SCF=AvKWznEaal_a_3eCiNqVu_sAVqVY0VjQh4w_ox-a2xIAc1DUa5f4TTTVkNYXfiLeW9vq3XZH4KEs9aL5agy3UJQ.; '
              'SUB=_2A25JW2DnDeRhGeFJ4lYY-SzLyz6IHXVqEdUvrDV8PUNbmtAGLRnfkW9Nfql58HLI829upDfcNncFuuWcPbzMHW2I; '
              'WBPSESS=2rqXSIe2CRXMw5gyf7yg3p-h_pfam9s-B3aqrPmxZ229NczdVXR61Xpn88ouRDZ8cEOAQUJ8qCF5jWMB5TM'
              '-rOGPoOmofHrESgWXhCSCumWCHgZxb2E96yI_h3adTa8-De6SeumzN9t7ghEMPnRAZQ==',
    'x-requested-with': 'XMLHttpRequest'
}

res1 = requests.get(url=o_url, headers=headers)

text = res1.text

a = json.loads(text)

number = a['total_number']

page = int(number / 18) + 1

max_id = a['max_id']

a = a['data']

for i in a:
    print(i['text'])


def geturl(max_id):
    r = 'https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=4529159030703841&is_show_bulletin=2&is_mix' \
        '=0&max_id=' + str(max_id) + '&count=20&uid=6885069945&fetch_level=0'
    return r


def getcomment(url):
    res = requests.get(url, headers=headers)
    res = res.text
    jso = json.loads(res)
    max_id = jso['max_id']
    print(max_id)
    jso = jso['data']
    for j in jso:
        print(j['text'])


def getid(url):
    respon = requests.get(url, headers=headers)
    respontext = respon.text
    js1 = json.loads(respontext)
    return js1['max_id']


for i in range(0, page+1):
    url = geturl(max_id)
    getcomment(url)
    max_id = getid(url)
