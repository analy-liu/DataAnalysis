---
title:  sklearn-基础使用
layout: default
---
[![返回](/assets/images/back.png)](../../../../)

# Scikit-learn基础使用

## 流水线（Pipeline）

流水线的输入为一连串的数据挖掘步骤，其中最后一步必须是估计器，前几步是转换器。输入的数据集经过转换器的处理后，输出的结果作为下一步的输入。最后，用位于流水线最后一步的估计器对数据进行分类。
每一步都用元组（ ‘名称’，步骤）来表示。现在来创建流水线。

[官网参数](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline)：

```python
# 简略
sklearn.pipeline.Pipeline(steps, *, memory=None, verbose=False)
# 展开
sklearn.pipeline.Pipeline(
  steps, # [('step_name1',method1),('step_name2',method2),('step_name3',method3)]
  memory=None, # 用于缓存管道的拟合变压器
  verbose=False # 设置为True，则打印每个步骤所花的时间
  )
# 属性
named_steps # Bunch Access the steps by name.
classes_ # ndarray of shape (n_classes,) The classes labels.
n_features_in_int # Number of features seen during first step fit method.
feature_names_in_ # ndarray of shape (n_features_in_,) Names of features seen during first step fit method.
```

|方法|描述|
|:-|:-|
|decision_function(X)|Transform the data, and apply decision_function with the final estimator.|
|fit(X[, y])|Fit the model.|
|fit_predict(X[, y])|Transform the data, and apply fit_predict with the final estimator.|
|fit_transform(X[, y])|Fit the model and transform with the final estimator.|
|get_feature_names_out([input_features])|Get output feature names for transformation.|
|get_params([deep])|Get parameters for this estimator.|
|inverse_transform(Xt)|Apply inverse_transform for each step in a reverse order.|
|predict(X, **predict_params)|Transform the data, and apply predict with the final estimator.|
|predict_log_proba(X, **predict_log_proba_params)|Transform the data, and apply predict_log_proba with the final estimator.|
|predict_proba(X, **predict_proba_params)|Transform the data, and apply predict_proba with the final estimator.|
|score(X[, y, sample_weight])|Transform the data, and apply score with the final estimator.|
|score_samples(X)|Transform the data, and apply score_samples with the final estimator.|
|set_params(**kwargs)|Set the parameters of this estimator.|
|transform(X)|Transform the data, and apply transform with the final estimator.|

使用例子：

```
# 
pipe = Pipeline([
  ('scaler', StandardScaler()), 
  ('svc', SVC())
],
verbose = True)
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

## 预处理

主要在sklearn.preprcessing包下。

[sklearn-数据清洗](../../../../2022/09/20/Python_SKlearn_Preprocessing.html)

## 特征

### 特征抽取

sklearn.feature_extraction

### 特征选择

sklearn.feature_selection

## 降维

sklearn.decomposition

主成分分析算法（Principal Component Analysis， PCA）

## 组合

sklearn.ensemble

组合技术即通过聚集多个分类器的预测来提高分类准确率。
常用的组合分类器方法：
(1)通过处理训练数据集。即通过某种抽样分布，对原始数据进行再抽样，得到多个训练集。常用的方法有装袋（bagging）和提升（boosting）。
(2)通过处理输入特征。即通过选择输入特征的子集形成每个训练集。适用于有大量冗余特征的数据集。随机森林（Random forest）就是一种处理输入特征的组合方法。
(3)通过处理类标号。适用于多分类的情况，将类标号随机划分成两个不相交的子集，再把问题变为二分类问题，重复构建多次模型，进行分类投票。

## 模型评估（度量）

sklearn.metrics

### 分类评估

### 回归评估

### 多标签评估

### 聚类评估

## 交叉验证

选出最优评分的模型，步骤如下：
1. K折交叉划分数据集
2. 对每次划分的结果执行：
   1. 在训练集上训练学习器
   2. 使用学习器预测测试集，返回测试性能得分
3. 收集所有的测试性能得分，放入一个数组并返回

sklearn提供了cross_validation函数来便利的实现上面的步骤

[官网参数](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate)

```python
# 简略
sklearn.model_selection.cross_validate(estimator, X, y=None, *, groups=None, scoring=None, cv=None, n_jobs=None, verbose=0, fit_params=None, pre_dispatch='2*n_jobs', return_train_score=False, return_estimator=False, error_score=nan)
# 展开
sklearn.model_selection.cross_validate(
  estimator, # 分类器
  X, 
  y=None,
  groups=None, # 将数据集拆分为train/test的标签
  scoring=None, # 模型的评估类型
  cv=None, # 交叉验证的折数
  n_jobs=None, # 使用cpu核数，默认None为1核
  verbose=0, # 控制训练时返回的消息，越高返回消息越多。int
  fit_params=None, # 训练参数
  pre_dispatch='2*n_jobs', # 控制并行数，默认就好
  return_train_score=False, # 返回训练集分数，bool
  return_estimator=False, # 返回每折的估计器
  error_score=nan)
```

## 网格搜索

网格搜索(GridSearchCV)，是自动化调参的常见技术之一，实际上就是for循环暴力搜索选出最优参数，运行过程中包含了交叉验证。

[官网参数](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV)：

```python
# 简略
sklearn.model_selection.GridSearchCV(estimator, param_grid,scoring=None, n_jobs=None, refit=True, cv=None, verbose=0, pre_dispatch='2*n_jobs', error_score=nan, return_train_score=False)
# 展开
sklearn.model_selection.GridSearchCV(
  estimator, # 分类器
  param_grid, # 需要优化的算法参数，用字典或列表的形式给出
  scoring=None, # 模型的评估类型，str, callable, list, tuple or dict
  n_jobs=None, # 使用cpu核数，默认None为1核，-1使用全部核心
  refit=True, # 使用找到的最佳参数重新训练数据
  cv=None, # 交叉验证的折数，把样本数据随机的分成K份，每次随机的选择K-1份作为训练集，剩下的1份做验证集,一般从3开始取
  verbose=0, # 控制训练时返回的消息，越高返回消息越多。int
  pre_dispatch='2*n_jobs', # 控制并行数，默认就好
  error_score=nan, # 
  return_train_score=False # 返回训练集分数，bool)

# 属性
grid_scores_ # 命名元组组成的列表，列表中每个原始都对应了一个参数组合的测试得分
best_estimator_ # 一个学习器对象，代表根据候选参数筛选出来的最佳学习器
best_score_ # 最佳学习器的性能评分
best_params_ # 最佳参数组合
# 方法
fit(x[,y]) # 执行参数优化
predict(X) # 使用学习到的最佳学习器来预测数据
predict_log_proba(X) # 
predict_proba(x) #
score(x[,y])
```

## 多分类、多标签分类