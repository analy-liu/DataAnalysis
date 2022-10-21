---
title:  lxml-解析html
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# lxml使用

lxml是一个Python库，使用它可以轻松处理XML和HTML文件，还可以用于web爬取。

## 1. 卸载与安装

```
# 卸载
pip uninstall lxml
# 安装  
python -m pip install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 2. 基本语法

```python
from lxml import etree

# 根据html字符串建立html_xml, 这里使用requests.get的返回值
html_xml = etree.HTML(r.text)
target_element = html_xml.xpath('xpath')
```

## 3. 使用示例

示例html

```html
<!DOCTYPE html>\n<html lang="zh-CN">
<head>
</head>
<body>
    <ul id="menu" class="menu">
        <li><a title="1" href="https://www.1.com">一</a></li>
        <li><a title="2" href="https://www.2.com">二</a></li>
        <li><a title="3" href="https://www.3.com">三</a></li>
    </ul>
    <ul id="text" class="text">
        <li><a title="1" href="https://www.text1.com">text一</a></li>
        <li><a title="2" href="https://www.text2.com">text二</a></li>
        <li><a title="3" href="https://www.text3.com">text三</a></li>
    </ul>
</body>
</html>
```

查找html内容

```python
#获取id="menu"的ul中的所有href
target_element = html_xml.xpath('\\ul[@id="menu"\li\a\@href')
# 返回
["https://www.1.com","https://www.2.com","https://www.3.com"]

#获取id="text"的ul中的倒数第二个文本内容
target_element = html_xml.xpath('\\ul[@id="text"\li[last()-1]\a\text()')
# 返回
["text二"]
```