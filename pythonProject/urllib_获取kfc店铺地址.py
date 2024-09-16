import urllib.request
import urllib.parse
import json


# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10


def get_data(page_1):
    base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    data = {
        'cname': '北京',
        'pageIndex': str(page_1),
        'pageSize': '10'
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url=base_url, data=data, headers=headers)

    content = urllib.request.urlopen(request).read().decode('utf-8')

    return content


def download_data(page_1, content):
    with open('kfc_' + str(page_1) + '.json', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    try:
        start_page = int(input('请输入初始页码'))
        end_page = int(input('请输入截止页码'))
        for page in range(start_page, end_page + 1):
            content_1 = get_data(page)
            download_data(page, content_1)
        print('Done!')
    except Exception as e: 
        print(e)