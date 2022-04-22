
 # python中pandas包使用笔记
- [python中pandas包使用笔记](#python中pandas包使用笔记)
  - [1. 包导入](#1-包导入)
  - [2. 数据IO](#2-数据io)
    - [2.1. 数据导入](#21-数据导入)
    - [2.2. 数据导出](#22-数据导出)
      - [2.2.1. pd.read_csv()参数](#221-pdread_csv参数)
    - [2.3. 数据导出](#23-数据导出)
      - [2.3.1. df.to_csv()参数](#231-dfto_csv参数)
  - [3. 数据查看](#3-数据查看)
  - [4. 数据操作](#4-数据操作)
    - [4.1. 数据切片](#41-数据切片)
      - [4.1.1. df.loc用法](#411-dfloc用法)
      - [4.1.2. df.iloc用法](#412-dfiloc用法)
    - [4.2. 添加与删除数据](#42-添加与删除数据)
      - [4.2.1. 添加删除列](#421-添加删除列)
      - [4.2.2. 添加删除行](#422-添加删除行)
      - [4.2.3. 数据去重](#423-数据去重)
    - [4.3. index操作](#43-index操作)
    - [4.4. 数据拆分](#44-数据拆分)
    - [4.5. 数据合并](#45-数据合并)
      - [4.5.1. merge](#451-merge)
      - [4.5.2. concat](#452-concat)
    - [4.6. 列与列计算](#46-列与列计算)
    - [4.7. 数据分组与聚合函数](#47-数据分组与聚合函数)
      - [4.7.1. groupby分组](#471-groupby分组)
      - [4.7.2. 聚合函数](#472-聚合函数)
## 1. 包导入


```python
import pandas as pd
import numpy as np
```

## 2. 数据IO

### 2.1. 数据导入
pd.read_csv(filename)： 从CSV文件导入数据  
pd.read_excel(filename)： 从Excel文件导入数据  
pd.read_table(filename)： 从限定分隔符的文本文件导入数据  
pd.read_json(json_string)： 从JSON格式的字符串导入数据  
pd.read_SQL(query, connection_object)： 从SQL表/库导入数据  
pd.read_html(url)： 解析URL、字符串或者HTML文件  
pd.read_clipboard()： 从粘贴板获取内容  
pd.DataFrame(dict)： 从字典对象导入数据  
### 2.2. 数据导出
```python
# 读取中文路径
path = open(r'.\data.csv')
# csv文件是gbk格式:open(r'.\文档\data.csv','rb')
pd.read_csv(path, sep='\t', skiprows=[0], nrows=0, na_values='1.#INF')
path.close
```
#### 2.2.1. pd.read_csv()参数


```python
pd.read_csv(filepath_or_buffer: Union[str, pathlib.Path, IO[~AnyStr]],
sep=',', delimiter=None, header='infer', names=None, index_col=None,
usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True,
dtype=None, engine=None, converters=None, true_values=None,
false_values=None, skipinitialspace=False, skiprows=None,
skipfooter=0, nrows=None, na_values=None, keep_default_na=True,
na_filter=True, verbose=False, skip_blank_lines=True,
parse_dates=False, infer_datetime_format=False,
keep_date_col=False, date_parser=None, dayfirst=False,
cache_dates=True, iterator=False, chunksize=None,
compression='infer', thousands=None, decimal: str = '.',
lineterminator=None, quotechar='"', quoting=0,
doublequote=True, escapechar=None, comment=None,
encoding=None, dialect=None, error_bad_lines=True,
warn_bad_lines=True, delim_whitespace=False,
low_memory=True, memory_map=False, float_precision=None)
```

|参数名|含义|输入|默认|pd.read_csv(用例)|注释|
|:-|:-|:-|:-|:-|:-|
|filepath<br>_or_buffer|文件路径|str|必填|(r'.\data.csv')|可以是url或本地路径|
|sep|指定分隔符|str|','|(./data.csv,<br> sep = '\t')|可用正则表达式|
|header|指定行作为表头<br>**数据开始**于下行|int or list[int]|'infer'|(./data.csv,<br>header = None)|数据中没有表头则需设置为None<br>默认会自动判断把第一行作为表头|
|names|设定列名|array-like|None|(./data.csv,<br>names = namelist)|没有表头时使用，同时设置header=None|
|dtype|每列数据的数据类型|str or dict|None|(./data.csv,<br>dtype = {'time': str, 'ID': int})||
|usecols|使用部分列|list[int] or list[str]|None|(./data.csv,<br>usecols=[0,4,3])|默认不按顺序，按顺序方法：(./data.csv, usecols=<br>lambda x: x.upper() in ['COL3','COL1'])|
|skiprows|跳过指定行|int list[int]|None|(./data.csv,<br>skiprows=range(2))|从文件头开始算起|
|skipfooter|尾部跳过|int list[int]|None|(./data.csv,<br>skipfooter=1)|用例为跳过最后一行<br>c引擎不支持|
|nrows|读取的行数|int|None|(./data.csv,<br>nrows=1000)|从文件头开始算起|
|true_values|真值转换|list|None|(./data.csv, true_values=['Yes'])||
|false_values|假值转换|list|None|(./data.csv, false_values=['No'])||
|na_values|空值替换|str<br>list<br>dict|None|(./data.csv,<br>na_values=["0"])|str: 'NA'<br>list: ["0","无"]<br>dict: {'col':0, 1:["无"]}指定列的指定值设NaN|
|keep_default_na|保留默认空值|bool|True|(./data.csv,<br>keep_default_na=False)|设定为False时<br>只依靠na_values判断空值|
|skip_blank_lines|跳过空行|bool|True|(./data.csv,<br>skip_blank_lines=False)|如果为True，则跳过空行；否则记为NaN。|
|parse_dates|日期时间解析|bool list dict|False|(./data.csv,<br>parse_dates=True)|指定日期时间字段进行解析:<br>parse_dates=['年份']<br>将1,4列合并为‘time’时间类型列<br>parse_dates={'time':[1,4]}|
|infer_datetime_format|自动识别日期时间|bool|False|(./data.csv,<br>parse_dates=True,<br>infer_datetime_format=True)|按用例方法，自动识别并解析，无需指定|

### 2.3. 数据导出
df.to_csv(filename)：导出数据到CSV文件  
df.to_excel(filename)：导出数据到Excel文件  
df.to_sql(table_name, connection_object)：导出数据到SQL表  
df.to_json(filename)：以Json格式导出数据到文本文件  
#### 2.3.1. df.to_csv()参数


```python
DataFrame.to_csv(path_or_buf=None, sep=', ', na_rep='', 
float_format=None, columns=None, 
header=True, index=True, index_label=None, mode='w', 
encoding=None, compression=None, 
quoting=None, quotechar='"', line_terminator='\n', 
chunksize=None, tupleize_cols=None, 
date_format=None, doublequote=True, escapechar=None, decimal='.')
```

|参数名|含义|输入|默认|注释|
|--|--|--|--|--|
|path_or_buf|导出路径|string or file handle|None|如果没有提供，结果将返回为字符串|
|sep|输出文件的字段分隔符|character|‘,’||
|columns|列顺序||None|可选列写入|
|index|是否输出index|boolean|True||
|encoding|编码格式|string|None|Python 3上默认为“UTF-8”|
|date_format|字符串对象转换为日期时间对象|string|None||
|decimal|字符识别为小数点分隔符|string|‘.’|欧洲数据使用 ​​’，’|

## 3. 数据查看
df.shape()：查看行数和列数  
df.info()：查看索引、数据类型和内存信息  
df.describe()：查看数值型列的汇总统计  
s.value_counts(dropna=False)：查看Series对象的唯一值和计数  
df.apply(pd.Series.value_counts)：查看DataFrame对象中每一列的唯一值和计数  
## 4. 数据操作

### 4.1. 数据切片

数据切片主要使用loc与iloc，loc指定列名，iloc指定位置  


```python
df = pd.read_csv(".\data_csv.csv", encoding = "gbk")
print("示例数据：")
df
```

    示例数据：
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>



#### 4.1.1. df.loc用法

**DataFrame.loc[ 行索引名称或条件 , 列索引名称 ]   # 闭区间（含最后一个值）**

1. 常规切片


```python
df.loc[1] # 显示第2行数据，返回Series
```




    ID             2
    姓名            李四
    年龄            40
    日期    2021年2月27日
    Name: 1, dtype: object




```python
df.loc[1, '日期'] # 显示列名为“日期”，行数为2的数据
```




    '2021年2月27日'




```python
df.loc[2:,['姓名','年龄']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>姓名</th>
      <th>年龄</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>



2. 条件切片


```python
df.loc[df['年龄'] > 45]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[df['年龄'] > 45, ["姓名"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>姓名</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>王五</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[lambda df: df['年龄'] == 50, ["姓名"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>姓名</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>王五</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
    </tr>
  </tbody>
</table>
</div>



更多条件切片参考：https://zhuanlan.zhihu.com/p/87334662

#### 4.1.2. df.iloc用法

**DataFrame.iloc[ 行索引位置 ,  列索引位置 ]   # 开区间（不含最后一个值）**


```python
df.iloc[1] # 显示第2行数据，返回Series
```




    ID             2
    姓名            李四
    年龄            40
    日期    2021年2月27日
    Name: 1, dtype: object




```python
df.iloc[1,3]
```




    '2021年2月27日'




```python
df.iloc[2:, 1:3] # 同df.iloc[2:, [1,2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>姓名</th>
      <th>年龄</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[lambda x: x.index % 2 == 0] # 取偶数行
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
  </tbody>
</table>
</div>



### 4.2. 添加与删除数据


```python
df = pd.read_csv(".\data_csv.csv", encoding = "gbk")
print("示例数据：")
df
```

    示例数据：
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>



会用到的函数：drop 与 loc  
loc介绍过了，介绍一下drop  

**drop**  
DataFrame.drop(labels=None, axis=0, index=None, columns=None, inplace=False)  
labels：要删除的行列的名字，用列表给定  
axis：默认0，删除行；1，删除列  
index：直接指定要删除的行  
columns：直接指定要删除的列  
inplace：True，修改了原始数据；默认False，不修改原始数据，返回新DataFrame  

#### 4.2.1. 添加删除列

单独添加一个数据方法，未添加的行显示为NaN空值


```python
df.loc[0,"性别"] = "男"
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
      <th>性别</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
      <td>男</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



添加一列为统一值


```python
df.loc[:,"性别"] = "男"
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
      <th>性别</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
      <td>男</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
      <td>男</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
      <td>男</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
      <td>男</td>
    </tr>
  </tbody>
</table>
</div>



添加一列为不同值，注意list长度需要与行数相同


```python
df.loc[:,"性别"] = ["男","女","男","女"]
# 同df["性别"] = ["男","女","男","女"]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
      <th>性别</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
      <td>男</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
      <td>女</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
      <td>男</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
      <td>女</td>
    </tr>
  </tbody>
</table>
</div>



删除增加的这一列


```python
df.drop(labels = ["性别"], axis = 1, inplace=True)
df
# 同df.drop(columns = "性别")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>



#### 4.2.2. 添加删除行

在最后一行添加数据


```python
df.loc[df.shape[0]] = [5, "阿七", 35, '2021年3月01日']
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>阿七</td>
      <td>35</td>
      <td>2021年3月01日</td>
    </tr>
  </tbody>
</table>
</div>



在第一行添加数据


```python
df.loc[-1] = [0, "老二", 40, '2021年3月01日'] # 增加一行
df.index = df.index + 1 # 把index的每一项增加1
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>阿七</td>
      <td>35</td>
      <td>2021年3月01日</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>老二</td>
      <td>40</td>
      <td>2021年3月01日</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(labels = [0, 5], inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>



#### 4.2.3. 数据去重


```python
df.drop_duplicates()
```

### 4.3. index操作

添加和删除行后，需要处理index，有set_index、sort_index()与reset_index()三种方法  

**set_index: 将 DataFrame 中的列转化为行索引。**  
DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)  
keys：设置索引  
append：添加新索引  
drop：默认Ture，不保留原索引；False，保留原索引在新列  
inplace：True，修改了原始数据；默认False，不修改原始数据，返回新DataFrame  

**sort_index：给index排序**  
DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None)  
axis：0按照行名排序；1按照列名排序  
ascending：默认True升序排列；False降序排列  
inplace：True，修改了原始数据；默认False，不修改原始数据，返回新DataFrame  

**reset_index：重置index**  
DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=”)  
drop：True，不保留原索引；默认False，保留原索引在新列  
inplace：True，修改了原始数据；默认False，不修改原始数据，返回新DataFrame  

修改index


```python
df.index = [7,6,4,8]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>



给index排序


```python
df.sort_index(inplace = True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>



重置index


```python
df.reset_index(drop=True, inplace = True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>王五</td>
      <td>50</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>李四</td>
      <td>40</td>
      <td>2021年2月27日</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>张三</td>
      <td>30</td>
      <td>2021年2月26日</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>赵六</td>
      <td>50</td>
      <td>2021年2月28日</td>
    </tr>
  </tbody>
</table>
</div>



### 4.4. 数据拆分


```python
df = pd.read_excel(".\data_excel.xlsx")
print("示例数据：")
df.head()
```

    示例数据：
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>订单编号</th>
      <th>订单日期</th>
      <th>数量</th>
      <th>产品名称</th>
      <th>产品类型</th>
      <th>产品描述</th>
      <th>产品单价</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>10</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>0.5规格中性笔</td>
      <td>￥1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>2</td>
      <td>透明胶</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>裁纸刀</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>NaN</td>
      <td>￥1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2020-07-06</td>
      <td>1</td>
      <td>橡皮擦</td>
      <td>文具</td>
      <td>NaN</td>
      <td>￥3</td>
    </tr>
  </tbody>
</table>
</div>



方法一：使用split，使用split需要用str将数据集转化为字符串  
Series.str.split(sep,n,expand=false)从前往后切分  
Series.str.rsplit(sep,n,expand=false)从后往前切分  
sep表示用于分割的字符，n表格分割成多少列；expand：True输出Dataframe，False输出Series。


```python
df.loc[:,"单价"] = df.loc[:,"产品单价"].str.split('￥', expand=True)[1].astype("int")
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>订单编号</th>
      <th>订单日期</th>
      <th>数量</th>
      <th>产品名称</th>
      <th>产品类型</th>
      <th>产品描述</th>
      <th>产品单价</th>
      <th>单价</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>10</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>0.5规格中性笔</td>
      <td>￥1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>2</td>
      <td>透明胶</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>裁纸刀</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



方法二：使用extract  
Series.str.extract(pat, flags=0, expand=True)  
pat:具有捕获组的正则表达式模式，flags:int，默认值为0(无标志)，expand：True输出Dataframe，False输出Series。


```python
df.loc[:,"单价"] = df.loc[:,"产品单价"].str.extract('((?<=￥).*)', expand=False).astype("int")
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>订单编号</th>
      <th>订单日期</th>
      <th>数量</th>
      <th>产品名称</th>
      <th>产品类型</th>
      <th>产品描述</th>
      <th>产品单价</th>
      <th>单价</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>10</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>0.5规格中性笔</td>
      <td>￥1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>2</td>
      <td>透明胶</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>裁纸刀</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



### 4.5. 数据合并

DataFrame合并主要使用两种方法，merge与concat


```python
df1 = pd.DataFrame({"name":['zhangs', 'lisi', 'wangwu', 'zhaoliu'], "score":[80,75,90,70], "class":[1,1,2,3]})
df2 = pd.DataFrame({"name":['zhangs', 'lisi', 'linji', 'zhoujl'], "age":[15,14,34,39], "gender":[0,0,1,1]})
```


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>80</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>75</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wangwu</td>
      <td>90</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>zhaoliu</td>
      <td>70</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>14</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>linji</td>
      <td>34</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>zhoujl</td>
      <td>39</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### 4.5.1. merge

提供了类似于SQL数据库连接操作的功能，支持左联、右联、内联和外联等全部四种SQL连接操作类型


```python
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, 
left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), 
copy=True, indicator=False, validate=None)
```

|参数|说明|
|:-:|--|
|left|参与合并的左侧DataFrame|
|right|参与合并的右侧DataFrame|
|how|连接方式：‘inner’（默认）；还有，‘outer’、‘left’、‘right’|
|on|用于连接的列名，必须同时存在于左右两个DataFrame对象中，如果未指定，则以left和right列名的交集作为连接键|
|left_on|左侧DataFarme中用作连接键的列|
|right_on|右侧DataFarme中用作连接键的列|
|left_index|将左侧的行索引用作其连接键|
|right_index|将右侧的行索引用作其连接键|
|sort|根据连接键对合并后的数据进行排序，默认为True。有时在处理大数据集时，禁用该选项可获得更好的性能|
|suffixes|字符串值元组，用于追加到重叠列名的末尾，默认为（‘_x’,‘_y’）.例如，左右两个DataFrame对象都有‘data’，则结果中就会出现‘data_x’，‘data_y’|
|copy|设置为False，可以在某些特殊情况下避免将数据复制到结果数据结构中。默认总是赋值|

使用：
```python
# 方法一
df1.merge(df2)
# 方法二
df3 = pd.merge(df1,df2)
```

内连接（inner默认)基于共同列的交集进行连接


```python
df3 = pd.merge(df1,df2,on='name')
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
      <th>class</th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>80</td>
      <td>1</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>75</td>
      <td>1</td>
      <td>14</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



外连接（outer）基于共同列的并集进行连接


```python
df3 = pd.merge(df1,df2,how='outer',on='name')
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
      <th>class</th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>80.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>75.0</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wangwu</td>
      <td>90.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>zhaoliu</td>
      <td>70.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>linji</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>34.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>zhoujl</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>39.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



左连接（left）基于左边位置dataframe的列进行连接


```python
df3 = pd.merge(df1,df2,how='left',on='name')
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
      <th>class</th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>80</td>
      <td>1</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>75</td>
      <td>1</td>
      <td>14.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wangwu</td>
      <td>90</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>zhaoliu</td>
      <td>70</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



右连接（right）基于右边位置dataframe的列进行连接


```python
df3 = pd.merge(df1,df2,how='right',on='name')
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
      <th>class</th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>80.0</td>
      <td>1.0</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>75.0</td>
      <td>1.0</td>
      <td>14</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>linji</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>34</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>zhoujl</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>39</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### 4.5.2. concat

提供了axis设置可用于df间行方向（增加行，下同）或列方向（增加列，下同）进行内联或外联拼接操作


```python
pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, 
levels=None, names=None, verify_integrity=False, sort=False, copy=True)
```

|参数|默认|说明|
|:-:|:-:|--|
|objs|必填|参与连接的列表或字典，且列表或字典里的对象是pandas数据类型，唯一必须给定的参数|
|axis=0|0|指明连接的轴向，0是纵轴，1是横轴|
|join|‘outer’|‘inner’（交集），‘outer’（并集），指明轴向索引的索引是交集还是并集|
|ignore_index|False|不保留连接轴上的索引，产生一组新索引range（total_length）|
|keys|None|与连接对象有关的值，用于形成连接轴向上的层次化索引（外层索引），可以是任意值的列表或数组、元组数据、数组列表（如果将levels设置成多级数组的话）|
|levels|None|指定用作层次化索引各级别（内层索引）上的索引，如果设置keys的话|
|names|None|用于创建分层级别的名称，如果设置keys或levels的话|
|verify_integrity|False|检查结果对象新轴上的重复情况，如果发横则引发异常，允许重复|
|sort|False|根据连接键对合并后的数据进行排序。有时在处理大数据集时，禁用该选项可获得更好的性能|
|copy|True|默认True时是深拷贝，False时为浅拷贝|

行拼接


```python
pd.concat([df1,df2], ignore_index=True, sort=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
      <th>class</th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>80.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>75.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wangwu</td>
      <td>90.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>zhaoliu</td>
      <td>70.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>zhangs</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>lisi</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>linji</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>34.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>zhoujl</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>39.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



列拼接


```python
pd.concat([df1,df2], axis=1, sort=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
      <th>class</th>
      <th>name</th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>zhangs</td>
      <td>80</td>
      <td>1</td>
      <td>zhangs</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lisi</td>
      <td>75</td>
      <td>1</td>
      <td>lisi</td>
      <td>14</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wangwu</td>
      <td>90</td>
      <td>2</td>
      <td>linji</td>
      <td>34</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>zhaoliu</td>
      <td>70</td>
      <td>3</td>
      <td>zhoujl</td>
      <td>39</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### 4.6. 列与列计算


```python
df = pd.DataFrame({"商品":["中性笔","透明胶", "裁纸刀" ,"橡皮擦"], "零售价":[5,8,6,4], "本月销量":[47,59,64,37], "上月销量":[48,95,34,16]})
print("示例数据：")
df
```

    示例数据：
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>商品</th>
      <th>零售价</th>
      <th>本月销量</th>
      <th>上月销量</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>中性笔</td>
      <td>5</td>
      <td>47</td>
      <td>48</td>
    </tr>
    <tr>
      <th>1</th>
      <td>透明胶</td>
      <td>8</td>
      <td>59</td>
      <td>95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>裁纸刀</td>
      <td>6</td>
      <td>64</td>
      <td>34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>橡皮擦</td>
      <td>4</td>
      <td>37</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 单列计算：团购价 = 零售价 - 1
df.loc[:, '团购价'] = df.loc[:, '零售价'].map(lambda x: x-1)
# 多列计算
## 加法：总销量=本月销量+上月销量
df.loc[:,"总销量"] = df.loc[:,"本月销量"] + df.loc[:,"上月销量"]
## 减法：销售差=本月销量-上月销量
df.loc[:,"销售差"] = df.loc[:,"本月销量"] - df.loc[:,"上月销量"]
## 乘法：本月销售额 = 本月销量*零售价
df.loc[:,"本月销售额"] = df.loc[:,"本月销量"] * df.loc[:,"零售价"]
## 除法：本月销售额占比 = 本月销量/总销量
df.loc[:,"本月销售额占比"] = df.loc[:,"本月销量"] / df.loc[:,"总销量"]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>商品</th>
      <th>零售价</th>
      <th>本月销量</th>
      <th>上月销量</th>
      <th>团购价</th>
      <th>总销量</th>
      <th>销售差</th>
      <th>本月销售额</th>
      <th>本月销售额占比</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>中性笔</td>
      <td>5</td>
      <td>47</td>
      <td>48</td>
      <td>4</td>
      <td>95</td>
      <td>-1</td>
      <td>235</td>
      <td>0.494737</td>
    </tr>
    <tr>
      <th>1</th>
      <td>透明胶</td>
      <td>8</td>
      <td>59</td>
      <td>95</td>
      <td>7</td>
      <td>154</td>
      <td>-36</td>
      <td>472</td>
      <td>0.383117</td>
    </tr>
    <tr>
      <th>2</th>
      <td>裁纸刀</td>
      <td>6</td>
      <td>64</td>
      <td>34</td>
      <td>5</td>
      <td>98</td>
      <td>30</td>
      <td>384</td>
      <td>0.653061</td>
    </tr>
    <tr>
      <th>3</th>
      <td>橡皮擦</td>
      <td>4</td>
      <td>37</td>
      <td>16</td>
      <td>3</td>
      <td>53</td>
      <td>21</td>
      <td>148</td>
      <td>0.698113</td>
    </tr>
  </tbody>
</table>
</div>



### 4.7. 数据分组与聚合函数

数据分组通过groupby函数实现  
实现类似SQL聚合函数的运算通过agg，transform和apply实现  
apply虽然灵活，但比agg,transform慢，能用agg,transform解决就用。

**agg**：聚合函数，聚合函数操作始终是在轴（默认是列轴，也可设置行轴）上执行
DataFrame.agg（func, axis=0, * args, ** kwargs）  

func：传入聚合函数作用于每一列或行  
axis：0，每一列；1，每一行  
写法：DataFrame.agg(['sum', "max"]) or DataFrame.agg('sum') or DataFrame.agg(np.sum)  

**transform**：与agg不同的是，transform会在每个对应位置上返回结果，结果长度与原df长度一样

**apply**：自动遍历整个 Series 或者 DataFrame, 对每一个元素运行指定的函数  
DataFrame.apply(func, axis=0, broadcast=None, raw=False, reduce=None, result_type=None, args=(), **kwds)  

func：function作用于每一列或行，可传入任意函数  
axis：0，每一列；1，每一行  
result_type：{‘expand’, ‘reduce’, ‘broadcast’, None} 默认 None  

    expand：类似列表的结果将转换为列  
    reduce：返回Series  
    broadcast：结果将广播到DataFrame的原始形状，保留原始索引和列  
raw：默认False，传递Series；True，传递ndarray  

不推荐使用以下参数，推荐使用result_type：  
broadcast：广播，仅与聚合函数有关。False or None,返回一个Series；True，在原本DataFrame上添加一列  
reduce：默认None，系统自动判断返回值；True，返回Series；False，返回DataFrame  

|聚合函数|numpy|用途|
|--|--|--
|min|np.min|最小值|
|max|np.max|最大值|
|sum|np.sum|求和|
|mean|np.mean|平均值|
|median|np.median|中位数|
|std|np.std|标准差|
|var|np.var|方差|
|count|np.count|计数|
|prod|np.prod|累积|
|NaN|np.power|幂运算|
|NaN|np.sqrt|开方|
|NaN|np.argmin|最小值下标|
|NaN|np.argmax|最大值下标|
|NaN|np.inf|无穷大|
|NaN|np.exp(10)|以e为底的指数|
|NaN|np.log(10)|对数|


```python
df = pd.read_excel(".\data_excel.xlsx")
print("示例数据：")
df.head()
```

    示例数据：
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>订单编号</th>
      <th>订单日期</th>
      <th>数量</th>
      <th>产品名称</th>
      <th>产品类型</th>
      <th>产品描述</th>
      <th>产品单价</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>10</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>0.5规格中性笔</td>
      <td>￥1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>2</td>
      <td>透明胶</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>裁纸刀</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>NaN</td>
      <td>￥1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2020-07-06</td>
      <td>1</td>
      <td>橡皮擦</td>
      <td>文具</td>
      <td>NaN</td>
      <td>￥3</td>
    </tr>
  </tbody>
</table>
</div>



#### 4.7.1. groupby分组

groupby的过程就是将原有的DataFrame按照groupby的字段，划分为若干个分组DataFrame  
由于返回值是一个DataFrameGroupBy对象，返回的结果是其内存地址，并不利于直观地理解，转为list可查看。

**单列分组**


```python
list(df.groupby('订单日期'))
```




    [(Timestamp('2020-07-06 00:00:00'),
         订单编号       订单日期  数量  产品名称  产品类型      产品描述  产品单价
      0     1 2020-07-06  10   中性笔    文具  0.5规格中性笔    ￥1
      1     1 2020-07-06   2   透明胶  办公用品       NaN    ￥3
      2     1 2020-07-06   3   裁纸刀  办公用品       NaN    ￥5
      3     2 2020-07-06   3   中性笔    文具       NaN    ￥1
      4     2 2020-07-06   1   橡皮擦    文具       NaN    ￥3
      5     2 2020-07-06   2    铅笔    文具       NaN    ￥1
      6     2 2020-07-06   2   作业本    文具       NaN    ￥1
      7     3 2020-07-06   2  婴儿尿片  婴儿用品         包  ￥100
      8     3 2020-07-06  10  青岛啤酒    饮料        罐装    ￥5),
     (Timestamp('2020-07-15 00:00:00'),
          订单编号       订单日期  数量    产品名称  产品类型 产品描述  产品单价
      9      4 2020-07-15   5  勇闯天涯啤酒    饮料   罐装    ￥5
      10     4 2020-07-15  10      可乐    饮料   罐装    ￥5
      11     5 2020-07-15   5      雪碧    饮料   罐装    ￥4
      12     6 2020-07-15   2     透明胶  办公用品  NaN    ￥3
      13     6 2020-07-15   3     裁纸刀  办公用品  NaN    ￥5
      14     6 2020-07-15   4   502胶水  办公用品  NaN    ￥5
      15     6 2020-07-15   5    AB胶水  办公用品  NaN    ￥6
      16     7 2020-07-15   1    儿童背包    文具  NaN   ￥50
      17     7 2020-07-15   1     文具盒    文具  NaN   ￥20
      18     8 2020-07-15   1     橡皮擦    文具  NaN    ￥3
      19     8 2020-07-15   2      铅笔    文具  NaN    ￥1
      20     8 2020-07-15   2     作业本    文具  NaN    ￥1
      21     8 2020-07-15   2    婴儿尿片  婴儿用品    包  ￥100),
     (Timestamp('2020-08-15 00:00:00'),
          订单编号       订单日期  数量    产品名称  产品类型 产品描述 产品单价
      22     9 2020-08-15  10    青岛啤酒    饮料   罐装   ￥5
      23     9 2020-08-15   5  勇闯天涯啤酒    饮料   罐装   ￥5
      24     9 2020-08-15  10      可乐    饮料   罐装   ￥5
      25     9 2020-08-15   5      雪碧    饮料   罐装   ￥4
      26     9 2020-08-15   2     透明胶  办公用品  NaN   ￥3
      27    10 2020-08-15   3     裁纸刀  办公用品  NaN   ￥5
      28    10 2020-08-15   4   502胶水  办公用品  NaN   ￥5
      29    10 2020-08-15   5    AB胶水  办公用品  NaN   ￥6
      30    11 2020-08-15   1    儿童背包    文具  NaN  ￥50
      31    11 2020-08-15   1     文具盒    文具  NaN  ￥20)]



**多列分组**


```python
list(df.groupby(['订单日期', '产品类型']))
```




    [((Timestamp('2020-07-06 00:00:00'), '办公用品'),
         订单编号       订单日期  数量 产品名称  产品类型 产品描述 产品单价  产品总销量
      1     1 2020-07-06   2  透明胶  办公用品  NaN   ￥3      6
      2     1 2020-07-06   3  裁纸刀  办公用品  NaN   ￥5      9),
     ((Timestamp('2020-07-06 00:00:00'), '婴儿用品'),
         订单编号       订单日期  数量  产品名称  产品类型 产品描述  产品单价  产品总销量
      7     3 2020-07-06   2  婴儿尿片  婴儿用品    包  ￥100      4),
     ((Timestamp('2020-07-06 00:00:00'), '文具'),
         订单编号       订单日期  数量 产品名称 产品类型      产品描述 产品单价  产品总销量
      0     1 2020-07-06  10  中性笔   文具  0.5规格中性笔   ￥1     13
      3     2 2020-07-06   3  中性笔   文具       NaN   ￥1     13
      4     2 2020-07-06   1  橡皮擦   文具       NaN   ￥3      2
      5     2 2020-07-06   2   铅笔   文具       NaN   ￥1      4
      6     2 2020-07-06   2  作业本   文具       NaN   ￥1      4),
     ((Timestamp('2020-07-06 00:00:00'), '饮料'),
         订单编号       订单日期  数量  产品名称 产品类型 产品描述 产品单价  产品总销量
      8     3 2020-07-06  10  青岛啤酒   饮料   罐装   ￥5     20),
     ((Timestamp('2020-07-15 00:00:00'), '办公用品'),
          订单编号       订单日期  数量   产品名称  产品类型 产品描述 产品单价  产品总销量
      12     6 2020-07-15   2    透明胶  办公用品  NaN   ￥3      6
      13     6 2020-07-15   3    裁纸刀  办公用品  NaN   ￥5      9
      14     6 2020-07-15   4  502胶水  办公用品  NaN   ￥5      8
      15     6 2020-07-15   5   AB胶水  办公用品  NaN   ￥6     10),
     ((Timestamp('2020-07-15 00:00:00'), '婴儿用品'),
          订单编号       订单日期  数量  产品名称  产品类型 产品描述  产品单价  产品总销量
      21     8 2020-07-15   2  婴儿尿片  婴儿用品    包  ￥100      4),
     ((Timestamp('2020-07-15 00:00:00'), '文具'),
          订单编号       订单日期  数量  产品名称 产品类型 产品描述 产品单价  产品总销量
      16     7 2020-07-15   1  儿童背包   文具  NaN  ￥50      2
      17     7 2020-07-15   1   文具盒   文具  NaN  ￥20      2
      18     8 2020-07-15   1   橡皮擦   文具  NaN   ￥3      2
      19     8 2020-07-15   2    铅笔   文具  NaN   ￥1      4
      20     8 2020-07-15   2   作业本   文具  NaN   ￥1      4),
     ((Timestamp('2020-07-15 00:00:00'), '饮料'),
          订单编号       订单日期  数量    产品名称 产品类型 产品描述 产品单价  产品总销量
      9      4 2020-07-15   5  勇闯天涯啤酒   饮料   罐装   ￥5     10
      10     4 2020-07-15  10      可乐   饮料   罐装   ￥5     20
      11     5 2020-07-15   5      雪碧   饮料   罐装   ￥4     10),
     ((Timestamp('2020-08-15 00:00:00'), '办公用品'),
          订单编号       订单日期  数量   产品名称  产品类型 产品描述 产品单价  产品总销量
      26     9 2020-08-15   2    透明胶  办公用品  NaN   ￥3      6
      27    10 2020-08-15   3    裁纸刀  办公用品  NaN   ￥5      9
      28    10 2020-08-15   4  502胶水  办公用品  NaN   ￥5      8
      29    10 2020-08-15   5   AB胶水  办公用品  NaN   ￥6     10),
     ((Timestamp('2020-08-15 00:00:00'), '文具'),
          订单编号       订单日期  数量  产品名称 产品类型 产品描述 产品单价  产品总销量
      30    11 2020-08-15   1  儿童背包   文具  NaN  ￥50      2
      31    11 2020-08-15   1   文具盒   文具  NaN  ￥20      2),
     ((Timestamp('2020-08-15 00:00:00'), '饮料'),
          订单编号       订单日期  数量    产品名称 产品类型 产品描述 产品单价  产品总销量
      22     9 2020-08-15  10    青岛啤酒   饮料   罐装   ￥5     20
      23     9 2020-08-15   5  勇闯天涯啤酒   饮料   罐装   ￥5     10
      24     9 2020-08-15  10      可乐   饮料   罐装   ￥5     20
      25     9 2020-08-15   5      雪碧   饮料   罐装   ￥4     10)]



#### 4.7.2. 聚合函数

统计不同产品的总销量，使用agg与apply


```python
df.groupby('产品名称')['数量'].agg('sum').index
```




    Index(['502胶水', 'AB胶水', '中性笔', '作业本', '儿童背包', '勇闯天涯啤酒', '可乐', '婴儿尿片', '文具盒',
           '橡皮擦', '裁纸刀', '透明胶', '铅笔', '雪碧', '青岛啤酒'],
          dtype='object', name='产品名称')




```python
df.groupby('产品名称')['数量'].agg('sum')
# 同df.groupby('产品名称')['数量'].apply(lambda x:x.sum())
# 同df.groupby('产品名称')['数量'].apply(np.sum)
```




    产品名称
    502胶水      8
    AB胶水      10
    中性笔       13
    作业本        4
    儿童背包       2
    勇闯天涯啤酒    10
    可乐        20
    婴儿尿片       4
    文具盒        2
    橡皮擦        2
    裁纸刀        9
    透明胶        6
    铅笔         4
    雪碧        10
    青岛啤酒      20
    Name: 数量, dtype: int64



将总销量添加到对应商品上，使用transform


```python
df['产品总销量'] = df.groupby('产品名称')['数量'].transform('sum')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>订单编号</th>
      <th>订单日期</th>
      <th>数量</th>
      <th>产品名称</th>
      <th>产品类型</th>
      <th>产品描述</th>
      <th>产品单价</th>
      <th>产品总销量</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>10</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>0.5规格中性笔</td>
      <td>￥1</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>2</td>
      <td>透明胶</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>裁纸刀</td>
      <td>办公用品</td>
      <td>NaN</td>
      <td>￥5</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2020-07-06</td>
      <td>3</td>
      <td>中性笔</td>
      <td>文具</td>
      <td>NaN</td>
      <td>￥1</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2020-07-06</td>
      <td>1</td>
      <td>橡皮擦</td>
      <td>文具</td>
      <td>NaN</td>
      <td>￥3</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



多列分组：输出不同订单日期不同商品的销售总量


```python
df.groupby(['订单日期', '产品类型'])['产品总销量'].agg('sum')
```




    订单日期        产品类型
    2020-07-06  办公用品    15
                婴儿用品     4
                文具      36
                饮料      20
    2020-07-15  办公用品    33
                婴儿用品     4
                文具      14
                饮料      40
    2020-08-15  办公用品    33
                文具       4
                饮料      60
    Name: 产品总销量, dtype: int64


