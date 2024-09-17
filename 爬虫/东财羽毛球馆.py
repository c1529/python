import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import requests
import json
import random
import datetime

headers = {
    'Origin': 'http://fiddle.jshell.net',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 '
                  'Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'http://fiddle.jshell.net/_display/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}


data_1 = [
    {
        "field_name": "姓名",
        "field_key": 1,
        "field_value": "张三",
        "ignore": 0
    },
    {
        "field_name": "预约身份",
        "field_key": "fa4a111b-742a-5e68-dd2a-7896cbe3b8b9",
        "field_value": "学生",
        "new_field_value": "1cdb5",
        "ignore": 0
    },
    {
        "field_name": "学院",
        "field_key": "d5d29d49-25cd-649d-4190-a88eea9802a3",
        "field_value": "金融",
        "ignore": 0
    },
    {
        "field_name": "学号",
        "field_key": "0ca270b7-3f48-bf88-a3fe-c8899e936d56",
        "field_value": "2021211433",
        "ignore": 0
    },
    {
        "field_name": "教工号",
        "field_key": "2c74578e-c06b-1409-6ea4-cd26810d25dd",
        "field_value": "",
        "ignore": 1
    },
    {
        "field_name": "手机号",
        "field_key": 2,
        "field_value": "17542102452",
        "ignore": 0
    },
    {
        "field_name": "管理员备注",
        "field_key": 6,
        "ignore": 0
    }
]
data_2 = [
    {
        "field_name": "姓名",
        "field_key": 1,
        "field_value": "李四",
        "ignore": 0
    },
    {
        "field_name": "预约身份",
        "field_key": "fa4a111b-742a-5e68-dd2a-7896cbe3b8b9",
        "field_value": "学生",
        "new_field_value": "1cdb5",
        "ignore": 0
    },
    {
        "field_name": "学院",
        "field_key": "d5d29d49-25cd-649d-4190-a88eea9802a3",
        "field_value": "金融",
        "ignore": 0
    },
    {
        "field_name": "学号",
        "field_key": "0ca270b7-3f48-bf88-a3fe-c8899e936d56",
        "field_value": "2022210419",
        "ignore": 0
    },
    {
        "field_name": "教工号",
        "field_key": "2c74578e-c06b-1409-6ea4-cd26810d25dd",
        "field_value": "",
        "ignore": 1
    },
    {
        "field_name": "手机号",
        "field_key": 2,
        "field_value": "18642825614",
        "ignore": 0
    },
    {
        "field_name": "管理员备注",
        "field_key": 6,
        "ignore": 0
    }
]


eid = '614be5a8c129362f6378b3d4'


# 获取时间
def item_data():
    # 获取当前时间
    current_date = datetime.date.today()
    past_date = datetime.date(2024, 9, 8)
    # 计算时间差
    delta = current_date - past_date
    # print(f"距离2023年12月31日已经过去了 {delta.days} 天")
    # 因为预约明天所以多加一个1
    return int(delta.days + 1) * 3600 * 24 + 1725724800


def get_token(phone,password):
    path = Service('./chromedriver.exe')
    web = Chrome(service=path)
    web.get('http://baominggongju.com/phoneLogin')
    time.sleep(2)
    phone_post = web.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/form/div[1]/div/div[1]/input')
    password_post = web.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/form/div[2]/div/div/input')
    phone_post.send_keys(phone)
    password_post.send_keys(password)
    time.sleep(1)
    button = web.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/button")
    button.click()
    time.sleep(2)
    url_login = 'https://api-xcx-qunsou.weiyoubot.cn/xcx/enroll/v1/login_by_phone'
    data_post = {
        # "encrypt": 1,
        "origin": "enroll_pc",
        "phone": phone,
        "password": password
    }
    response = requests.post(url_login, headers=headers, data=json.dumps(data_post))
    result = json.loads(response.text)
    access_token = result['data']['access_token']
    print(access_token)
    time.sleep(2)
    return access_token

def get_playgroud(token, data, start, end, items_date):
    url = "http://api-xcx-qunsou.weiyoubot.cn/xcx/enroll/v5/enroll"
    while True:
        ground_list = ['6457af48b7fe40c5d291eb32', '6457af48b7fe40c5d291eb33', '6457af48b7fe40c5d291eb34',
                       '6457af48b7fe40c5d291eb35']
        key = (random.choice(ground_list))
        payload = json.dumps({
            "access_token": token,
            "eid": '614be5a8c129362f6378b3d4',
            'from': "xcx",
            "info": data,
            "items": [
                {
                    "key": key,
                    "count": 1,
                    "date": items_date,
                    "start": start,
                    "end": end
                }
            ],
            "on_behalf": 1,
            'pay_source': "pc",
            "referer": "odVL41Ka6bn_ismciUZRRlIBTl6c"
        })
        time.sleep(0.1)
        response = requests.request("POST", url, headers=headers, data=payload, verify=False, timeout=2)
        result = json.loads(response.text)
        print(result)
        print(result['sta'])
        if result['sta'] == -1:
            print('失败')
        elif result['sta'] == 700:
            print('请求过于频繁，请稍后重试')
        else:
            break



# 请输入你的手机号和密码
phone1 = ''
password1 = ''
start1 = 68400
end1 = 73800

phone2 = ''
password2 = ''
start2 = 63000
end2 = 68400


access_token1 = get_token(phone1, password1)
access_token2 = get_token(phone2, password2)

item_data1 = item_data()

from threading import Thread
thread1 = Thread(target=get_playgroud, args=(access_token1, data_1, start1, end1,item_data1))
thread2 = Thread(target=get_playgroud, args=(access_token2, data_2, start2, end2,item_data1))
thread1.start()  # 线程1开始
thread2.start()  # 线程2开始













