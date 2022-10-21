---
title:  python内置函数
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# python内置函数

## 1. 异常处理-try except else finally
```python
try:
    必定会执行:测试代码
except:
    可能会执行:测试代码运行 错误 时执行
else:
    可能会执行:测试代码运行 正常 时执行
finally:
    必定会执行:收尾代码
```

## 2. break

跳出循环

## 3. enumerate

enumerate枚举器，在同时需要序号和内容时使用比较方便

```
for index,item in enumerate(list_):
    print(index,item)

# 下面代码有同样效果

for index in range(len(list_)):
    print(index,list_[index])
```

## 4. 文本执行

### 4.1 eval

```python
eval('print("hello world")')
>>>"hello world"
```

### 4.2 globals()

```python
globals()['num'] = 1
print(a)
>>>1
```