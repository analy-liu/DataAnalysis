---
title:  python-日期与时间
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# python中的日期与时间

python 中时间的库有：datetime time Calendar  
在pandas里也有很多pandas.Timestamp. 的方法

**通用指代时间代码**  

%a 星期的简写。星期一 ： Mon  
%A 星期的全写。星期一 ：Monday  
%b 月份的简写。一月：Jan  
%B 月份的全写。一月：January  
%c 日期时间的字符串表示。'Mon Jan 14 00:00:00 2019'  
%d 日在这个月中的天数（这个月的第几天）  
%f 微秒  
%H 24小时制  
%h 12小时制  
%j 日在年中的天数[001,366]  
%m 月份[01,12]  
%M 分钟[00,59]  
%p AM 或者 PM  
%S 秒[00,61]  
%U 在当年的第几周，星期天作为周的第一天  
%w 今天在这周的第几天[0,6]，6表示星期天  
%W 是当年的第几周，星期一作为周的第一天  
%x 日期字符串  
%X 时间字符串  
%y 2个数字表示年份  
%Y 4个数字表示年份  
%z 与utc时间的间隔（如果是本地时间，返回空字符串）  
%Z 时区名称（如果是本地时间，返回空字符串）  

## 1. time

```python
import time

# 获取日期字符串
print(time.strftime('%Y-%m-%d %H:%M:%S')) # 今日
print(time.strftime('%Y-%m-01')) # 月初
# 其他格式类型
print(time.time()) # 时间戳
print(time.localtime(time.time())) # time格式
```

**out**:  
```
2021-06-08 15:21:02  
1623136862.034063  
time.struct_time(tm_year=2021, tm_mon=6, tm_mday=8, tm_hour=15, tm_min=21, tm_sec=2, tm_wday=1, tm_yday=159, tm_isdst=0)  
```

## 2. datetime

包导入
```python
import datetime
```
### 2.1 日期差
```python
# 今天
print(datetime.datetime.now())# datetime日期格式
print(datetime.datetime.now().strftime("%Y-%m-%d")) # 字符串
# 前后几天
delta = datetime.timedelta(days=1)
now = datetime.datetime.now()
yesterday = now-delta
tomorrow = now+delta
print("昨天",yesterday.strftime("%Y-%m-%d"))
print("明天",tomorrow.strftime("%Y-%m-%d"))
# 日期差
print((tomorrow-yesterday).days) # 用datetime格式相减
```

**out**:  
```
2021-06-08 15:48:19.438862  
2021-06-08  
昨天 2021-06-07  
明天 2021-06-09  
2  
2021-09-02  
```

### 2.2 特殊日期

```python
# 特殊日期
now = datetime.datetime.now() # 设置今日
print("今天",now.strftime("%Y-%m-%d"))
print("昨天",datetime.datetime(now.year, now.month, now.day-1))
print("明天",datetime.datetime(now.year, now.month, now.day+1))
print("本周初",datetime.datetime(now.year, now.month, now.day-now.weekday()))
print("本周末",datetime.datetime(now.year, now.month, now.day+6-now.weekday()))
print("月初",datetime.datetime(now.year, now.month, 1))
print("月末",datetime.datetime(now.year, now.month+1, 1)-datetime.timedelta(days=1))
print("季初",datetime.datetime(now.year, now.month-(now.month+2)%3, 1))
print("季末",datetime.datetime(now.year, now.month-(now.month+2)%3+3, 1)-datetime.timedelta(days=1))
print("年初",datetime.datetime(now.year, 1, 1))
print("年末",datetime.datetime(now.year, 12, 31))
```

**out**:  
```
今天 2021-06-08  
昨天 2021-06-07 00:00:00  
明天 2021-06-09 00:00:00  
本周初 2021-06-07 00:00:00  
本周末 2021-06-13 00:00:00  
月初 2021-06-01 00:00:00  
月末 2021-06-30 00:00:00  
季初 2021-04-01 00:00:00  
季末 2021-06-30 00:00:00  
年初 2021-01-01 00:00:00  
年末 2021-12-31 00:00:00  
```

### 2.3 格式转换

```python
# 格式转换
now = datetime.datetime.now()# datetime格式
print(now.date())# date格式
print(now.strftime("%Y-%m-%d")) # 字符串格式
datetime.datetime.strptime('2021-09-02', '%Y-%m-%d') # 字符串转datetime
```

**out**:  
```
2021-06-08  
2021-06-08  
datetime.datetime(2021, 9, 2, 0, 0)  
```

## 3. pandas中的日期

### 3.1 日期格式转换

**日期转化函数：to_datetime**

```python
# 函数
pd.to_datetime(
    arg, # 需要转化为时间格式的数据
    errors='raise', # {‘ignore’, ‘raise’, ‘coerce’}, 默认‘raise’。ignore：错误时返回原值，raise：错误时报错，coerce：错误时返回NaT
    dayfirst=False, # True按日月年解析，例如："10/11/12"解析为2012-11-10
    yearfirst=False, # True按年月日解析，例如："10/11/12"解析为2010-11-12
    utc=None, # 控制与时区有关的解析
    format=None, # str。解析文本日期的格式，例如："%Y年%m月%d日"
    exact=True, # 是否精准匹配日期格式
    unit='ns', # str, default ‘ns’。D，S，MS，US，NS 控制最小时间单位
    infer_datetime_format=False, # True会在没设置format时推断日期格式，易错且效率低，慎用
    origin='unix', # scalar, 默认‘unix’。定义初始日期，unix：1970-01-01
    cache=True 
    )

# 使用
# 主要使用arg,format次要使用origin,errors,unit
# 转化为日期格式
df['日期'] = pd.to_datetime(df['日期'])

# 转化时间
pd.to_datetime('2022年01月04日', format='%Y年%m月%d日')
>>>Timestamp('2022-04-01 00:00:00')

# 时间比较
df.loc[0,'日期'] < pd.to_datetime('2021-02-02 00:00:00')
df.loc[0,'日期'] < pd.Timestamp('2021-02-02')
df.loc[0,'日期'] < pd.Timestamp('2021-02-02 17:40:52.192548651')

# 时间格式下的函数
df['时间季度'] = df['日期'].dt.to_period("Q") # 返回季度
```

### 3.2 Timestamp方法

```python
# 示例时间
pt = pd.Timestamp('2022-09-14 17:40:52.192548651')
>>> Timestamp('2022-09-14 17:40:52.192548651')
# 示例写法 pandas.Timestamp.date()
pt.date()
>>> datetime.date(2022, 9, 14)
```

下表的方法均写在pandas.Timestamp后面

|方法|作用|返回值示例|返回值类型|
|--|--|--|--|
|date()|返回日期部分|datetime.date(2022, 9, 14)|datetime.date|
|day_name()|返回星期英文|'Saturday'|str|