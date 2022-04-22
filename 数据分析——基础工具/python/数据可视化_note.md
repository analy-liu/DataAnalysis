
# python中数据可视化

## 基础：matplotlib

### 导入包


```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

### 画图框架（Figure、Axes)

框架图：
![](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/fig_map.webp)

axes里的元素：
![](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/anatomy.webp)


```python
# 准备数据
x = np.arange(1,11)
y = np.random.randn(10)
z = np.random.rand(10)
```

**框架理解**


```python
# Figure,是一张白纸
fig = plt.figure()# 定义一张白纸
# fig.xxx都是对这个张白纸的操作

# 区域1
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8 # 距离左边框0.1，底边框0.1，宽度0.8，长度0.8
ax1 = fig.add_axes([left, bottom, width, height])# add_axes为自定义划分
ax1.plot(x, y, 'r')
ax1.set_title('area1')

# 区域2，和画画一样，后画的会在先画的前面
ax2 = fig.add_subplot(221)  # add_subplot为网格划分区域，画布分为[2,2]的网格，取[1,1]
ax2.scatter(x,y)
ax2.set_title('area2')

# 区域3
ax3 = fig.add_subplot(224)  # add_subplot为网格划分区域，画布分为[2,2]的网格，取[2,2]
ax3.hist(z)
ax3.set_title('area3')

#展示
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_9_0.png)


**Axes里详细参数设置**


```python
fig = plt.figure()
ax = fig.add_subplot(111)# 使用整张纸
ax.scatter(x, y, color = 'r', label = "1")# 画散点图
ax.plot(x, z, color = 'b', label = "2")# 画折线图
# 标题、坐标轴标题、图例等文字设定
ax.set_title('Title',fontsize=18)
ax.set_xlabel('xlabel', fontsize=15)
ax.set_ylabel('ylabel', fontsize=15)
ax.legend()

# xy坐标轴的一些属性设定
ax.set_aspect('equal') 
# ax.minorticks_on() # 添加网格
ax.set_xlim(0,11) 
ax.grid(which='minor', axis='both')
# 坐标轴tick设定
ax.xaxis.set_tick_params(labelsize=10,colors='b')
ax.yaxis.set_tick_params(labelsize=10,colors='r') 
start, end = ax.get_xlim() 
ax.xaxis.set_ticks(np.arange(start, end,1)) 
ax.yaxis.tick_right()
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_11_0.png)


### 通用参数

#### 基础设置


```python
plt.rc("font", family="SimHei")# #显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
```

#### 颜色：color

color参数：  
k：Black黑色；w：white白色  
r：red红色；m：magenta紫红色；pink：粉色；  
b：blue蓝色；c：cyan青色  
g：green绿色；lightgreen：亮绿  
y：yellow黄色；orange：橘色；gold：金黄  

其他颜色：https://blog.csdn.net/weixin_44726682/article/details/104836920


```python
y = np.random.rand(5)*10
plt.bar(range(len(y)), y, color = ['c','g','r','m','pink'])
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_17_0.png)


#### 线line与标记marker的类型

|线的标记|	描述|
|--|--|
|'.'	|点标记|
|','	|像素标记|
|'o'	|圆圈标记|
|'s'	|方形标记|
|'p'	|五角大楼标记|
|'*'	|星形标记|
|'+'	|加号标记|
|'x'	|x 标记|
|'D'	|钻石标记|
|线的类型|	描述|
|'-'	|实线样式|
|'--'|虚线样式|
|'-.'|破折号-点线样式|
|':'	|虚线样式|

#### 横纵坐标标签xlabel,ylabel

**函数**：  
plt.xlabel(xlabel, rotation, horizontalalignment, verticalalignment)  
plt.ylabel同  
**参数**：  
xlabel：设置标签内容  
rotation：设置标签的旋转度(逆时针)  
horizontalalignment：水平对齐（分为center、right和left）  
verticalalignment：垂直对齐（分为center、top和bottom）  


```python
y = np.random.normal(10,1,1000)# 生成1000个均值为10方差为1的正态分布样本
plt.hist(y, bins=20)
plt.xlabel('->', rotation=90)
plt.ylabel("y轴", rotation=0)
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_22_0.png)


#### 图例legend与标题title

首先需要在设置图的参数时设置label参数，然后在show之前设置plt.legend()  
如果需要将图例显示在图外，则需设置legend参数：plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)

**函数**：  
plt.legend(loc,fontsize,frameon,ncol,title,shadow,markerfirst,markerscale,
numpoints,fancybox,framealpha,borderpad,labelspacing,handlelength,bbox_to_anchor,)  
**参数**：  
Loc：	图例位置  
bbox_to_anchor：	如果要自定义图例位置需要设置该参数。  
Fontsize：	设置字体大小。  
Frameon：	是否显示图例边框。  
title：	为图例添加标题。  
Shadow：	是否为图例边框添加阴影。  
Fancybox：	是否将图例框的边角设为圆形。  
Framealpha：	控制图例框的透明度。  
Labelspacing：	图例中条目之间的距离。  
Handlelength：	图例句柄的长度。  
Borderpad：	图例框内边距。  
Ncol：	图例的列的数量，默认为1。  
Markerfirst：	True表示图例标签在句柄右侧，False反之。  
Markerscale：	图例标记为原图标记中的多少倍大小。  
Numpoints：	表示图例中的句柄上的标记点的个数，一般设为1。  


```python
data1 = np.random.rand(100,100)
data2 = np.random.rand(100,100)
p2 = plt.scatter(data1[0],data1[1],label='0',marker = 'o',s =30)
p1 = plt.scatter(data2[0],data2[1],label='1',marker = '.',s =30)
plt.legend(loc=0, bbox_to_anchor=(1.01,1.0),borderaxespad = 0.1,
          title="title") # 显示图例，并让图例显示在图外
plt.title('scatter')# 设置标题
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_26_0.png)


### plt 快速绘图

基本图标函数:

|函数|描述|
|--|--|
|plt.plot()|绘制折线图|
|plt.boxplot()|绘制箱形图|
|plt.bar()|绘制条形图|
|plt.barh()|绘制横向条形图|
|plt.polar()|绘制极坐标图|
|plt.pie()|绘制饼图|
|plt.psd()|绘制功率谱密度图|
|plt.specgram()|绘制谱图|
|plt.cohere()|绘制相关性函数|
|plt.scatter()|绘制散点图|
|plt.hist()|绘制直方图|
|plt.stem()|绘制柴火图|
|plt.plot_date()|绘制数据日期|

#### 柱状图：plt.bar()

1. 柱状图(bar chart)X轴为分类数据
2. 柱状图比较数据的大小，柱状图是一个二维图表，只能有一个变量需要比较，利用柱子的高度反映数值的差异
3. 柱状图柱子有间隔
4. 柱状图适用于小数据集分析
5. 柱形图横过来，就变成了条形图

**函数**：  


```python
plt.bar(position, data, width = 0.8, bottom = 0, 
color = 'b',alpha = 1, linewidth = 0, edgecolor = 'b',
tick_label = None) 
```

**参数**：  
position：柱子中心位置  
data：数据  
width：条形宽度0至1，默认0.8  
bottom：y轴起始坐标，默认0  
alpha：透明度0至1，默认1  
linewidth：边框宽度，默认0  
edgecolor：边框颜色，默认"b"  
tick_label：设置x轴文字  
height；条形高度    
align：条形的中心位置  
orientation：竖直："vertical"，水平条："horizontal"  


```python
y_1 = np.random.rand(5)*10
plt.bar(range(2017,2017+len(y_1)), y_1, 
        color = 'c', bottom = 2, alpha = 0.7, linewidth = 1, edgecolor = 'k', width=0.5, label = 'y_1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('常规柱状图')
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) # 显示图例，并让图例显示在图外
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_34_0.png)



```python
y_1 = np.random.rand(5)*10
y_2 = np.random.rand(5)*10
plt.bar(range(2017,2017+len(y_1)), y_1, 
        color = 'c', width=0.5, label = 'y_1')
plt.bar(range(2017,2017+len(y_2)), y_2, 
        color = 'gold', bottom = y_1, width=0.5, label = 'y_2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('堆叠柱状图')
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) # 显示图例，并让图例显示在图外
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_35_0.png)



```python
position = np.array([1,5,6,7,8])
y_1 = np.random.rand(5)*10
y_2 = np.random.rand(5)*10
plt.bar(position-0.2, y_1, 
        color = 'c', width=0.4, label = 'y_1', tick_label = [2017,2018,2019,2020,2021])
plt.bar(position+0.2, y_2, 
        color = 'gold', width=0.4, label = 'y_2', tick_label = [2017,2018,2019,2020,2021])
plt.xlabel('x')
plt.ylabel('y')
plt.title('并列柱状图')
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) # 显示图例，并让图例显示在图外
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_36_0.png)


#### 直方图：plt.hist()

1. 直方图(histogram)展示数据的分布
2. 直方图X轴为定量数据
3. 直方图柱子无间隔
4. 柱子的宽度代表了区间的长度

**函数**：


```python
plt.hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, 
         histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, 
         label=None, stacked=False, normed=None, hold=None, data=None, **kwargs)
```

**参数**：  
x：指定要绘制直方图的数据。  
bins：指定直方图条形的个数。  
range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值。  
density：若为True，返回元组的第一个元素将是归一化的计数，以形成概率密度。  
weights：该参数可以为每一个数据点设置权重。  
cumulative：是否需要计算累计频数或频率。  
bottom：可以为直方图的每个条形添加基准线，默认为0。  
histtype：指定直方图的类型，默认为bar，还有’barstacked’、‘step’等。  
align：设置条形边界值的对其方式，默认为mid，还有’left’和’right’。  
orientation：设置直方图的摆放方向，水平方向'horizontal'，默认为'vertical'垂直方向，。  
rwidth：设置直方图条形宽度的百分比。  
log：是否需要对绘图数据进行对数变换。  
color：设置直方图的填充色。  
label：设置直方图的标签，可以通过legend展示其图例。  
stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放。  


```python
y = np.random.normal(10,1,1000)# 生成1000个均值为10方差为1的正态分布样本
plt.hist(y, bins=20, density = True)
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_42_0.png)


#### 条形图：plt.barh()

条形图可以看作是柱形图逆时针旋转90°后形成的图表  
与柱形图相比，条形图更适合于展现排名

**函数**：


```python
plt.barh(position, data,height,width=0.8,bottom=None,*,align='center',data=None, **kwargs)
```

**参数**：  
position：柱子中心位置  
data：数据  
width：条形宽度0至1，默认0.8  
bottom：y轴起始坐标，默认0  
alpha：透明度0至1，默认1  
linewidth：边框宽度，默认0  
edgecolor：边框颜色，默认"b"  
tick_label：设置x轴文字  
height；条形高度    
align：条形的中心位置  
orientation：竖直："vertical"，水平条："horizontal"  
log：	y轴使用科学计算法表示。 


```python
data = np.random.rand(5)
plt.barh(range(len(data)),data)
plt.title("条形图")
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_48_0.png)



```python
data = np.random.rand(5)
plt.barh(range(len(data)),data)
plt.barh(range(len(data)),-data/2)
plt.title("正负条形图")
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_49_0.png)


#### 折线图：plt.plot()

1. 折线图通常用于查看随着时间推移某个事物的值的**变化趋势**
2. 适用于连续数据
3. 折线图可以与其他图形结合使用（与柱状图结合、与面积图结合等）

**函数**：


```python
plt.plot([x], y, [fmt], data=None, **kwargs)
```

**参数**：  
x,y：	设置数据点的水平或垂直坐标。  
Fmt：	用一个字符串来定义图的基本属性如颜色，点型，线型。  
Data：	带有标签的绘图数据。  


```python
data = [range(1,11),[2,4,5,4,7,8,5,3,5,8]]
plt.plot(data[0],data[1], color = 'r',marker = 'o')
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_55_0.png)


#### 饼图：plt.pie()

饼图(pie)用于反映某个部分占整体比重多少  
缺点：
1. 只能反映一个系列
2. 数值不能有负数
3. 类别不易过大，否则不好看

**函数**：


```python
plt.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, 
    shadow=False, labeldistance=1.1, startangle=None, radius=None, 
    counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, 
    rotatelabels=False, *, data=None)
```

**参数**：  
x:	每一块的比例，如果sum(x) > 1则会进行归一化处理。  

labels:	每一块饼图外侧显示的说明文字。  
labeldistance:	label标记的绘制位置，相对于半径的比例，默认值为1.1， 如<1则绘制在饼图内侧。  
rotatelabels:	布尔类型，可选，默认为False。如果为True，旋转每个label到指定的角度。  

autopct:	控制饼图内百分比设置，'%.1f%%'表示小数点后一位  
pctdistance:	类似于labeldistance，指定autopct的位置刻度，默认值为0.6。  

startangle:	起始绘制角度，默认图是从x轴正方向逆时针画起，如设定=90则从y轴正方向画起。  
counterclock:	指定指针方向，可选，默认为True，即逆时针。  
center:	浮点类型的列表，可选，默认值(0，0)。图标中心位置。  
explode:	每一块离开中心的距离。  
shadow:	在饼图下面画一个阴影。默认为False，即不画阴影。  

wedgeprops:	字典类型，可选，默认值None。参数字典传递给wedge对象用来画饼图。  
textprops:	设置标签和比例文字的格式，字典类型，可选，默认值为None。  
frame:	布尔类型，可选，默认为False。如果是True，绘制带有表的轴框架。  


```python
# x = np.random.rand(5)
label = ["一",'二','三','四','五']
plt.axes(aspect='equal')# 使饼图变圆
plt.pie(x, 
        labels = label, # 设置标签
        labeldistance = 1.2, # 设置label位置
        autopct='%.1f%%',  #饼图中添加数值标签
        explode=[0.1,0.1,0.1,0.1,0.1],#每一块离开中心的距离
        radius=1, # 设置饼图的半径
        startangle=90, # 设置饼图的初始角度
        counterclock=False,  # 将饼图的顺序设置为顺时针方向
       )
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_61_0.png)


#### 散点图：plt.scatter()

散点图(scatter)可以用于观察数据的分布情况，判断变量间关系，寻找离群点

**函数**：


```python
scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, 
        vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, 
        data=None, **kwargs)
```

**参数**：  
x,y：	绘图的数据，都是向量且必须长度相等。  
S：	设置标记大小。  
C：	设置标记颜色。  
marker：	设置标记样式。  
cmap：	设置色彩盘。  
norm：	设置亮度，为0到1之间。  
vmin，vmax：	设置亮度，如果norm已设置，该参数无效。  
alpha：	设置透明度，为0到1之间。  
linewidths：	设置线条的宽度。  
edgecolors：	设置轮廓颜色。  


```python
data1 = np.random.rand(100,100)
data2 = np.random.rand(100,100)
p2 = plt.scatter(data1[0],data1[1],label='0',marker = 'o',s =20, c='gold')
p1 = plt.scatter(data2[0],data2[1],label='1',marker = '.',s =30, c='c')
plt.legend(loc=0, bbox_to_anchor=(1.01,1.0),borderaxespad = 0.1,
          title="title") # 显示图例，并让图例显示在图外
plt.title('scatter')# 设置标题
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_67_0.png)


#### 箱型图：plt.boxplot()

箱型图优点：
1. 直观明了地识别数据批中的异常值
2. 利用箱线图判断数据批的偏态和尾重

缺点：
1. 不能精确地衡量数据分布的偏态和尾重程度
2. 对于批量比较大的数据，反映的信息更加模糊以及用中位数代表总体评价水平有一定的局限性

**函数**：


```python
plt.boxplot(x,notch=None,sym=None,vert=None,whis=None,positions=None,widths=None,
            patch_artist=None,meanline=None,showmeans=None,showcaps=None,showbox=None,
            showfliers=None,boxprops=None,labels=None,flierprops=Non，medianprops=None,
            meanprops=None, capprops=None,whiskerprops=None)
```

**参数**：  
X：	指定要绘制箱线图的数据。  
labels：	为箱线图添加标签，类似于图例的作用。  

sym：	指定异常点的形状，默认为+号显示。  
whis：	指定上下须与上下四分位的距离，默认为1.5倍的四分位差。  
positions：	指定箱线图的位置，默认为[0，1，2…]。  
widths：	指定箱线图的宽度，默认为0.5。  

输入dict  
boxprops：	设置箱体的属性，如边框色，填充色等。  
filerprops：	**设置异常值的属性**，如异常点的形状、大小、填充色等。  
medianprops：	**设置中位数的属性**，如线的类型、粗细等。  
meanprops：	**设置均值的属性**，如点的大小、颜色等。  
capprops：	设置箱线图顶端和末端线条的属性，如颜色、粗细等。  
whiskerprops：	设置须的属性，如颜色、粗细、线的类型等。  
notch：	是否是凹口的形式展现箱线图，默认非凹口。  

输入bool  
vert：	是否需要将箱线图垂直摆放，默认垂直摆放。  
patch_artist：	是否填充箱体的颜色。  
meanlin：e	是否用线的形式表示均值，默认用点来表示。  
showmeans：	**是否显示均值**，默认不显示。  
showcaps：	是否显示箱线图顶端和末端的两条线，默认显示。  
showbox：	是否显示箱线图的箱体，默认显示。  
showfliers：	是否显示异常值，默认显示。  

![title](箱型图图解.png)


```python
data = np.random.randn(3, 100)
plt.boxplot([data[0],data[1],data[2]], 
            labels = ['一','二','三'], 
            showmeans=True, meanprops = {'marker':'o'})
plt.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_74_0.png)


#### 雷达图

用于显示独立数据系列之间以及某个特定系列与其他系列的整体关系。每个分类都拥有自己的数值坐标轴，这些坐标轴同心点向外辐射，并由折线将同系列中值连接起来。  
雷达图适用于多维数据（四维以上）且每个维度必须可以排序


```python
class radarplot(object):
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, polar=True)
        self.ax.grid(True)# 添加网格线
        self.plot_num = 0
    def plot(self, data, feature = range(len(data)), label = None):
        N = len(data)
        angles = np.linspace(0, 2*np.pi, N, endpoint=False)
        # 首尾相连
        data = np.concatenate((data,[data[0]]))
        angles=np.concatenate((angles,[angles[0]]))
        
        # 添加雷达
        self.plot_num +=1
        if not label:
            label = self.plot_num
        self.ax.plot(angles, data, 'o-', linewidth=2, label = label)
        self.ax.fill(angles, data, alpha=0.25)#填充颜色
        self.ax.set_thetagrids(angles * 180/np.pi, feature)# 添加每个特征的标签
        self.ax.set_ylim(0,5)# 设置雷达图的范围
        plt.legend(loc=0, bbox_to_anchor=(1.01,1.0),borderaxespad = 0.1)# 设置图例
    def show(self):
        plt.show()
```


```python
values = [3.2,2.1,3.5,2.8,3]
values2 = [4,4.1,4.5,4,4.1]
feature = ['个人能力','QC知识','解决问题能力','服务质量意识','团队精神']
```


```python
radar = radarplot()
radar.plot(values,feature = feature, label="学习前")
radar.plot(values2,feature = feature, label="学习后")
radar.show()
```


![png](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/output_79_0.png)


## 交互：Pyecharts

### 导入包
