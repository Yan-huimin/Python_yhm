from urllib.error import HTTPError

from lxml import etree
import urllib.request
import urllib.parse
from urllib.parse import urljoin
import socket
import time

# https://sc.chinaz.com/tupian/ribenmeinv.html
# https://sc.chinaz.com/tupian/ribenmeinv_2.html

base_url = 'https://sc.chinaz.com/tupian/ribenmeinv'

socket.setdefaulttimeout(20)

cnt_pic = 1

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

def create_request(page):
    url = base_url + '.html' if page == 1 else base_url + '_' + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    response.close()
    time.sleep(2)
    return content

def down_load_pic(content, begin):
    try:
        cur = begin
        global cnt_pic
        tree = etree.HTML(content)
        #需要url和名称
        name = tree.xpath('//div[starts-with(@class, "item")]//img/@alt')
        src = tree.xpath('//div[starts-with(@class, "item")]//img/@data-original')
        for i in range(begin, len(name)):
            cur = i
            file_ect = src[i][-4:]
            # 否则默认jpg格式
            if not file_ect.startswith('.'):
                file_ect = '.jpg'
            url = urljoin(base_url, src[i])
            file_name = 'D:\\Python_code\\pythonProject\\Japanese_beauty_pictures\\' + name[i] + file_ect
            urllib.request.urlretrieve(url, file_name)
            print('已下载{}张图片'.format(cnt_pic))
            cnt_pic += 1
    except:
        down_load_pic(content, cur)



if __name__ == '__main__':
    try:
        start_page = int(input('请输入起始页码\n'))
        end_page = int(input('请输入结束页码\n'))
        for page in range(start_page, end_page + 1):
            #定制对象
            request = create_request(page)
            #获取源码
            content = get_content(request)
            #下载图片
            down_load_pic(content, 0)
        print('下载成功......')
        print('下载信息: {}张图片成功下载'.format(cnt_pic))
    except ValueError:
        print(ValueError)
    except TypeError:
        print(TypeError)
    except IndexError:
        print(IndexError)