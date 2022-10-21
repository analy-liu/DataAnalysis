---
title:  函数实现-腾讯文档表格抓取
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# 1. 腾讯文档表格抓取函数

共享文档是工作中常用的工具，其中腾讯文档的共享表格，是很多人都在用的。  
有些表格，经常需要获取上面的数据信息，每次都打开链接导出表格很麻烦。  
这时python爬虫脚本可以提高你的工作效率，结合任务计划程序来定时的获取数据到本地表格，之后还可以通过企业微信机器人发送到特定群组中。

## 1.1 函数说明
示例腾讯文档链接

[https://docs.qq.com/sheet/**DRXpPcW10Q1p4bFBE**?tab=**BB08J2**&u=f754a513e0104b3cbffa015b5b6f074c](https://docs.qq.com/sheet/DRXpPcW10Q1p4bFBE?tab=BB08J2&u=f754a513e0104b3cbffa015b5b6f074c)

加粗部分就是函数的两个参数  
table_id = DRXpPcW10Q1p4bFBE  
sheet_id = BB08J2  

注意1：仅支持读取不含公式的表格，并且表格中无空值
注意2：腾讯文档的权限，至少需要有所有人可查看的权限

## 1.2 函数
```python
def docqqAPI(table_id,sheet_id = None):
    """
    作者：AnalyZL（github:https://github.com/analy-liu)
    """
    import time
    import pandas as pd
    import requests
    import json
    if sheet_id == None:
        sheet_id = 'BB08J2'
    headers = {'referer':"https://docs.qq.com/sheet/{}?tab={}".format(table_id,sheet_id),
          'authority' : "docs.qq.com",
          'accept' : "*/*"}
    success = 0
    num = 0
    while success == 0:
        try:
            # 获取腾讯文档信息
            r = requests.get('https://docs.qq.com/dop-api/opendoc?tab={}&id={}&outformat=1&normal=1'.format(sheet_id,table_id),headers=headers)
            text = json.loads(r.text)
            text = text['clientVars']['collab_client_vars']
            text_keys = list(text['initialAttributedText']['text'][0][-1][0]['c'][1].keys())
            doc = text['initialAttributedText']['text'][0][-1][0]['c'][1].values()
            doc = pd.DataFrame(doc)["2"]
            doc = doc.dropna()
            # 获取最大列数
            try:
                maxCol = 0
                while text_keys[maxCol]==str(maxCol):
                    maxCol+=1
                text_keys[maxCol]
            except:
                maxCol = 0
                while True:
                    try:
                        doc[maxCol]
                        maxCol+=1
                    except:
                        break
                if len(doc) == maxCol:
                    maxCol = text['maxCol']
                doc = doc.reset_index(drop=True)
            # 生成DataFrame
            data = []
            temp = []
            for i in range(len(doc)):
                try:
                    temp.append(doc[i][1])
                except:
                    temp.append(doc[i])
                if (i)%maxCol == maxCol-1:
                    data.append(temp)
                    temp = []
            doc = pd.DataFrame(data = data[1:],columns=data[0])
            doc = doc.loc[:,[x for x in doc.columns if not pd.isnull(x)]]
            success = 1
        except:
            time.sleep(1)
            num += 1
            print('再次尝试获取',num)
    return doc
```

## 1.3 函数调用
```python
from docqqAPI import docqqAPI
# 不删除任何行列测试
df = docqqAPI('DRXpPcW10Q1p4bFBE',sheet_id = 'BB08J2')
# 删除空白行列测试
df = docqqAPI('DRXpPcW10Q1p4bFBE',sheet_id = 'i4a0k6&u')
```