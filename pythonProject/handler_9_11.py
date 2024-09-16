import urllib.request
import urllib.parse

url = 'https://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

ip = {
    'ip': '154.203.132.49:8080'
}

request = urllib.request.Request(url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=ip)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

print(content)