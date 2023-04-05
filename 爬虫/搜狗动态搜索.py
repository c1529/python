import requests
a = input("请输入你想搜索的东西")

url = 'http://www.sogou.com/web?query='+a

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36'
}

# get请求
responses = requests.get(url=url, headers=head)
print(responses.text)




