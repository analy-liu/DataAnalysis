
# python中sklearn包中各种算法应用

本篇介绍sklearn包，及其各种算法的使用与调参


```python
# 依赖包
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

## 数据据操作

### 数据集加载工具


```python
from sklearn import datasets
```

#### 自带的小数据集（packaged dataset）

scikit-learn 内置有一些小型标准数据集，不需要从某个外部网站下载任何文件，用datasets.load_xx()加载。


```python
# 适用于分类任务
iris = datasets.load_iris()  # 导入鸢尾花数据
digits = datasets.load_digits()  # 导入手写数字数据
wine = datasets.load_wine()  # 导入红酒数据
cancer = datasets.load_breast_cancer()  # 导入乳腺癌数据，二分类
# 适用于回归任务
boston = datasets.load_boston()  # 导入波士顿房价数据
diabetes = datasets.load_diabetes()  # 导入糖尿病数据

# 查看数据集，以iris为例
iris.keys() # 查看键(属性)['data','target','feature_names','DESCR', 'filename']
iris.data.shape # 查看数据的形状
iris.target.shape # 查看数据的形状
iris.feature_names # 查看有哪些特征
iris.DESCR # 描述这个数据集的信息
iris.filename # 文件路径
```

#### 可在线下载的数据集（Downloaded Dataset）

scikit-learn 提供加载较大数据集的工具，并在必要时可以在线下载这些数据集，用datasets.fetch_xx()加载。


```python
olivetti = datasets.fetch_olivetti_faces() # 脸部图片数据集
newsgroups = datasets.fetch_20newsgroups() # 20,000左右的新闻组文档，均匀分为20个不同主题的新闻组集合
```

#### 计算机生成的数据集（Generated Dataset）

##### 生成簇


```python
centers = [[2,2],[8,2],[2,8],[8,8]]
x, y = datasets.make_blobs(n_samples=1000, n_features=2, centers=4,cluster_std=1)
```

n_samples:样本数

n_features:特征数（维度）

centers:中心数，也可以是中心的坐标

cluster_std:簇的方差


```python
p1 = plt.scatter(x[:,0],x[:,1],marker = '.',s =20)
plt.xlabel('x')
plt.ylabel('y')
plt.title('plot')
# plt.legend() # 显示图例
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_16_0.png)


#### svmlight/libsvm格式的数据集

#### 从买了data.org在线下载获取的数据集

### 数据预处理

#### z-score标准化（规范化）


```python
from sklearn.preprocessing import StandardScaler
```

StandardScaler对数据进行规范化处理，即使数据每一列均值为0，方差为1。  
还可以在训练数据集上做了标准转换操作之后，把相同的转换应用到测试训练集中。

**函数**


```python
StandardScaler(copy=True, with_mean=True, with_std=True)
```

**参数**

**copy** : boolean, optional, default True  
    如果为False，设置为False以执行就地行规范化并避免复制。但并不能保证总是在原数据上进行替换，例如当数据为NumPy array时。  
**with_mean** : boolean, default True  
    是否均值中心化  
**with_std** : boolean, default True  
    是否方差规模化为1。


```python
data_train = np.array([[2, 0], [2, 0], [3, 1], [3, 1]])# 训练集
data_test = np.array([[2, 5]]) # 测试集
scaler = StandardScaler(copy=True, with_mean=True, with_std=True)# 设置实例
print(scaler.fit(data_train))# 训练数据
print("原数据：")
print(data_train)
print("mean:", scaler.mean_)# 每列均值
print("var:", scaler.var_)# 每列方差
print("scale", scaler.scale_)# 每个要素的数据相对缩放比例
print("估计器处理的样本数:", scaler.n_samples_seen_)
print("规范化后的训练数据：")
print(scaler.transform(data_train)) # 变化后的数据
print("将训练集的均值方差应用到测试集，进行规范化：")                      
print(scaler.transform(data_test)) # 变化后的数据
```

    StandardScaler(copy=True, with_mean=True, with_std=True)
    原数据：
    [[2 0]
     [2 0]
     [3 1]
     [3 1]]
    mean: [2.5 0.5]
    var: [0.25 0.25]
    scale [0.5 0.5]
    估计器处理的样本数: 4
    规范化后的训练数据：
    [[-1. -1.]
     [-1. -1.]
     [ 1.  1.]
     [ 1.  1.]]
    将训练集的均值方差应用到测试集，进行规范化：
    [[-1.  9.]]
    

    D:\python notebook\Anaconda\Lib\site-packages\sklearn\utils\validation.py:475: DataConversionWarning: Data with input dtype int32 was converted to float64 by StandardScaler.
      warnings.warn(msg, DataConversionWarning)
    D:\python notebook\Anaconda\Lib\site-packages\sklearn\utils\validation.py:475: DataConversionWarning: Data with input dtype int32 was converted to float64 by StandardScaler.
      warnings.warn(msg, DataConversionWarning)
    

#### min-max标准化（归一化）


```python
from sklearn.preprocessing import MinMaxScaler
```

使用方法与StandardScaler很像，只是数据会被规模化到[-1,1]之间。公式：$$x' = \frac{x-x_{min}}{x_{max}-x_{min}}$$  
   这个方法对那些已经中心化均值为0或者稀疏的数据有意义。

**函数**


```python
MinMaxScaler(feature_range=(0, 1), copy=True)
```

**参数**

**MinMaxScaler**(feature_range=(0, 1), copy=True)  
缩放范围，默认0-1之间  
**copy** : boolean, optional, default True  
设置为False以执行就地行规范化并避免复制  


```python
data_train = np.array([[2, 0], [2, 0], [3, 1], [3, 1]])# 训练集
data_test = np.array([[2, 5]]) # 测试集
scaler = MinMaxScaler()# 设置实例
print(scaler.fit(data_train))# 训练数据
print("原数据：")
print(data_train)
print("min:", scaler.data_min_)# 每列最小值
print("max:", scaler.data_max_)# 每列最大值
print("scale", scaler.scale_)# 每个要素的数据相对缩放比例
print("每个特征范围:", scaler.data_range_)
print("规范化后的训练数据：")
print(scaler.transform(data_train)) # 变化后的数据
print("将训练集的均值方差应用到测试集，进行规范化：")                      
print(scaler.transform(data_test)) # 变化后的数据
```

    MinMaxScaler(copy=True, feature_range=(0, 1))
    原数据：
    [[2 0]
     [2 0]
     [3 1]
     [3 1]]
    min: [2. 0.]
    max: [3. 1.]
    scale [1. 1.]
    每个特征范围: [1. 1.]
    规范化后的训练数据：
    [[0. 0.]
     [0. 0.]
     [1. 1.]
     [1. 1.]]
    将训练集的均值方差应用到测试集，进行规范化：
    [[0. 5.]]
    

    D:\python notebook\Anaconda\Lib\site-packages\sklearn\utils\validation.py:475: DataConversionWarning: Data with input dtype int32 was converted to float64 by MinMaxScaler.
      warnings.warn(msg, DataConversionWarning)
    

#### 训练集与测试集区分


```python
from sklearn.model_selection import train_test_split
```

函数：  
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,test_size=0.3)


```python
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
```

## 回归算法

回归是一种用于连续型数值变量预测和建模的监督学习算法。
回归算法有很多，这些算法的不同主要在于三方面：
1. 自变量的个数：一个or多个
2. 因变量的类型：连续or离散
3. 回归线的形状：线性or非线性

对于那些有创意的人，如果你觉得有必要使用上面这些参数的一个组合，你甚至可以创造出一个没有被使用过的回归模型。

常用的回归算法有：线性回归、多项式回归、岭回归、Lasso回归、弹性网络回归、逐步回归、回归树  
逻辑回归虽然也是叫回归，但是不是预测算法，是用于分类的，将在分类算法中介绍。

### 线性回归(Linear Regression)


```python
from sklearn.linear_model import LinearRegression
```

**函数**


```python
LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)
```

**参数**

**fit_intercept=True**, 是否计算该模型的截距。如果设置为False，在计算中将不使用截距  
**normalize=False**, 当fit_intercept设置为False时，此参数将被忽略。如果为True，则回归变量X将在回归之前通过以下方式归一化减去均值并除以l2-范数。  
**copy_X=True**, 如果为True，将复制X。否则，它可能会被覆盖。  
**n_jobs=1**，用于计算的作业数。如果为-1，则使用所有CPU。这只会提供加速

**例子**  
使用数据：sin函数数据


```python
# Xsin函数数据
X = np.random.uniform(1,25,2500)*0.041
# sklearn 要求输入的特征为二维数组类型。
X = X.reshape(-1,1) #数据集只有1个特征，需要用array.reshape(-1, 1)来改变数组的形状
y = np.sin(2*np.pi*X)+np.random.normal(0,0.3,2500).reshape(-1,1)
# 区分训练集与测试集
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
```


```python
#画图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X,y,marker = '.')
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_50_0.png)



```python
model = LinearRegression()
model.fit(X_train, y_train)

print(model)
a = model.intercept_# 截距
b = model.coef_#斜率
y_pred = model.predict(X_test) # 预测值
print (a)
print (b)
```

    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    [1.04944144]
    [[-1.97897722]]
    


```python
# 画出区分线
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X,y,marker = '.')
ax.plot(np.sort(X_test.reshape(len(y_test))), y_pred.reshape(len(y_test))[np.argsort(X_test.reshape(len(y_test)))], color='r')
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_52_0.png)


可以看到线性规划对非线性数据的拟合效果不理想，后面将使用多项式回归进行改进

### 多项式回归(Polynomial Regression)

**例子**  
使用数据与线性回归时相同：sin函数数据


```python
from sklearn.linear_model import LinearRegression #多项式回归本质还是线性回归
```

**自己构建多项式回归**


```python
## 为数据增加特征
X_train_poly = np.hstack([X_train,X_train**2,X_train**3])
X_test_poly = np.hstack([X_test,X_test**2,X_test**3])
# 使用增维后的训练数据训练模型
model = LinearRegression()
model.fit(X_train_poly, y_train)

print(model)
a = model.intercept_# 截距
b = model.coef_#斜率
# 使用增维后的测试数据获得预测结果
y_pred = model.predict(X_test_poly) # 预测值
print (a)
print (b)
```

    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    [-0.2813604]
    [[ 12.32341682 -34.87623992  22.91706699]]
    


```python
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X, y, marker='.')
ax.plot(np.sort(X_test.reshape(len(y_test))), 
        y_pred.reshape(len(y_test))[np.argsort(X_test.reshape(len(y_test)))], 
        color='r')
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_59_0.png)


可以看到多项式回归对数据的拟合效果很好

**使用PolynomialFeatures构建多项式回归**

**函数**


```python
PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
```

**参数**

**degree** : integer, default = 2。多项式中的次数  
**interaction_only** : boolean, default = False。是否只产生交互项  
**include_bias** : boolean。如果为True（默认值），生成一列截距项  


```python
from sklearn.preprocessing import PolynomialFeatures
```


```python
## 为数据增加特征
poly = PolynomialFeatures(degree=3)
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
poly.fit(X_test)
X_test_poly = poly.transform(X_test)
# 使用增维后的训练数据训练模型
model = LinearRegression()
model.fit(X_train_poly, y_train)

print(model)
a = model.intercept_# 截距
b = model.coef_#斜率
# 使用增维后的测试数据获得预测结果
y_pred = model.predict(X_test_poly) # 预测值
print (a)
print (b)
```

    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    [-0.28485678]
    [[  0.          12.17621653 -34.68596287  22.93775037]]
    


```python
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X, y, marker='.')
ax.plot(np.sort(X_test.reshape(len(y_test))), 
        y_pred.reshape(len(y_test))[np.argsort(X_test.reshape(len(y_test)))], 
        color='r')
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_68_0.png)


### 岭回归(Ridge Regression)

**使用数据：波士顿房价**


```python
boston = datasets.load_boston()
y = boston.target
X = pd.DataFrame(boston.data, columns=boston.feature_names)
# 区分训练集与测试集
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
```


```python
from sklearn.linear_model import Ridge
```

**函数**


```python
Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True,
      max_iter=None, tol=0.001, solver='auto', random_state=None)
```

**参数**

**alpha = 1.0**, 正则强度；必须为正浮点数。  
**fit_intercept = True**, 是否计算此模型的截距。如果设置为False，在计算中将不使用截距。  
**normalize = False**, 当fit_intercept设置为False时，此参数将被忽略。如果为True，则回归变量X将在回归之前通过以下方式归一化减去均值并除以l2-范数。  
**copy_X = True**, 如果为True，将复制X。否则，它可能会被覆盖。  
**max_iter = None**, 共轭梯度求解器的最大迭代次数。  
**tol = 0.001**, 解决方案的精度。  
**solver = 'auto'**, 在计算例程中使用的求解器  
**random_state = None**, 在对数据进行混洗时使用的伪随机数生成器的种子。  
* 如果为int，则random_state是随机数生成器使用的种子；否则为false。
* 如果是RandomState实例，则random_state是随机数生成器；否则，
* 如果为None，则随机数生成器为RandomState


```python
model = Ridge(alpha=100) # alpha为正则项系数，等于0相当于没有惩罚，和线性回归一样的
model.fit(X_train, y_train) 
print(model)
a = model.intercept_# 截距
b = model.coef_#斜率
y_pred = model.predict(X_test) # 预测值
print (a)
print (b)
```

    Ridge(alpha=100, copy_X=True, fit_intercept=True, max_iter=None,
       normalize=False, random_state=None, solver='auto', tol=0.001)
    33.99714384593979
    [-0.09390563  0.04001784 -0.06479426  0.31601924 -0.19995065  2.29614152
     -0.00621919 -0.83551794  0.26990333 -0.01646376 -0.71182796  0.00667029
     -0.56477841]
    

### 套索回归 (Lasso Regression)

**与岭回归使用数据相同：波士顿房价**


```python
from sklearn.linear_model import Lasso
```

**函数**


```python
Lasso(alpha=1.0, fit_intercept=True, normalize=False, precompute=False, copy_X=True, max_iter=1000,
      tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')
```

**参数**

**alpha=1.0**,  与L1项相乘的常数。默认为1.0。alpha = 0等效于一个普通的最小二乘法  
**fit_intercept = True**, 是否计算此模型的截距。如果设置为False，在计算中将不使用截距。  
**normalize = False**, 当fit_intercept设置为False时，此参数将被忽略。如果为True，则回归变量X将在回归之前通过以下方式归一化减去均值并除以l2-范数。  
**precompute=False**, 是否使用预先计算的Gram矩阵来加快速度计算。可设置为"auto"对于稀疏输入此选项始终为“ True”以保留稀疏性  
**copy_X=True**, 如果为True，将复制X;否则，它可能会被覆盖。  
**max_iter=1000**, 最大迭代次数  
**tol=0.0001**, 优化的容忍度  
**warm_start=False**, 设置为True时，重用上一个调用的解决方案以适合初始化，否则，只需擦除以前的解决方案即可。
**positive=False**, 设置为True时，强制系数为正数。  
**random_state=None**, 在对数据进行混洗时使用的伪随机数生成器的种子。  
**selection='cyclic'**,  如果设置为“ random”，则每次迭代都会更新一个随机系数，而不是默认情况下按顺序遍历功能。这（设置为“random”）通常会大大加快收敛速度特别是当tol高于1e-4时。 


```python
model = Lasso(alpha=0.1, precompute=True, selection='random')
model.fit(X_train, y_train)
print(model)
a = model.intercept_  # 截距
b = model.coef_  # 斜率
y_pred = model.predict(X_test) # 预测值
print(a)
print(b)
```

    Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
       normalize=False, positive=False, precompute=True, random_state=None,
       selection='random', tol=0.0001, warm_start=False)
    16.085274933944255
    [-0.07797194  0.02993933 -0.0183403   0.         -0.          4.71282552
     -0.02209376 -0.78274467  0.20314846 -0.01526007 -0.66817992  0.00787969
     -0.40898228]
    

### 弹性网络回归(ElasticNet Regression)

### 逐步回归（stepwise regression）

### 回归树

## 分类算法


```python
# 乳腺癌数据，二分类算法
cancer = datasets.load_breast_cancer()
y = cancer.target
X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
```

### 逻辑回归(Logistic Regression)

### 线性判别分析算法（LDA）

### 朴素贝叶斯

### 支持向量机(SVM)

### KNN

### 决策树

### 随机森林

### XGBoost


```python
import xgboost as xgb
```


```python
# 计算正负不平衡参数
value_label = pd.value_counts(y_train)
# false/ture
F = list (value_label)[0]
T = list (value_label)[1]
F_T = F/T
```


```python
# parameter
params = {                
  'objective' :'binary:logistic', #学习目标：二元分类的逻辑回归，输出概率
  'colsample_bytree' : 0.7, #子采样率
  'eta' : 0.3, #学习速率
  'max_depth' : 6, #最大深度
  'n_estimators' : 100, #最大迭代次数
  'scale_pos_weight' : F_T, #正负权重平衡
  'max_delta_step' : 0, #子叶输出最大步长
  'subsample' : 0.9 ,#训练实例的子样本比率
  'gamma' : 2.9 ,#节点分裂所需的最小损失函数下降值
  'min_child_weight' : 4 ,#决定最小叶子节点样本权重和
  'nthread' : 4 ,#线程数
  'alpha' : 0.01 ,#L1正则化速率
  'lambda' : 0.1, #L2正则化速率
#   'eval_metric ': 'logloss'
    
}
# set model
dtrain = xgb.DMatrix(X_train, y_train)
# dtest = xgb.DMatrix(X_test, y_test)
num_rounds = params['n_estimators']
```


```python
# cv select best num_boost_round(xg) and train model
def modelfit(dtrain, params, num_rounds, useTrainCV=True, cv_folds=5, early_stopping_rounds=50):
    if useTrainCV:
        cvresult = xgb.cv(params, dtrain, num_boost_round=params['n_estimators'], nfold=5,
                          metrics='auc', early_stopping_rounds=early_stopping_rounds, verbose_eval=True)
        params['n_estimators'] = cvresult.shape[0]
    num_rounds = params['n_estimators']
    # train model
    print(cvresult.shape[0])
    model = xgb.train(params, dtrain, num_rounds)

    return model, num_rounds
```


```python
model,num_rounds = modelfit(dtrain,params,num_rounds,useTrainCV = True,early_stopping_rounds = 10)
```
    

## 聚类算法

### k-means聚类

### 层次聚类

## 降维算法

### 主成分分析法（PAC）

### 奇异值分解（SVD）

## 整合机器学习流程

在sklearn中，提供了pipeline方法，能将多个处理数据的函数打包在一起，数据按照顺序进行训练和转换。  
作用：减少代码量，同时让机器学习的流程变得直观  
例如：数据可以先进行PCA降维，在进行标准化，最后训练模型。  
注意：除了最后一个步骤，前面的步骤都要有transform函数，最后一个步骤一般为模型，pipeline继承最后一个函数的所有方法。


```python
from sklearn.pipeline import Pipeline
```

这里以多项式回归为例


```python
# 训练
model = Pipeline([
    ('poly', PolynomialFeatures(degree=3)),# 构建多项式回归
    ('std_scale', StandardScaler()),# 数据规范化
    ('lin_reg', LinearRegression())# 训练线性回归
])  
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# 画图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X, y, marker='.')
ax.plot(np.sort(X_test.reshape(len(y_test))), 
        y_pred.reshape(len(y_test))[np.argsort(X_test.reshape(len(y_test)))], 
        color='r')
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_114_0.png)


## 模型评价与调优

### 模型评价


```python
from sklearn import metrics
```

#### 线性回归模型评价


```python
def score_linreg(y_true, y_predict, X_train):
    n = X_train.shape[0]
    k = X_train.shape[1]
    MSE = metrics.mean_squared_error(y_true, y_predict)
    r2 = metrics.r2_score(y_true, y_predict)
    r2_Adjusted = 1-(1-r2)*(n-1)/(n-k-1)
    # MSE是均方残差，MSE越小模型越准确
    print ("MSE:",MSE)
    # 估计标准误差，越小说明估计值越接近真实值
    print ("RMSE:",np.sqrt(MSE))
    #可决系数，0-1之间，越接近1模型对数据的拟合度越好
    print ("R-square:",metrics.r2_score(y_true, y_predict))
    #修正可决系数，消除了样本数量和特征数量的影响。0-1之间，一般要大于0.4，太接近1需要考虑过拟合问题
    print ("Adjusted R-Square",r2_Adjusted)
```


```python
#y_pred = model.predict(X_test) # 使用模型计算估计值
score_linreg(y_test, y_pred, X_train)
```

    MSE: 0.09657704865020164
    RMSE: 0.31076848078626257
    R-square: 0.8462848630144177
    Adjusted R-Square 0.8461969252930301
    

#### 分类模型评价

**函数**


```python
metrics.recall_score(y_true, y_pred, labels=None, pos_label=1, average='binary', sample_weight=None)
metrics.precision_score(y_true, y_pred, labels=None, pos_label=1, average='binary', sample_weight=None)
metrics.f1_score(y_true, y_pred, labels=None, pos_label=1, average='binary', sample_weight=None)
metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)
metrics.roc_auc_score(y_true, y_score, average='macro', sample_weight=None)
metrics.log_loss(y_true, y_pred, eps=1e-15, normalize=True, sample_weight=None, labels=None)
```

**参数**

y_true,  
y_pred,  

**recall、precision与f1_score参数**  
labels=None,   
pos_label=1,   
average='binary',   
sample_weight=None  

**accuracy与auc参数**  
sample_weight=None  
normalize=True  
average='macro'  

**logloss**  
eps=1e-15,


```python
# accuracy and auc
def score_xgb(model,X_data,y_data):
    dtest = xgb.DMatrix(X_data)
    preds =  model.predict(dtest)
    y_pred = [round(value) for value in preds]
    accuracy = metrics.accuracy_score(y_data, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    roc_auc = metrics.roc_auc_score(y_data, predictions)
    print("auc: %.2f%%" % (roc_auc * 100.0))
    recall = metrics.recall_score(y_data, predictions)
    print("recall: %.2f%%" % (recall * 100.0))
    precision = metrics.precision_score(y_data, predictions)
    print("precision: %.2f%%" % (precision * 100.0))
    f1 = metrics.f1_score(y_data, predictions)
    print("f1: %.2f%%" % (f1 * 100.0))
    log_loss = metrics.log_loss(y_data, predictions)
    print("log_loss:", log_loss)
```


```python
score_xgb(model,X_test,y_test)
```

    Accuracy: 94.15%
    auc: 92.72%
    recall: 98.15%
    precision: 92.98%
    f1: 95.50%
    log_loss: nan
    

    D:\python notebook\Anaconda\Lib\site-packages\sklearn\metrics\classification.py:1694: RuntimeWarning: divide by zero encountered in log
      loss = -(transformed_labels * np.log(y_pred)).sum(axis=1)
    D:\python notebook\Anaconda\Lib\site-packages\sklearn\metrics\classification.py:1694: RuntimeWarning: invalid value encountered in multiply
      loss = -(transformed_labels * np.log(y_pred)).sum(axis=1)
    

### 模型调优

#### 网格搜索


```python
from sklearn.model_selection import GridSearchCV
```

#### 交叉验证


```python
from sklearn.model_selection import cross_val_predict
```


```python
predicted = cross_val_predict(model, X, y, cv=10)
score_linreg(y, predicted, X)
```

    MSE: 34.0628028155975
    RMSE: 5.836334707296824
    R-square: 0.5965057817576581
    Adjusted R-Square 0.5858443491618239
    
