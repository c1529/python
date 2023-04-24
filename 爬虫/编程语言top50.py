import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = Service('./chromedriver.exe')

url = 'https://www.tiobe.com/tiobe-index/'

web = Chrome(service=path)

web.get(url)

time.sleep(3)

cc = web.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/button')

cc.click()

time.sleep(2)

a = web.find_elements(By.XPATH, '//*[@id="top20"]/tbody/tr')

# 找了thody的父标签，数据在tbody中，但是这里XPATH搜索到tbody会报错

for i in a:
    grade = i.find_element(By.XPATH, './td[1]').text
    lang = i.find_element(By.XPATH, './td[5]').text
    Ratings = i.find_element(By.XPATH, './td[6]').text
    Change = i.find_element(By.XPATH, './td[7]').text
    print(grade, lang, Ratings, Change)

# 21-50

b = web.find_elements(By.XPATH, '//*[@id="otherPL"]/tbody/tr')

for i in b:
    grade = i.find_element(By.XPATH, './td[1]').text
    lang = i.find_element(By.XPATH, './td[2]').text
    Change = i.find_element(By.XPATH, './td[3]').text
    print(grade, lang, Change)







