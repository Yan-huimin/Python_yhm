import requests

url = 'https://www.baidu.com'

response = requests.get(url)

# 一个类型：<class 'requests.models.Response'>
# print(type(response))

# 六个方法

# 1. 获取网页的源码(字符串格式)
# print(response.text)

# 2. 访问或定制编码格式
# response.encoding = 'utf-8'
# print(response.text)

# 3. 获取请求的url
# print(response.url)

# 4. 响应的字节类型,返回的是二进制的数据
# print(response.content)

# 5. 返回状态码 (200, 404, 502, ......)
# print(response.status_code)

# 6. 返回响应的头信息
# print(response.headers)