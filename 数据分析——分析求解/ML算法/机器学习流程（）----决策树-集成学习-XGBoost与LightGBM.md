 # 集成学习-系统理解XGBoost与LightGBM

- [集成学习-系统理解XGBoost与LightGBM](#集成学习-系统理解xgboost与lightgbm)
  - [1. 决策树](#1-决策树)
    - [1.1. 分类树](#11-分类树)
      - [1.1.1. 信息熵](#111-信息熵)
      - [1.1.2. 基尼指数(Gini)](#112-基尼指数gini)
    - [1.2. 回归树](#12-回归树)
  - [2. 梯度下降](#2-梯度下降)
    - [2.1. 偏导数和方向导数](#21-偏导数和方向导数)
    - [2.2. 梯度(Gradient)](#22-梯度gradient)
  - [3. 集成学习](#3-集成学习)
    - [3.1. bagging:随机森林](#31-bagging随机森林)
      - [3.1.1. 随机森林](#311-随机森林)
    - [3.2. boostng:adaboost,GBDT,XGBoost,LightGBM](#32-boostngadaboostgbdtxgboostlightgbm)
      - [3.2.1. AdaBoost](#321-adaboost)
      - [3.2.2. GBDT](#322-gbdt)
      - [3.2.3. LightGBM](#323-lightgbm)

## 1. 决策树

决策树从上自下的构造如下
根决策节点——决策节点——叶子节点
决策节点后面都会有分支，叶子节点后面没有分支

### 1.1. 分类树

#### 1.1.1. 信息熵

用信息熵构建分类决策树，就是追求每次分裂后，信息增益最大，也就是最求用最少的分裂节点来将类分完。

**信息熵**  

用来衡量信息不确定性的指标，不确定性是一个事件出现不同结果的可能性。信息熵越大，不确定性越高。  
计算方法如下：
$$H(X) = -\sum^{n}_{i=1}P(X=i)log_2P(X=i)$$
例如：
1. 正面概率0.5 反面概率0.5
   $Entropy = -(0.5 \times log_{2}0.5+0.5 \times log_{2}0.5)=1$
2. 正面概率0.99 反面概率0.01
   $Entropy = -(0.99 \times log_{2}0.99+0.01 \times log_{2}0.01)=0.08$

**条件熵**  

条件熵：在给定随机变量Y的条件下，随机变量X的不确定性  
$$H(X|Y=v) = -\sum^{n}_{i=1}P(X=i|Y=v)log_2P(X=i|Y=v)$$

信息增益=信息熵-条件熵，代表了在一个条件下，信息不确定性减少的程度  
条件熵越小，说明分类越彻底  ；信息增益越大，划分得越好  
$$I(X,Y) = H(X)-H(X|Y)$$

例如：  
父节点正面14例，反面16例，共30例  
子节点一正面13例，反面4例，共17例  
子节点二正面1例，反面12例，共13例  

正面在子节点熵的信息增益：  
$信息熵 = -(\frac{14}{30} \times log_{2}\frac{14}{30}+\frac{16}{30} \times log_{2}\frac{16}{30})=0.996$  
$子节点一熵 = -(\frac{13}{17} \times log_{2}\frac{13}{17}+\frac{4}{17} \times log_{2}\frac{4}{17}) = 0.787$  
$子节点二熵 = -(\frac{1}{13} \times log_{2}\frac{1}{13}+\frac{12}{13} \times log_{2}\frac{12}{13}) = 0.391$  
$条件熵  =\sum子节点权重*子节点熵=\frac{17}{30}0.787+\frac{13}{30}0.391 = 0.615$
$信息增益 = 信息熵-条件熵 = 0.996-0.615 = 0.381$

#### 1.1.2. 基尼指数(Gini)

基尼指数（Gini不纯度）表示在样本集合中一个随机选中的样本被分错的概率  
注意：Gini指数越小表示集合中被选中的样本被分错的概率越小，当集合中所有样本为一个类时，基尼指数为0
$$Gini(p) = \sum^K_{k=1}{p_k(1-p_k)} = 1-\sum^K_{k=1}{p_k^2}$$
$p_k$表示选中的样本属于第k个类别的概率

例如：  
总类别：正面5 反面9 共14  
子类别一：正面2 反面3 共5 占比0.36
子类别二：正面4 反面0 共4 占比0.29
子类别三：正面3 反面2 共5 占比0.36

$总Gini = 1-(\frac{5}{14}^2+\frac{9}{14}^2)=0.459$
$子一Gini = 1-(\frac{2}{5}^2+\frac{3}{5}^2)=0.48$
$子二Gini = 1-(\frac{4}{4}^2+\frac{0}{4}^2)=0.0$
$子三Gini = 1-(\frac{3}{5}^2+\frac{2}{5}^2)=0.48$
$子类Gini = \frac{5}{14}*0.48+\frac{4}{14}*0+\frac{5}{14}*0.48 = 0.342$
$Gini增益 = 0.459-0.342 = 0.117$

Gini越小分类越纯，所以Gini增益越大，表示该子类分类效果越好

### 1.2. 回归树

回归树，就是用树模型做回归问题，每一片叶子都输出一个预测值。预测值一般是叶子节点所含训练集元素输出的**均值**。

回归树分支标准（损失函数）：
  1. 标准方差
  2. 残差平方和/样本个数
回归树使用某一特征将原集合分为多个子集
  1. 用标准方差衡量子集中的元素是否相近，越小表示越相近，父节点标准方差-子节点加权标准方差最小为分支
  2. 用子集的残差平方和/样本个数相加起来，选最小的作为分支

停止条件，变化系数小于设定值（10%），或者元素个数小于某个值，或者树深度限制

## 2. 梯度下降

学习视频：https://www.bilibili.com/video/BV1uZ4y1L7bB

### 2.1. 偏导数和方向导数

**偏导数**

平行X或Y轴变化的斜率

$$f_x(x_0,y_0)=\lim_{\Delta x \to 0}\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x}$$
$$f_y(x_0,y_0)=\lim_{\Delta y \to 0}\frac{f(x_0,y_0+\Delta y)-f(x_0,y_0)}{\Delta y}$$

**方向余弦**（方向导数的角度）

$$\overrightarrow{l} = (a,b)$$
单位化
$$
\begin{align}
\overrightarrow{l}& = \frac{1}{\sqrt{a^2+b^2}}(a,b)\\
&= (\frac{a}{\sqrt{a^2+b^2}},\frac{b}{\sqrt{a^2+b^2}})\\
&= (cos\alpha,cos\beta)
\end{align}
$$

**方向导数**

方向导数是一个数，是函数上一点某一方向的斜率

$$\frac{\partial z}{\partial t}\mid _{(x_0,y_0)}=\lim_{t \to 0}\frac{f(x_0+tcos\alpha,y_0+tcos\beta)-f(x_0,y_0)}{t}$$

方向导数就是在方向任意的偏导数  
偏导数其实就是特殊的方向导数  

**方向导数的计算（需要可微）**

方向向量可以用x和y两个方向的偏导数结合方向余弦进行组合来表示

$$\frac{\partial z}{\partial t}\mid _{(x_0,y_0)}=f_x(x_0,y_0)cos\alpha+f_x(x_0,y_0)cos\beta $$

当$cos\alpha$与$cos\beta$ 都是1是，增长最快，也就是该点的梯度

### 2.2. 梯度(Gradient)

在空间的每一个点都可以确定无限多个方向，一个多元函数在某个点也必然有无限多个方向。因此，导数在这无限多个**方向导数中最大的一个**（它直接反映了函数在这个点的变化率的数量级）等于多少？它是**沿什么方向**达到的？描述这个最大方向导数及其所沿方向的矢量，就是我们所说的梯度。

概念：梯度是一个向量，梯度的方向就是函数在这点增长最快的方向，梯度的模就是该点的变化率，以此类推，降低最快的就是梯度的反方向，变化最慢的就和梯度垂直。

$$
grad f(x,y) = \nabla f(x,y) = (f_x,f_y)=\frac{\partial f}{\partial x}i+\frac{\partial f}{\partial y}j
$$

**梯度下降**  
朝着相反梯度的方向，就是下降的最大的方向

## 3. 集成学习

Bagging: 基学习器之间无强依赖关系，可同时生成的并行化方法  
Boosting：基学习器之前存在强烈的依赖关系，必须串行生成基分类器的方法

### 3.1. bagging:随机森林

设置基学习器数量，对数据集随机采样，生成子数据集，用于训练基学习器。  
然后分类树用每个分类器输出结果的众数作为结果，回归树用每个分类器的结果的平均值

#### 3.1.1. 随机森林

随机森林 = bagging+决策树

同时训练多个决策树，预测时综合考虑多个结果进行预测，例如取多个节点的均值（回归），或者众数（分类）

优势：
1. 消除了决策树容易过拟合的缺点
2. 减少了预测的方差，预测值不会因为训练数据的小变化而剧烈变化

随机体现在两点：
1. 从原来的训练数据集随机取一个子集作为森林中某一个决策树的训练数据
2. 每一次寻找分叉的特征时，在子集里随机选择

### 3.2. boostng:adaboost,GBDT,XGBoost,LightGBM

Boosting是将"弱学习算法"提升为"强学习算法"的过程。  
通过反复学习，得到一系列弱分类器，组合这些弱分类器得到一个强分类器。  
Boosting算法要涉及到加法模型和前向分布算法  

#### 3.2.1. AdaBoost

Adaboost是将关注点放在被错误分类的样本上，减小上一轮被正确分类的样本权值，提高被错误分类的样本权值

Adaboost采用加权投票的方法，分类误差小的弱分类器的权重大，而分类误差大的弱分类器的权重小

#### 3.2.2. GBDT

**BDT**  

BDT(提升决策树），是GBDT的基础。  
使用CART决策树为基学习器的集成学习方法  
计算步骤：
1. 输入数据$D = {(x_i,y_i)},i = 1,2,···,N$
2. 初始化决策树$f(x)=0$
3. For m = 1,2,···,M 循环生成m个弱学习器
   1. 针对每一个样本$(x_i,y_i)$计算**残差**,将残差作为label进行下一个弱分类器学习
        $T_{m,i} = y_i-f_{m-1}(x_i),i = 1,2,···,N$
   2. 利用$\{(x_i,T_{m,i})\}_{i=1,2,···,N}$ 训练一个决策树，得到 $T(x;\theta_m)$
   3. 更新$f_m(x) = f_{m-1}(x)+T{(x;\theta_m)}$
4. 完成以上迭代，得到提升树$f_M(x) = \sum^M_{m=1}T(x;\theta_m)$

**GBDT**

GBDT(Gradient Boosting Decision Tree)，梯度提升决策树  
BDT是用残差拟合基学习器，GBDT使用损失函数的负梯度拟合基学习器  

为什么要用梯度？因为要使得算法适用于不同的损失函数，因为不同损失函数的凸优化问题不一样，但求梯度，就能找到不同损失函数最快优化的方向

目标：使得每增加一棵树进行提升后，损失更小
$L(y_i,F_m(x_i))<L(y_i,F_{m-1}(x_i))$
$L(y_i,F_{m-1}(x_i))-L(y_i,F_m(x_i))>0$

公式推导：
$$
\begin{align}\notag
&目标&：&L(y_i,F_{m-1}(x_i))-L(y_i,F_m(x_i))>0\\\notag
 &已知&：& 
  \begin{cases}
  y_i\\
  f_m(x)=f_{m-1}(x)+T(x;\theta_m)
  \end{cases}\\\notag
&一阶泰勒展开&：&f(x)\approx f(x_0)+f'(x_0)(x-x_0)\\\notag
&泰勒展开变为&：&L(y_i,F_{m}(x_i))\\\notag
&&&\approx L(y_i,F_{m-1}(x_i))+\left.\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right|_{f_m(x)=f_{m-1}(x)}\times(f_m(x)-f_{m-1}(x))\\\notag
&&&\approx L(y_i,F_{m-1}(x_i))+\left.\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right|_{f_m(x)=f_{m-1}(x)}\times T(x;\theta_m)\\\notag
&移项&：&L(y_i,F_{m-1}(x_i))-L(y_i,F_{m}(x_i))\approx -\left.\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right|_{f_m(x)=f_{m-1}(x)}\times T(x;\theta_m)\\\notag
&为了达成目标&：&-\left.\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right|_{f_m(x)=f_{m-1}(x)}\times T(x;\theta_m)>0\\\notag
&当&：&-\left.\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right|_{f_m(x)=f_{m-1}(x)}\approx T(x;\theta_m)时，形成平方，结果恒大于等于0\\\notag
&目标达成&：&L(y_i,F_{m-1}(x_i))-L(y_i,F_m(x_i))\ge0(当等于0时不取这颗树)\\\notag
&残差r_m计算&：&r_m(x,y)=-[\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}]_{f_m(x)=f_{m-1}(x)}\\\notag
&将(x_i,y_i)代入&&r_m(x,y),可计算出r_m，得到m轮数据集T_m\\\notag
&m轮数据集&：&T_m = \{(x_1,r_{m1}),(x_2,r_{m2}),···,(x_N,r_{mN})\}
\end{align}
$$

以

损失函数（为了求导方便，在前面乘1/2）：  
$$L(y_i,F(x_i))=\frac{1}{2}(y_i-F(x_i))^2$$  
对$F(x_i)$求导，则有：  
$$\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}=F(x_i)-y_i$$
残差是梯度的相反数，即：
$$r_{ti}=y_i-F_{t-1}(X)=-[\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}]_{F(x)=F_{t-1}(x)}$$

GBDT的梯度提升流程：
1. 输入数据$D = {(x_i,y_i)},i = 1,2,···,N$
2. 初始化决策树$f(x)=argmin_{h_0}\sum^N_{i=1}L(y_i,h_0(x))$
3. for t = 1 to T do
   1. 计算负梯度
      $\tilde{y} = -[\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}]_{F(x)=F_{t-1}(x)},i=1,2,···,N$
   2. 拟合残差得到基学习器，$w_t$是错误率
      $w_t=argmin_{w_t}\sum^N_{i=1}L(\tilde{y}-h_1(x;w_t))$
   3. 得到基学习器的权重，$\alpha_t$是权重
      $\alpha_t=argmin_{\alpha_t}\sum^N_{i=1}L(y_i,f_{t-1}(x_i)+\alpha_th_t(x;w_t))$
   4. 更新
      $F_t(x)=F_{t-1}(x_i)+\alpha_th_t(x;w_t)$

GBDT的流程（回归）：
1. 输入数据$D = {(x_i,y_i)},i = 1,2,···,N$
2. 初始化决策树$f(x)=argmin_{h_0}\sum^N_{i=1}L(y_i,h_0(x))=argmin_{h_0}\sum^N_{i=1}L(y_i,c)$
3. for t = 1 to T do
   1. 计算负梯度
      $\tilde{y} = -[\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}]_{F(x)=F_{t-1}(x)},i=1,2,···,N$
   2. 拟合残差得到回归树，得到第t棵树的叶节点区域
      $h_t(x)=\sum^K_{k=1}c_kI(X\in R_{tk})$
   3. 更新
      $F_t(x)=F_{t-1}(x_i)+h_t(x)$
4. 得到加法模型：$F(x)=\sum^T_{t=1}h_t(x)$

#### 3.2.3. LightGBM

LightGBM是一款常用的GBDT工具包，由微软亚洲研究院开发，速度比XGBoost快，精度也不错。设计理念是：
- 单个机器在不牺牲速度的情况下，尽可能多的用上更多的数据
- 多级并行的时候，通信代价尽可能地低，并且在计算上可以做到线性加速
所以其使用了分布式的GBDT，选择了基于直方图的决策树算法

**直方图算法**

1. 数值型分桶
   对特征值去重后从大到小排序，并统计每个值的数量
   取max_bin和去重后值的个数中的最小值作为分桶个数
   计算bins中的mean_bin_size（num/bins_num)，如果某个distinct_value的count大于mean_bin_size，则把该特征值作为bins的上界，小于该特征值的第一个distinct_value作为下界；若某个distinct_value的count小于mean_bin_size，则要累计后再进行分组
   总结：就是要先确定分桶个数，再让每个桶里的特征值数量相同
2. 类别型分桶
