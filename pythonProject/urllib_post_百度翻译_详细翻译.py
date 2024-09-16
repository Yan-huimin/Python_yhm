import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/transapi'

headers = {
    "cookie": "BAIDUID=2248FF922462CE166C6623E192781BD1:FG=1; BDUSS=XpQelB5UkJwTVVaZVlqWUhvaGI1UjBmNFFpczAydy1JQ0dWREhVMkZuQ3Z1dFZtSVFBQUFBJCQAAAAAABAAAAEAAADUDRb8zOy3xcfnwcvTtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK8trmavLa5mL; BDUSS_BFESS=XpQelB5UkJwTVVaZVlqWUhvaGI1UjBmNFFpczAydy1JQ0dWREhVMkZuQ3Z1dFZtSVFBQUFBJCQAAAAAABAAAAEAAADUDRb8zOy3xcfnwcvTtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK8trmavLa5mL; newlogin=1; BIDUPSID=2248FF922462CE166C6623E192781BD1; PSTM=1725025134; H_PS_PSSID=60448_60628_60663_60678_60681_60699; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=2248FF922462CE166C6623E192781BD1:FG=1; delPer=0; PSINO=7; BA_HECTOR=a58l250k0l8l01ag010hal8gb35vuo1jd5d9d1u; ZFY=:A4opcR9:BC9I:BSvxV7GGs2nXOFoacQ82yQKVwIy5IHWQ:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; ab_sr=1.0.1_YzEzMTEyM2MwNjVkY2U1NjlmMTFkYmU2OTE5M2UxOWQyNTcxNjZiMjY1ZTA4MzgyZTUxMjJiNTQ3ZTEwZTA1OGQ5NmRhMmVlNzRlYmRkYzAyZGZmZDdjZmRkOTZkMTQ0NTEyNjZhNGVmOWIwZDExMGY0ZTBmZWVlNjdlZmMzZjcwMGM2MzdkNTQ3MDBjZmFjNzU2ZDRhZjg5ODI1ODdmYQ=="
}

data = {
    'from': 'en',
    'query': 'spider',
    'source': 'txt',
    'to': 'zh'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url = url, data = data, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)















