---
title:  requests爬虫
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# requests使用

```python
# 包导入
import requests
```

## 1. get使用

```python
requests.get(
    url: str | bytes,   
    params: SupportsItems | Tuple | Iterable | str | bytes | None = ..., 
    **kwargs) -> Response

# 简单使用(只使用url参数)
target_url = 'https://github.com/'
r = requests.get(target_url)

# 进阶使用(使用params参数)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("'https://www.google.com.hk/search", params=payload)
# r.url的输出为：
# 'https://www.google.com.hk/search?key2=value2&key1=value1'

# 详细使用(使用**kwargs)
proxy = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'Cookie':'',
    'Host':'',
    'Referer':'',
    'Accept': 'application/json, text/javascript, */*; q=0.01'
}
## 设置头部信息，代理ip，不使用证书
r = requests.get(target_url, verify=False, headers=header, proxies=proxy) 
```
## 2. post使用

```python
requests.post(url, data=None, json=None, **kwargs)

# url: 必填
# data与json 根据请求头中的Content-Type情况选择一个输入
payload_str = 'ATest=0001&BTest=0002' # 字符串格式参数
payload_dict = {'ATest':'0001','BTset':'0002'} # 字典格式参数
if headers['Content-Type'] == 'application/x-www-form-urlencoded':
    # 使用data参数，传入str
    requests.post(url, data=payload_str, headers=headers)
elif headers['Content-Type'] == 'application/json':
    # 使用json参数，传入dict
    requests.post(url, json=payload_dict, headers=headers)
```
通常会需要将字符串格式的json与字典格式互转，下面是使用json包进行互转的代码
```python
import json
# dict转json
json_data = json.dumps(dict_data)
# json转dict
dict_data = json.loads(json_data)
```

## 3. 返回值描述

返回值通常命名为 r 或 response

|代码|描述|
|:-|:-|
|**r.status_code**|响应状态码|
|**r.raw**|原始响应体，使用r.raw.read()读取|
|**r.content**|字节方式的响应体，需要进行解码|
|**r.content.decode**|("编码格式") 当编码格式与响应头部的字符编码相同时，内容与r.text|
|**r.text**|字符串方式的响应体，会自动更具响应头部的字符编码进行解码|
|**r.headers**|以字典对象储存服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在，则返回None|
|**r.json()**|request中内置的json解码器|
|**r.raise_for_status()**|请求失败(非200响应)，抛出异常|
|**r.url**|获取请求的url|
|**r.cookies**|获取请求后的cookies|
|**r.encoding**|获取编码格式|