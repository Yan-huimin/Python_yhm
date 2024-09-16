# <font color = orange>文件读取</font>

<font color = red>**Code**</font>：

```python
#Case_1
try:
    file = open('test.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('waiting......')
    
#Case_2
with(open('test.txt', 'w')) as file:
    file.write(str.decode('utf-8'))
#其中decode为解码，将从网站爬取到的二进制数据解码为字符串类型
```

******

## <font color = blue>文件读取操作</font>

- `r`：读取模式

  - 默认模式，用于读取文件内容，如果文件不存在，会抛出`filenotfounderror`异常

  - For Example: 

    ```python
    with(open('test.txt', 'r')) as file:
    ```

- `w`:写入模式
  - 对对应文件写入相应的内容，如果文件不存在就创建一个新的文件进行写入

- `a`：追加模式
  - 用于在文件末尾追加内容，如果文件不存在，会创建一个新的文件

- `b`：二进制模式
  - 适用于二进制文件，可与其他模式组合使用，如`rb`:读取二进制文件，`wb`：写入二进制文件

- `x`：独占创建模式
  - 仅用于创建新文件，如果文件已经存在，则会抛出`FileExistsError`异常
- `+`:更新模式
  
  - 可与其他模式组合，如`r+`:读写已有文件，如果文件不存在，则抛出异常，`w+`:读写文件，如果文件不存在，那么就创建一个新文件。

<font color = green>*Tips:*</font> 在进行文件的读取的时候尽量使用`with`，这样不仅可以快速捕捉异常，同时可以隐式的释放内存，使用`try-except-finally`则显得过于冗长。

******

# <font color = orange>urllib的基本使用</font>

<font color = red>**Code : **</font>

```python
import urllib.requst

#以百度为例
url = 'https://www.baidu.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

try:
    with(open('maincode.txt', 'w'))
except:
    print('系统正在维护中......')
```

<font color = green>*Tips:*</font> 在这里使用`decode`转码是因为从网站获取的源码为`byte`（二进制）格式，为了使我们能够看懂，应该转换为`utf-8`格式。

******



## <font color = purple>一个类型六个方法</font>

<font color = pink>***一个类型***  ：</font>

```python
import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

print(type(response))

#输出：
#<class 'http.client.HTTPResponse'>
```

`<class 'http.client.HTTPResponse'>`是Python中的一种类，表示通过HTTP协议接收到的响应。它属于`http.client`模块，该模块是用于处理HTTP客户端请求的低级接口。

`HTTPResponse`对象代表通过HTTP请求从服务器接收到的响应。它包含了关于响应的状态、头部信息以及响应体的内容。

***主要属性和方法***

以下是`HTTPResponse`对象中一些常用的属性和方法：

1. **`status`**:
   - 表示HTTP响应的状态码（如200, 404, 500）。
   - 示例：`response.status` 会返回状态码。
2. **`reason`**:
   - 表示HTTP响应状态码的描述（如"OK"对于200，"Not Found"对于404）。
   - 示例：`response.reason` 返回状态描述。
3. **`headers`**:
   - 一个包含响应头部信息的字典类对象。
   - 示例：`response.headers['Content-Type']` 获取内容类型。
4. **`read([amt])`**:
   - 读取响应体中的内容。`amt`是一个可选参数，用于指定读取的字节数。
   - 示例：`content = response.read()` 读取全部内容。
5. **`getheader(name, default=None)`**:
   - 获取指定头部字段的值。
   - 示例：`content_type = response.getheader('Content-Type')`
6. **`getheaders()`**:
   - 返回一个包含所有头部字段及其值的列表。
   - 示例：`headers = response.getheaders()`
7. **`version`**:
   - 表示HTTP协议的版本。
   - 示例：`response.version` 返回HTTP版本（如11表示HTTP/1.1）。

<font color = pink>*六个方法*</font>

- `read`	<font color = red>按字节读取，一个字节一个字节读取，直至结束</font>

- `read(number)`      <font color = orange>返回`number`个字节的内容</font>

- `readline`       <font color = yellow>读取一行并返回</font>

- `readlines`     <font color = green>一行一行读取直至结束</font>

- `getcode `        <font color = blue>获取网站状态（200 ， 404 …）</font>

- `geturl `          <font color = pink>获取网站URL</font>

- `getheaders `    <font color = purple>获取状态信息</font>



```python
import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

content = response.read()

content = response.read(num)

content = response.readline()

content = response.readlines()

content = response.getcode()

content = response.geturl()

content = response.getheaders()
```

## <font color = pink>数据下载</font>

<font color = red>**Code**</font>

```python
import urllib.request

#下载网站
url = 'http://www.baidu.com'

urllib.request.urlretrieve(url, filename = 'baidu.html')

#下载图片
url = 'http://www.图片.com'

urllib.request.urlretrieve(url, filename = '图片.jpg')

#下载视频
url_video = 'https://lf16-fe.resso.me/obj/tos-alisg-v-0000/okcMokFZbABW0MnwDeIm2EIgQeND0MvEKQDQBY'

urllib.request.urlretrieve(url_video, 'video.mp4')

print("下载成功......")
```

<font color = green>*Tips:*</font> 对于`urlretrieve`函数，其中包含两个参数，第一个`url`即为所下载内容的网页地址，第二个`filename`即为下载文件的名称以及他的格式。

******

## <font color = orange>请求对象的定制</font>

正常情况下我们使用以下代码爬取到一个网站的源代码

```python
import urllib.request

url = "http://www.baidu.com"

response = urllib.request.urlopen(url)

content = responses.read().decode('utf-8')

print(content)
```

但是，当我们将`url`改变为`https://www.baidu.com`，这时我们将会发现上面的代码不再能够正常爬取网站的源码，这是因为网站进行了一个很简单的反爬，此时网站察觉到我们在通过一种不合法的手段获取网站的源码，这是我们就需要对自己进行伪装，通过另一种方式进行网页源代码的获取。

![image-20240831134040390](https://github.com/Yan-huimin/Image/blob/main/image-20240831134040390.png)

![图片](C:\Users\Y_hm\Desktop\My_Note\Python_Pa\Image\image-20240831134040390.png)

按照上面的操作，我们获取正常访问网页的ua,然后将自己伪装为正常ua,这样就可以正常爬取网页的源码了。

<font color = red>**Code : **</font>

```python
import urllib.request

url = "https://www.baidu.com"

#在这边定义一个字典类型的容器用于保存正常ua
headers = {
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

#使用另一种方式定制专属访问方式
url_ope = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(url_ope)

content = response.read().decode('utf-8')

print(content)
```

通过专属定制这种方式我们就可以简单的破解这种反爬手段，获取到网页的源码。

******

## <font color = orange>quote方法</font>

`quote`

该方法存在于`urllib.parse`中，在使用时`import`即可

这种方法的作用是将一些字符转换为Unicode编码，下面是例子

```python
import urllib.request
import urllib.parse

url = "https://www.baidu.com/s?wd="

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/128.0.0.0 "
                  "Safari/537.36"
}

name = urllib.parse.quote('周杰伦')

url_ope = urllib.request.Request(url=url + name, headers=headers)

response = urllib.request.urlopen(url_ope)

html = response.read().decode('utf-8')

print(html)
```

在这个例子里面我们将`周杰伦`这三个字转换为Unicode编码`%E5%91%A8%E6%9D%B0%E4%BC%A6`.

******

## <font color = orange>urlencode方法</font>

`urlencode`

位于`urllib.parse`中

用于批量的将一些字符转换为Unicode编码的字符串并使用`&`进行连接

<font color = red>**Code : **</font>

```python
import urllib.request
import urllib.parse

url = "https://www.baidu.com/s?"

data = {
    'wd' : '周杰伦',
    'sex' : '男',
    'location' : '中国台湾省'
}

url += urllib.parse.urlencode(data)

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/128.0.0.0 "
                  "Safari/537.36"
}

request = urllib.request.Request(url=url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
```

******

* 上述代码在运行结束后`url`将会从

> ​	<font color = green>`https://www.baidu.com/s?`</font>

变为

>  <font color = pink>`https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81`</font>

******

后面增加的内容即为使用`urlencode`方法将`data`中的中文字符串转换为Unicode编码并使用`&`连接添加到初始`url`后面。

******

## <font color = orange>post请求访问百度翻译</font>

<font color = red>**Code : **</font>

```python
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

data = {
    'kw': 'spider'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)
```

<font color = green>**Tips : **</font>

* 在使用post进行访问的时候，访问信息，也就是代码中的`data`要将其作为参数传入`Request`函数.
* `data`初始为字典类型，应该使用`urlencode`函数将其转换为Unicode编码，然后再使用`encode`函数将其从Unicode字符串类型转换为`byte`类型的数据

<font color = green>**关于转码函数 ：** </font>

<font color = red>`encode`</font>

> 作用是将一个字符串对象（`str`）转换为字节对象（`bytes`）。在 Python 中，字符串是以 Unicode 形式存储的，而字节对象则表示二进制数据。因此，`encode` 是将字符串按照指定的字符编码转换成对应的字节表示。

<font color = red>**`decode`**</font>

> 作用是将 `bytes` 对象转换回 `str`（字符串）对象。它通常与 `encode` 函数成对使用。

******

## <font color = orange>ajax的get请求获取豆瓣电影数据</font>

<font color = red>**Code : **</font>

```python
import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('movie.json', 'w', encoding='utf-8') as f:
    f.write(content)
```

* `url`获取

  ![image-20240831201234156](C:\Users\Y_hm\Desktop\My_Note\Python_Pa\Image\image-20240831201234156.png)
  
  ![image-20240831201234156](https://github.com/Yan-huimin/Image/blob/main/image-20240831201234156.png)

按照上面步骤即可获取`URL`.

- 在保存数据为json文件时需要注意，`read`方法使用的是gbk编码，但是我们希望将他保存为汉字，那么就需要在`read`里面添加一下参数 : `encoding = 'utf-8'`.

## <font color = orange>文件删除</font>

<font color = green>**Background : **</font>

在下载数据的时候会涉及到某一个内容存在页码数量很多，每一个页码都需要占据一个文件，这样就是的我们在删除文件的时候非常麻烦，因此，我在这里使用了一个`python`代码用来清理这些垃圾文件，因为在爬取数据及的时候为这些文件命名都十分有规律，因此在这里我使用以首字母为`key`进行文件的删除，下面是代码。

<font color = red>**Code : **</font>

```python
import os

def delete_kfc_files(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否以 'kfc' 开头（不区分大小写）
        if filename.lower().startswith('kfc_'):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")


if __name__ == '__main__':
    #这里的路径直接复制绝对路径即可
    #for example: `D:\Python_code\pythonProject`
    folder_path = input("请输入要遍历的文件夹路径: ")
    delete_kfc_files(folder_path)
    print("完成删除操作！")
```

<font color = green>Tips : </font>

> 如果想要实现其他文件的删除，可以对上面的代码进行适当的修改。

## <font color = orange>实现爬取Acwing的网页源代码</font>

首先要获取`url`以及网页的`cookie`和`Referer`.

在这里以Acwing的题库页面为例：

![image-20240831232834675](C:\Users\Y_hm\Desktop\My_Note\Python_Pa\Image\image-20240831232834675.png)

![图片_03](https://github.com/Yan-huimin/Image/blob/main/image-20240831232834675.png)

按照上面的步骤即可获取到我们所需要的信息。

<font color = red>**Code : **</font>

```python
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
```

**异常处理**：

- 当前的异常处理只是简单地打印错误信息。为了更好的调试，可以在捕获异常时打印更多信息，比如堆栈跟踪。可以用 `traceback` 模块来实现：

  ```python
  import traceback
  except Exception as e:
      print(f"An error occurred: {e}")
      print(traceback.format_exc())
  ```

<font color = green>**Result : **</font>

![image-20240831233614201](C:\Users\Y_hm\Desktop\My_Note\Python_Pa\Image\image-20240831233614201.png)

![图片_04](https://github.com/Yan-huimin/Image/blob/main/image-20240831233614201.png)

![image-20240831233632721](C:\Users\Y_hm\Desktop\My_Note\Python_Pa\Image\image-20240831233632721.png)

![图片_05](https://github.com/Yan-huimin/Image/blob/main/image-20240831233632721.png)

<font color = green>Tips : </font>

> 一般我们复制到的`Request Headers`主要包含一下内容：
>
> ```html
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
> Accept-Encoding: gzip, deflate, br, zstd
> Accept-Language: en,zh-CN;q=0.9,zh;q=0.8
> Cache-Control: max-age=0
> Connection: keep-alive
> Cookie: csrftoken=KVUEcZsQ8WSCx1BkJIFQh5lmdqMy25u2Xz4lx9pqN2xxrE9I48ZhLmqPj0wb3pZO; sessionid=9r979bo5oci8qhyfu8f6x5a0n2pxwkls
> Host: www.acwing.com
> Referer: https://www.acwing.com/about/
> Sec-Fetch-Dest: document
> Sec-Fetch-Mode: navigate
> Sec-Fetch-Site: same-origin
> Sec-Fetch-User: ?1
> Upgrade-Insecure-Requests: 1
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
> sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"
> sec-ch-ua-mobile: ?0
> sec-ch-ua-platform: "Windows"
> ```
>
> 其中的
>
> ```html
> Accept-Encoding: gzip, deflate, br, zstd
> ```
>
> 需要注释掉，同时，在爬取信息的时候一般只需要保留`cookie`和`Referer`即可。

:zap:<font color = red>`cookie`</font>

> 该字段通常用于发送存储在客户端（例如浏览器）中的 cookie 数据到服务器。服务器可以使用这些 cookie 来维护会话状态、身份验证信息等。
>
> `Cookie` 包含两个键值对：`csrftoken` 和 `sessionid`。这些通常是与用户会话相关的信息，例如 CSRF 令牌（用于防止跨站请求伪造攻击）和会话 ID。

:zap:<font color = red>`Referer`</font>

> 该字段指示请求来自哪个页面，通常用于服务器跟踪从哪个页面点击了链接以访问当前页面。在某些情况下，服务器可能会根据 `Referer` 验证请求的合法性。
>
> 在上述代码中，`Referer` 被设置为 `'https://www.acwing.com/about/'`，表明请求是从这个 URL 页面发出的。

## <font color = orange>handler的使用</font>

:zap: 通过`handler`获取网页源码

<font color = red>**Code**</font>

```python
import urllib.request
import urllib.parse

url = 'https://www.baidu.com'

#定制headers模拟浏览器向网站发出请求
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

#创建了一个Request对象，将url和headers作为参数传入。Request对象代表一个HTTP请求，允许你附加请求头等信息。
request = urllib.request.Request(url = url, headers = headers)

#创建了一个HTTPHandler对象，这个对象是用来处理HTTP协议的请求。
handler = urllib.request.HTTPHandler()

#使用HTTPHandler创建了一个opener对象，opener用于打开URL并发起请求，处理各种协议（如HTTP、HTTPS）。
opener = urllib.request.bulid_opener(handler)

#使用opener对象打开request，发送HTTP请求到指定的URL（百度），并返回一个response对象。response对象包含了服务器响应的信息。
response = opener.open(request)

#读取服务器响应的内容并进行解码。response.read()会返回字节数据，通过.decode('utf-8')将其解码为UTF-8编码的字符串。
content = response.read().decode('utf-8')

print(content)
```

## <font color = orange>代理的使用</font>

:anguished:为什么上面要使用这么复杂的步骤获取源码呢？下面就来介绍为什么使用这种方式进行源码的获取。

```python
import urllib.request
import urllib.parse

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

url = 'http://www.baidu.com'

#在这里我们使用代理ip进行网站的访问
#注意：ip和headers一样，都是使用字典进行保存
#这里使用ip是美国加利福尼亚的代理ip
ip = {
    'http': '154.203.132.49:8080'
}

handler = urllib.request.ProxyHandler(proxies = ip)

request = urrlib.request.Request(url = url, headers = headers)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.heml', 'w', encoding = 'utf-8') as f:
    f.write(content)
```

在上面的代码中我们不再被动的使用本机的`ip`地址进行网页的访问，我们可以通过`ip`地址的购买，使用代理`ip`进行网页的访问:sunglasses:.

[IP地址购买](https://www.kuaidaili.com/)

## <font color = orange>代理池的使用</font>

一般情况下不可能一直使用一个`ip`进行同一个网站的数据爬取，这时候就需要使用代理池了。

代理池一般情况下是存储在一个列表中

```
ip_pool = [
	{'http': '50.205.202.249:3128'},
	{'http': '12.234.123.421:1244'}
]
```

在使用的时候只需要使用随机数随机出一个列表中的代理进行使用即可

```python
import urllib.request
import urllib.parse
import random

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

ip_pool = [
    {'http': '50.205.202.249:3128'},
    {'http': '12.234.123.421:1244'}
]

ip = random.choice(ip_pool)

url = 'https://ipaddress.my/?lang=zh_TW'

#在这里我们使用代理ip进行网站的访问
request = urllib.request.Request(url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=ip)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(content)
```

<font color = green>*Tips:*</font>主要区别在于使用`random.choice()`函数进行代理的随机选择。

# <font color = orange>Xpath</font>

## <font color = pink>xpath语法:wrench:</font>

- :deciduous_tree:路径查询
  - `//`查找子孙节点，不考虑层级关系
  - `/`查找直接子节点
- :deciduous_tree:关键词查询
  - `//div[@id]`查找含有`id`属性的标签
  - `//div[@id='name']`查找含有`id`属性&&`id="name"`的标签
- :deciduous_tree:属性查询
  - `//@class`查找属性值
- :deciduous_tree:模糊查询
  - `//div[contains(@id, "he")]`
  - `//div[starts-with(@id, "he")]`
- :deciduous_tree:内容查询
  - `//div/h1/text()`
- :deciduous_tree:逻辑运算
  - `//div[@id="name_1" and @class="city"]`
  - `//title | //price`

## <font color = pink>解析本地`html`文件 & xpath语法应用</font>

<font color = red>**Code**</font>

```python
from lxml import etree

tree = etree.parse('文件名称.html')

#查找body下面的ul中的所有li
content = tree.xpath('//body/ul/li')

#查找ul中的含有id属性的li
content = tree.xpath('//ul/li[@id]')

#查找ul中含有的id属性为name_1的li
content = tree.xpath('//ul/li[@id="name_1"]/text()')

#查找ul中含有的id为name_1的li的calss属性值
content = tree.xpath('//ul/li[@id="name_1"]/@class')

#查找ul中含有的id包含name关键字的li标签
content = tree.xpath('//ul/li[contains(@id, "xpath_label")]')

#查找ul中含有的id以关键词xpath开头的li标签
content = tree.xpath('//ul/li[starts-with(@id, "xpath")]/text()')

#查找ul中含有的id以p开头并且class为province的li标签
content = tree.xpath('//ul/li[starts-with(@id, "p") and contains(@class, "province")]/text()')

#查找ul中含有id为name_3或者name_4的li标签
content = tree.xpath('//ul/li[@id="name_3"]/text() | //ul/li[@id="name_4"]/text()')

print(content)
```

所要解析的`html`文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        <li id="name_1_xpath_label" class="city">北京</li>
        <li id="xpath_name_2" class="city">上海</li>
        <li id="name_3" class="city">南京</li>
        <li id="name_4" class="city">武汉</li>
    </ul>
    <ul>
        <li class="province" id="p_1">河南</li>
        <li class="province" id="p_2">河北</li>
        <li class="province" id="p_3">黑龙江</li>
        <li class="province" id="p_4">广东</li>
    </ul>
</body>
</html>
```

当我们运行上面的py代码，会发现出现下面的报错信息：

![xpath_01](C:\Users\Y_hm\AppData\Roaming\Typora\typora-user-images\image-20240912124047408.png)

![图片_06](https://github.com/Yan-huimin/Image/blob/main/xpath_01.png)

:smirk:但是这个错误并不需要担心，这个错误是因为`xpath`严格遵守html的规范，但是我们写的html文件中，有一条语句并没有严格按照html的规范进行书写，下面介绍如何进行更改：

将上面的html代码中的：

```html
    <meta charset="UTF-8">
```

修改为：

```html
    <meta charset="UTF-8"/>
```

加一个`/`的目的是为了标识该标签是自闭合标签。



## <font color = orange>解析服务器响应文件</font>

<font color = red>**Code**</font>

```python
import urllib.request
from lxml import etree

url = 'https://www.baidu.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

#定制请求头文件
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

#获取服务器响应文件
content = response.read().decode('utf-8')

#解析源码数据，因为这里是在线获取的服务器响应文件，因此应该使用xpath.HTML
tree = etree.HTML(content)

my_list = tree.xpath('//input[@id="su"]/@value')

print(my_list)
print(type(my_list))
print(len(my_list))》
```

:clipboard:<font color = green>*Tips:关于`xpath helper`的使用方式*</font>

> ![xPath_02](C:\Users\Y_hm\AppData\Roaming\Typora\typora-user-images\image-20240912142048711.png)
>
> ![图片_07](https://github.com/Yan-huimin/Image/blob/main/xpath_02.png)

:pencil2:<font color = yellow>*`xpath helper`的快捷键可以在扩展管理中进行设置，一般设置为`Ctrl + Shift + X`*</font>

## <font color = pink>:computer:爬取站长网页图片</font>

[图片网址](https://sc.chinaz.com/tupian/ribenmeinv.html)

:heavy_exclamation_mark:这里为了简单，直接爬取网页上的缩略图即可

<font color = red>**:trident:Code**</font>

```python
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
```

:ghost:上面的代码主要分为三步：

​	:one: 定制请求

​	:two: 获取源码

​	:three: 下载图片

下面对这三个步骤进行解析：

<font color = yellow>**Step_1:**</font> 										:cherry_blossom:定制请求

> - 首先我们需要一个`ua`，这个获取很简单，随便打开一个网页即可获取，需要注意的是这个`ua`需要存储在一个字典容器中。
>
>   - ```python
>     headers = {
>         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
>     }
>     ```
>
> - 其次我们需要获取网页的`url`，但是这次不是单纯的一个`url`，而是好几页的`url`，那么我们应该怎么做呢？:anguished:
>
>   - 首先观察每一个页面的`url`，
>
>     > ```python
>     > # https://sc.chinaz.com/tupian/ribenmeinv.html    第一页
>     > # https://sc.chinaz.com/tupian/ribenmeinv_2.html  第二页
>     > # https://sc.chinaz.com/tupian/ribenmeinv_3.html  第三页
>     > # https://sc.chinaz.com/tupian/ribenmeinv_4.html  第四页
>     > ```
>     >
>     > 我们发现这个`url`还是非常有规律的，这样我们就可以很快的写出一个简单的小算法来组合出不同页面的`url`，我们唯一需要知道的就是这个页面的起始页码和终止页码即可:sunglasses:。

<font color = yellow>**Step_2:**</font> 										:cherry_blossom:获取源码

> :tipping_hand_man:这里需要注意的是因为我们要爬取许多页的图片，每一页都对应一个`url`，上面第一部我们已经分析过了，这里我们可以使用`urllib()`函数进行`url`的连接。关于`urljoin()`函数的用法可以在网上查到，这里就不再重复了，贴一个地址：[How to use urljoin](https://stackoverflow.com/questions/10893374/python-confusions-with-urljoin)       

<font color = yellow>**Step_3:**</font> 										:cherry_blossom:下载图片

>:broken_heart:这一步就稍微有点儿难度了……
>
>首先我们需要使用`etree`去解析获取到的源码`content`.因为上面学的是`xpath`，所以在这里我们就使用`xpath`进行网页源码的解析操作，这一步骤需要在你的浏览器上安装`xpath hepler`这个插件，同时需要在你的`pycharm`或者`vscode`上安装`lxml`这个包。
>
>![xpath_03](C:\Users\Y_hm\AppData\Roaming\Typora\typora-user-images\image-20240912201935337.png)
>
>![图片_08](https://github.com/Yan-huimin/Image/blob/main/xpath_03.png)
>
>在上面的图片中我使用的是过滤解析源码中的`src`数据，可以看到左侧已经册成功显示出解析出来的源码。
>
><font color = red>**:heavy_exclamation_mark:但是我们会发现左侧的src与我们想要的完全不一样，这是因为该网页使用了懒加载，因此我们在代码书写的时候，应该根据具体爬取到的源码进行适当的修改**</font>
>
>那么我们应该怎么样进行修改呢？:eyes:
>
>正常情况下我们的代码应该是
>
>```python
>src = tree.xpath('//div[starts-with(@class, "item")]//img/@src')
>```
>
>但是，上面我们已经提到了，直接使用`src`是不行的，这时候我们可以根据爬取到的源码进行观察，我们会发现源码中的`data-original`这个属性的内容与我们在网页上看到的对应图片的`src`一致，这样子，我们就可以通过适当修改`xpath`语句从而获取到真实的`src`，而不是一个空白图片。
>
>```python
>src = tree.xpath('//div[starts-with(@class, "item")]//img/@data-original')
>```
>
>当然，以上的代码分析以及修改只是针对我上面所举出的例子，真正在我们自己书写代码的时候我们应该根据情况自己适当的修改我们的代码。
>
>​															:wavy_dash: 以上是关于源码解析的内容 :wavy_dash:
>
>源码解析之后我们就可以进行最后的一步了。
>
>当我们想要使用`py`进行图片的保存的时候，我们会想到哪一个函数？没错，就是`urlretrieve()`函数，这个函数是在`urllib.request`中的，因此在使用之前需要导入一下这个东西。
>
>对于`urlretrieve()`函数，它包含两个参数，一个是`url`,另一个是`filename`，其中的`url`即为每一个图片对应的`src`，另一个`filename`就是图片的保存名称以及图片的保存位置。
>
>:star:<font color = green>*Tips:*</font>这里如果想将图片保存到指定的文件夹当中，应该使用绝对路径。
>
>关于`url`的组合上面已经介绍了，直接使用`urljoin()`函数进行字符串的拼接即可，当然，`urljoin`的用法还是比较多的，使用前建议详细查看一下使用介绍。
>
>我们观察上面的每一个图片的`url`会发现，每一个`url`最后四个字符即为这张图片的格式后缀，这样就方便下面的为每一张图片的命名了。
>
>我们截取每一个图片的`src`字符串的最后四位字符`file_ext = src[i][-4:]`,将它作为每一张图片的后缀名，每一张图片的名称我们就直接使用网站内的明明，也就是其中的`alt`标签，字符串的拼接直接使用`+`即可。

<font color = red>*Tips:*</font> 上面的代码中使用到了一部分的递归，这是因为在爬取的过程中，当我们使用同一个`ip`地址大量访问该页面就会导致`ip`被拒绝访问，出现下面的错误：

```
urllib.error.urlerror: <urlopen error [winerror 10054] 远程主机强迫关闭了一个现有的连接。>
```

因此，在这里为了避免程序因为这种情况直接退出，我们在每次捕捉到异常的时候重新调用这个函数，直至图片成功下载位置，在这里我尝试限定最大递归次数来避免程序的崩溃，但是后面发现是我多虑了，即使不设置最大递归次数限制，我们在递归两次最有即可成功下载图片，但是当我们在设置递归次数限制后反而又会出现上面的错误，因此在这里我并没有设置，这个问题有待进一步的思考。:expressionless:

# <font color = orange>jsonpath</font>

<font color = green>*Tips:*</font> 因为`jsonpath`的语法与`xpath`类似，所以在这里我就没有在进行总结了，需要的话可以去网上找。

:telescope:[贴一个链接](https://blog.csdn.net/mouday/article/details/107928131)

这里我使用一个案例来介绍`jsonpath`如何使用。

<font color = red>**`Jsonpath`解析淘票票网页的地名**</font>

![json_01](C:\Users\Y_hm\AppData\Roaming\Typora\typora-user-images\image-20240914195826351.png)

![json_02](https://github.com/Yan-huimin/Image/blob/main/json_01.png)

我们通过捕捉点击那个黑三角获取到的`json`数据进行爬取。

![json_02](C:\Users\Y_hm\AppData\Roaming\Typora\typora-user-images\image-20240914200223128.png)

![json_02](https://github.com/Yan-huimin/Image/blob/main/json_02.png)

但是当我们使用浏览器访问这个地址会发现：

```json
jsonp109({"returnCode":"0","returnValue":{}});
```

这是因为他进行了一些反爬操作。

下面是代码：

<font color = red>**Code**</font>

```python
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
    if_find_r = 0
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

#<font color = green>*Tips:*</font> 注意，jsonpath只能解析本地文件，因此应该先将读取到的json数据保存到本地，在使用json解析数据

city = json.load(open('data.json', encoding = 'utf-8'))

city_list = jsonpath.jsonpath(city, '$..regionName')

with open('city.txt', 'w', encoding='utf-8') as f:
    n = 1
    for city in city_list:
        f.write(city + '\t')
        if n % 8 == 0:
            f.write('\n')
        n += 1
```

我们在headers中添加cookie和referer即可破解。

我们打印我们获取到的json数据会发现是这样子的：

```json
jsonp109({"returnCode":"0","returnValue":{"A":[{"id":3643,"parentId":0,"regionName":"阿坝","cityCode":513200,"pinYin":"ABA"},{"id":3090,"parentId":0,"regionName":"阿克义","cityCode":520300,"pinYin":"ZUNYI"}]}});

```

因为中间的内容太多了，所以在这里我就把中间的大部分内容给删除了，这里只是展示了开头和结尾的部分内容。

我们会发现开头和结尾分别有一个：

:star: <font color = yellow>*Start*</font>

```json
json109(
```

:star2: <font color = yellow>*End*</font>

```json
);
```

只要我们把这两个东西给他去掉我们就可以得到正确的json数据了。

在上面的代码中我是用了一个`rm_start()`函数来进行这个操作，但是因为Pyhton本身就非常强大，我们同样也可以使用Python中的工具进行分割字符串：

```python
content = "json......"

content = content.split('(')[1].split(')')
```

使用上面这段代码同样可以获得相同的效果，至于原因，可以看看[Python_split](https://www.runoob.com/python/att-string-split.html)。

:speech_balloon: 注意，`jsonpath`只能解析本地的数据，因此我们需要将处理得到的`json`数据保存到本地，再使用`jsonpath`进行解析。

这里我们需要获取的是所有的地名，就是`json`数据中的`regionName`，解析方式就是`$..regionName`，获取所有的`Name`即可。



# <font color = orange>Bs4爬取高清图片</font>

:revolving_hearts: 个人认为`bs4 + xpath helper`最好用的，但是前提是你得会用`xpath`，当然`xpath`也非常好用。

下面是我的关于`bs4`解析`html`文件的一些代码总结，仅供参考。

<font color = red>**Html Code**</font>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <div>
        <ul>
            <li id="per">张三</li>
            <li id="per_1">李四</li>
            <li id="per_2">王五</li>
            <a href="http://www.google.com" id="Google">谷歌</a>
            <a href="", class="city">北京</a>
            <a href="", class="city">上海</a>
        </ul>
        <li>test</li>
        <a href="">百度</a>
        <a href="">必应</a>
        <ul>
            <span name="red">红色</span>
            <span name="blue">蓝色</span>
            <span name="green">绿色</span>
        </ul>
    </div>
</body>
</html>
```

<font color = red>**Py Code**</font>

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4_test.html', encoding='utf-8'), 'lxml')

# 找到的是第一个符合条件的a标签
# print(soup.a)

# attrs获取标签的属性和属性值
# print(soup.a.attrs)

# find()函数
# 返回的是第一个符合条件的数据
# print(soup.find('a'))
# print(soup.find('a', class_='city'))

# find_all()函数
# 返回的是符合条件的所有数据
# print(soup.find_all('li'))

# print(soup.find_all(['a', 'span'], limit=6))


# select()函数

# 返回的是所有符合条件的标签
# print(soup.select('a'))

# 类选择器，使用.来进行class筛选
# print(soup.select('.city'))

# 类选择器，使用#来进行id的筛选
# print(soup.select('#per_2'))

# 属性选择器
# print(soup.select('li[id]'))
#
# print(soup.select('li[id="per"]'))

# 层级选择器 <space>表示选择后代
# print(soup.select('div li'))

# 子代选择器 a > b
# 选择某标签的第一级子标签
# print(soup.select('div > li'))
# print(soup.select('div > ul > li'))

#选择所有的a标签和li标签
# print(soup.select('a, li'))

# id_list = soup.select('a, li')
# for id in id_list:
#     print(id.string)

# print(id_list[0].get_text())

# 如果选定的标签下面不存在其他标签，那么string和get_text函数均可以获取到标签下面的内容
# 但是，如果标签下面存在其他的标签，那么string函数将无法获取到标签下面的内容，但是get_text函数可以获取到。
# 因此，一般情况建议使用get_text函数

# name返回的是标签的名称(a, p, span, div, ......)
# attrs则是将这个标签的所有属性值作为字典进行返回
# l_list = soup.select('div > ul > span')
# for i in l_list:
#     print(i.name)
#     print(i.attrs)
#     print(i.get_text())

# 因为attrs返回的是一个字典，所以可以直接是使用get函数获取某个属性的内容
# 下面的三种方式均可以获得想要的属性内容
# l_list = soup.select('div > ul > span')
# for i in l_list:
#     print(i.attrs.get('name'))
#     print(i.get('name'))
#     print(i['name'])
```

:speech_balloon: 一般在解析网页的时候都是使用`select()`函数。

下面是使用`bs4`爬取站长素材网站的风景图片网页的所有图片的案例[风景图片](https://sc.chinaz.com/tupian/fengjingtupian.html)。

:traffic_light: 上次我们使用`xpath`只是获取到了这些图片的缩略图，但是这样子是肯定不行的，缩略图拿来什么用都没有，所以这一次我们直接使用`bs4`解析获取每一张图片的高清图片。

二话不说，先上代码：

<font color = red>**Code:**</font>

```python
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import socket
import time

# https://sc.chinaz.com/tupian/fengjing.html
# https://sc.chinaz.com/tupian/fengjing_2.html


# # //div[contains(@class, "container")]//div[@class="right-div tupian-right-div"]//div/p[@class="bg-bull btn-p com-right-down-btn"]/a
# # //div[@class="item masonry-brick"]/div/a
# # //div[@class="container"]//div[@class="bot-div"]/a


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
            time.sleep(2)  # 暂停 2 秒后重试 这里可以自定义，不一定必须是2s
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
```

我这里解析的是服务器数据，如果需要解析本地文件，可以使用下面代码：

```python
soup = Beautiful(open('file_path + file_name', encoding='utf-8'), 'lxml')
```

:soon: 下面就来分析上面的代码是如何进行数据解析的。

首先我们需要的便是这个网站的`url`，我们可以通过浏览器的检查功能获取到每一页的`url`：

```asciiarmor
# https://sc.chinaz.com/tupian/fengjing.html
# https://sc.chinaz.com/tupian/fengjing_2.html
```

:cherry_blossom:观察上面的`url`我们会发现她和我们上次分析的一样，第一页不需要进行操作，从第二页往后，每次都是在基础`url`的基础上增加`“_str(page)”`，这样子我们就很容易获取到这个网页每一页的`url`了。

:cherry_blossom:然后便是访问每一页`url`来获取到每一张图片的真实地址，那么我们就需要进行访问对象的定制了，我们这里直接在`headers`里面放入`cookie`和`referer`就可以正常进行访问了。

```python
headers = {
    'cookie': '_clck=pstu63%7C2%7Cfp4%7C0%7C1716; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1726122656,1726141579,1726314568; HMACCOUNT=22173AC77CF84B49; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1726324824',
    'referer': 'https://sc.chinaz.com/tupian/'
}
```

这样我们就可以通过对象定制访问到这个网页，那么接下来我们就可以获取网页的源码了，这时，好玩儿的东向西就来了，这个网页是动态加载的，这意味着我们在线访问到的网页的源码与我们爬取下来的网页源码是存在差别的，而这样的差别也会导致我们在进行网页数据解析的时候出现问题。

一开始在在线网页进行解析，对应数据的`xpath`语句应该是

```python
//div[@class="item masonry-brick"]/div/a
```

但是如果按照这样的`xpath`语句，那么你将无法访问到真实的网页，甚至你无法获取到他的网页`url`，这时应该怎么办呢?

因为我目前还没有学习对于动态网页的源码爬取，这时我想到了一种方法，我们先将源码给爬取下来保存到本地的`html`文件中，然后我们运行此程序，根据运行获得的网页再次进行`xpath`解析，这样子我们就可以正常获取到我们想要的内容了。

```python
//div[@class="container"]//div[@class="bot-div"]/a
```

这是我根据爬取到的源码再次进行数据解析获取的`xpath`语句，我们发现这两个`xpath`语句存在很大差异，因此在网页源码爬取的时候应该没写一个小的功能函数，然后输出一下看看这个函数的功能是否和我们预期的一样。

获取到源码后我们需要获取那个高清图片页面的`url`，上次我们获取到的只是缩略图的`src`地址，但是这次我们的目标是所有的高清图片，肯定不能只是满足于`src`。

我想到了一种方法，我们从则会个页面的源码中解析出每一个下载高清图片的页面的`url`，然后我们再通过模拟浏览器访问这个页面爬取到这个下载页面的源码，我们再根据下载页面源码解析出高清图片下载的真实地址。

​															<font color = pink>*理论成功，那么我们就开始实践！*</font>

这时我们需要注意与上面相同的问题，我们爬取到的源码与在线页面的源码存在差异，因此我们应该根据源码适当调整我们的`xpath`语句。

在获取到图片的下载链接之后我们便可以着手进行图片的下载了，图片下载已经再熟悉不过了，直接使用`urlretrieve()`函数就可以了。

这里是`bs4`的练习，那么我们就需要根据`xpath`语句，将其翻译为`bs4`语句就OK了。

经过上面的操作步骤，我们就可以成功获取到页面的<font color = red>**某些**</font>高清图片了。

:question: 为什么是某些呢？

这里就涉及到一些异常处理的问题了，首先解释一下下面这段代码的作用：

```python
import socket

socket.setdefaulttimeout(20)
```

:triangular_ruler:这行代码的主要作用是**为全局的网络操作设置一个默认的超时时间**。在这个例子中，它将超时时间设定为 20 秒。这意味着通过 `urllib` 或其他库进行的所有网络连接（如 HTTP 请求）将等待最多 20 秒来尝试与目标服务器建立连接或接收数据。如果超过 20 秒没有成功连接或接收到数据，连接将被视为超时，并抛出一个 `socket.timeout` 异常。

<font color = green>*主要作用：*</font>

1. **防止长时间挂起**：当程序执行网络请求时，如果没有设置超时时间，网络操作可能会因为网络问题（如服务器无响应、网络堵塞等）而无限期地等待响应。`socket.setdefaulttimeout(20)` 能确保程序在 20 秒后停止等待，避免长时间挂起。
2. **异常处理**：如果连接超时，程序会抛出 `socket.timeout` 异常，开发者可以捕获并处理这个异常，避免程序崩溃，或根据需要进行重试等操作。

### 知识延展：

#### 1. **超时设置的灵活性**：

- `socket.setdefaulttimeout()` 设置的是**全局的默认超时时间**。所有通过 `urllib` 或 `httplib` 等使用 `socket` 进行的网络连接都将应用此超时设置。

- 你也可以在具体的网络操作中手动设置超时。例如：

  ```python
  urllib.request.urlopen(url, timeout=10)
  ```

  这行代码会为单个`urloepn`请求设置超时为 10 秒，而不会影响其他网络请求的超时时间。

#### 2. **超时的类型**：

- **连接超时（Connection Timeout）**：指客户端与服务器建立连接的时间。如果在设定的时间内无法成功连接服务器，则会触发超时。
- **读超时（Read Timeout）**：指客户端与服务器成功建立连接后，等待服务器响应数据的时间。如果在设定时间内服务器没有返回数据，则会触发超时。

#### 3. **与重试机制的结合**：

通常情况下，超时与网络请求的重试机制结合使用。当某次网络请求超时时，可以尝试重试以应对临时的网络问题。比如爬虫程序中，超时后可以重试下载图片，防止由于某个请求失败导致整个程序终止。

#### 4. **默认超时 vs 无超时**：

- 如果不设置 `socket.setdefaulttimeout()` 或 `timeout` 参数，网络库默认是**没有超时限制的**。这意味着网络请求可能会无限期挂起等待。
- 设置合适的超时时间非常重要，特别是在构建爬虫、数据抓取工具或者其他需要大量网络请求的应用时。

#### 5. **异常处理**：

当设置了超时后，你可以通过捕获 `socket.timeout` 或 `urllib.error.URLError` 异常来处理超时问题：

```python
pythonCopy codetry:
    response = urllib.request.urlopen(url, timeout=10)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("连接超时")
```

### 延展示例

假设我们在爬取网页时遇到不稳定的网络连接，超时设置可以与重试机制结合，避免因为一次超时导致整个程序停止。下面是一个简化的例子：

```python
pythonCopy codeimport urllib.request
import socket

socket.setdefaulttimeout(10)  # 全局超时设置为 10 秒

def fetch_url(url, retries=3):
    while retries > 0:
        try:
            response = urllib.request.urlopen(url)
            return response.read()
        except socket.timeout:
            print(f"连接超时，剩余重试次数: {retries}")
            retries -= 1
            if retries == 0:
                print("多次重试后仍然失败，停止请求。")
                return None

url = 'http://example.com'
content = fetch_url(url)
```

在这个例子中，如果请求 `url` 时发生了超时，程序会重试最多 3 次。在超过重试次数后，程序放弃请求并返回 `None`。

在最上面的爬取图片的代码中，我使用的是每一次访问图片链接的时候进行异常捕获，最多尝试三次，超过三次将会自动跳过本图片的下载。

我们在自己书写爬虫代码的时候一定要注意异常捕获的操作，这在很大程度上可以提升我们代码的鲁棒性。

# <font color = orange>Selenium</font>

```python
import time

from selenium import webdriver

# 这个By一定要手动导入，否则虽然可以直接使用，但是发生报错
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com'

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

btn = driver.find_element(by=By.ID, value='kw')

btn_search = driver.find_element(by=By.ID, value='su')

# 获取标签的名称，而不是value
# print(btn.tag_name)

time.sleep(2)

btn.send_keys('周杰伦')

btn_search.click()

# 尽量在每一个操作之后都休眠一段时间，否则会出现某些指令无法正常执行
time.sleep(2)

# 屏幕下滑
to_end = 'document.documentElement.scrollTop=100000'
driver.execute_script(to_end)

time.sleep(2)

btn_next_page = driver.find_element(by=By.CLASS_NAME, value='n')

btn_next_page.click()

time.sleep(2)

driver.execute_script(to_end)

time.sleep(2)

driver.back()

time.sleep(2)

driver.forward()

time.sleep(2)

driver.quit()
```

这段代码的作用就是模拟浏览器，并且使用代码控制浏览器进行操作：

向百度的搜索框中输入`周杰伦`，随后点击百度一下进行检索，到达页面后休眠两秒，滑动至页面底端，点击下一页，再从第二页滑动至页面的底端，再返回第一页，再返回第二页。	:joy:

上面的代码会使得代码自己启动浏览器，但是这样子会导致反应速度很慢，因此这里就有了`handless chrome`的概念，大致意思就是同样会执行上面的操作，但是不会再桌面上显示出整个过程，通过下面一段代码来介绍则这个东西。

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
#
# browser = webdriver.Chrome(options=chrome_options)

url = 'https://www.baidu.com'

def share_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    browser = webdriver.Chrome(options=chrome_options)
    return browser

my_b = share_browser()

my_b.get(url)

my_b.save_screenshot('screenshot.png')
```

上面代码的效果就是访问百度首页并且截取一张图片再退出，这张图片将保存在本地。

如果按照一开始那种操作方式，这个过程我们是可以看到的，但是通过上面这段代码，我们就可以隐式的完成相关操作（用这种方式主要是运行效率更高）。

上面的函数是将一个固定的内容进行了封装，我们在每次使用的时候将这个函数调用直接生成一个`browser`对象就可以直接使用了，这里封装起来就非常方便了。

# <font color = orange>requests</font>

```python
import requests

url = 'https://www.baidu.com'

response = requests.get(url)

# 一个类型：<class 'requests.models.Response'>
# print(type(response))

# 六个方法

# 1. 获取网页的源码(字符串格式)
# print(response.text)

# 2. 访问或定制编码格式
# response.encoding = 'utf-8'
# print(response.text)

# 3. 获取请求的url
# print(response.url)

# 4. 响应的字节类型,返回的是二进制的数据
# print(response.content)

# 5. 返回状态码 (200, 404, 502, ......)
# print(response.status_code)

# 6. 返回响应的头信息
# print(response.headers)
```

## <font color = yellow>Get请求</font>

```python
import requests

url = 'https://www.baidu.com'

headers = {
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

data = {
    'wd': '周杰伦'
}

# def get(url, params=None, **kwargs):
# url 请求资源的路径
# params 参数
# kwargs 字典，传入headers
response = requests.get(url=url, params=data, headers=headers)

response.encoding = 'utf-8'

print(response.text)
```

## <font color = yellow>Post请求</font>

```python
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
```





























































