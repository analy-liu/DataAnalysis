分享一个数据科学利器 PyCaret，几行代码搞定从数据处理到模型部署
- [初始化](#初始化)
- [比较所有模型](#比较所有模型)
- [创建逻辑回归模型](#创建逻辑回归模型)
- [调节 LR 模型](#调节-lr-模型)
- [创建一个决策树模型](#创建一个决策树模型)
- [blend_models 混合特殊的模型](#blend_models-混合特殊的模型)
- [创建单个模型，用于stacking](#创建单个模型用于stacking)
- [stacking 模型](#stacking-模型)
- [创建逻辑回归模型](#创建逻辑回归模型-1)
- [创建一个模型](#创建一个模型)
- [创建模型](#创建模型)
- [finalize a model](#finalize-a-model)
- [创建模型](#创建模型-1)
- [最终确定模型](#最终确定模型)
- [部署模型](#部署模型)
- [创建模型](#创建模型-2)
- [二进制保存模型](#二进制保存模型)
东哥起飞
专栏作者
共发布 5 篇文章
 关注
学习数据科学很久了，从数据探索、数据预处理、数据模型搭建和部署这些过程一直有些重复性的工作比较浪费时间，尤其当你有个新的想法想要快速尝试下效果的时候，效率很低。

东哥最近发现一个开源的 Python 机器学习库，名字叫 PyCaret，这个轮子正好可以为了解决我刚才所描述的困扰，它的特点是以 low-code 低代码量来快速解决从数据预处理到模型部署的整个流程。

用了一下感觉确实有点香，因此也和大家分享一下。



PyCaret 是什么？
PyCaret 是一个将我们常用到的机器学习库进行封装了的轮子。

常用的都有啥呢？

比如 pandas,numpy 做数据处理的，matplotlib,seaborn 数据可视化的，sklearn,xgboost,catboost,lightgbm 等各种模型的，总共有 30 个。在安装 PyCaret 的时候会附带着一起都安装上。

封装这么多库干什么用？

PyCaret 依赖了这么多的神库肯定是要搞事情啊。

没错，机器学习中的一些操作步骤都可在 PyCaret 自动开发的 pipeline 中进行复现。在 Pycaret 中所执行的所有操作均按顺序存储在 Pipeline 中，该 Pipeline 针对模型部署进行了完全配置。

PyCaret 就像是把所有都安排好了一样，我们按照它定义的函数使用就可以了。不管是填充缺失值、转换类别数据、执行特征工程设计，还是调参，Pycaret 都能够自动执行。

所以才可以实现用几行代码搞定从预处理到模型部署的整个流程。

而且 pipeline 可以保存为二进制文件格式，支持在不同环境中进行迁移。



PyCaret 支持的模型算法
PyCaret 支持 6 个模块，有监督和无监督模型的训练和部署，分别有分类、回归、聚类、异常检测、自然语言处理和关联规则挖掘。





PyCaret 安装
pip install pycaret
老样子，命令行 pip install 皆可安装。

为了防止安装的这些依赖可能与之前你已安装过的发生冲突，建议可以创建个 Python 的虚拟环境安装 PyCaret 以减少不必要的麻烦，比如用 python3 virtualenv 或者 conda。就拿 conda 为例吧。

#创建一个新的虚拟环境
conda create --name yourenvname python=3.7
#激活
conda activate yourenvname
#安装
pip install pycaret
如果不好使也可以尝试从源安装。

pip install C:/path_to_download/pycaret-version.tar.gz


PyCaret 如何使用？
像这种数据建模类的工作会涉及很多交互式的操作，所以东哥首推在 Jupyter notebook 中运行代码。

PyCaret 库的函数有五个大类，初始化、模型训练、模型集成、模型分析与模型部署，基本上覆盖了我们正常建模的顺序，只不过预处理都在初始化中完成了。

具体使用方法见后面实例。

初始化
PyCaret 初始化包括了两部分内容：

一、获取数据；二、建立环境。

1. 获取数据

PyCaret 自带了很多数据集，样本几万条的，特征几百个的，对于我们练习绝对是够用了。比如这样：

from pycaret.datasets import get_data
data = get_data('juice') 
2. 建立环境

这一步是必须的。

首先，我们要选择使用哪个模块，分类、回归、聚类 还是其他的。比如我们要用 classification 分类模型。

from pycaret.datasets import get_data
diabetes = get_data('diabetes')
# 初始化
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')
上面 setup 函数就建立了基础环境，其中参数约束了数据集和目标变量。



setup 参数除了上面这两个以外，还有 N 多个参数可以控制。所有预处理的步骤都会应用至 setup() 中，PyCaret 拥有 20 余项功能可运用于 ML 相关的数据准备，比如样本的划分、数据预处理，缺失值处理、独热编码、归一化、特征工程、特征选择等等。



比如要用归一化，那么令 normalize 为 Ture 就好了，其它的同理。

clf1 = setup(data = pokemon, target = 'Legendary', normalize = True)
如果还要用其他的，在 setup 里面加就好了，至于处理的顺序不用我们管，pipeline 已经自动搞定了。

另外，PyCaret 的一大优点是：Pipeline 可保存成二进制，轻松地在各环境之间相互迁移，比如大规模运行或是轻松部署到生产环境中。



模型训练
模型训练包括三个部分，模型比较，模型创建，模型调优。

1. 模型比较

这是模型训练的第一步。compare_models 函数会训练模型库中的所有模型，并使用 k 折交叉验证（默认 k=10）来比较常见的评估指标。所使用的评估指标如下所示：

分类模块：Accuracy, AUC, Recall, Precision, F1, Kappa
回归模块：MAE, MSE, RMSE, R2, RMSLE, MAPE
下面是模型比较函数的使用，只需要这么一行代码！

# 比较所有模型
compare_models()
来看一下结果，直接给出所有模型跑出的结果，直观地对比。



2. 模型创建

当我们比较了各模型的结果后，知道了哪个模型最适合，这时只要在创建函数 create_model 中传入一个模型参数就行，同样一行代码搞定。

# 创建逻辑回归模型
lr = create_model('lr')


PyCaret 有 60 多个开源即用型算法，每个模型都有对应的缩写（可以查表），比如上面逻辑回归直接写上 lr 就可以完成。

变量 lr 存储一个由 create_model 函数返回的训练模型对象，可以通过在变量后使用标点. 来访问训练对象的原始属性。

3. 模型调优

同样的，在模型调优 tune_model 函数中传入模型 lr 参数，PyCaret 将自动调优。

# 调节 LR 模型
tuned_lr = tune_model('lr')




模型集成
1. 集成模型

模型集成函数 ensemble_model 可以直接调用生成的模型对象，然后做集成处理。默认使用 Bagging 方法用于模型集成，用户也可函数中的 method 参数将其转换为 Boosting。

# 创建一个决策树模型
dt = create_model('dt')
dt_bagged = ensemble_model(dt)


除此外，PyCaret 还提供了 blend_models 和 stack_models 功能，来集成多个训练好的模型。

2. blend 模型

# blend_models 混合特殊的模型
blender = blend_models(estimator_list = [dt, catboost, lightgbm])
3. stack 模型

# 创建单个模型，用于stacking
ridge = create_model('ridge')
lda = create_model('lda')
gbc = create_model('gbc')
xgboost = create_model('xgboost')
# stacking 模型
stacker = stack_models(estimator_list = [ridge,lda,gbc], meta_model = xgboost)


模型分析
模型分析主要可以做两个事情：

一、模型绘制；二、模型解释。

1. 模型绘制

我们需要分析什么模型指标，只要传入函数中即可，比如对 adaboost 模型分析 AUC 指标。

# 创建逻辑回归模型
adaboost = create_model('adaboost') 
plot_model(adaboost, plot = 'auc') # AUC plot
plot_model(adaboost, plot = 'boundary') # Decision Boundary
plot_model(adaboost, plot = 'pr') # Precision Recall Curve
plot_model(adaboost, plot = 'vc') # Validation Curve


如果你不想单独绘制所有这些可视化，那么 PyCaret 库有另一个惊人的功能 evaluate_model。在此功能中，只需要传递模型对象，PyCaret 将创建一个交互式窗口，供你・以所有可能的方式查看和分析模型：



2. 模型解释

在大多数机器学习项目中，解释复杂模型非常重要。通过分析模型认为重要的内容，有助于模型调优。在 PyCaret 中，此步骤非常简单，只需编写 interpret_model 即可获取 Shapley 值。

# 创建一个模型
xgboost = create_model('xgboost')
interpret_model(xgboost) # summary plot
interpret_model(xgboost, plot = 'correlation') # correlation plot


测试数据集上特定数据点的解释可以通过 reason 图来评估。如下图所示：在测试数据集上检查首个实例。

interpret_model(xgboost, plot = 'reason', observation = 0)




模型部署
模型调优后要将模型在测试集上进行测试，使用 predict_model 函数。

1. 模型预测

# 创建模型
rf = create_model('rf') # 预测测试集
rf_holdout_pred = predict_model(rf)
以上是对模型测试集进行的预测，如果对于未见过的新数据预测，PyCaret 提供一个迭代的预测结果，在 predict_model 函数指定 data，像下面这样。



2. 模型完成

最后确认模型 finalize_model 才能进行部署。

# finalize a model
final_rf = finalize_model(rf)
3. 模型部署

该功能将 pipeline 和经过训练的模型保存为最终用户应用程序可以作为二进制 pickle 文件使用。或者，可以使用 PyCaret 将模型部署在云上。在云上部署模型就像编写 deploy_model 一样简单。

比如对于 AWS 用户来说，在将模型部署到 AWS S3（'aws'）之前，必须使用命令行界面配置环境变量。要配置 AWS 环境变量，请在 python 命令行中输入 aws configure。需要以下信息，可以使用亚马逊控制台帐户的身份和访问管理（IAM）门户生成。

AWS 访问密钥 ID
AWS 访问密钥
默认区域名称（可以在您的 AWS 控制台的 “全局设置” 下看到）
默认输出格式（必须留空）
# 创建模型
lr = create_model('lr')
# 最终确定模型
final_lr = finalize_model(lr)
# 部署模型
deploy_model(final_lr, model_name = 'lr_aws', platform = 'aws', authentication = { 'bucket'  : 'pycaret-test' })
用户也能够以二进制文件的格式保存整个实验，包括所有中间输出。

# 创建模型
adaboost = create_model('ada') 
# 二进制保存模型
save_model(adaboost, model_name = 'ada_for_deployment') 
以上就是 PyCaret 的介绍和使用方法，具体教程也可以参考：

https://pycaret.org/guide/
https://mp.weixin.qq.com/s/5DMJn85ME8LqUCewc5OWBg
如果文章对你有帮助，别忘记点赞、评论、Get！

—————————————————————

公众号：Python 数据科学

以 Python 为核心语言，分享大量数据挖掘实战项目分析和讲解，以及海量的学习资源。欢迎关注！

工具使用PyCaret
2021.02.25
相关文章
必知必会的 8 个 Python 列表技巧
实用干货Python数据结构


朱卫军·专栏作者
573 阅读 · 0 评论
Python 新手应该避免哪些坑
新手必看数据结构实用干货


朱卫军·专栏作者
这个 Pandas 函数可以自动爬取 Web 图表
Python爬虫实用干货


朱卫军·专栏作者
我来说几句...
x1.00
