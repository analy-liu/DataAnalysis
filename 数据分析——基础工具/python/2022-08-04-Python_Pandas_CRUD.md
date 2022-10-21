---
title:  pandas-增查删改
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

本篇字数长达23771，包含pandas有关增查删改的所有内容。并且有很多细节的处理，能使用过程中解决绝大部分问题。特别推荐函数apply部分。
每小节的结构大多按照 1 函数参数介绍 2 使用示例代码 3 示例代码输出 的顺序，觉得参数介绍繁琐的可以先往下看。
觉得有用，可以点个赞，收藏起来慢慢看。

为了更加直观的体现数据变化，本文每个函数都将作用在下面生成的示例表

```python
dict_ = {'编号':['A-01','A-02','B-01','B-01'],
         '销量':[36,75,24,34],'单价':[40,50,60,60],
         '日期':["2019-07-01","2021-03-21","2022-07-19","2022-08-20"],
         '客户':['张三','',np.nan,None]}
df = pd.DataFrame(dict_) 
```

||编号|销量|单价|日期|负责人|
|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|
|1|A-02|75|50|2021-03-21||
|2|B-01|24|60|2022-07-19|NaN|
|3|B-01|34|60|2022-08-20|None|

# 1. Create 增

## 1.1 增加行列

**增加行**

```python
def insert_row(df,content,index):
    # 在插入处拆分为两个表
    df1 = df.iloc[0:index,:]
    df2 = df.iloc[index:,:]
    # 在表1末尾插入内容
    df1.loc[df1.shape[0]] = content
    # 合并表1表2
    df = pd.concat([df1,df2], ignore_index=True, sort=False)
    return df
# 在第2行后插入内容
df = insert_row(df,["C-01", 14, 30, '2021-03-01',"李四"],2)
```

||编号|销量|单价|日期|负责人|
|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|
|1|A-02|75|50|2021-03-21||
|2|C-01|14|30|2021-03-01|李四|
|3|B-01|24|60|2022-07-19|NaN|
|4|B-01|34|60|2022-08-20|None|

**增加列**

**方法一：使用insert函数**
优点：可以插入到任意位置
```python
# 使用函数insert
DataFrame.insert(loc,column,value,allow_duplicates=False)
# 参数(插入位置，新列名，内容，是否允许新增已存在的列)

df.insert(3,"流水",df['销量']*df['单价'])# 插入计算列到第3列后
df.insert(6,"备注",["无","空字符","np.nan","None"])# 插入内容列到第5列后
```

||编号|销量|单价|流水|日期|负责人|备注|
|--|--|--|--|--|--|--|--|
|0|A-01|36|40|1440|2019-07-01|张三|无|
|1|A-02|75|50|3750|2021-03-21||空字符|
|2|B-01|24|60|1440|2022-07-19|NaN|np.nan|
|3|B-01|34|60|2040|2022-08-20|None|Non|

**方法二：直接赋值**
优点：写法简单 缺点：只能添加在最后一列
```python
df['流水'] = df['销量']*df['单价']
df.loc[:,"备注"] = ["无","空字符","np.nan","None"]
# 两种写法均可
```

||编号|销量|单价|日期|负责人|流水|备注|
|--|--|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|1440|无|
|1|A-02|75|50|2021-03-21||3750|空字符|
|2|B-01|24|60|2022-07-19|NaN|1440|np.nan|
|3|B-01|34|60|2022-08-20|None|2040|None|

## 1.2 数据拆分

**方法一：使用split，使用split需要用str将数据集转化为字符串**  
Series.str.split(sep,n,expand=false)从前往后切分  
Series.str.rsplit(sep,n,expand=false)从后往前切分  
sep：用于分割的字符，n：分割次数，expand：True输出Dataframe，False输出Series。
```python
df.loc[:,"编号字母"] = df.loc[:,"编号"].str.split('-',n = 1, expand=True)[0]
df.loc[:,"编号数字"] = df.loc[:,"编号"].str.split('-',n = 1, expand=True)[1]
```

||编号|销量|单价|日期|负责人|编号字母|编号数字|
|--|--|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|A|01|
|1|A-02|75|50|2021-03-21||A|02|
|2|B-01|24|60|2022-07-19|NaN|B|01|
|3|B-01|34|60|2022-08-20|None|B|01|

**方法二：使用extract，正则表达式**  
Series.str.extract(pat, flags=0, expand=True)  
pat:具有捕获组的正则表达式模式  
flags:int，默认值为0(无标志)  
expand：True输出Dataframe，False输出Series。

```python
df.loc[:,"年份"] = df.loc[:,"日期"].str.extract('(^\d{4})', expand=False).astype("int")
df.loc[:,"编号字母"] = df.loc[:,"编号"].str.extract('(^.*(?=-))', expand=False)
```

||编号|销量|单价|日期|负责人|年份|编号字母|
|--|--|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|2019|A|
|1|A-02|75|50|2021-03-21||2021|A|
|2|B-01|24|60|2022-07-19|NaN|2022|B|
|3|B-01|34|60|2022-08-20|None|2022|B|

更多正则表达式相关知识请看[python-字符串与正则表达式](../../../../2022/08/05/Python_Re_StrAndReg.html)

## 1.3 数据合并

DataFrame合并主要使用两种方法，merge与concat  

merge以指定字段为连接索引，提供了类似于SQL数据库连接操作的功能，支持左联、右联、内联和外联等全部四种SQL连接操作类型  

concat以轴为连接索引，常用于合并结构相同的新旧表

**merge**  

DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, 
left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), 
copy=True, indicator=False, validate=None)

|参数|说明|
|--|--|
|left|参与合并的左侧DataFrame|
|right|参与合并的右侧DataFrame|
|how|连接方式：‘inner’（默认）；还有，‘outer’、‘left’、‘right’|
|on|用于连接的列名，必须同时存在于左右两个DataFrame对象中，如果未指定，则以left和right列名的交集作为连接键|
|left_on|左侧DataFarme中用作连接键的列|
|right_on|右侧DataFarme中用作连接键的列|
|left_index|将左侧的行索引用作其连接键|
|right_index|将右侧的行索引用作其连接键|
|sort|根据连接键对合并后的数据进行排序，默认为True。有时在处理大数据集时，禁用该选项可获得更好的性能|
|suffixes|字符串值元组，用于追加到重叠列名的末尾，默认为（‘x’,‘y’）.例如，左右两个DataFrame对象都有‘data’，则结果中就会出现‘data_x’，‘data_y’|
|copy|设置为False，可以在某些特殊情况下避免将数据复制到结果数据结构中。默认总是赋值|

```python
# 写法一
df = df1.merge(df2,on = ['key1', 'key2'],how='outer')
# 写法二
df = pd.merge(df1,df2,on = 'key1',how='left')
```

**concat**  

pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, 
levels=None, names=None, verify_integrity=False, sort=False, copy=True)

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

```python
# 行拼接
pd.concat([df1,df2], ignore_index=True, sort=False)
# 列拼接
pd.concat([df1,df2], axis=1, sort=False)
```

## 1.4 函数apply使用

apply函数主要功能是生成条件列，其极高的自由度能实现几乎所有条件的批量数据处理，堪称数据处理大杀器。

**apply参数**

```python
DataFrame.apply(
    func: 'AggFuncType', # 应用到每行或列的函数，可以是lambda匿名函数或自定义函数
    axis: 'Axis' = 0, # 对每一行或列数据应用函数。列：0 or index；行：1 or columns
    raw: 'bool' = False, # 控制数据是以Series还是ndarray传递，False：Series；True：ndarray
    result_type=None, # axis=1时起作用，{'expand'：返回列, 'reduce'：返回Series, 'broadcast'：结果将被广播到 DataFrame 的原始形状, None：类似列表的结果将作为这些结果的 Series 返回。但是，如果应用函数返回一个 Series ，这些结果将被扩展为列}
    args=(), # 以元组传递额外参数
    **kwargs # 以字典传递额外参数)
```

**apply应用**

**示例一：** 根据每行情况，新增条件列

新增列，日期为今年显示今年，往年显示往年
```python
df['日期'] = pd.to_datetime(df['日期']) # 将文本格式日期转为日期格式
## 写法一：对单行进行处理，不用声明axis=1
df['是否今年'] = df['日期'].apply(lambda x: '今年' if x>datetime.datetime(datetime.datetime.today().year,1,1) else '往年')
## 写法二：对整个DataFrame处理，x.列名可表示单独列，需要加上axis=1
df['是否今年'] = df.apply(lambda x: '今年' if x.日期>datetime.datetime(datetime.datetime.today().year,1,1) else '往年',axis=1)
## 写法三：构造自定义函数，并调用
def YNyear(date):
    if date>datetime.datetime(datetime.datetime.today().year,1,1):
        return "今年"
    else:
        return "往年"
df['是否今年'] = df.apply(lambda x: YNyear(x.日期),axis=1)
```

||编号|销量|单价|日期|负责人|是否今年|
|--|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|往年|
|1|A-02|75|50|2021-03-21||往年|
|2|B-01|24|60|2022-07-19|NaN|今年|
|3|B-01|34|60|2022-08-20|None|今年|

**示例二：** 根据每列情况，计算数值

列出销量与单价的最大最小值

```python
## 写法一：匿名函数
df.loc[:,['销量','单价']].apply(lambda x: pd.Series([x.min(),x.max()],index=['min','max']),axis=0)
## 写法二：自定义函数
def minmax(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])
df.loc[:,['销量','单价']].apply(minmax,axis=0) #axis=0可以不写，默认就是0
```

||销量|单价|
|--|--|--|
|min|24|40|
|max|75|60|

**示例三：** 自定义函数与匿名函数（含args与**kwargs使用）

新增列，判断流水是否大于均值，并标出最低流水，流水=销量*单价

```python
# 方法一： 匿名函数 优点：不用命名函数，缺点：条件多时不直观
df['流水等级'] = df.apply(lambda x: "低于均值,最低流水：{}".format(x.销量*x.单价) if x.销量*x.单价 == min(df['销量']*df['单价']) else "高于均值" if x.销量*x.单价>(df['销量']*df['单价']).mean() else "小于等于均值",axis=1)
# 方法二：自定义函数
def flow_level(x,v_min,v_mean):
    flow = x['销量']*x['单价']
    if flow == v_min:
        return "低于均值,最低流水：{}".format(flow)
    elif flow > v_mean:
        return "高于均值"
    else:
        return "小于等于均值"
## 使用args传递参数
df['流水等级'] = df.apply(flow_level,axis=1,args=(min(df['销量']*df['单价']),(df['销量']*df['单价']).mean(),))
## 使用**kwargs传递参数
df['流水等级'] = df.apply(flow_level,axis=1,v_min=min(df['销量']*df['单价']),v_mean=(df['销量']*df['单价']).mean())
```

||编号|销量|单价|日期|负责人|流水等级|
|--|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|低于均值,最低流水：1440|
|1|A-02|75|50|2021-03-21||高于均值|
|2|B-01|24|60|2022-07-19|NaN|低于均值,最低流水：1440|
|3|B-01|34|60|2022-08-20|None|小于等于均值|

## 1.5 函数实现-vlookup

在excel中，有一个函数是必须学会的，那就是vlookup，简单的表连接都靠这个函数实现

python的pandas包中没有vlookup函数，但有一个类似的函数merge，功能比vlookup多。  
但也正是因为功能比较多，使得参数设置繁琐，使用起来比vlookup麻烦。

于是写了下面这个函数，优化了参数，并内置其他一些便捷功能，可直接复制使用

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

最简单的写法

```python
pdexcel(左表).nbvlookup(右表, lookdict=数值列名称, on=连接列).df
```

默认左连接，重复列会自动加上_R后缀
```python
# 左右表连接列列名不同时用left_on与right_on
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


# 2. Read 查

pandas查数据叫做切片，主要用loc与iloc来实现，query则是类似SQL的查询语句

还是使用此表格进行演示

||编号|销量|单价|日期|负责人|
|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|
|1|A-02|75|50|2021-03-21||
|2|B-01|24|60|2022-07-19|NaN|
|3|B-01|34|60|2022-08-20|None|

**基础查询：loc与iloc指定行列**

loc与iloc结构类似，两者均是[行参数,列参数]的形式

通过几组等价写法，能直观的了解二者的基础写法和区别

```python
# 查询第二行，编号列，返回DataFrame
df.loc[1:1,['编号']] # 1:1 左闭右闭
df.iloc[1:2,0:1] # 1:2 左闭右开，所以返回相同
# 查询第二行，编号列，返回Series
df.loc[1:1,'编号']
df.iloc[1:2,0]
# 查询第二行，编号列，返回内容
df.loc[1,'编号']
df.iloc[1,0]

# 查全部行列
df.loc[:,:]
df.iloc[:,:]
"""
行参数：
查单行写n，
查范围写n:m，区别在于loc是左闭右闭，iloc是左闭右开

列参数：
iloc的行参数与列参数写法相同，查范围均是左闭右开
loc的列参数是列名，查单列用str，查范围用list

查全部，单独写 :
"""
```

**条件查询：通常用loc和query**

```python
# 查数值
df.loc[df['销量']>35,:]
df.query("(销量>35)")

# 查非空值 ~表示取反
df.loc[~df['负责人'].isnull(),:]
df.loc[~df['负责人'].isna(),:] # isnull与isna基本等同，用哪个都行
df.query("(~负责人.isna())",engine='python')

# 文字模糊查询 可以使用 | 进行多个条件的筛选
df.loc[df['编号'].str.contains("B|02"),:]
df.query("(编号.str.contains('B|02'))",engine='python')

# 查多个固定数值或字符串
df.loc[df['单价'].isin([50,60]),:]
df.query("(单价.isin([50,60]))",engine='python')

# 查日期范围
df['日期'] = pd.to_datetime(df['日期'])
df.loc[df['日期']>datetime.datetime(datetime.datetime.today().year,1,1),:]
df.query("(日期>datetime.datetime(datetime.datetime.today().year,1,1))")

# 多条件查询时每个条件都要用小括号括起来 
# 逻辑运算：&(且) |(或) ~(取反) ^(异或) 
df.loc[(df['销量']<40)&(~df['负责人'].isnull()),:]
df.query("(销量<40)&(~负责人.isna())",engine='python')

# 取偶数行
df.iloc[lambda x: x.index % 2 == 0]
df.loc[lambda x: x.index % 2 == 0]
df.query("(index % 2 == 0)")
```

# 3. Delete删

## 3.1 删除行列

pandas里删除行和列，可以使用drop函数，也可以用条件查询排除需要删除的列  
但drop会略快于用iloc和loc

```python
df.drop(
    labels=None, # str or list。需要删除的字段
    axis=0, # {0 or ‘index’, 1 or ‘columns’}, 默认 0 。选择删除行或者列
    index=None, # str or list。删除行时，可直接写index=labels
    columns=None, # str or list。删除列时，可直接写index=labels
    level=None, # int or level name。在多重索引下，选择删除的级别
    inplace=False,# bool, 默认 False。True将会直接修改原表
    errors='raise' # {‘ignore’, ‘raise’}, 默认 ‘raise’。是否报错，ignore会忽略错误，删除存在的标签
)
```

**应用**

```python
# 删除行
## 删除指定行
df.drop([0,2])
## 删除范围行：删除第二 第三行
df.drop([x for x in range(1,3)]) # 10000次5.32s
df.iloc[~df.index.isin(range(1,3)),:] # 10000次6.34s

# 删除列
## 删除指定列
df.drop(['负责人'],axis=1)
df.drop(columns=['负责人'])
# 模糊删除列：删除列名包含“号”
df.drop([x for x in df.columns if '号' in x],axis=1) # 10000次6.9s
df.loc[:,[x for x in df.columns if '号' not in x]] # 10000次7.9s
# 删除范围列：删除第二 三列
df.iloc[:,[x for x in range(len(df.columns)) if x not in range(1,3)]] 
```

## 3.2 数据去重

**drop_duplicates函数**

```python
df.drop_duplicates(
    subset=None, # str or list，默认整个表。需要去重的字段
    keep='first', # {‘first’, ‘last’, False}, 默认 ‘first’。first:保留第一次出现，last:保留最后一次出现，False：删除全部重复
    inplace=False, # bool, 默认 False。True将会直接修改原表
    ignore_index=False) # boll，默认False。True将会重置index为0：n-1
```

**应用**

```python
df.drop_duplicates(['编号'],keep='last') # 去重掉了第三列
```

||编号|销量|单价|日期|负责人|
|--|--|--|--|--|--|
|0|A-01|36|40|2019-07-01|张三|
|1|A-02|75|50|2021-03-21||
|3|B-01|34|60|2022-08-20|None|


# 4. Update 改

## 4.1 行与列排序与重命名

#### **行与列排序**

DataFrame的行名称为索引（index），df.index 表示索引，df.columns 表示列名

pandas常用于排序的有两个。一是针对索引的sort_index，二是针对值的sort_values

**函数**

```python
df.sort_index(
    axis=0, # {0 or ‘index’, 1 or ‘columns’}, 默认 0。 0对行排序；1对列排序  
    level=None, # int|level name|list of ints|list of level names。指定排序层级
    ascending=True, # bool or list-like of bools, 默认 True。True升序；False降序  
    inplace=False, # bool, 默认 False。True将会直接修改原表
    kind='quicksort', # {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, 默认 ‘quicksort’。几种排序方法
    na_position='last', # {‘first’, ‘last’}, 默认 ‘last’。空值的排序位置
    sort_remaining=True, # bool, default True。是否在排序完指定level后也排序其他levels
    ignore_index=False, # boll，默认False。True将会重置index为0：n-1。New in version 1.0.0.
    key=None # callable，key接受函数，能在排序后对index进行相同区块的合并。New in version 1.1.0.
    )  

df.sort_values(
    by, # str or list of str。需要排序的列或行
    axis=0, # 后续参数同sort_index
    ascending=True, 
    inplace=False, 
    kind='quicksort', 
    na_position='last', 
    ignore_index=False, 
    key=None)
```

**应用**

```python
# 行排序
df.sort_index() # index排序
df.sort_values('销量',ascending=False) # 单独对销量排序
df.sort_values(['单价','销量'],ascending=False) # 先排序单价，再排序销量

# 列排序
df.sort_index(axis=1) # 一般用于按字母排序
# 给定列名进行排序
df[['日期','编号','负责人','销量', '单价']] # 与下列效果相同
df.loc[:,['日期','编号','负责人','销量', '单价']]
# 提取出列，修改完后再插入
df_col_1 = df.loc[:,'日期']
df = df.drop('日期', axis = 1)
df.insert(0, '日期', df_col_1)
```

#### **行与列重命名**

**设置index：set_index**

```python
# 函数
df.set_index(
    keys, # str or list。用于作为index的列名或列名list，也可以是自定义Series
    drop=True, # bool, 默认True。删除用于作为索引的列
    append=False, # bool, 默认False。是否将列附加到现有索引
    inplace=False, # bool, 默认False。True将会直接修改原表
    verify_integrity=False # bool, 默认False
    )
# 使用
df.set_index('日期')
df.set_index(['日期', '编号'])
df.set_index([pd.Index([2019, 2021, 2022, 2022]), '年'])
```

**重置index：reset_index**

```python
# 函数
df.reset_index(
    level=None, # int, str, tuple, or list, 默认 None。仅从索引中删除给定的级别。默认情况下删除所有级别
    drop=False, # bool, 默认 False。False会将原本的index作为一列增加到表中
    inplace=False, # bool, 默认 False。True将会直接修改原表
    col_level=0, # int or str, default 0。drop=False时，新列插入的层级
    col_fill='' # 用于填充其他层级名
    )
# 使用
df.reset_index(drop=True, inplace = True)
```

[level使用案例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)

**重命名行列：rename**

```python
# 函数
df.rename(
    mapper=None, # dict or function。配合axis使用达到重命名行或列的选择
    index=None, # 内容同mapper，对index操作，无需设置axis
    columns=None, # 内容同mapper，对columns操作，无需设置axis
    axis=None, # {0 or ‘index’, 1 or ‘columns’}, 默认0
    copy=True, # bool, default True。
    inplace=False, # bool, 默认 False。True将会直接修改原表
    level=None, # int or level name, 默认 None。
    errors='ignore' # {‘ignore’, ‘raise’}, 默认忽略错误
    )
# 使用
df.rename(columns={'编号':'ID'}) # 重命名列名
df.rename(index={0: "x", 1: "y", 2: "z"}) # 重命名index
df.rename(str.lower, axis='columns') # 使用函数，将列名中英文大写变小写
```

## 4.2 数据类型转换

pandas中，查看数据类型可以使用 df.dtypes 或者 df.info()

下面是pandas中的数据类型
|Pandas dtype|类型|
|--|--|
|object|文本|
|int64|整数|
|float64|浮点数|
|datetime64|日期格式|
|timedelta|时间差|
|bool|布尔值|
|category|类别|

**通用转化函数：astype**

```python
# 函数
Series.astype(dtype, copy=True, errors='raise')

df['销量'].astype('object') # 转化为文本
df['销量'].astype('int') # 转化为数值
df['日期'].astype('datetime64') # 转化为日期
```

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

# 时间格式下的函数
df['时间季度'] = df['日期'].dt.to_period("Q") # 返回季度
```

**数值转化函数：to_numeric**

```python
pd.to_numeric(df['销量'])
```

**日期差转化函数：to_timedelta**

```python
# 函数
pd.to_timedelta(
    arg, 
    unit=None, # Defaults to "ns".  
    errors='raise'
    )

# 使用
pd.to_timedelta(np.arange(5), unit='d')
>>>TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'],
               dtype='timedelta64[ns]', freq=None)
```

unit 可选值：

- 星期：‘W’
- 日：‘D’ / ‘days’ / ‘day’
- 小时：‘hours’ / ‘hour’ / ‘hr’ / ‘h’
- 分钟：‘m’ / ‘minute’ / ‘min’ / ‘minutes’ / ‘T’
- 秒：‘S’ / ‘seconds’ / ‘sec’ / ‘second’
- 毫秒：‘ms’ / ‘milliseconds’ / ‘millisecond’ / ‘milli’ / ‘millis’ / ‘L’
- 微秒：‘us’ / ‘microseconds’ / ‘microsecond’ / ‘micro’ / ‘micros’ / ‘U’
- 纳秒：‘ns’ / ‘nanoseconds’ / ‘nano’ / ‘nanos’ / ‘nanosecond’ / ‘N’
（1s = 1000ms,1ms = 1000us,1us = 1000ns）

## 4.3 空值处理

python里的空值有 None 和 NaN 两种  
None 是python自带的  
NaN 是numpy包里的空值，表示不是任何数

- 在pandas中， 如果其他的数据都是数值类型， pandas会把None自动替换成NaN
- 导入数据库时，None会作为空值处理，NaN会报错
- pandas和numpy，很多函数能处理NaN，不能处理None

所以数据清洗时，一般会将None统一转换为NaN，导出时再统一转化为None

**NaN与None相互替换**

```python
# 将空值都转化为NaN
df = df.fillna(np.nan) # fillna会将None与NaN都认为空值
# 将空值都转化为None
df.where(df.notnull(), None) # pd.where(条件，条件假时返回）条件真时返回原值
```

**判断空值：isna**

numpy里边查找NaN值用np.isnan()  
pandas里边查找NaN值用.isna()和.isnull()，两则基本等同  
判断非空值用 .notnull()

```python
df.loc[~df['负责人'].isnull(),:]
df.loc[~df['负责人'].isna(),:] 
df.loc[df['负责人'].notnull(),:] 
```

**替换空缺值：fillna**

```python
# 函数
df.fillna(
    value=None, # scalar, dict, Series, or DataFrame。替换值，不能是列表
    method=None, # {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, 默认None。填充方法，'backfill','bfill'向前，'pad','ffill'向后
    axis=None, # {0 or ‘index’, 1 or ‘columns’}, 默认0
    inplace=False, # bool, 默认 False。True将会直接修改原表
    limit=None, # int。限制修改数量
    downcast=None # 向下转化为适当的相等类型字符串，如从float64到int64
    )

df.fillna("无") # 填充缺失值
df.fillna(method='ffill') #向后广播

# 用字典替换，
values = {'A': 0, 'C': 2,}
df.fillna(value=values)
# 只替换第一个值
df.fillna(value=values, limit=1)
```

**删除含空缺值的行或列：dropna**

```python
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
df.dropna(axis=1)# 删除含空缺值的列
```

## 4.4 值修改

```python
# 函数
df.replace(
    to_replace=None, # str, regex(正则), list, dict, Series, int, float, or None。被替换的值
    value=None, # scalar, dict, list, str, regex, default None。用于替换的值
    inplace=False, # bool, 默认 False。True将会直接修改原表
    limit=None, # int。限制修改数量
    regex=False, # 
    method=None # {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}。填充方法，'backfill','bfill'向前，'pad','ffill'向后
    )

# 使用
# str
df.replace('A-01','new')# 简单替换：所有A-01换为new

# list
df.replace(['A-01',60],'new')# 列表统一替换，列表中的都替换为new
df.replace(['A-01',60],['str','int']) # 列表依次替换，列表中的替换成对应值

# dict
df.replace({'A-01':'str',60:'int'}) # 单字典替换，所有keys替换成values
df.replace({'单价':{60:'int'}})# 嵌套字典替换，一层字典限定列，二层字典keys替换成values
df.replace({'单价':60,'编号':'A-01'},{'单价':'int','编号':'str'})# 双参数字典替换，一参字典限定列与被替换值，二参为替换值

# regex
df.replace(r'^A.*', 'new', regex=True)# 一参直接写正则表达式，需要设置regex=True
df.replace({'编号': r'^A.*'}, {'编号': 'new'}, regex=True) # 字典限制下的正则
df.replace(regex=r'^A.*', value='new') # 直接在regex参数里写正则，顶替第一参数
df.replace(regex=[r'^A.*', 60], value='new')# # 在regex参数里写含正则的列表
df.replace(regex={r'^A.*': 'new', '60': 'int'})# 在regex参数里写含正则的字典
```

[更多使用案例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html)

# 5. 其他常用函数与方法

**信息查看**

```python
df.shape() # 查看行数和列数
df.dtypes # 查看数据类型
df.info() # 查看索引、数据类型和内存信息
df.describe() # 查看数值型列的汇总统计
df.apply(pd.Series.value_counts) # 查看DataFrame对象中每一列的唯一值和计数
s.value_counts(dropna=False) # 查看Series对象的唯一值和计数
```