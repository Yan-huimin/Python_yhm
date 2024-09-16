import requests

url = 'https://www.baidu.com'

headers = {
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

data = {
    'wd': '周杰伦'
}

# def get(url, params=None, **kwargs):
# url 请求资源的路径
# params 参数
# kwargs 字典，传入headers
response = requests.get(url=url, params=data, headers=headers)

response.encoding = 'utf-8'

print(response.text)