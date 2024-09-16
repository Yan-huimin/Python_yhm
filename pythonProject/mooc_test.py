import json
from selenium import webdriver
import time

url = 'https://www.icourse163.org/'

# 启动浏览器
bro = webdriver.Chrome()

time.sleep(2)

# 访问目标URL
bro.get(url)

# 最大化窗口
bro.maximize_window()

time.sleep(2)
