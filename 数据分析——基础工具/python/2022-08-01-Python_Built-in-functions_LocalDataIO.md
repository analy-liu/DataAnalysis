---
title:  内置函数-本地数据读取与保存
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# Python 文件I/O

## 1. Open使用

**三种使用形式**
```python
# 简易模式
f = open("test.txt") # 在当前文件夹打开文件
f = open(r"F:\data\test\English_Path\test.txt") # 指定完整路径,默认只读模式
f.close() # 关闭文件

# try-finally形式
try:
    # mode指定文件打开模式 encoding指定文件编码
    f = open(r"F:\data\test\English_Path\test.txt", mode='r',encoding = 'utf-8')
finally:
    # 即使引发了导致程序流停止的异常，也可以保证文件正确关闭
    f.close()

# with形式 能保证在退出 with 语句中的块时关闭文件
with open(r"F:\data\test\English_Path\test.txt", mode='w',encoding = 'utf-8') as f:
    f.write("第一行\n") # \n换行
    f.write("第二行")
    f.write("第二行\n")
    # 会覆盖原内容,无文件会新建
```

## 2. Open对象方法

**方法列表**

```python
# 文件状态属性
fileno() # 返回文件的整数号（文件描述符）
isatty() # 文件是否连接到一个终端设备

# 光标
tell() # 当前指针位置
seek(int,[0,1,2]) 
# 参数一偏移量：整数，单位-比特
# 参数二初始位置：0-文件头，1-当前位置，默认值，2-文件尾

# 读
read(int) # 读取文件全部内容。如果指定，则最多读取n字节/字符
readline(int) # 读取文件当前行。如果指定，则最多读取n字节/字符
readlines(int) # 读取并返回文件中的行列表。如果指定，则最多读取n字节/字符

# 写
write(str) # 写入
writelines(list) # 将列表按顺序写入

# 缓冲区
flush() # 将缓冲区中的数据立刻写入文件，并且清空缓冲区
truncate(10) # 删除当前指针n个字节后内容，不指定默认0
detach() # 将基础原始流与缓冲区分开并返回 Separate the underlying raw stream from the buffer and return it.
```

**具体使用**

```python
try:
    # 打开文件
    f = open(r"F:\data\test\English_Path\test.txt", mode='a+',encoding = 'utf-8')
    print("使用a+模式读取")
    print("fileno() 返回文件的整数号（文件描述符）：%s"%f.fileno())
    print("isatty() 文件是否连接到一个终端设备：%s"%f.isatty())
    
    # 移动文件指针，并读取文件内容
    print("\ntell() 移动前指针位置：%s"%f.tell())
    f.seek(0,0) # f.seek(偏移量：整数，单位-比特,初始位置：0-文件头，1-当前位置，默认值，2-文件尾)
    print("seek(0,0) 指针移动回文件头")
    print("tell() 移动后指针位置：%s"%f.tell())
    
    print("\nread() 读取文件全部内容。如果指定，则最多读取n字节/字符\n[\n%s\n]"%f.read())
    print("tell() 读取全部后指针位置：%s"%f.tell())
    
    f.seek(0,0)
    print("\nseek(0,0) 指针移动回文件头")
    print("readline() 读取文件当前行。如果指定，则最多读取n字节/字符\n[\n%s\n]"%f.readline())
    print("tell() 读取当前行后指针位置：%s"%f.tell())
    print("readline() 读取文件当前行。如果指定，则最多读取n字节/字符\n[\n%s\n]"%f.readline())
    print("tell() 读取当前行后指针位置：%s"%f.tell())
    
    f.seek(0,0)
    print("\nseek(0,0)指针移动回文件头")
    print("readlines(5) 读取并返回文件中的行列表。如果指定，则最多读取n字节/字符\n[\n%s\n]"%f.readlines(5))
    
    f.seek(0,0)
    print("\nseek(0,0)指针移动回文件头")
    f.truncate(10) 
    print("truncate(10) 删除当前指针n个字节后内容，不指定默认0")
    print("read() 读取截断后内容\n[\n%s\n]"%f.read())
    
    f.seek(0,2)
    print("\nseek(0,0)指针移动到文件尾")
    # 写入文件
    f.write("第二行")
    f.write("第二行\n")
    f.writelines(["第三行\n","第四行\n"])
    
    f.flush()
    print("\nflush() 将缓冲区中的数据立刻写入文件，并且清空缓冲区")
    print("read() 读取刷新缓冲区后内容\n[\n%s\n]"%f.read())
finally:
    # 即使引发了导致程序流停止的异常，也可以保证文件正确关闭
    f.close()
```
输出  
使用a+模式读取  
fileno() 返回文件的整数号（文件描述符）：4  
isatty() 文件是否连接到一个终端设备：False  

tell() 移动前指针位置：52  
seek(0,0) 指针移动回文件头  
tell() 移动后指针位置：0  

read() 读取文件全部内容。如果指定，则最多读取n字节/字符  
[  
第一行  
第二行第二行  
第三行  
第四行  
  
]  
tell() 读取全部后指针位置：52  
  
seek(0,0) 指针移动回文件头  
readline() 读取文件当前行。如果指定，则最多读取n字节/字符  
[  
第一行  
  
]  
tell() 读取当前行后指针位置：11  
readline() 读取文件当前行。如果指定，则最多读取n字节/字符  
[  
第二行第二行  
  
]  
tell() 读取当前行后指针位置：30  
  
seek(0,0)指针移动回文件头  
readlines(5) 读取并返回文件中的行列表。如果指定，则最多读取n字节/字符  
[  
['第一行\n', '第二行第二行\n']  
]  
  
seek(0,0)指针移动回文件头  
truncate(10) 删除当前指针n个字节后内容，不指定默认0  
read() 读取截断后内容  
[  
第一行  
  
]  
  
seek(0,0)指针移动到文件尾  
  
flush() 将缓冲区中的数据立刻写入文件，并且清空缓冲区  
read() 读取刷新缓冲区后内容  
[  
  
]  

## 3. Open文件对象常用的属性

```python
f = open(r"F:\data\test\English_Path\test.txt", mode='w',encoding = 'utf-8')

f.name # 文件路径与名称
f.mode # 打开文件的模式
f.encoding # 打开文件的编码
f.closed # 文件是否关闭

f.close()
```

## 4. Open参数

**open(file, encoding=None, mode='r', buffering=-1, errors=None, newline=None, closefd=True, opener=None)**

- **file 文件路径或文件描述符（必填）** 

- **encoding 编码模式 str类型**
  在mode参数包含t时不可指定，即仅文本模式可用
  None：默认值，windows下默认gbk
  常用：utf-8、ascii、gbk

- **mode 操作模式 str类型**
  基础模式：r w a x
  在基础模式上，可选择打开模式与是否升级同时读写，例如：rb r+b

|Mode 模式|描述|
|--|--|
|r |基础模式，只读不写，默认值，无文件报错|
|w |基础模式，覆盖写入，无文件则创建文件|
|a |基础模式，追加写入，无文件则创建文件|
|x |基础模式，新建写入，有文件则报错|
| t|打开形式，以文本模式打开，默认值|
| b|打开形式，以二进制模式打开|
| +|升级模式，使得基础模式能同时读写|

<details>
<summary>点击展开查看：非常用参数</summary>
<p>

<h4>buffering 缓冲设置 [-1,0,1]</h4>
  -1：默认值，使用系统默认缓冲机制<br>
  0:不使用缓冲，直接读写磁盘<br>
  1:单行缓冲<br>

<h4>errors 编解码报错的处理模式 str类型</h4>
  在mode参数包含t时不可指定，即仅文本模式可用<br>
  常用模式：<br>
  strict：编解码错误则报错<br>
  ignore：编解码出现错误会忽略，不报错<br>
  replace：编解码出现错误不会报错，会用“?”替代要写入或读取的无法解析的数据<br>

<h4>newline 换行符设置，str类型</h4>
  None（默认）、"\r"、"\n"、"\r\n"<br>

<h4>closefd 控制file参数的传入值类型 bool类型</h4>
  True：默认，file参数可以是表示文件路径的字符串，也可以是文件描述符<br>
  False：file参数只能是文件描述符，传入字符串会报错。<br>

<h4>opener</h4>
  传递一个可调用的 opener 来使用自定义 opener<br>
  <pre style="color:white">
  import os
  dir_fd = os.open('somedir', os.O_RDONLY)
  def opener(path, flags):
      return os.open(path, flags, dir_fd=dir_fd)

  with open('spamspam.txt', 'w', opener=opener) as f:
      print('This will be written to somedir/spamspam.txt', file=f)

  os.close(dir_fd)  # 不要泄漏文件描述符
  </pre><br>
  参考链接：<br>
  https://stackoverflow.com/questions/37241711/what-is-the-use-of-opener-argument-in-built-in-open-function
</p>
</details>

## 5. os基础使用

1. 获取文件夹下所有文件名称

  方法一：listdir，得到的是仅当前路径下的文件名，不包括子目录中的文件  

  ```python
  import os
  os.listdir(path)
  ```

  方法二：os.walk(top, topdown=Ture, onerror=None, followlinks=False)   

  可以得到一个三元元组(dirpath, dirnames, filenames)  
  dirpath：表示获取的目录的路径，以string形式返回值  
  dirnames： 包含了当前dirpath路径下所有的子目录名字  

  ```python
  os.walk(path)
  f = os.walk(path)
  for dirpath,dirnames,filenames in f:
      print(dirpath)
      print(dirnames)
      print(filenames)
  ```

  ps.os.path.splitext()函数将路径拆分为文件名+扩展名（后缀）
  ```python
  os.path.splitext(filenames[0])
  >>> ('D:\\data\test', '.xlsx')
  ```

## 6. [其他python内置函数](../../../../2022/08/03/Python-Built-in-functions_Note.html)