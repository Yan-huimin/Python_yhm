import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'

headers = {
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

response.encoding = 'utf-8'

content = response.text

soup = BeautifulSoup(content, 'lxml')

# __VIEWSTATE: ZzZbR/O5tmfheKF7TIXirOpCTTbXPbhxoYW9dhITnRRVS4EW3q1luoEuQ/EiR+ooZWoqUK64Wung1pOlgyEhLupR21k5s21veVg6ADJUBdNAeEtCWqCpHKdkku0z8qhQahqkGYfmm389DfbS0helztqD4K0=
# __VIEWSTATEGENERATOR: C93BE1AE

VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')
Viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

code_img = soup.select('#imgCode')[0].attrs.get('src')
basic_url = 'https://www.gushiwen.cn/' + code_img

# urllib.request.urlretrieve(basic_url, 'code_img.png')

session = requests.Session()
content_code = session.get(url=basic_url)

with open('code_img.jpg', 'wb') as fp:
    fp.write(content_code.content)

code_data = input('请输入验证码......\n')

data_post = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': Viewstategenerator,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': '2234489774@qq.com',
    'pwd': 'yhm20030117',
    'code': code_data,
    'denglu': '登录',
}

url_post = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

response = session.post(url=url_post, data=data_post, headers=headers)

response.encoding = 'utf-8'

with open('Poem.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
