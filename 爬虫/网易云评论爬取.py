import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
import re

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36'
}

data = {
    'csrf_token': "7401018746225dedc547c700f16a850d",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_26418808",
    'threadId': "R_SO_4_26418808"
}

f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'

g = '0CoJUm6Qyw8W8jud'

e = '010001'

i = "62ltMvMtf7FTo0YY"


def get_encseckey():
    return "d38509af6a5590006bd300b6b20eea1b3f196dc4770b0676af6fd0761f0640b00ab677eb6d5338f637d048600f75b71ffe584d1aefd2f179043f13d655a5952b858df89ece7d7f28629ab725314ec372b0d54f74aeedc68516aa75c9515c96cbbc90989a0ba40a60de40e4629289f323617245d3e9ec8339fe3dd7a04479ce9c"


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def encparams(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs), 'utf-8')


def get_params(data):
    first = encparams(data, g)
    sencond = encparams(first, i)
    return sencond


# 处理加密过程
"""
    function a(a) {   # 返回随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),  # 取整
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d:数据(data)     e:010001  f:      
        var h = {}
          , i = a(16);   # i是一个16位随机字符串
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),   # 得到params
        h.encSecKey = c(i, e, f),      # 得到encSecKey   e和f是固定的，如果把随机数i固定，那么该函数返回固定值
        h
    }
    function e(a, b, d, e) {     
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
"""

res = requests.post(url=url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encseckey()
}, headers=headers)
html = res.content.decode()
html = json.loads(html)
dir1 = html['data']['hotComments']
for i in dir1:
    print(i["content"])


