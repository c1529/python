import re

str1 = '我今年18岁，我有2000000w'
# findall参数一个是正则表达式，一个是字符串
# findall返回一个列表
# \在Python中默认转义字符，在前面加一个r就好了
a = re.findall(r'\d+', str1)
print(a)

# 重点
# b是一个迭代器
b = re.finditer(r'\d+', str1)
for i in b:  # 从迭代器中拿到内容
    print(i)
    print(i.group())  # 拿到数据

# search只会匹配到第一次匹配到的数据
c = re.search(r'\d+', str1)
print(c)
print(c.group())

# match,match是从字符串开头匹配，相当于正则加了^
d = re.match(r'\d+', str1)
print(d)


obj = re.compile(r"\d+")
e = obj.finditer(str1)
print(e)

# 小例子
s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游记'><span id='10086'>中国移动</span></div>
"""
'''
ob = re.compile(r"<span id=('\d+')>(.*?)</span>")
f = ob.findall(s)
print(f)
'''
# 改良版(大写P)
'''
想要提取数据需要小括号括起来
(?P<名字>正则)
提取数据时需要group('名字')
'''
ob = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
f = ob.finditer(s)
for i in f:
    print(i.group('id'))
    print(i.group('name'))





