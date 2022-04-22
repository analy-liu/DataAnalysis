
# python中numpy包使用笔记

## 包导入


```python
import numpy as np
from pprint import pprint
import pandas as pd
```

## np.random生成随机数

### 随机数生成

在numpy中，常用于生成随机数的函数有：  

生成随机数：  

通用参数介绍  
size：输出的大小，可以是整数，或者元组。(2,3)生成两组样本量为3的数组  
(d0, d1, …, dn)：每个维度的长度 
1. **生成随机整数**：  
    返回[low, high)   
    np.random.randint(low, high=None, size=None, dtype='l')  
    参数：low :产生随机数的最小值，high : 给随机数设置个上限，dtype：期望结果的类型  
    返回[low, high]   
    np.random.random_integers(low, high=None, size=None)  
2. **均为从均匀分布[0,1)中随机采样**  
    np.random.random(size=None)  
    np.random.random_sample(size=None)  
    np.random.rand(d0, d1, …, dn)  
    例：np.random.random((0,10))等效于np.random.rand(0,10)等效于np.random.random_sample((0,10))    
    均匀分布是指在整个样本空间中的每一个样本点对应的概率（密度）都是相等的。
3. **从均匀分布[low,high)中随机采样**  
    np.random.uniform(low=0.0, high=1.0, size=None)  
4. **生成标准正态分布随机数**  
    np.random.randn(d0, d1, ..., dn)  
    获得一般正态分布：$\sigma \times np.random.randn(…) + \mu$或使用np.random.normal  

 

选取随机数
1. **从给定数组中随机选择样本**  
    np.random.choice(a, size=None, replace=True, p=None)    
参数：  
a：array or int，从array或range(int)中取随机数  
replace：True，放回抽样；False，不放回抽样  
p：array，参数a中每个数的对应的概率  

特殊分布随机数：  
1. **二项分布**  
    np.random.binomial(n, p, size=None)  
参数：  
n：实验次数  
p：成功概率  
2. **正态分布**
    np.random.normal(loc=0.0, scale=1.0, size=None)  
参数：  
loc：均值  
scale：方差  

### 随机种子

随机种子  
计算机生成的随机数其实是伪随机数，是由一定的方法计算出来的，因此我们可以按下面方法指定随机数生成的种子，这样的好处是以后重复计算时，能保证得到相同的模拟结果。  
np.random.seed(seed=None)  
注意种子设定是一次有效


```python
print("输出相同")
for i in range(3):
    np.random.seed(123)
    print(np.random.random())
print("输出不同")
np.random.seed(123)
for i in range(3):
    print(np.random.random())
```

    输出相同
    0.6964691855978616
    0.6964691855978616
    0.6964691855978616
    输出不同
    0.6964691855978616
    0.28613933495037946
    0.2268514535642031
    

## ndarray操作

### ndarray生成

**生成零矩阵**


```python
np.zeros((2,3))
```




    array([[0., 0., 0.],
           [0., 0., 0.]])



**按顺序生成指定shape矩阵**


```python
np.arange(16).reshape((2,2,4))
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7]],
    
           [[ 8,  9, 10, 11],
            [12, 13, 14, 15]]])



### ndarray查询操作

pandas是基于numpy包的，numpy的查询与pandas类似


```python
print("示例数据")
np.random.seed(1)
ndarray = np.random.randint(low = 0, high = 10, size = (3,4))
print(ndarray)
```

    示例数据
    [[5 8 9 5]
     [0 0 1 7]
     [6 9 2 4]]
    

查询矩阵的行


```python
print("单行:")
print(ndarray[0])
print('多行:')
print(ndarray[0:2])
```

    单行:
    [5 8 9 5]
    多行:
    [[5 8 9 5]
     [0 0 1 7]]
    

查询矩阵的列


```python
print('单列:')
print(ndarray[:, 0])
print('多列:')
print(ndarray[:, 0:2])
```

    单列:
    [5 0 6]
    多列:
    [[5 8]
     [0 0]
     [6 9]]
    

### ndarray计算

#### 单个ndarray加减乘除


```python
print("示例数据")
np.random.seed(1)
ndarray = np.random.randint(low = 0, high = 10, size = (3,4))
print(ndarray)
```

    示例数据
    [[5 8 9 5]
     [0 0 1 7]
     [6 9 2 4]]
    

对每个元素进行计算


```python
print(ndarray+1, "加法")
print(ndarray-1, "减法")
print(ndarray*2, "乘法")
print(ndarray/2, "除法")
```

    [[ 6  9 10  6]
     [ 1  1  2  8]
     [ 7 10  3  5]] 加法
    [[ 4  7  8  4]
     [-1 -1  0  6]
     [ 5  8  1  3]] 减法
    [[10 16 18 10]
     [ 0  0  2 14]
     [12 18  4  8]] 乘法
    [[2.5 4.  4.5 2.5]
     [0.  0.  0.5 3.5]
     [3.  4.5 1.  2. ]] 除法
    

对特定位置原始进行计算


```python
temp = ndarray.copy()
temp[0] += 1
print(ndarray,"原数据")
print(temp, "第一行加1")
```

    [[5 8 9 5]
     [0 0 1 7]
     [6 9 2 4]] 原数据
    [[ 6  9 10  6]
     [ 0  0  1  7]
     [ 6  9  2  4]] 第一行加1
    

#### 多个ndarray加减乘除

当两个ndarray的size相同时，加减乘除在对应位置上的数字进行计算


```python
print("示例数据")
np.random.seed(1)
ndarray_0 = np.random.randint(low = 0, high = 10, size = (3,4))
np.random.seed(2)
ndarray_1 = np.random.randint(low = 0, high = 10, size = (3,4))
print(ndarray_0)
print(ndarray_1)
```

    示例数据
    [[5 8 9 5]
     [0 0 1 7]
     [6 9 2 4]]
    [[8 8 6 2]
     [8 7 2 1]
     [5 4 4 5]]
    


```python
print(ndarray_0+ndarray_1, "加法")
print(ndarray_0-ndarray_1, "减法")
print(ndarray_0*ndarray_1, "乘法")
print(ndarray_0/ndarray_1, "除法")
```

    [[13 16 15  7]
     [ 8  7  3  8]
     [11 13  6  9]] 加法
    [[-3  0  3  3]
     [-8 -7 -1  6]
     [ 1  5 -2 -1]] 减法
    [[40 64 54 10]
     [ 0  0  2  7]
     [30 36  8 20]] 乘法
    [[0.625 1.    1.5   2.5  ]
     [0.    0.    0.5   7.   ]
     [1.2   2.25  0.5   0.8  ]] 除法
    

当ndarrayA是ndarrayB的单列或单行长度时，计算时会将ndarrayA与ndarrayB的每一行或列进行计算


```python
print("示例数据")
np.random.seed(1)
ndarray_B = np.random.randint(low = 0, high = 10, size = (3,4))
np.random.seed(2)
ndarray_A = np.random.randint(low = 0, high = 10, size = (3,1))
print(ndarray_A)
print(ndarray_B)
```

    示例数据
    [[8]
     [8]
     [6]]
    [[5 8 9 5]
     [0 0 1 7]
     [6 9 2 4]]
    


```python
print(ndarray_B+ndarray_A, "加法")
print(ndarray_B-ndarray_A, "减法")
print(ndarray_B*ndarray_A, "乘法")
print(ndarray_B/ndarray_A, "除法")
```

    [[13 16 17 13]
     [ 8  8  9 15]
     [12 15  8 10]] 加法
    [[-3  0  1 -3]
     [-8 -8 -7 -1]
     [ 0  3 -4 -2]] 减法
    [[40 64 72 40]
     [ 0  0  8 56]
     [36 54 12 24]] 乘法
    [[0.625      1.         1.125      0.625     ]
     [0.         0.         0.125      0.875     ]
     [1.         1.5        0.33333333 0.66666667]] 除法
    

#### 矩阵计算


```python
print("示例数据")
np.random.seed(1)
A = np.random.randint(low = 0, high = 10, size = (3,1))
np.random.seed(2)
B = np.random.randint(low = 0, high = 10, size = (1,3))
print(A)
print(B)
```

    示例数据
    [[5]
     [8]
     [9]]
    [[8 8 6]]
    


```python
print(A @ B) # 同np.dot(A,B)
print(B @ A)# 同np.dot(B,A)
```

    [[40 40 30]
     [64 64 48]
     [72 72 54]]
    [[158]]
    

这里结果是(A @ B)的，而不是(B @ A)，矩阵乘法尽量不要使用*符号，因为*号会自行判断进行计算。


```python
B * A 
```




    array([[40, 40, 30],
           [64, 64, 48],
           [72, 72, 54]])



### 数据合并
np.concatenate((a1, a2, ...), axis=0, out=None) # 根据axis堆叠数组

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b.T), axis=1))
```

    [[1 2]
     [3 4]
     [5 6]]
    [[1 2 5]
     [3 4 6]]
    
np.hstack() # 按水平堆叠数组

```python
a = np.array((1,2,3))
b = np.array((2,3,4))
print(np.hstack((a,b)))
a = np.array([[1],[2],[3]])
b = np.array([[2],[3],[4]])
print(np.hstack((a,b)))
```

    [1 2 3 2 3 4]
    [[1 2]
     [2 3]
     [3 4]]
    

## np函数库

### np数学公式


```python
fun = np.array([['np.pi()', '圆周率'],
                ['np.sin()', 'sin函数']])
pd.DataFrame(fun,columns = ["函数","简介"])
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
      <th>函数</th>
      <th>简介</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>np.pi()</td>
      <td>圆周率</td>
    </tr>
    <tr>
      <th>1</th>
      <td>np.sin()</td>
      <td>sin函数</td>
    </tr>
  </tbody>
</table>
</div>



### 生成等差数列np.linspace
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
start:数列开头
end;数列结尾
num:生成个数
endpoint:是否包含end
retstep:Ture返回元组(数列,步长)，False返回数列

```python
np.linspace(3,9,3,retstep=True)
```




    (array([3., 6., 9.]), 3.0)


