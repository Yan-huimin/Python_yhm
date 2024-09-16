import jsonpath
import json
import urllib.request
import urllib.parse

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1726311329458_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'cookie': 'cna=jllsH8s8CD4CAd0NzkTay1bO; xlly_s=1; isg=BOHh3pK1I1WEE48h2OjK8Jgp8K37jlWASMdN2EO2sOhHqgF8i9-FUEHkDNYsZ-24',
    'referer': 'https://www.taopiaopiao.com/?tbpm=3',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

def rm_start(content):
    ss = ''
    is_find_l = 0
    for s in content:
        if s == '(':
            is_find_l = 1
            continue
        if is_find_l == 1 and s != ')':
            ss = ss + s
        if s == ')':
            break
    return ss

data = rm_start(response.read().decode('utf-8'))

with open('data.json', 'w', encoding='utf-8') as f:
    f.write(data)

# <font color = green>*Tips:*</font> 注意，jsonpath只能解析本地文件，因此应该先将读取到的json数据保存到本地，在使用json解析数据

city = json.load(open('data.json', encoding = 'utf-8'))

city_list = jsonpath.jsonpath(city, '$..regionName')

with open('city.txt', 'w', encoding='utf-8') as f:
    n = 1
    for city in city_list:
        f.write(city + '\t')
        if n % 8 == 0:
            f.write('\n')
        n += 1