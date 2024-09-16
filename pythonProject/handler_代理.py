import urllib.request
import urllib.parse
import random

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

ip_pool = [
    {'http': '50.205.202.249:3128'},
    {'http': '12.234.123.421:1244'}
]

ip = random.choice(ip_pool)

url = 'https://ipaddress.my/?lang=zh_TW'

#在这里我们使用代理ip进行网站的访问
request = urllib.request.Request(url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=ip)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(content)
