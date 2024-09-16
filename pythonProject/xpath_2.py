# import urllib.request
# from lxml import etree
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# # 设置 WebDriver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
#
# url = 'https://sc.chinaz.com/tupian/ribenmeinv.html'
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
# }
#
# #定制请求头文件
# request = urllib.request.Request(url=url, headers=headers)
#
# response = urllib.request.urlopen(request)
#
# #获取服务器响应文件
# content = response.read().decode('utf-8')
#
# #解析源码数据，因为这里是在线获取的服务器响应文件，因此应该使用xpath.HTML
# tree = etree.HTML(content)
#
# my_list = tree.xpath('//div[@class="item masonry-brick"]/img/@src')
#
# print(content)
#
# print(my_list)
# print(type(my_list))
# print(len(my_list))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree

# 设置 WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://sc.chinaz.com/tupian/ribenmeinv.html'
driver.get(url)

# 获取页面源代码
content = driver.page_source

# 解析源码数据
tree = etree.HTML(content)

# 使用 XPath 提取 src 属性
my_list = tree.xpath('//div[@class="item masonry-brick"]/img/@src')

# 打印结果
print(my_list)
print(type(my_list))
print(len(my_list))

driver.quit()

