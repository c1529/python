from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.lagou.com/'

path = Service('./chromedriver.exe')

web = Chrome(service=path)

web.get(url)

# 1.找到界面的x按钮，并且点击它
x_button = web.find_element(By.ID, "cboxClose")

x_button.click()

# 点完x后浏览器需要反应，这里休眠2秒
time.sleep(1)

# 2.找到搜索框，输入想要搜索的内容并且进行搜索

s_search = web.find_element(By.ID, "search_input")

s_search.send_keys("python", Keys.ENTER)

# time.sleep(1)


time.sleep(20)

# 手动进行微信扫码
# 重新搜索
s_search = web.find_element(By.ID, "search_input")

s_search.send_keys("python", Keys.ENTER)

# 3.数据提取

a = web.find_elements(By.CLASS_NAME, 'item__10RTO')
for i in a:
    m = i.find_element(By.ID, 'openWinPostion')
    print(m.text)




