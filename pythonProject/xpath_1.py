from lxml import etree

tree = etree.parse('test_html.html')

# content = tree.xpath('//body/ul/li')

# content = tree.xpath('//ul/li[@id="name_1"]/text()')

#查找ul中含有的id为name_1的li的calss属性值
# content = tree.xpath('//ul/li[@id="name_1"]/@class')

# #查找ul中含有的id包含name关键字的li标签
# content = tree.xpath('//ul/li[contains(@id, "xpath_label")]/text()')

# #查找ul中含有的id以关键词xpath开头的li标签
# content = tree.xpath('//ul/li[starts-with(@id, "xpath")]/text()')

#查找ul中含有的id以p开头并且class为province的li标签
# content = tree.xpath('//ul/li[starts-with(@id, "p") and contains(@class, "province")]/text()')

#查找ul中含有id为name_1或者name_2的li标签
content = tree.xpath('//ul/li[@id="name_3"]/text() | //ul/li[@id="name_4"]/text()')

print(content)
print(len(content))
print(type(content))
