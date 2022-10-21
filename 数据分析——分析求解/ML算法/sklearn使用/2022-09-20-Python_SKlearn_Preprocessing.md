---
title:  python-Sklearn数据清洗
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# sklearn-preprocessing中的方法

**使用方法**
```
pre.fit(X_train) # 训练
pre.transform(X_train) # 转化
pre.fit_transform(X_train) # 训练并转化
```

**方法**

```python
# 标准化（Standardization）
preprocessing.StandardScaler() # 标准化z-score，（x-mean)/std
preprocessing.MinMaxScaler() # 归一化min-max，(x-min)/(max-min)
preprocessing.MaxAbsScaler() # 最大绝对值归一化，x/|max|

# 非线性转换（Non-linear transformation）
preprocessing.QuantileTransformer() # 针对每个特征，使用非参数化的分位数变换，将它转化为特定的分布（高斯分布或均匀分布）
preprocessing.PowerTransformer() # 对数转换，将偏态分布尽可能转化为正态分布

# 正则化（Normalization）该方法主要运用在文本和聚类中
preprocessing.normalize()
preprocessing.Normalizer()

# 编码分类特征（Encoding categorical features）
preprocessing.OrdinalEncoder()
preprocessing.OneHotEncoder() # 独热编码

# 离散化（Discretization）
preprocessing.KBinsDiscretizer()
preprocessing.FunctionTransformer()
preprocessing.Binarizer() # 二进制化

# 缺失值处理（Imputation of missing values）
preprocessing.Imputer()

# 生成多项式特征（Generating polynomial features）

# 自定义转化器（Custom transformers）
from sklearn.preprocessing import FunctionTransformer
```
