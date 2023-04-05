import requests

url = 'https://fanyi.baidu.com/sug'


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36'
}

data = {'kw': input("请输入一个单词")}

responses = requests.post(url, data=data, headers=headers)
# responses 是json类型，需要用json函数处理，最后得到的数据时字典类型
print(responses.json())




