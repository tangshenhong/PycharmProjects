# 获取html内容字符串，进行分析
with open('bs1.html',encoding='utf8') as f:
    html_doc = f.read()

# 导入 BeautifulSoup
from bs4 import BeautifulSoup

# 指定用html5lib来解析html文档
soup = BeautifulSoup(html_doc, "html5lib")

# print(soup.title)
# print(soup.find('title'))
#获取标签名
# print(soup.meta.name)
# 获取 tag文本内容
# print(soup.title.string)
#也可以
# print(soup.title.get_text())
# 如果要获取 tag 的父节点tag
# print(soup.title.parent)
# print(soup.title.parent.name)

# 如果要获取元素的属性值
# print(soup.div['id'])
# print(soup.p['style'])

# print(soup.find_all('a')[1])

print(soup.find('a',href="http://example.com/lacie",id="link2"))

