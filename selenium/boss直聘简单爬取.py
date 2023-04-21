import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

url = 'https://www.zhipin.com/'

path = Service('./chromedriver.exe')

web = Chrome(service=path)

web.get(url)

# time.sleep(3)

a = web.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/div[2]/p/input')

a.send_keys("数据分析师", Keys.ENTER)

# 需要停留时间来方便获取网页信息
time.sleep(10)

job = web.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul')

m = web.find_elements(By.CLASS_NAME, 'job-card-wrapper')

for i in m:
    t = i.find_element(By.XPATH, './div[1]/a/div[1]/span[1]')
    print(t.text)




