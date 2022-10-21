---
title:  函数实现-pandas透视表增强
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)


在数据获取-数据预处理作完后，就需要开始查看数据情况，正式开始进行数据分析。通常会先进行描述性分析，为了使得数据更直观且清晰，就需要使用数据透视表与可视化图表。本文主要介绍在Pandas中如何优雅的进行数据透视。

# 1. pivot_table函数

## 1.1 函数参数

```python
DataFrame.pivot_table(
    values=None, # list or str, 需要进行聚合统计的值 示例："产品大类"或['产品大类','产品中类','产品小类']
    index=None, # list or str, 用于分组的列,相当于行索引 示例：格式同values
    columns=None, # list or str, 进行列分组的字段 示例：格式同values
    aggfunc='mean', # dict or str, 聚合的方法，默认均值 示例："sum"或{"销量":"sum","产品小类":"count"}
    fill_value=None, # 用于替换空值的值
    margins=False, # bool, 是否生成汇总行
    dropna=True, # bool，如果列的所有值都是NaN，将不作为计算列
    margins_name='All', # str, 汇总行的命名
    observed=False, # bool，是否显示观测值
    sort=True # bool,是否排序（New in version 1.3.0）
    )
```

**aggfunc可选聚合方法**

|聚合函数|numpy|用途|
|--|--|--|
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

## 1.2 基础示例 

**示例底表**

||产品大类|产品中类|产品小类|销量|进货量|
|--|--|--|--|--|--|
|0|主食|米|珍珠米|100|200|
|1|主食|米|糯米|150|260|
|2|主食|面|挂面|50|140|
|3|肉类|猪肉|猪蹄|30|60|
|4|肉类|鱼肉|三文鱼|20|70|
|5|肉类|鱼肉|罗非鱼|100|350|

```python
df.pivot_table(index = ['产品大类','产品中类','产品小类'],values=['销量','进货量'],margins=True,aggfunc='sum')
```

**示例透视表**

||||进货量|销量|
|--|--|--|--|--|--|
|产品大类|产品中类|产品小类|||
|主食|米|珍珠米|200|100|
|||糯米|260|150|
||面|挂面|140|50|
|肉类|猪肉|猪蹄|60|30|
||鱼肉|三文鱼|70|20|
|||罗非鱼|350|100|
|All|||1080|450|

## 1.3 功能对比

看了简单示例后，会发现有一个问题，在index有多级的情况下，和excel的透视表相比，缺少了每一行的汇总。

且实际使用时，还需要对列的值进行排序，pivot_table产生的表结构是multiindex，直接使用sort_values函数进行排序，无法达到分级排序的效果。

于是为了实现分级求和与分级排序的功能，对pivot_tabel进行了优化，下表是优化过后的透视表。

|||进货量|销量||
|--|--|--|--|--|--|
|产品大类|产品中类|产品小类|||
|All|||1080|450|
|主食|All:主食||600|300|
||米|All:米|460|250|
|||糯米|260|150|
|||珍珠米|200|100|
||面|All:面|140|50|
|||挂面|140|50|
|肉类|All:肉类||480|150|
||鱼肉|All:鱼肉|420|120|
|||罗非鱼|350|100|
|||三文鱼|70|20|
||猪肉|All:猪肉|60|30|
|||猪蹄|60|30|

可以看到，与示例相比，优化透视表有了每级的汇总，并且按照销量进行分级排序。

下面是pivot_table优化函数的实现，与使用教程。

# 2. pivot_table优化函数-pdpivot

pdpivot函数，在pivot_table的基础上进行了功能升级，不仅能实现分级求和与分级排序，还优化了视觉展示，加上了分级优先展示汇总行的功能，以及按级别分组排序，这点是excel的透视表无法做到的。

## 2.1 函数

```python
import pandas as pd
import numpy as np
class pdpivot(object):
    def __init__(self,df):
        """
        作者：AnalyZL（github:https://github.com/analy-liu)
        """
        if str(type(df))=="<class 'pandas.core.frame.DataFrame'>":
            self.df = df.copy() # 建立副本，后续操作不改变原数据
        else:
            print('请输入pandas.DataFrame')
    def pivot_margins(self,index,values,aggfunc = 'sum',columns = None, margins_name=' All'):
        """
        pivot_margins 在官方pivot_table函数的基础上，优化了输入，并锁定输出时margins=True，即带有汇总行。
        优化输入是简化了使用aggfunc指定特定列的统计方法时，只需输入非sum统计的列，剩余列会默认用sum统计，无需补全
        """
        # 补全aggfunc字典
        if type(aggfunc) == dict:
            # 删除已有设置
            value = values.copy()
            for i in aggfunc.keys():
                value.remove(i)
            # 未设置默认求和
            sumagg = ['sum' for x in value]
            updict = dict(zip(value,sumagg))
            aggfunc.update(updict)
        self.df = self.df.pivot_table(index=index,values=values,columns=columns,aggfunc=aggfunc,margins=True,margins_name=margins_name)
        self.df = self.df.loc[:,values]
        return self # 默认继续链式运算
    def subtotal(self,margins_name=' All'):
        """
        subtotal 实现次级汇总统计，官方pivot_table只能统计最高级的汇总
        """
        df_pivot = self.df
        # 获取表格信息
        index_names = df_pivot.index.names
        index_level = len(index_names)
        # 汇总与明细分离
        df_sum_All = df_pivot.query("{} == '{}'".format(index_names[0],margins_name))# 汇总表
        df_detail = df_pivot.query("{} != '{}'".format(index_names[0],margins_name))# 明细表
        # 循环添加各层级汇总,最后一级不求和
        for i in range(index_level-1):
            df_sum = df_pivot.sum(level=index_names[0:i+1],axis = 0).iloc[0:-1,:]# 各层级求和，去除总计
            tuples = df_sum.index.tolist()# 求和表的index
            if type(tuples[0])==str:#统一为元组
                tuples = [tuple([x]) for x in tuples]
            tuples_plus = [tuple([margins_name+':'+x[-1]])+('',)*(index_level-i-2) for x in tuples]# 构造附加index，使求和表的index和原表长度统一
            tuples = [x+y for x,y in zip(tuples,tuples_plus)]# 补全index
            index = pd.MultiIndex.from_tuples(tuples, names=index_names)# 构造index
            df_sum.index = index # 设置求和表index
            # 将求合表与原表连接
            df_sum_All = pd.concat([df_sum_All,df_sum])
        self.df = pd.concat([df_sum_All,df_detail])
        return self.df # 默认输出结果
    def subsort_by(self,sort_by, top_level = 0, margins_name=' All', ascending=False):
        """
        subsort_by 实现分级排序，并且可以选择置顶的汇总级别
        top_level = 0时，是excel中透视表的形式
        """
        df_pivot = self.df
        # 按照1.Top 2.Level标记 穿插对应Level的index列 3.指定排序值 的顺序排序和最后一级index列
        sort_list = []
        ascending_list = []
        drop_sort = []
        # 获取表格信息
        index_names = df_pivot.index.names
        index_level = len(index_names)
        # 1. 新建TOP层级标记列
        for i in range(top_level+1):
            df_pivot['top_sign{}'.format(i)] = df_pivot.apply(lambda x: 1 if 'All' in x.name[i] else 0,axis=1)
            sort_list.append('top_sign{}'.format(i))
            ascending_list.append(False)
            drop_sort.append('top_sign{}'.format(i))
        # 2. 新建Level标记 穿插对应Level的index列
        for i in range(index_level-1):
            # 返回当前层index在下层中的汇总值,同时限制上层级相同
            def get_level_value(x,i,df_pivot,margins_name,index_names,sort_by):
                # 限制上层
                level_limit = ''
                if i > 0:# 如果不是第一层
                    for j in range(i):#增加每层的限制
                        last_level_limit = "&{}=='{}'".format(index_names[0+j],x.name[0+j])
                        level_limit+=last_level_limit
                # 当前层是汇总层则设置无限大
                if margins_name in x.name[i] or x.name[i] == '':
                    if ascending:# 若升序，设置负无穷
                        return -np.inf
                    else:# 若降序，设置正无穷
                        return np.inf
                else:
                    return df_pivot.query("{}.str.contains('{}')&{}.str.contains('{}'){}".format(index_names[i+1],x.name[i],index_names[i+1],margins_name,level_limit),engine='python').loc[:,sort_by][0]
            
            df_pivot['level_sign{}'.format(i)] = df_pivot.apply(lambda x:get_level_value(x,i,df_pivot,margins_name,index_names,sort_by),axis=1)
            sort_list.extend(['level_sign{}'.format(i),index_names[i]])
            ascending_list.extend([ascending,True])
            drop_sort.append('level_sign{}'.format(i))
            
        # 3. 新建汇总标记列
        df_pivot['total_sign'] = df_pivot.apply(lambda x: 1 if 'All' in str(x.name) else 0,axis=1)
        sort_list.extend(['total_sign'])
        ascending_list.extend([False])
        drop_sort.extend(['total_sign'])
        # 4. 添加指定值排序和最后一级index列
        sort_list.extend([sort_by,index_names[-1]])
        ascending_list.extend([ascending,True])

        # 排序列
        self.df = df_pivot.sort_values(sort_list, ascending=ascending_list)
        self.df.drop(columns=drop_sort, inplace=True)
        return self.df # 默认输出结果
    def levelsort_by(self,sort_by, margins_name=' All', ascending=False):
        """
        levelsort_by 实现完全分级排序，主要用于查看各层级的排名
        效果类似：
            区域0：0-level汇总:pivot_table margins产生的行
            区域1：1-level汇总行排序：1级别汇总行的排序
            ···
            区域n：n-level汇总行排序
            区域n+1：非汇总行不分组排序
        """
        df_pivot = self.df
        def set_level(index_name,margins_name):
            for i in range(len(index_name)):
                if margins_name in index_name[i]:
                    return i
            return i+1
        df_pivot['level_sign'] = df_pivot.apply(lambda x:set_level(x.name,margins_name),axis=1)
        self.df = df_pivot.sort_values(['level_sign',sort_by], ascending=[True,ascending])
        self.df.drop(columns=['level_sign'], inplace=True)
        return self.df
```

## 2.2 使用

**示例表：**  


||产品大类|产品中类|产品小类|销量|进货量|
|--|--|--|--|--|--|
|0|主食|米|珍珠米|100|200|
|1|主食|米|糯米|150|260|
|2|主食|面|挂面|50|140|
|3|肉类|猪肉|猪蹄|30|60|
|4|肉类|鱼肉|三文鱼|20|70|
|5|肉类|鱼肉|罗非鱼|100|350|

**使用示例**  

```python
# 示例表构成
dict_ = {'产品大类':['主食','主食','主食','肉类','肉类','肉类'],
         '产品中类':['米','米','面','猪肉','鱼肉','鱼肉'],
         '产品小类':['珍珠米','糯米','挂面','猪蹄','三文鱼','罗非鱼'],
         '销量':[100,150,50,30,20,100],
         '进货量':[200,260,140,60,70,350]}
df = pd.DataFrame(dict_) 

"""pdpivot函数示例，pivot_margins构建透视表 .subtotal()分级求和"""
df_pivot = pdpivot(df).pivot_margins(index = ['产品大类','产品中类','产品小类'],values=['销量','进货量']).subtotal()

# 透视后计算
df_pivot['剩余库存'] = df_pivot['进货量']-df_pivot['销量']
```

输出：

||||销量|进货量|剩余库存|
|--|--|--|--|--|--|
|产品大类|产品中类|产品小类||||
|All|||450|1080|630|
|主食|All:主食||300|600|300|
|肉类|All:肉类||150|480|330|
|主食|米|All:米|250|460|210|
||面|All:面|50|140|90|
|肉类|猪肉|All:猪肉|30|60|30|
||鱼肉|All:鱼肉|120|420|300|
|主食|米|珍珠米|100|200|100|
|||糯米|150|260|110|
||面|挂面|50|140|90|
|肉类|猪肉|猪蹄|30|60|30|
||鱼肉|三文鱼|20|70|50|
|||罗非鱼|100|350|250|

```python
# subsort_by 基础：excel透视表形式
pdpivot(df_pivot).subsort_by(sort_by = '流水',top_level=0)
```

输出：

||||销量|进货量|剩余库存|
|--|--|--|--|--|--|
|产品大类|产品中类|产品小类||||
|All|||450|1080|630|
|肉类|All:肉类||150|480|330|
||鱼肉|All:鱼肉|120|420|300|
|||罗非鱼|100|350|250|
|||三文鱼|20|70|50|
||猪肉|All:猪肉|30|60|30|
|||猪蹄|30|60|30|
|主食|All:主食||300|600|300|
||米|All:米|250|460|210|
|||糯米|150|260|110|
|||珍珠米|100|200|100|
||面|All:面|50|140|90|
|||挂面|50|140|90|

```python
# subsort_by 特色：置顶一级汇总
pdpivot(df_pivot).subsort_by(sort_by = '剩余库存',top_level=1)
```

输出：可以看到产品大类的汇总行相比上面，移动到了表上方，非汇总行，在各自层级内排序

||||销量|进货量|剩余库存|
|--|--|--|--|--|--|
|产品大类|产品中类|产品小类||||
|All|||450|1080|630|
|肉类|All:肉类||150|480|330|
|主食|All:主食||300|600|300|
|肉类|鱼肉|All:鱼肉|120|420|300|
|||罗非鱼|100|350|250|
|||三文鱼|20|70|50|
||猪肉|All:猪肉|30|60|30|
|||猪蹄|30|60|30|
|主食|米|All:米|250|460|210|
|||糯米|150|260|110|
|||珍珠米|100|200|100|
||面|All:面|50|140|90|
|||挂面|50|140|90|

```python
# levelsort_by：完全分级排序
pdpivot(df_pivot).levelsort_by(sort_by = '剩余库存')
```

输出：可以看到最下面的非汇总行，只按指定列排序，没有按产品大中类分类

||||销量|进货量|剩余库存|
|--|--|--|--|--|--|
|产品大类|产品中类|产品小类||||
|All|||450|1080|630|
|肉类|All:肉类||150|480|330|
|主食|All:主食||300|600|300|
|肉类|鱼肉|All:鱼肉|120|420|300|
|主食|米|All:米|250|460|210|
||面|All:面|50|140|90|
|肉类|猪肉|All:猪肉|30|60|30|
||鱼肉|罗非鱼|100|350|250|
|主食|米|糯米|150|260|110|
|||珍珠米|100|200|100|
||面|挂面|50|140|90|
|肉类|鱼肉|三文鱼|20|70|50|
||猪肉|猪蹄|30|60|30|