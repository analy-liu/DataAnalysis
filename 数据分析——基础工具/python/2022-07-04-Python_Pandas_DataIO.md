---
title:  pandas-数据导入与导出
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# pandas-数据导入与导出

## 1. 包载入

```python
import pandas as pd
import numpy as np
```

## 2. 数据读取
1. 读取excel文件
   ```python
   # 读取 excel 文件
   target_path = r'F:\data\test\中文路径\测试数据.xlsx'
   sheet = 'Sheet1'
   df = pd.read_excel(target_path, sheet_name=sheet)
   ```

   <details>
   <summary>点击查看pd.read_excel更多参数</summary>
   <p>
   pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, 
                      squeeze=False, dtype=None, engine=None, converters=None, true_values=None, 
                      false_values=None, skiprows=None, nrows=None,na_values=None, 
                      keep_default_na=True, verbose=False, parse_dates=False, date_parser=None, 
                      thousands=None, comment=None, skip_footer=0, skipfooter=0, convert_float=True, 
                      mangle_dupe_cols=True, **kwds)<br>
   <b>参数</b><br>
   io ：文件路径url，例如：r'../data.xlsx'  <br>
   sheet_name ： 选择表，可按顺序012，可按表名"sheet"，设置None则读取全部工作表  <br>
   usecols ：选取表中具体列，默认None读取所有列，写法：[A,C] [A,C:E] [0,2] ["col1","col3"]  <br>
   header ：用于解析的列标签的行（索引为0，默认0）  <br>
   names ：表示自定义表头的名称，需要传递数组参数。["col1","col2"]  <br>
   dtype ：设置数据类型，例如：{'a': np.float64, 'b': np.int32}  <br>
   parse_dates ：指定将哪些列，解析为日期格式。写法：[0,1] ["col1","col3"]  <br>
   skiprows ：开头要跳过的行  <br>
   nrows ：要解析的行数  <br>
   na_values ：识别为NAN的字符，写法：["值1","值2"] {"列1":[”值1“,"值2"]}  <br>
   converters ：对某一列使用Lambda函数，进行某种运算，例如{"col":lambda x: x + 1000}  <br>
   </p>
   </details>

2. 读取csv文件
   ```python
   # 读取 csv 文件
   ## 方式一
   target_path = r'F:\data\test\中文路径\测试数据.csv'
   df = pd.read_csv(target_path,sep=',')
   ## 方式二
   path = open(r'F:\data\test\中文路径\测试数据.csv')
   # csv文件是gbk格式:open(r'.\文档\data.csv','rb')
   pd.read_csv(path, sep='\t', skiprows=[0], nrows=0, na_values='1.#INF')
   path.close
   ```

   <details>
   <summary>点击查看pd.read_csv更多参数</summary>
   <p>
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
   low_memory=True, memory_map=False, float_precision=None)<br>
   <table class="table table-bordered table-striped table-condensed">
     <tr>
       <td>参数名</td>
       <td>含义</td>
       <td>输入</td>
       <td>默认</td>
       <td>pd.read_csv(用例)</td>
       <td>注释</td>
     </tr>
     <tr>
       <td>filepath<br>_or_buffer</td>
       <td>文件路径</td>
       <td>str</td>
       <td>必填</td>
       <td>(r'.\data.csv')</td>
       <td>可以是url或本地路径</td>
     </tr>
     <tr>
       <td>sep</td>
       <td>指定分隔符</td>
       <td>str</td>
       <td>','</td>
       <td>(./data.csv,<br> sep = '\t')</td>
       <td>可用正则表达式</td>
     </tr>
     <tr>
       <td>header</td>
       <td>指定行作为表头<br>**数据开始**于下行</td>
       <td>int or list[int]</td>
       <td>'infer'</td>
       <td>(./data.csv,<br>header = None)</td>
       <td>数据中没有表头则需设置为None<br>默认会自动判断把第一行作为表头</td>
     </tr>
     <tr>
       <td>names</td>
       <td>设定列名</td>
       <td>array-like</td>
       <td>None</td>
       <td>(./data.csv,<br>names = namelist)</td>
       <td>没有表头时使用，同时设置header=None</td>
     </tr>
     <tr>
       <td>dtype</td>
       <td>每列数据的数据类型</td>
       <td>str or dict</td>
       <td>None</td>
       <td>(./data.csv,<br>dtype = {'time': str, 'ID': int})</td>
     </tr>
     <tr>
       <td>usecols</td>
       <td>使用部分列</td>
       <td>list[int] or list[str]</td>
       <td>None</td>
       <td>(./data.csv,<br>usecols=[0,4,3])</td>
       <td>默认不按顺序，按顺序方法：(./data.csv, usecols=<br>lambda x: x.upper() in ['COL3','COL1'])</td>
     </tr>
     <tr>
       <td>skiprows</td>
       <td>跳过指定行</td>
       <td>int list[int]</td>
       <td>None</td>
       <td>(./data.csv,<br>skiprows=range(2))</td>
       <td>从文件头开始算起</td>
     </tr>
     <tr>
       <td>skipfooter</td>
       <td>尾部跳过</td>
       <td>int list[int]</td>
       <td>None</td>
       <td>(./data.csv,<br>skipfooter=1)</td>
       <td>用例为跳过最后一行<br>c引擎不支持</td>
     </tr>
     <tr>
       <td>nrows</td>
       <td>读取的行数</td>
       <td>int</td>
       <td>None</td>
       <td>(./data.csv,<br>nrows=1000)</td>
       <td>从文件头开始算起</td>
     </tr>
     <tr>
       <td>true_values</td>
       <td>真值转换</td>
       <td>list</td>
       <td>None</td>
       <td>(./data.csv, true_values=['Yes'])</td>
     </tr>
     <tr>
       <td>false_values</td>
       <td>假值转换</td>
       <td>list</td>
       <td>None</td>
       <td>(./data.csv, false_values=['No'])</td>
     </tr>
     <tr>
       <td>na_values</td>
       <td>空值替换</td>
       <td>str<br>list<br>dict</td>
       <td>None</td>
       <td>(./data.csv,<br>na_values=["0"])</td>
       <td>str: 'NA'<br>list: ["0","无"]<br>dict: {'col':0, 1:["无"]}指定列的指定值设NaN</td>
     </tr>
     <tr>
       <td>keep_default_na</td>
       <td>保留默认空值</td>
       <td>bool</td>
       <td>True</td>
       <td>(./data.csv,<br>keep_default_na=False)</td>
       <td>设定为False时<br>只依靠na_values判断空值</td>
     </tr>
     <tr>
       <td>skip_blank_lines</td>
       <td>跳过空行</td>
       <td>bool</td>
       <td>True</td>
       <td>(./data.csv,<br>skip_blank_lines=False)</td>
       <td>如果为True，则跳过空行；否则记为NaN。</td>
     </tr>
     <tr>
       <td>parse_dates</td>
       <td>日期时间解析</td>
       <td>bool list dict</td>
       <td>False</td>
       <td>(./data.csv,<br>parse_dates=True)</td>
       <td>指定日期时间字段进行解析:<br>parse_dates=['年份']<br>将1,4列合并为‘time’时间类型列<br>parse_dates={'time':[1,4]}</td>
     </tr>
     <tr>
       <td>infer_datetime_format</td>
       <td>自动识别日期时间</td>
       <td>bool</td>
       <td>False</td>
       <td>(./data.csv,<br>parse_dates=True,<br>infer_datetime_format=True)</td>
       <td>按用例方法，自动识别并解析，无需指定</td>
     </tr>
   </table>
   </p>
   </details>

3. 读取数据库文件
   ```python
   # 载入数据库包
   import pymysql
   # 建立数据库连接
   con = pymysql.connect(host='数据库地址',user='账户名',password='密码', port=0000, charset='utf8')
   cursor = con.cursor()
   cursor.execute('USE {};'.format('数据库名称'))
   # 编写sql
   sql = """
   SELECT * FROM 表名称;
   """
   # 读取数据
   df = pd.read_sql(sql, con=con)

   cursor.close() # 关闭光标
   con.close() # 关闭连接对象，否则会导致连接泄漏，消耗数据库资源
   ```
   <details>
   <summary>点击查看pd.read_sql更多参数</summary>
   <p>
   pd.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)  <br>
    <b>参数</b>  <br>
   sql, SQL查询语句<br>
   con, 数据库连接<br>
   index_col=None, string or list要设置为索引（多索引）的列<br>
   coerce_float=True, 尝试转换非字符串，非数字对象（例如十进<br>制（Decimal.Decimal）到浮点数
   params=None, 传递给执行方法的参数列表。<br>
   parse_dates=None, list or dict要解析为日期的列名列表。 <br>
   columns=None,  要从SQL表中选择的列名列表<br>
   chunksize=None, int如果指定，则返回一个迭代器，其中“ <br>chunksize”为每个块中要包括的行数。 <br>
   </p>
   </details>
4. pd.read_总览
   pd.read_csv(filename)： 从CSV文件导入数据  <br>
   pd.read_excel(filename)： 从Excel文件导入数据  <br>
   pd.read_table(filename)： 从限定分隔符的文本文件导入数据  <br>
   pd.read_json(json_string)： 从JSON格式的字符串导入数据  
   pd.read_SQL(query, connection_object)： 从SQL表/库导入数据  <br>
   pd.read_html(url)： 解析URL、字符串或者HTML文件  <br>
   pd.read_clipboard()： 从粘贴板获取内容  <br>

## 3. 数据构建
```python
# 生成dataframe
# 方法一：从字典对象导入数据,字典keys是列名，对应的values是一列的值
dict_ = {'字母':['A','B'],'数字':[1,2]}
pd.DataFrame(dict_) 
# 方法二：构建二维列表，内层列表里每个列表是一行
Multi_list = [['A',1],['B',2]]
columns = ['字母','数字']
pd.DataFrame(data = Multi_list, columns = columns) 
# 方法三：用series直接构成DataFrame
s.to_frame()
```

## 4. 数据导出

1. 导出到excel
    ```python
    # 更新excel指定sheet,删除原有数据加入新数据
    def nb_to_excel(path, data, sheet_name, replace = True,index=False):
        from openpyxl import load_workbook
        # 保存新的数据
        writer = pd.ExcelWriter(path, engine='openpyxl',mode='w')
        book = load_workbook(writer.path)
        writer.book = book
        if replace:
            # 清除原来的数据
            idx = book.sheetnames.index(sheet_name)
            book.remove(book.worksheets[idx])
            book.create_sheet(sheet_name, idx)
            writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        # 保存文件
        data.to_excel(excel_writer=writer, sheet_name=sheet_name,  index=index)
        writer.save()
    ```
    使用
    ```python
   target_path = r"F:\data\test\中文路径\测试数据.xlsx"
   nb_to_excel(target_path, df,'Sheet1')
    ```
2. 导出到csv
   <details>
   <summary>点击展开查看</summary>
   <p>
   df.to_csv(path_or_buf=None, sep=', ', na_rep='', 
   float_format=None, columns=None, 
   header=True, index=True, index_label=None, mode='w', 
   encoding=None, compression=None, 
   quoting=None, quotechar='"', line_terminator='\n', 
   chunksize=None, tupleize_cols=None, 
   date_format=None, doublequote=True, escapechar=None, decimal='.')<br>
   <table class="table table-bordered table-striped table-condensed">
     <tr>
       <td>参数名</td>
       <td>含义</td>
       <td>输入</td>
       <td>默认</td>
       <td>注释</td>
     </tr>
     <tr>
       <td>path_or_buf</td>
       <td>导出路径</td>
       <td>string or file handle</td>
       <td>None</td>
       <td>如果没有提供，结果将返回为字符串</td>
     </tr>
     <tr>
       <td>sep</td>
       <td>输出文件的字段分隔符</td>
       <td>character</td>
       <td>‘,’</td>
     </tr>
     <tr>
       <td>columns</td>
       <td>列顺序</td>
       
       <td>None</td>
       <td>可选列写入</td>
     </tr>
     <tr>
       <td>index</td>
       <td>是否输出index</td>
       <td>boolean</td>
       <td>True</td>
     </tr>
     <tr>
       <td>encoding</td>
       <td>编码格式</td>
       <td>string</td>
       <td>None</td>
       <td>Python 3上默认为“UTF-8”</td>
     </tr>
     <tr>
       <td>date_format</td>
       <td>字符串对象转换为日期时间对象</td>
       <td>string</td>
       <td>None</td>
     </tr>
     <tr>
       <td>decimal</td>
       <td>字符识别为小数点分隔符</td>
       <td>string</td>
       <td>‘.’</td>
       <td>欧洲数据使用 ​​’，’</td>
     </tr>
   </table>
   </p>
   </details>
3. 导出到数据库
   <details>
   <summary>点击展开查看</summary>
   <p>
   df.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, 
             chunksize=None, dtype=None, method=None)<br>
    <b>参数</b><br>
   name, 表名<br>
   con, 数据库的连接<br>
   schema=None, 指定模式<br>
   if_exists='fail', 如果表已经存在{"fail":"引发ValueError","replace":"覆盖","append":"追加"}<br>
   index=True, 是否写入索引作为一列<br>
   index_label=None, 给出索引列<br>
   chunksize=None, int,每次写入行数，默认全部写入<br>
   dtype=None, dict,指定列的类型<br>
   method=None，导入方法{None, 'multi', callable}<br>
   </p>
   </details>

## 5. 多表信息查看与导入

有时我们会需要读取文件夹下所有excel，每个excel里还有多个sheet，当数量多时，想要快速掌握这些excel的基本信息，一个个单独查看效率比较低，把所有表信息与内容汇总到一张表里，就能快速了解各表数据结构、大小，来进行下一步的数据处理。

```python
import pandas as pd
import os
def summary_filexlsx_info(path):
    # 将多个excel中sheet读取到一张表中，展示信息
    filenames = os.listdir(path)
    sheet_info_list = []
    for index,item in enumerate(filenames):
        sheet_index = 0
        # 遍历sheet
        while True:
            try:
                # sheet存在，则保存到df
                df = pd.read_excel('{}\\{}'.format(path,item),sheet_name=sheet_index)
                if df.shape == (0,0):
                    break # 空sheet则退出，不录入信息
            except:
                break # sheet不存在则退出while循环
            else:
                # 构建每个sheet的信息
                sheet_info_temp = [item,index,sheet_index,df.shape[0],df.shape[1],df.columns.tolist(),type(df.columns.tolist()[0]),df.dtypes.to_dict(),df.to_dict()]
                sheet_info_list.append(sheet_info_temp)
                sheet_index+=1
    return pd.DataFrame(data=sheet_info_list,columns=['表名','表ID','sheet序号','行','列','表头','表头类型','数据类型','数据'])
```

使用

```python
path = r"D:\data"
df_info = summary_filexlsx_info(path)
# 查看具体表数据
pd.DataFrame(df_info.loc[0,'数据'])
```