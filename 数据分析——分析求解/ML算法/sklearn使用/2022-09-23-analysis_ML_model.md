---
title:  机器学习模型
layout: default
---
[![返回](/assets/images/back.png)](../../../../)

# 机器学习模型

## 回归

回归是一种用于连续型数值变量预测和建模的监督学习算法。
回归算法有很多，这些算法的不同主要在于三方面：
1. 自变量的个数：一个or多个
2. 因变量的类型：连续or离散
3. 回归线的形状：线性or非线性

对于那些有创意的人，如果你觉得有必要使用上面这些参数的一个组合，你甚至可以创造出一个没有被使用过的回归模型。

常用的回归算法有：线性回归、多项式回归、岭回归、Lasso回归、弹性网络回归、逐步回归、回归树  
逻辑回归虽然也是叫回归，但是不是预测算法，是用于分类的，将在分类算法中介绍。

### 线性回归（LinearRegression）

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
