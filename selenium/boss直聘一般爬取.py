# 出了点小问题，不过数据都获取了

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from threading import Thread
import csv

# url = 'https://www.zhipin.com/web/geek/job?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&city=100010000&page=2'

path = Service('./chromedriver.exe')

web = Chrome(service=path)

# web.get(url)
# time.sleep(10)

head = ['职位名称', '地点', '薪资', '经验', '学历', '公司名称', '公司规模', '技巧', '福利']

with open("BOSS直聘.csv", mode="w", encoding="gbk", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(head)


def close_window():
    try:
        time.sleep(0.5)
        if web.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[1]/span/i'):
            web.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[1]/span/i').click()
    except BaseException as e:
        a = e
        # print("无弹框", e)


# close_window()
# res = web.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li')
# for i in res:
#     name = i.find_element(By.XPATH, './div[1]/a/div[1]/span[1]')
#     place = i.find_element(By.XPATH, './div[1]/a/div[1]/span[2]/span')
#     money = i.find_element(By.XPATH, './div[1]/a/div[2]/span')
#     jinyan = i.find_element(By.XPATH, './div[1]/a/div[2]/ul/li[1]')
#     xueli = i.find_element(By.XPATH, './div[1]/a/div[2]/ul/li[2]')
#     gongsi = i.find_element(By.XPATH, './div[1]/div/div[2]/h3/a')
#     guimo = i.find_element(By.XPATH, './div[1]/div/div[2]/ul')
#     kill = i.find_element(By.XPATH, './div[2]/ul')
#     fuli = i.find_element(By.XPATH, './div[2]/div')
#     print(name.text, place.text, money.text, jinyan.text, xueli.text, gongsi.text, guimo.text)
#     print(kill.text, fuli.text)

def ffff():
    close_window()
    res = web.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li')
    for i in res:
        name = i.find_element(By.XPATH, './div[1]/a/div[1]/span[1]').text
        place = i.find_element(By.XPATH, './div[1]/a/div[1]/span[2]/span').text
        money = i.find_element(By.XPATH, './div[1]/a/div[2]/span').text
        jinyan = i.find_element(By.XPATH, './div[1]/a/div[2]/ul/li[1]').text
        xueli = i.find_element(By.XPATH, './div[1]/a/div[2]/ul/li[2]').text
        gongsi = i.find_element(By.XPATH, './div[1]/div/div[2]/h3/a').text
        guimo = i.find_element(By.XPATH, './div[1]/div/div[2]/ul').text
        kill = i.find_element(By.XPATH, './div[2]/ul').text
        fuli = i.find_element(By.XPATH, './div[2]/div').text
        # print(name.text, place.text, money.text, jinyan.text, xueli.text, gongsi.text, guimo.text)
        # print(kill.text, fuli.text)
        with open("BOSS直聘.csv", mode="a", encoding="gbk", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, place, money, jinyan, xueli, gongsi, guimo, kill, fuli])


url = 'https://www.zhipin.com/web/geek/job?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&city=100010000&page=1'
web.get(url)
close_window()
res = web.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li')
for i in res:
    name = i.find_element(By.XPATH, './div[1]/a/div[1]/span[1]').text
    place = i.find_element(By.XPATH, './div[1]/a/div[1]/span[2]/span').text
    money = i.find_element(By.XPATH, './div[1]/a/div[2]/span').text
    jinyan = i.find_element(By.XPATH, './div[1]/a/div[2]/ul/li[1]').text
    xueli = i.find_element(By.XPATH, './div[1]/a/div[2]/ul/li[2]').text
    gongsi = i.find_element(By.XPATH, './div[1]/div/div[2]/h3/a').text
    guimo = i.find_element(By.XPATH, './div[1]/div/div[2]/ul').text
    kill = i.find_element(By.XPATH, './div[2]/ul').text
    fuli = i.find_element(By.XPATH, './div[2]/div').text
    # print(name.text, place.text, money.text, jinyan.text, xueli.text, gongsi.text, guimo.text)
    # print(kill.text, fuli.text)
    with open("BOSS直聘.csv", mode="a", encoding="gbk", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, place, money, jinyan, xueli, gongsi, guimo, kill, fuli])

for j in range(2, 11):
    h = str(j)
    url = 'https://www.zhipin.com/web/geek/job?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&city=100010000&page=' + h
    web.get(url)
    time.sleep(8)
    ffff()
