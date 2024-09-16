import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

s = input('请输入单词......\n')

data = {
    'kw': str(s)
}

# def post(url, data=None, json=None, **kwargs):
# json 不需要输入
response = requests.post(url=url, headers=headers, data=data)

obj = json.loads(response.text)

list_word_translate = obj.get('data')

for i in list_word_translate:
    print(i)