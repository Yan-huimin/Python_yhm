# import urllib.parse
# import urllib.request
# from bs4 import BeautifulSoup
# import socket
# import time
#
# # https://sc.chinaz.com/tupian/fengjing.html
# # https://sc.chinaz.com/tupian/fengjing_2.html
#
# # //div[contains(@class, "container")]//div[@class="right-div tupian-right-div"]//div/p[@class="bg-bull btn-p com-right-down-btn"]/a
# # //div[@class="item masonry-brick"]/div/a
# # //div[@class="container"]//div[@class="bot-div"]/a
#
# socket.setdefaulttimeout(20)
#
# headers = {
#     'cookie': '_clck=pstu63%7C2%7Cfp4%7C0%7C1716; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1726122656,1726141579,1726314568; HMACCOUNT=22173AC77CF84B49; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1726324824',
#     'referer': 'https://sc.chinaz.com/tupian/'
# }
#
# base_url = 'https://sc.chinaz.com/tupian/fengjing'
# main_page_url_head = 'https://sc.chinaz.com/'
# cnt_img = 1
#
# def get_url(index):
#     g_url = base_url + '.html' if index == 1 else base_url + '_' + str(index) + '.html'
#     return g_url
#
# def get_request(url_1):
#     re = urllib.request.Request(url=url_1, headers=headers)
#     return re
#
# def enter_main_page(main_page_url):
#     main_page_content = urllib.request.urlopen(main_page_url).read().decode('utf-8')
#     main_page_soup = BeautifulSoup(main_page_content, 'lxml')
#     img_url = main_page_soup.select('p.bg-bull.btn-p.com-right-down-btn > a')
#     # print(img_url[0].get('href'))
#     down_load_img(img_url[0].get('href'))
#
# def down_load_img(img_url_end):
#     global cnt_img
#     file_end = img_url_end[-4:]
#     if not file_end.startswith('.'):
#         file_end = '.jpg'
#     urllib.request.urlretrieve(img_url_end, 'D:\\Python_code\\pythonProject\\Img_f\\' + str(cnt_img) + file_end)
#     print('成功下载{}张图片......'.format(cnt_img))
#     cnt_img += 1
#
# # def get_main_page(request_url, begin):
# #     try:
# #         index = 0
# #         soup = BeautifulSoup(urllib.request.urlopen(request_url).read().decode('utf-8'), 'lxml')
# #         img_list = soup.select('div.container div.bot-div > a')
# #         for i in range(begin, len(img_list)):
# #             index = i
# #             enter_main_page(main_page_url_head + img_list[i].get('href'))
# #         time.sleep(1)
# #     except:
# #         get_main_page(request_url, index)
#
# def get_main_page(request_url, begin, retry_count=3):
#     try:
#         index = 0
#         soup = BeautifulSoup(urllib.request.urlopen(request_url).read().decode('utf-8'), 'lxml')
#         img_list = soup.select('div.container div.bot-div > a')
#         if not img_list:  # 防止 img_list 为空
#             print('未找到图片链接，跳过该页面')
#             return
#
#         for i in range(begin, len(img_list)):
#             index = i
#             enter_main_page(main_page_url_head + img_list[i].get('href'))
#         time.sleep(1)
#     except Exception as e:
#         if retry_count > 0:
#             print(f"发生异常: {e}, 重试 {retry_count} 次...")
#             time.sleep(2)  # 防止频繁重试
#             get_main_page(request_url, index, retry_count - 1)
#         else:
#             print("多次重试失败，跳过该页面。")
#
#
# if __name__ == '__main__':
#     start_page = int(input('请输入起始页码......\n'))
#     end_page = int(input('请输入终止页码......\n'))
#     for page in range(start_page, end_page+1):
#         url = get_url(page)
#         request = get_request(url)
#         print('*'*15 + '{}'.format(page) + '*'*15)
#         get_main_page(request, 0)
#     print('-'*50)
#     print('下载成功......')
#     print('本次成功下载{}张图片......'.format(cnt_img))

import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import socket
import time

# https://sc.chinaz.com/tupian/fengjing.html
# https://sc.chinaz.com/tupian/fengjing_2.html

socket.setdefaulttimeout(20)

headers = {
    'cookie': '_clck=pstu63%7C2%7Cfp4%7C0%7C1716; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1726122656,1726141579,1726314568; HMACCOUNT=22173AC77CF84B49; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1726324824',
    'referer': 'https://sc.chinaz.com/tupian/'
}

base_url = 'https://sc.chinaz.com/tupian/fengjing'
main_page_url_head = 'https://sc.chinaz.com/'
cnt_img = 1


def get_url(index):
    g_url = base_url + '.html' if index == 1 else base_url + '_' + str(index) + '.html'
    return g_url


def get_request(url_1):
    re = urllib.request.Request(url=url_1, headers=headers)
    return re


def enter_main_page(main_page_url, retry_count=3):
    """处理每一张图片，并设置最大重试次数"""
    try:
        main_page_content = urllib.request.urlopen(main_page_url).read().decode('utf-8')
        main_page_soup = BeautifulSoup(main_page_content, 'lxml')
        img_url = main_page_soup.select('p.bg-bull.btn-p.com-right-down-btn > a')
        if img_url:
            down_load_img(img_url[0].get('href'))
        else:
            print("未找到图片链接，跳过该图片。")
    except Exception as e:
        if retry_count > 0:
            print(f"下载图片时发生错误: {e}，重试中... 剩余重试次数: {retry_count}")
            time.sleep(2)  # 暂停 2 秒后重试
            enter_main_page(main_page_url, retry_count - 1)
        else:
            print(f"图片下载失败，跳过该图片。错误: {e}")


def down_load_img(img_url_end):
    global cnt_img
    file_end = img_url_end[-4:]
    if not file_end.startswith('.'):
        file_end = '.jpg'
    urllib.request.urlretrieve(img_url_end, 'D:\\Python_code\\pythonProject\\Img_f\\' + str(cnt_img) + file_end)
    print('成功下载{}张图片......'.format(cnt_img))
    cnt_img += 1


def get_main_page(request_url, begin):
    """处理每一页的所有图片链接"""
    try:
        index = 0
        soup = BeautifulSoup(urllib.request.urlopen(request_url).read().decode('utf-8'), 'lxml')
        img_list = soup.select('div.container div.bot-div > a')
        if not img_list:
            print("该页面没有图片链接，跳过。")
            return

        for i in range(begin, len(img_list)):
            index = i
            enter_main_page(main_page_url_head + img_list[i].get('href'))
        time.sleep(1)
    except Exception as e:
        print(f"获取页面时发生错误: {e}，重试...")
        get_main_page(request_url, index)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码......\n'))
    end_page = int(input('请输入终止页码......\n'))
    for page in range(start_page, end_page + 1):
        url = get_url(page)
        request = get_request(url)
        print('*' * 15 + '{}'.format(page) + '*' * 15)
        get_main_page(request, 0)
    print('-' * 50)
    print('下载成功......')
    print('本次成功下载{}张图片......'.format(cnt_img))

