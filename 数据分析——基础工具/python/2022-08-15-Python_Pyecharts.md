---
title:  python-数据可视化-Pyecharts
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# 1. Pyecharts图表

- [1. Pyecharts图表](#1-pyecharts图表)
  - [1.1 直角坐标系](#11-直角坐标系)
    - [1.1.1 直方图](#111-直方图)
    - [1.1.2 折线图](#112-折线图)
    - [1.1.3 散点图](#113-散点图)
    - [1.1.4 箱线图](#114-箱线图)
    - [1.1.5 K线图](#115-k线图)
  - [1.2 非直角坐标系基本图表](#12-非直角坐标系基本图表)
    - [1.2.1 饼图](#121-饼图)
    - [1.2.2 雷达图](#122-雷达图)
    - [1.2.3 词云图](#123-词云图)
    - [1.2.4 仪表盘](#124-仪表盘)
  - [1.3 地图](#13-地图)
  - [1.4 3D图表](#14-3d图表)
- [2. 组合图](#2-组合图)
- [3. Pyecharts配置项](#3-pyecharts配置项)
  - [简易使用流程](#简易使用流程)
  - [<a href="#pre_init">初始化配置</a><a id="init"></a>](#初始化配置)
  - [<a href="#set_data">设置数据</a><a id="setdata"></a>](#设置数据)
  - [<a href="#pre_global_opts">全局配置global_opts</a><a id="global_opts"></a>](#全局配置global_opts)
    - [标题配置](#标题配置)
    - [图例配置](#图例配置)
    - [提示框配置](#提示框配置)
    - [坐标轴配置](#坐标轴配置)
    - [视觉映射配置](#视觉映射配置)
    - [区域缩放](#区域缩放)
  - [<a href="#pre_series_opts">局部系列配置</a><a id="series_opts"></a>](#局部系列配置)
    - [文本样式配置](#文本样式配置)
    - [分割线配置](#分割线配置)
    - [分隔区域配置](#分隔区域配置)
    - [线样式配置](#线样式配置)
    - [涟漪效果配置](#涟漪效果配置)
    - [图元配置](#图元配置)
    - [标签配置项](#标签配置项)
    - [标记点配置](#标记点配置)
    - [标记线配置](#标记线配置)
    - [标记区域配置](#标记区域配置)
  - [部分配置通用参数详解](#部分配置通用参数详解)
    - [color](#color)
    - [formatter](#formatter)

## 1.1 直角坐标系

### 1.1.1 直方图

### 1.1.2 折线图

### 1.1.3 散点图

### 1.1.4 箱线图

### 1.1.5 K线图

## 1.2 非直角坐标系基本图表

### 1.2.1 饼图

### 1.2.2 雷达图

### 1.2.3 词云图

### 1.2.4 仪表盘

## 1.3 地图

## 1.4 3D图表

# 2. 组合图

# 3. Pyecharts配置项

Pyecharts的配置项按模块分为初始配置、全局配置、系列配置三块  
系列配置分为整体配置和局部配置  

新配置会覆盖旧配置  
例如新全局配置只包含标题项，旧全局配置包含图例 区域缩放  
设置新全局配置后，图例 区域缩放的配置会失效

## 简易使用流程

本节展示简易使用流程，方便对整体先有个概念  
详细参数配置见详细参数  

**初始设置**<a id="pre_init"></a>

```python
# 虚假数据
x_data = ['抖音', '微博', '今日头条', '微信朋友圈', '知乎', 'B站'] # 广告商
y_data_1 = [130, 120, 150, 200, 90, 70] # 成本
y_data_2 = [200, 240, 300, 450, 600, 120] # 收益

# 设置初始配置
ax1 = Eplot.Bar(
    init_opts=opts.InitOpts(width='900px',height='500px')
)
```

<a href="#init">详细参数</a>

**系列配置方法一：局部配置**<a id="pre_series_opts_one"></a>

```python
# 系列配置方法一：局部配置
## 文本样式配置
title_TextStyle = opts.TextStyleOpts(color='red')
## 分割线配置
SplitLine = opts.SplitLineOpts(is_show=True)
## 分隔区域配置
### 区域填充样式配置
AreaStyle = opts.AreaStyleOpts(opacity=0.6)
SplitArea = opts.SplitAreaOpts(
    is_show=True,
    areastyle_opts=AreaStyle)
## 特定图表样式配置
### 线样式配置-折线图
LineStyle = opts.LineStyleOpts(width=5) # linestyle_opts=LineStyle
### 涟漪效果配置-涟漪散点图
Effect = opts.EffectOpts(scale=10, period=5) # effect_opts=Effect
```

<a href="#series_opts">详细参数</a>

**设置数据**<a id="set_data"></a>

```python
# 设置数据
ax1.add_xaxis(x_data)
ax1.add_yaxis('成本', y_data_1)
ax1.add_yaxis('收益', y_data_2)
```

<a href="#setdata">详细参数</a>

**全局配置**<a id="pre_global_opts"></a>

```python
# 全局配置
ax1.set_global_opts(
    # 标题配置
    title_opts=opts.TitleOpts(
        title="主标题", subtitle='副标题',
        title_textstyle_opts=title_TextStyle # 系列局部配置-文本样式
        ),
    # 图例配置
    legend_opts=opts.LegendOpts(is_show=True),
    # 设置默认的工具箱 
    toolbox_opts= opts.ToolboxOpts(), 
    # 提示框配置
    tooltip_opts=opts.TooltipOpts(
        is_show=True,
        axis_pointer_type = 'cross', # 十字准星
        trigger_on="mousemove|click"# 鼠标移动或者点击时触发
        ),
    # 坐标轴配置
    yaxis_opts=opts.AxisOpts(
        name='广告商',
        splitline_opts=SplitLine, # 系列局部配置-分割线配置
        splitarea_opts=SplitArea # 系列局部配置-分隔区域配置
        ),
    xaxis_opts=opts.AxisOpts(name='元'),
    # 视觉映射配置
    visualmap_opts=opts.VisualMapOpts(is_show=False),
    # 区域缩放配置
    datazoom_opts=[
        opts.DataZoomOpts(orient="vertical",range_start=0,range_end=100),
        opts.DataZoomOpts(range_start=0,range_end=100)]
    )
```

<a href="#global_opts">详细参数</a>

**系列配置方法二：整体配置**<a id="pre_series_opts_all"></a>
对图表中包含的所有系列数据生效

```python
# 系列配置方法二：整体配置，对图表中包含的所有系列数据生效
# 只展示常用于系列整体配置的配置项
ax1.set_series_opts(
    # 图元样式配置项
    itemstyle_opts=opts.ItemStyleOpts(border_color='black'),
    # 标签配置项
    label_opts=opts.LabelOpts(is_show=False),# 显示关闭标签
    # 标记点配置
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="x轴最大",value_index=0)
        ]),
    # 标记线配置
    markline_opts=opts.MarkLineOpts(
        data=[
            opts.MarkLineItem(type_="min", name="最小值")
        ])
    # 标记区域配置
    markarea_opts=opts.MarkAreaOpts(
        data=[
            opts.MarkAreaItem(name="特别关注", x=("微信朋友圈", "今日头条")),
        ])
    )
```

<a href="#series_opts">详细参数</a>

**数据展示与保存**

```python
ax1.render_notebook()

from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot 

path = r'F:\data\pyecharts_html\{}.html'
make_snapshot(snapshot, ax1.render(), path)
```

## <a href="#pre_init">初始化配置</a><a id="init"></a>

**init_opts=opts.InitOpts**

```python
# 设置图表初始化属性
ax1 = Eplot.Bar(
    init_opts=opts.InitOpts(
        width='900px', # 图表画布宽度
        height='500px', # 图标画布长度
        chart_id = None, # 图表 ID，图表唯一标识，用于在多图表时区分
        renderer = 'canvas', # 渲染风格，可选 "canvas", "svg" 
        page_title = "Awesome-pyecharts", # 网页标题
        theme = "white", # 图表主题 white dark
        bg_color = None, # 图表背景颜色 可用颜色英文或者rgb(0,0,0)通道颜色配置
        js_host = "", # 远程 js host，如不设置默认为 https://assets.pyecharts.org/assets/
        # animation_opts = AnimationOpts() # 画图动画初始化配置，参考 `global_options.AnimationOpts
    )
) 
```

**主题选项**

|主题|底色|色调|
|:-|:-|:-|
|white|白底|红深蓝|
|infographic|白底|红蓝|
|roma|白底|深红蓝|
|vintage|白底|红灰|
|shine|白底|红黄|
|light|白底|金蓝|
|macarons|白底|亮紫蓝|
|walden|白底|浅蓝色系|
|westeros|白底|深蓝色系|
|wonderland|白底|蓝色系|
|essos|白底|红色系|
|romantic|粉底|粉色系|
|chalk|深底|粉绿|
|dark|深底|红蓝|
|purple-passion|深底|紫色系|

## <a href="#set_data">设置数据</a><a id="setdata"></a>

```python
# 通用参数
ax.add_yaxis(
    '', 
    data,
    label_opts=opts.LabelOpts() # 标签配置项目
    )

# 折线图参数
ax.add_yaxis(
    '', 
    data,
    is_smooth = False,# 是否平滑曲线
    is_connect_nones = False, # 是否连接空数据
    is_step = False, # 是否展示为阶梯图
    linestyle_opts=opts.LineStyleOpts()
    )
```

## <a href="#pre_global_opts">全局配置global_opts</a><a id="global_opts"></a>

### 标题配置

title_opts=opts.TitleOpts

```python
set_global_opts(
    title_opts=opts.TitleOpts(
        title=None,# 主标题文本，支持使用 \n 换行
        subtitle=None,# 副标题
        title_textstyle_opts = None, # 主标题字体样式配置项，参考局部系列配置-文字样式配置
        subtitle_textstyle_opts = None, # 副标题字体样式配置项
        pos_left = None,# title 组件离容器左侧的距离。  
        pos_right = None,# title 组件离容器右侧的距离。  
        pos_top = None,# title 组件离容器上侧的距离
        pos_bottom = None,# title 组件离容器下侧的距离。  
        padding = None,# 内边距[5,10,5,10]对应[上,右,下,左]
        item_gap = None,# 主副标题间距
        title_link = None, # 超链接
        subtitle_link = None,# 超链接
        title_target = None, # 跳转方式 'self' 当前窗口打开; 'blank' 新窗口打开
        subtitle_target = None
    ))
```

### 图例配置

legend_opts=opts.LegendOpts

```python
set_global_opts(
    legend_opts=opts.LegendOpts(
        is_show = True ,# 是否显示图例
        type_ = None ,# 图例类型 'plain' 默认图例类型 'scroll'可滚动翻页的图例
        selected_mode = None, # 图例选择模式 True 可选 'single' 单选 'multiple' 多选
        pos_right = None, # 图例组件离容器边侧侧的距离
        pos_bottom = None,# # 可以是 int str 例如 20 '20%'
        pos_left = None, # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐
        pos_top = None, # 'top', 'middle', 'bottom'
        orient = None, # 图例列表的布局朝向。可选：'horizontal', 'vertical'  
        align = None, # 图例标记和文本的对齐。默认`auto`, `left`, `right`
        padding = 5, # 图例内边距
        item_gap = 10, # 图例每项直接的间隔
        item_width = 25, # 图例标记的图形宽度
        item_height = 14, # 图例标记的图形高度
        inactive_color = None, # 图例关闭时的颜色。默认是 #ccc
        textstyle_opts = None, # 图例组件字体样式 参考局部系列配置-文字样式配置
        # 图例项的 icon
        # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'  
        # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。  
        # 可以通过 'path://' 将图标设置为任意的矢量路径。
        legend_icon = None 
        )
    )
```

### 提示框配置

```python
.set_global_opts(
    tooltip_opts=opts.TooltipOpts(
        is_show = True,  # 是否显示提示框组件
        trigger = "item",  # 触发类型 'item': 数据项图形触发 axis': 坐标轴触发 'none': 什么都不触发 
        trigger_on = "mousemove|click",  # str 提示框触发的条件 'mousemove' 'click' 'mousemove|click' 'none'
        axis_pointer_type = "line",  # str 指示器类型。可选'line' 'shadow' 'none' 'cross'
        formatter = None,  # str 标签内容格式器 见部分配置通用参数详解
        background_color = None,  # str 提示框浮层的背景颜色。
        border_color = None,  # str 提示框浮层的边框颜色。  
        border_width = 0,  # Numeric 提示框浮层的边框宽
        textstyle_opts = TextStyleOpts(font_size=14) # 文字样式配置项
        )
    )
```

### 坐标轴配置

```python
.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        type_ = None,  # str 坐标轴类型。可选 'value' 'category' 'time' 'log'
        name = None,  # str 坐标轴名称。
        is_show = True,  # bool 是否显示 x 轴。
        is_scale = False,  # bool 是否是脱离 0 值比例，只在数值轴中（type: 'value'）有效，设置 min 和 max 之后该配置项无效
        is_inverse = False,  # bool 是否反向坐标轴。
        name_location = "end",  # str 坐标轴名称显示位置。可选：'start', 'middle' 或者 'center','end'
        name_gap = 15,  # Numeric 坐标轴名称与轴线之间的距离
        name_rotate = None,  # Numeric 坐标轴名字旋转，角度值。
        interval = None,  # Numeric 强制设置坐标轴分割间隔 无法在类目轴中使用。在时间轴（type: 'time'）中需要传时间戳，在对数轴（type: 'log'）中需要传指数值
        grid_index = 0,  # Numeric x 轴所在的 grid 的索引，默认位于第一个 grid
        position = None,  # str x 轴的位置。可选：'top', 'bottom' 
        offset = 0,  # Numeric Y 轴相对于默认位置的偏移，在相同的 position 上有多个 Y 轴的时候有用。
        split_number = 5,  # Numeric 坐标轴的分割段数
        boundary_gap = None,  # Union[str, bool, None] 坐标轴两边留白策略,list写法['20%', '20%']
        min_ = None,  # Union[Numeric, str, None]，坐标轴刻度最小值，可选特殊值dataMin：取数据在该轴上的最小值
        max_ = None,  # Union[Numeric, str, None]，坐标轴刻度最大值，可选特殊值dataMax：取数据在该轴上的最大值
        min_interval = 0,  # Numeric 最小间隔大小，可以设置成1保证坐标轴分割刻度显示成整数
        max_interval = None,  # Numeric 坐标轴最大间隔大小，时间轴（（type: 'time'））可以设置成 3600 * 24 * 1000 保证坐标轴分割刻度最大为一天
        axisline_opts = None,  # Union[AxisLineOpts, dict, None] 坐标轴刻度线配置项
        axistick_opts = None,  # Union[AxisTickOpts, dict, None] 坐标轴刻度配置项
        axislabel_opts = None,  # Union[LabelOpts, dict, None] 坐标轴标签配置项
        axispointer_opts = None,  # Union[AxisPointerOpts, dict, None] 坐标轴指示器配置项
        name_textstyle_opts = None,  # Union[TextStyleOpts, dict, None] 坐标轴名称的文字样式
        splitarea_opts = None,  # Union[SplitAreaOpts, dict, None] 分割区域配置项
        splitline_opts = SplitLineOpts(),  # Union[SplitLineOpts, dict] 分割线配置项
        )
    )
```

部分参数详解

type_

    # 坐标轴类型。可选：  
    # 'value': 数值轴，适用于连续数据。  
    # 'category': 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。  
    # 'time': 时间轴，适用于连续的时序数据，与数值轴相比时间轴带有时间的格式化，在刻度计算上也有所不同，  
    # 例如会根据跨度的范围来决定使用月，星期，日还是小时范围的刻度。  
    # 'log' 对数轴。适用于对数数据。  

### 视觉映射配置

```python
.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        is_show=False, # 是否显示视觉映射配置
        type_ = "color"
    )
)
class VisualMapOpts(  
    # 是否显示视觉映射配置  
    is_show: bool = True,  

    # 映射过渡类型，可选，"color", "size"  
    type_: str = "color",  

    # 指定 visualMapPiecewise 组件的最小值。  
    min_: Union[int, float] = 0,  

    # 指定 visualMapPiecewise 组件的最大值。  
    max_: Union[int, float] = 100,  

    # 两端的文本，如['High', 'Low']。  
    range_text: Union[list, tuple] = None,  

    # visualMap 组件过渡颜色  
    range_color: Union[Sequence[str]] = None,  

    # visualMap 组件过渡 symbol 大小  
    range_size: Union[Sequence[int]] = None,  

    # visualMap 图元以及其附属物（如文字标签）的透明度。  
    range_opacity: Optional[Numeric] = None,  

    # 如何放置 visualMap 组件，水平（'horizontal'）或者竖直（'vertical'）。  
    orient: str = "vertical",  

    # visualMap 组件离容器左侧的距离。  
    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
    # 也可以是 'left', 'center', 'right'。  
    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。  
    pos_left: Optional[str] = None,  

    # visualMap 组件离容器右侧的距离。  
    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
    pos_right: Optional[str] = None,  

    # visualMap 组件离容器上侧的距离。  
    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
    # 也可以是 'top', 'middle', 'bottom'。  
    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。  
    pos_top: Optional[str] = None,  

    # visualMap 组件离容器下侧的距离。  
    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
    pos_bottom: Optional[str] = None,  

    # 对于连续型数据，自动平均切分成几段。默认为5段。连续数据的范围需要 max 和 min 来指定  
    split_number: int = 5,  

    # 指定取哪个系列的数据，默认取所有系列。  
    series_index: Union[Numeric, Sequence, None] = None,  

    # 组件映射维度  
    dimension: Optional[Numeric] = None,  

    # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。  
    is_calculable: bool = True,  

    # 是否为分段型  
    is_piecewise: bool = False,  

    # 是否反转 visualMap 组件  
    is_inverse: bool = False,  

    # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：  
    # pieces: [  
    #   {"min": 1500}, // 不指定 max，表示 max 为无限大（Infinity）。  
    #   {"min": 900, "max": 1500},  
    #   {"min": 310, "max": 1000},  
    #   {"min": 200, "max": 300},  
    #   {"min": 10, "max": 200, "label": '10 到 200（自定义label）'},  
    #   {"value": 123, "label": '123（自定义特殊颜色）', "color": 'grey'}, //表示 value 等于 123 的情况  
    #   {"max": 5}     // 不指定 min，表示 min 为无限大（-Infinity）。  
    # ]  
    pieces: Optional[Sequence] = None,  

    # 定义 在选中范围外 的视觉元素。（用户可以和 visualMap 组件交互，用鼠标或触摸选择范围）  
    #  可选的视觉元素有：  
    #  symbol: 图元的图形类别。  
    #  symbolSize: 图元的大小。  
    #  color: 图元的颜色。  
    #  colorAlpha: 图元的颜色的透明度。  
    #  opacity: 图元以及其附属物（如文字标签）的透明度。  
    #  colorLightness: 颜色的明暗度，参见 HSL。  
    #  colorSaturation: 颜色的饱和度，参见 HSL。  
    #  colorHue: 颜色的色调，参见 HSL。  
    out_of_range: Optional[Sequence] = None,  

    # 图形的宽度，即长条的宽度。  
    item_width: int = 0,  

    # 图形的高度，即长条的高度。  
    item_height: int = 0,  

    # visualMap 组件的背景色。  
    background_color: Optional[str] = None,  

    # visualMap 组件的边框颜色。  
    border_color: Optional[str] = None,  

    # visualMap 边框线宽，单位px。  
    border_width: int = 0,  

    # 文字样式配置项，参考 `series_options.TextStyleOpts`  
    textstyle_opts: Union[TextStyleOpts, dict, None] = None,  
)
```

### 区域缩放

```python

```

## <a href="#pre_series_opts">局部系列配置</a><a id="series_opts"></a>

<a href="#pre_series_opts_one">系列配置方法一预览：局部配置</a>
<a href="#pre_series_opts_all">系列配置方法一预览：全局配置</a>


### 文本样式配置

```python
opts.TextStyleOpts(
    color=None,# 文字颜色
    font_style=None,# 文字风格 可选：'normal'，'italic'，'oblique'  
    font_weight=None,# 文字粗细
    font_family=None,# 文字系列 'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei'
    font_size=None,# 文字大小 
    align=None,# 文字水平对齐方式，默认自动
    vertical_align=None,# 文字垂直对齐方式，默认自动
    line_height=None,# 行高
    background_color=None,# 文字块背景颜色
    border_color=None,# 文字块边框颜色
    border_width=None,# 文字块边框宽度
    border_radius=None,# 文字块的圆角 Numeric Sequence
    padding=None,# 文字块内边距 [3, 4, 5, 6]：表示 [上, 右, 下, 左] 
    shadow_color=None,# 文字块背景阴影颜色
    shadow_blur=None,# 文字块背景阴影长度
    width=None,# 文字块的宽度
    height=None,# 文字块的高低
    rich=None# 富文本
),
```

### 分割线配置



在set_global_opts中的xaxis_opts或yaxis_opts  
配置opts.AxisOpts里的  
splitline_opts=opts.SplitLineOpts

```python
.set_global_opts(
    # 显示X轴分割线
    xaxis_opts=opts.AxisOpts(
        splitline_opts=opts.SplitLineOpts(
            is_show=True, # 是否显示
            linestyle_opts = LineStyleOpts() # 见线样式配置
            )
        )
    )
```

### 分隔区域配置

在set_global_opts中的xaxis_opts或yaxis_opts  
配置opts.AxisOpts里的  
splitarea_opts=opts.SplitAreaOpts

```python
.set_global_opts(
    # 显示Y轴分割区域
    yaxis_opts=opts.AxisOpts(
        splitarea_opts=opts.SplitAreaOpts(
            is_show=True, # 是否显示
            areastyle_opts=opts.AreaStyleOpts( # 分隔区域的样式配置项
                opacity=1,# 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
                color = None # 填充的颜色 见部分配置通用参数详解
                )
            )
        )
    )

```

### 线样式配置

```python
line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', 
        y_data, 
        linestyle_opts=opts.LineStyleOpts(
            is_show = True,  # bool 是否显示
            width = 1,  # Numeric 线宽
            opacity = 1,  # Numeric 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形
            curve = 0,  # Numeric 线的弯曲度，0 表示完全不弯曲
            type_ = "solid",  # str 线的类型。可选 'solid', 'dashed', 'dotted'
            color = None  # [Union str, Sequence, None] 线的颜色 见部分配置通用参数详解
            )
        )
    )
```

### 涟漪效果配置

effect_opts=opts.EffectOpts

```python
effectScatter = (
    EffectScatter()
    .add_xaxis(x_data)
    .add_yaxis(
        '', 
        y_data,
        effect_opts=opts.EffectOpts(
            is_show: bool = True,  # 是否显示特效
            brush_type: str = "stroke",  # 波纹的绘制方式 可选 'stroke' 和 'fill' Scatter 类型有效
            scale = 2.5,  # Numeric 动画中波纹的最大缩放比例 Scatter 类型有效
            period = 4,  # Numeric 动画的周期，秒数，Scatter 类型有效
            color = None,  #str 特效标记的颜色
            symbol = None,  #str 特效图形的标记 可选 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
            symbol_size = None,  #Numeric List 特效标记的大小
            trail_length = None,  #Numeric 特效尾迹的长度
            )
        )
```

### 图元配置

```python
itemstyle_opts=opts.ItemStyleOpts(
    color=None,# 图形的颜色 见部分配置通用参数详解
    color0 = None,# 阴线 图形的颜色
    border_color = None,# 图形的描边颜色。支持的颜色格式同 color，不支持回调函数。
    border_color0 = None,# 阴线 图形的描边颜色。
    opacity = None # 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
    )
```

### 标签配置项

```python
label_opts=opts.LabelOpts(
    is_show=False,# bool 是否显示标签。
    position = "top",# 标签位置，可选：# 'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight','insideTop'，'insideBottom'， 'insideTopLeft'，'insideBottomLeft','insideTopRight'，'insideBottomRight'  
    color = None,# 文字的颜色。
    font_size = 12,# 文字的字体大小  
    font_style = None,# 文字字体的风格，可选：'normal'，'italic'，'oblique'  
    font_weight = None,# 文字字体的粗细，可选：'normal'，'bold'，'bolder'，'lighter'  
    font_family = None,  # str ,文字的字体系列 可选：'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei', ... 
    rotate = None, # Numeric  # 标签旋转。从 -90 度到 90 度。正值是逆时针。
    margin = 8, # Numeric  # 刻度标签与轴线之间的距离。  
    interval = None, # Numeric str, None 坐标轴刻度标签的显示间隔，在类目轴中有效。设置成 0 强制显示所有标签,设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推
    horizontal_align = None, # str  # 文字水平对齐方式，可选：'left'，'center'，'right'  
    vertical_align = None, # str  # 文字垂直对齐方式，可选：'top'，'middle'，'bottom'  
    formatter = None, # str  标签内容格式器
    rich = None, # dict  在 rich 里面，可以自定义富文本样式。利用富文本样式，可以在标签中做出非常丰富的效果
    )
```

### 标记点配置

```python
markpoint_opts=opts.MarkPointOpts(
    data=[
        opts.MarkPointItem(type_="max", name="x轴最大",value_index=0),
        opts.MarkPointItem(type_="min", name="y轴最小值" value_index=1),
        opts.MarkPointItem(type_="average", name="平均值"),
        opts.MarkPointItem(coord=['朋友圈', 200], name="坐标"),
        opts.MarkPointItem(x=200, y=160, name="像素值"),
        opts.MarkPointItem(coord=[4, 150], name="设置value", value='hi')
    ]),
```

### 标记线配置

```python
markline_opts=opts.MarkLineOpts(
    data=[
        opts.MarkLineItem(type_="min", name="最小值"),
        opts.MarkLineItem(type_="max", name="最大值"),
        opts.MarkLineItem(type_="average", name="平均值")
        opts.MarkLineItem(x="微信朋友圈", name="x=微信朋友圈"),
        opts.MarkLineItem(y=100, name="y=100")
    ])
```

### 标记区域配置

```python
markarea_opts=opts.MarkAreaOpts(
    data=[
        opts.MarkAreaItem(name="特别关注", x=("微信朋友圈", "今日头条")),
    ])
```

## 部分配置通用参数详解

### color

包含该参数配置项：图元，线样式

```python
# 颜色英文
itemstyle_opts=opts.ItemStyleOpts(color='blue')
# 十六进制格式
itemstyle_opts=opts.ItemStyleOpts(color='#0000FF')
# RGB通道
itemstyle_opts=opts.ItemStyleOpts(color='rgb(0, 0, 255)')
# RGBA通道,增加透明度alpha
itemstyle_opts=opts.ItemStyleOpts(color='rgba(0, 0, 255, 0.5)')
# 线性渐变
itemstyle_opts=opts.ItemStyleOpts(
        color={
            'type':'linear',
            'x':0, # 从左往右
            'y':0, # 从上往下
            'x2':0,# 从右往左
            'y2':1, # 从下往上
            'colorStops':[
             {'offset':0,'color':'red'}, # 0% 处的颜色
             {'offset':1,'color':'blue'} # 100% 处的颜色
            ],
            'global':False
        }
    )
# 径向渐变，从圆心向四周渐变
itemstyle_opts=opts.ItemStyleOpts(
        color={
            'type':'radial',
            'x':0, # 圆心x
            'y':0, # 圆心y
            'r':0, # 半径
            'colorStops':[
             {'offset':0,'color':'red'}, # 圆心颜色
             {'offset':1,'color':'blue'} # 圆周颜色
            ],
            'global':False
        }
    )
```

### formatter

标签内容格式器，支持字符串模板和回调函数两种形式，字符串模板与回调函数返回的字符串均支持用 \n 换行。  
模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等。  
在 trigger 为 'axis' 的时候，会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2} 这种后面加索引的方式表示系列的索引。    
不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样。 其中变量{a}, {b}, {c}, {d}在不同图表类型下代表数据含义为：   

|图|{a}|{b}|{c}|{d}|
|:--|:--|:--|:--|:--|
|折线（区域）图、柱状（条形）图、K线图|系列名称|类目值|数值|无|
|散点图（气泡）图|系列名称|数据名称|数值数组|无|
|地图|系列名称|区域名称|合并数值|无|
|饼图、仪表盘、漏斗图|系列名称|数据项名称|数值|百分比|

```python
# 通常用法
label_opts = opts.LabelOpts(
    formatter='数值:{c} 类目:{b}'
)

# JS用法
# 在非饼图、仪表盘、漏斗图显示百分比
# 将浮点数转为百分比的JavaScript代码，用于标签和提示
per_js = """function (param) {return Math.floor(param.value[1] * 100)+'%';}"""
# 将浮点数转为百分比的JavaScript代码,用于坐标轴
ax_per_js = """function (value) {return Number(value *100)+'%';}"""

.add_yaxis(
    '百分比', 
    data,
    label_opts=opts.LabelOpts(
        formatter=JsCode(per_js)# 通过执行JavaScript代码将标签转为百分比
        )
    )
.set_global_opts(
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(formatter=JsCode(ax_per_js))# 坐标轴也显示百分比
        )
    )
```