import time

from selenium import webdriver

# 这个By一定要手动导入，否则虽然可以直接使用，但是发生报错
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com'

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

time.sleep(2)
#
# btn = driver.find_element(by=By.ID, value='kw')
#
# btn_search = driver.find_element(by=By.ID, value='su')
#
# # 获取标签的名称，而不是value
# # print(btn.tag_name)
#
# time.sleep(2)
#
# btn.send_keys('周杰伦')
#
# btn_search.click()
#
# # 尽量在每一个操作之后都休眠一段时间，否则会出现某些指令无法正常执行
# time.sleep(2)
#
# # 屏幕下滑
# to_end = 'document.documentElement.scrollTop=100000'
# driver.execute_script(to_end)
#
# time.sleep(2)
#
# btn_next_page = driver.find_element(by=By.CLASS_NAME, value='n')
#
# btn_next_page.click()
#
# time.sleep(2)
#
# driver.execute_script(to_end)
#
# time.sleep(2)
#
# driver.back()
#
# time.sleep(2)
#
# driver.forward()
#
# time.sleep(2)
#
# driver.quit()