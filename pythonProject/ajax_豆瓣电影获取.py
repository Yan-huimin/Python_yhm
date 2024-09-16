import json
import urllib.request
import urllib.parse

base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

def generate_url(page_):
    data = {
        'start': str((page_ - 1) * 20),
        'limit': '20'
    }

    res_url = base_url + urllib.parse.urlencode(data)

    return res_url


def get_request(url_1):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }
    request_res = urllib.request.Request(url=url_1, headers=headers)

    content_res = urllib.request.urlopen(request_res).read().decode('utf-8')

    return content_res


def download_json(content_1, page_1):
    with open('douban.json_' + str(page_1) + '.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(content_1, ensure_ascii=False))


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结尾页码'))
    for page in range(start_page, end_page + 1):
        url = generate_url(page)
        content = get_request(url)
        download_json(content, page)
    print('Done!')
