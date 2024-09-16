import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = 'https://sc.chinaz.com/tupian/24090324967.htm'

headers = {
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}


# //p[@class="bg-bull btn-p com-right-down-btn"]/a

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

html = response.read().decode('utf-8')

soup = BeautifulSoup(open('main_page.html', encoding='utf-8'), 'lxml')

url_list = soup.select('p.bg-bull.btn-p.com-right-down-btn > a')

print(url_list[0].get('href'))