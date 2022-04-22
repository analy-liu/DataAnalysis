 # python中pandas包的使用
- [python中pandas包的使用](#python中pandas包的使用)
  - [1. 包导入](#1-包导入)
  - [2. 数据IO](#2-数据io)
    - [2.1. 数据导入](#21-数据导入)
      - [2.1.1. pd.read_csv()参数：](#211-pdread_csv参数)
        - [2.1.1.1. 基本导入参数：](#2111-基本导入参数)
        - [2.1.1.2. 数据选择参数：](#2112-数据选择参数)
        - [2.1.1.3. 值的处理参数：](#2113-值的处理参数)
    - [2.2. 数据导出](#22-数据导出)
      - [2.2.1. df.to_csv()参数](#221-dfto_csv参数)
        - [2.2.1.1. 基本导出参数](#2211-基本导出参数)
  - [3. 数据查看](#3-数据查看)
  - [4. 数据操作](#4-数据操作)
    - [4.1. 数据切片](#41-数据切片)
      - [4.1.1. df.loc用法](#411-dfloc用法)
      - [4.1.2. df.iloc用法](#412-dfiloc用法)
    - [4.2. 数据合并](#42-数据合并)
      - [4.2.1. merge](#421-merge)
      - [4.2.2. concat](#422-concat)
      - [4.2.3. append](#423-append)
      - [4.2.4. join](#424-join)

pandas可以将数据文件读取形成DataFrame，通常命名为df。  
pandas 是一个开源的 Python 库，可提供高性能的数据处理和分析。将 Python 与 pandas 组合使用，无论数据来源如何，您都可以完成五个典型的数据处理和分析步骤：加载、准备、操作、建模和分析。  
在使用 pandas 进行数据处理时，有很多选项。下面的列表显示了利用 pandas 可以完成的一些操作。
* 通过删除或替换缺失值来清理数据
* 转换数据格式
* 行排序
* 删除或添加行和列
* 合并或连接数据帧
* 以透视或重塑的方式汇总数据
* 创建可视化效果
## 1. 包导入
```python
import pandas as pd
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
```python
# 读取中文路径
path = open(r'.\文档\data.csv')
# csv文件是gbk格式:open(r'.\文档\data.csv','rb')
pd.read_csv(path, sep='\t', skiprows=[0], nrows=0, na_values='1.#INF')
path.close
```
#### 2.1.1. pd.read_csv()参数：
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

##### 2.1.1.1. 基本导入参数：
|参数名|含义|输入|默认|pd.read_csv(用例)|注释|
|--|--|--|--|--|--|
|filepath<br>_or_buffer|文件路径|str|必填|(r'.\data.csv')|可以是url或本地路径|
|sep|指定分隔符|str|','|(./data.csv,<br> sep = '\t')|可用正则表达式|
|header|指定行作为表头<br>**数据开始**于下行|int or list[int]|'infer'|(./data.csv,<br>header = None)|数据中没有表头则需设置为None<br>默认会自动判断把第一行作为表头|
|names|设定列名|array-like|None|(./data.csv,<br>names = namelist)|没有表头时使用，同时设置header=None|
|dtype|每列数据的数据类型|str or dict|None|(./data.csv,<br>dtype = {'time': str, 'ID': int})||

##### 2.1.1.2. 数据选择参数：
|参数名|含义|输入|默认|pd.read_csv(用例)|注释|
|--|--|--|--|--|--|
|usecols|使用部分列|list[int] or list[str]|None|(./data.csv,<br>usecols=[0,4,3])|默认不按顺序，按顺序方法：(./data.csv, usecols=<br>lambda x: x.upper() in ['COL3','COL1'])|
|skiprows|跳过指定行|int list[int]|None|(./data.csv,<br>skiprows=range(2))|从文件头开始算起|
|skipfooter|尾部跳过|int list[int]|None|(./data.csv,<br>skipfooter=1)|用例为跳过最后一行<br>c引擎不支持|
|nrows|读取的行数|int|None|(./data.csv,<br>nrows=1000)|从文件头开始算起|
##### 2.1.1.3. 值的处理参数：
|参数名|含义|输入|默认|pd.read_csv(用例)|注释|
|--|--|--|--|--|--|
|true_values|真值转换|list|None|(./data.csv, true_values=['Yes'])||
|false_values|假值转换|list|None|(./data.csv, false_values=['No'])||
|na_values|空值替换|str<br>list<br>dict|None|(./data.csv,<br>na_values=["0"])|str: 'NA'<br>list: ["0","无"]<br>dict: {'col':0, 1:["无"]}指定列的指定值设NaN|
|keep_default_na|保留默认空值|bool|True|(./data.csv,<br>keep_default_na=False)|设定为False时<br>只依靠na_values判断空值|
|skip_blank_lines|跳过空行|bool|True|(./data.csv,<br>skip_blank_lines=False)|如果为True，则跳过空行；否则记为NaN。|
|parse_dates|日期时间解析|bool list dict|False|(./data.csv,<br>parse_dates=True)|指定日期时间字段进行解析:<br>parse_dates=['年份']<br>将1,4列合并为‘time’时间类型列<br>parse_dates={'time':[1,4]}|
|infer_datetime_format|自动识别日期时间|bool|False|(./data.csv,<br>parse_dates=True,<br>infer_datetime_format=True)|按用例方法，自动识别并解析，无需指定|
### 2.2. 数据导出
df.to_csv(filename)：导出数据到CSV文件
df.to_excel(filename)：导出数据到Excel文件
df.to_sql(table_name, connection_object)：导出数据到SQL表
df.to_json(filename)：以Json格式导出数据到文本文件

#### 2.2.1. df.to_csv()参数
```python
DataFrame.to_csv(path_or_buf=None, sep=', ', na_rep='', 
float_format=None, columns=None, 
header=True, index=True, index_label=None, mode='w', 
encoding=None, compression=None, 
quoting=None, quotechar='"', line_terminator='\n', 
chunksize=None, tupleize_cols=None, 
date_format=None, doublequote=True, escapechar=None, decimal='.')
```
##### 2.2.1.1. 基本导出参数
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
示例数据：
|index|ID|姓名|年龄|日期|
|--|--|--|--|--|
|0|1|张三|30|2021年2月26日|
|1|2|李四|40|2021年2月27日|
|2|3|王五|50|2021年2月26日|
|3|4|赵六|50|2021年2月28日|
#### 4.1.1. df.loc用法
**DataFrame.loc[ 行索引名称或条件 , 列索引名称 ]   # 闭区间（含最后一个值）**
1. 常规切片
```python
>>> df.loc[1] # 显示第2行数据，返回Series
ID             2
姓名            李四
年龄            40
日期    2021年2月27日
Name: 1, dtype: object

>>> df.loc[1, '日期'] # 显示列名为“日期”，行数为2的数据
'2021年2月27日'

>>> df.loc[2:,['姓名','年龄']]
        姓名	年龄
2	王五	50
3	赵六	50
```
2. 条件切片
```python
>>> df.loc[df['年龄'] > 45]
        ID	姓名	年龄	日期
2	3	王五	50	2021年2月26日
3	4	赵六	50	2021年2月28日

>>> df.loc[df['年龄'] > 45, ["姓名"]]
	姓名
2	王五
3	赵六

>>> df.loc[lambda df: df['年龄'] == 50, ["姓名"]]
	姓名
2	王五
3	赵六

更多条件切片参考：https://zhuanlan.zhihu.com/p/87334662
```
#### 4.1.2. df.iloc用法
**DataFrame.iloc[ 行索引位置 ,  列索引位置 ]   # 开区间（不含最后一个值）**
1. 常规切片
```python
>>> df.iloc[1] # 显示第2行数据，返回Series
ID             2
姓名            李四
年龄            40
日期    2021年2月27日
Name: 1, dtype: object

>>> df.iloc[1,3] 
'2021年2月27日'

>>> df.iloc[2:, 1:3] # 同df.iloc[2:, [1,2]]
        姓名	年龄
2	王五	50
3	赵六	50

>>> df.iloc[lambda x: x.index % 2 == 0] # 取偶数行
	ID	姓名	年龄	日期
0	1	张三	30	2021年2月26日
2	3	王五	50	2021年2月26日
```
### 4.2. 数据合并
示例数据
|df1|name|	score|	class|
|--|--|--|--|
|0	|zhangsan|	80|	1|
|1	|lisi|	75|	1|
|2	|wangwu|	90|	2|
|3	|zhaoliu|	70|	3|

|df2|	name|	age|	gender|
|--|--|--|--|
|0|	zhangsan|	15|	男|
|1|	lisi|	14|	女|
|2|	linjj|	34|	男|
|3|	zhoujl|	39|	男|
#### 4.2.1. merge
pandas的顶级方法，提供了类似于SQL数据库连接操作的功能，支持左联、右联、内联和外联等全部四种SQL连接操作类型
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
用法：
```python
# 方法一
df1.merge(df2)
# 方法二
df3 = pd.merge(df1,df2)

"内连接（inner默认)基于共同列的交集进行连接"
>>> df3 = pd.merge(df1,df2,on='name')
index   name        score   class   age	gender
0	zhangsan    80      1	    15	男
1	lisi        75	    1	    14	女
"外连接（outer）基于共同列的并集进行连接"
>>> df3 = pd.merge(df1,df2,how='outer',on='name')
index   name	score	class	age	gender
0	zhangsan 80.0	1.0	15.0	男
1	lisi	 75.0	1.0	14.0	女
2	wangwu	 90.0	2.0	NaN	NaN
3	zhaoliu	 70.0	3.0	NaN	NaN
4	linjj	 NaN	NaN	34.0	男
5	zhoujl	 NaN	NaN	39.0	男
"左连接（left）基于左边位置dataframe的列进行连接"
>>> df3 = pd.merge(df1,df2,how='left',on='name')
index   name	score	class	age	gender
0	zhangsan 80	1	15.0	男
1	lisi	 75	1	14.0	女
2	wangwu	 90	2	NaN	NaN
3	zhaoliu	 70	3	NaN	NaN
"右连接（right）基于右边位置dataframe的列进行连接"
>>> df3 = pd.merge(df1,df2,how='right',on='name')
index   name	score	class	age	gender
0	zhangsan 80.0	1.0	15	男
1	lisi	 75.0	1.0	14	女
2	linjj	 NaN	NaN	34	男
3	zhoujl	 NaN	NaN	39	男
```
#### 4.2.2. concat
pandas的顶级方法，提供了axis设置可用于df间行方向（增加行，下同）或列方向（增加列，下同）进行内联或外联拼接操作
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
用法：
```python
"行拼接"
pd.concat([df1,df2], ignore_index=True, sort=False)
	name	score	class	age	gender
0	zhangsan 80.0	1.0	NaN	NaN
1	lisi	 75.0	1.0	NaN	NaN
2	wangwu	 90.0	2.0	NaN	NaN
3	zhaoliu	 70.0	3.0	NaN	NaN
4	zhangsan NaN	NaN	15.0	男
5	lisi	 NaN	NaN	14.0	女
6	linjj	 NaN	NaN	34.0	男
7	zhoujl	 NaN	NaN	39.0	男
"列拼接"
pd.concat([df1,df2], axis=1, sort=False)
        name	score	class	name	age	gender
0	zhangsan 80	1	zhangsan 15	男
1	lisi	 75	1	lisi	 14	女
2	wangwu	 90	2	linjj	 34	男
3	zhaoliu	 70	3	zhoujl	 39	男
```
#### 4.2.3. append
dataframe数据类型的方法，提供了行方向的拼接操作
#### 4.2.4. join
dataframe数据类型的方法，提供了列方向的拼接操作，支持左联、右联、内联和外联四种操作类型。  
merge和join方法基本上能实现相同的功能，建议用merge。


