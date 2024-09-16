# import urllib.request
# import urllib.parse
#
# url = 'https://www.acwing.com/problem/'
#
# headers = {
#     'Cookie': ' csrftoken=KVUEcZsQ8WSCx1BkJIFQh5lmdqMy25u2Xz4lx9pqN2xxrE9I48ZhLmqPj0wb3pZO; sessionid=9r979bo5oci8qhyfu8f6x5a0n2pxwkls',
#     'Referer': 'https://www.acwing.com/about/'
# }
#
# request = urllib.request.Request(url=url, headers=headers)
#
# try:
#     content = urllib.request.urlopen(request).read().decode('utf-8')
#     with open('acwing_1.html', 'w', encoding='utf-8') as file:
#         file.write(content)
# except Exception as e:
#     print(f"An error occurred: {e}")
import urllib.request
import urllib.parse
import traceback
from urllib.error import HTTPError, URLError

url = 'https://www.acwing.com/problem/'

headers = {
    'Cookie': 'csrftoken=KVUEcZsQ8WSCx1BkJIFQh5lmdqMy25u2Xz4lx9pqN2xxrE9I48ZhLmqPj0wb3pZO; sessionid=9r979bo5oci8qhyfu8f6x5a0n2pxwkls',
    'Referer': 'https://www.acwing.com/about/'  # 如果需要，可以考虑改为与请求 URL 更相关的页面
}

request = urllib.request.Request(url=url, headers=headers)

try:
    response = urllib.request.urlopen(request, timeout=10)
    content = response.read().decode('utf-8')

    with open('acwing_1.html', 'w', encoding='utf-8') as file:
        file.write(content)
    print("File written successfully.")
except HTTPError as e:
    print(f"HTTP error occurred: {e.code} - {e.reason}")
except URLError as e:
    print(f"URL error occurred: {e.reason}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print(traceback.format_exc())
