---
title:  函数实现-vlookup
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# vlookup-函数实现

在excel中，有一个函数是必须学会的，那就是vlookup，简单的表连接都靠这个函数实现

python的pandas包中，有一个类似但强于vlookup的函数merge  
但也正是功能强大，使得参数设置繁琐，而vlookup的功能往往需要经常使用

于是写了下面这个函数，优化了参数，并内置其他一些便捷功能，可直接复制使用

## 1. 函数
```python
import pandas as pd
class pdexcel(object):
    def __init__(self,df):
        self.df = df
    def nbvlookup(self,right,lookdict,on = None, left_on = None, right_on = None,na_input = None,how = 'left',merge_on=None,merge_suffixes=False):
        """
        作者：AnalyZL（github:https://github.com/analy-liu)
        right:必填，DataFrame。右侧表
        lookdict：必填，str or list。右侧表中需要加到左侧表的列
        on：默认None，str or list。用于连接的列名,必须同时存在于左右两个DataFrame对象中
        left_on：默认None，str or list。左侧DataFarme中用作连接键的列
        right_on：默认None，str or list。右侧DataFarme中用作连接键的列
        na_input：填充None，str or dict。替换空白值的值
        how：默认'left'.{'inner','outer','left','right'}。连接类型
        merge_on：默认None，str or list。填写left_on中需要用right_on填充空值的字段，并删除对应right_on，仅在how='outer'并left_on != right_on时生效
        merge_suffixes：默认False,bool。填True时，将左列空值用对应右后缀列填充，并删除右后缀列，仅在lookdict同时存在于左右表时生效
        """
        if on != None:
            left_on = on
            right_on = on
        left_col = self.df.columns # 左表原始列表
        right_col = [] # 右表保留列表
        right_col.extend(lookdict) if type(lookdict)==list else right_col.append(lookdict) # 添加值
        right_col.extend(right_on) if type(right_on)==list else right_col.append(right_on) # 添加连接键
        right = right.loc[:,right_col] # 保留需要的列
        # 连接到左表
        self.df = self.df.merge(right,left_on=left_on,right_on=right_on,how=how,suffixes=('', '_R'))
        
        # merge_on实现
        if how == 'outer' and left_on != right_on and merge_on!=None:
            # 统一merge_on left_on right_on为列表形式
            merge_on = [merge_on] if type(merge_on)==str else merge_on
            left_on = [left_on] if type(left_on)==str else left_on
            right_on = [right_on] if type(right_on)==str else right_on
            for i in merge_on:
                # 先后选择需要合并的左右两列，向前填充空值
                self.df.loc[:,i] = self.df.loc[:,[i,right_on[left_on.index(i)]]].fillna(method='bfill',axis=1).iloc[:,0]
                self.df.drop(columns = right_on[left_on.index(i)],inplace = True)
        # merge_suffixes实现
        if merge_suffixes:
            suffixes=('', '_R')
            lookdict = [lookdict] if type(lookdict)==str else lookdict
            df_col = self.df.columns
            # 给lookdict加上后缀，判断是否都在当前列里，都在则向前填充空值
            for index,item in enumerate(lookdict):
                left_suffixes = item+suffixes[0]
                right_suffixes = item+suffixes[1]
                if left_suffixes in df_col and right_suffixes in df_col:
                    self.df.loc[:,left_suffixes] = self.df.loc[:,[left_suffixes,right_suffixes]].fillna(method='bfill',axis=1).iloc[:,0]
                    self.df.drop(columns = right_suffixes,inplace = True)
        # 填充空值实现
        if na_input != None:
            # 仅填充新增列，不改变原始的左表
            fillna_col = [x for x in self.df.columns if x not in left_col]
            self.df.loc[:,fillna_col] = self.df.loc[:,fillna_col].fillna(value=na_input)
        return self
```

## 2. 使用

**示例表：**  

左表：df

||编号|销量|单价|日期|负责人|
|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|
|1|A-02|75|50|2021-03-21||
|2|B-01|24|60|2022-07-19|NaN|
|3|B-01|34|60|2022-08-20|None|

右表：df_cost

||日期2|成本|负责人|
|--|--|--|--|
|0|2019-07-01|20|张三|
|1|2021-03-21|30|李四|
|2|2022-07-19|35|王五|
|3|2022-08-21|36|赵六|

**使用示例**  

简单连接，默认左连接，左右表连接键名称相同可只使用on，重复列会自动加上_R后缀
```python
# pdexcel(左表).nbvlookup(右表, lookdict=数值列名称, left_on=左表连接列，right_on=右表连接列).df
pdexcel(df).nbvlookup(df_cost, lookdict = ['成本','负责人'], left_on = '日期',right_on='日期2').df
```

||编号|销量|单价|日期|负责人|成本|负责人_R|日期2|
|--|--|--|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|20.0|张三|2019-07-01|
|1|A-02|75|50|2021-03-21||30.0|李四|2021-03-21|
|2|B-01|24|60|2022-07-19|NaN|35.0|王五|2022-07-19|
|3|B-01|34|60|2022-08-20|None|NaN|NaN|NaN|

全连接,并且填充特定列空值
```python
pdexcel(df).nbvlookup(df_cost, lookdict = ['成本','负责人'], left_on = '日期',right_on='日期2',na_input={'成本':0},how = 'outer').df
```

||编号|销量|单价|日期|负责人|成本|负责人_R|日期2|
|--|--|--|--|--|--|--|--|--|
|0|A-01|36.0|40.0|2019-07-01|张三|20.0|张三|2019-07-01|
|1|A-02|75.0|50.0|2021-03-21||30.0|李四|2021-03-21|
|2|B-01|24.0|60.0|2022-07-19|NaN|35.0|王五|2022-07-19|
|3|B-01|34.0|60.0|2022-08-20|None|0.0|NaN|NaN|
|4|NaN|NaN|NaN|NaN|NaN|36.0|赵六|2022-08-21|

合并连接列 合并重复列 （均用右表内容填充左表空值）
```python
pdexcel(df).nbvlookup(df_cost, lookdict = ['成本','负责人'], left_on = '日期',right_on='日期2',how = 'outer',merge_on='日期',merge_suffixes = True).df
```

||编号|销量|单价|日期|负责人|成本|
|--|--|--|--|--|--|--|
|0|A-01|36.0|40.0|2019-07-01|张三|20.0|
|1|A-02|75.0|50.0|2021-03-21||30.0|
|2|B-01|24.0|60.0|2022-07-19|王五|35.0|
|3|B-01|34.0|60.0|2022-08-20|NaN|NaN|
|4|NaN|NaN|NaN|2022-08-21|赵六|36.0|