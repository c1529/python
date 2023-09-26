import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from threading import Thread
import csv
import random

header = ['职位', '薪资', '地区', '学历', '经验', '福利']

with open('b.csv', 'w', encoding='utf-8-sig', newline='') as f1:
    write1 = csv.writer(f1)
    write1.writerow(header)

# 谷歌驱动器
path = Service('./chromedriver.exe')

web = Chrome(service=path)

url = 'https://www.51job.com/'
# url = 'https://we.51job.com/pc/search?keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&searchType=2&sortType=0&metro='
web.get(url)
time.sleep(5)

search = web.find_element(By.XPATH, '//*[@id="kwdselectid"]')

search.send_keys('数据分析师')

time.sleep(1.5)

web.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/button').click()

time.sleep(5)
# //*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]
def get_data(page):
    if page==1:
        res = web.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')
    else:
        res = web.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')
    for i in res:
        name = i.find_element(By.XPATH, './/div[2]/div[1]/div/span').text
        money = i.find_element(By.XPATH, './div[2]/div[1]/p/span[1]').text
        place = i.find_element(By.XPATH, './div[2]/div[1]/p/span[2]/span[1]').text
        jingyan = i.find_element(By.XPATH, './div[2]/div[1]/p/span[2]/span[2]').text
        xueli = i.find_element(By.XPATH, './div[2]/div[1]/p/span[2]/span[3]').text
        gongsi = i.find_element(By.XPATH, './div[2]/div[2]/div[2]/a').text
        fuli = i.find_elements(By.XPATH, './div[3]/p/span')
        fuli_list = []
        for j in fuli:
            aa = j.find_element(By.XPATH, './i').text
            fuli_list.append(aa)
        with open('b.csv', 'a', encoding='utf-8-sig', newline='') as f2:
            write2 = csv.writer(f2)
            write2.writerow([name, money, place, xueli, jingyan, ' '.join(fuli_list)])
    time.sleep(2)

def click_next():
    web.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/button[2]').click()
    time.sleep(3)

try:
    for page in range(1, 50):
        print(f'第{page}页正在爬取')
        w_time = random.randint(2,5)
        time.sleep(w_time)
        get_data(page)
        click_next()
        print(f'第{page}页已爬取完')
except Exception as e:
    print(e)


