from pynput.keyboard import Key, Controller
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import random

# 创造键盘对象
keybord = Controller()

txt = input("请输入你的姓名：")
yard = input("请输入你的竞赛码：")

path = Service('./chromedriver.exe')

web = Chrome(service=path)

url = 'https://dazi.kukuw.com/'

web.get(url)

time.sleep(2)


# web.find_element(By.XPATH, '//*[@id="time"]').clear()
# web.find_element(By.XPATH, '//*[@id="time"]').send_keys(1)


def alt_name(txt1):
    # 找到姓名框
    web.find_element(By.XPATH, '//*[@id="name"]').click()
    # 找到修改位置
    name = web.find_element(By.XPATH, '//*[@id="new_username"]')
    name.send_keys(txt1)
    # 确认
    web.find_element(By.XPATH, '//*[@id="window_box"]/div/div[2]/a[1]').click()
    time.sleep(1)


def comp(yard_1):
    web.find_element(By.XPATH, '//*[@id="radio_group2"]').click()
    time.sleep(2)
    web.find_element(By.XPATH, '//*[@id="group_num"]').send_keys(yard_1)


alt_name(txt)

time.sleep(1)

comp(yard)

time.sleep(2)

web.find_element(By.XPATH, '//*[@id="form"]/ul[6]/li[2]/input').click()

time.sleep(3)


def write(row):
    # 获取文字
    x_path = r'//*[@id="i_' + str(row) + r'"]/div/span'
    a1 = web.find_element(By.XPATH, x_path).text
    print(a1)
    return a1 + ' '
    # # 输入文字
    # a2 = web.find_element(By.XPATH, r'//*[@id="i_' + str(row) + r'"]/input[2]')
    # a2.send_keys(a1)
    # a2.send_keys(' ')
    # time.sleep(6)


txt1 = ''

try:
    for row_1 in range(0, 100):
        txt1 += write(row_1)
except Exception as e:
    print('所有行已经准备好')

for i in txt1:
    # 等待时间
    time_wait = random.randint(1, 2)
    time.sleep(time_wait / 10)
    # 错误的概率
    error_cc = random.randint(1, 15)
    if error_cc % 11 == 0:
        keybord.press('a')
        # 进行退格操作
        keybord.press(Key.backspace)
        keybord.release(Key.backspace)
    keybord.press(i)

time.sleep(360)
