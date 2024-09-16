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
