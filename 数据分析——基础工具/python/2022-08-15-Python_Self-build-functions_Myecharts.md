---
title:  函数实现-Pyecharts简化函数
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# Pyecharts简化函数

出于学习与使用方便的目的，写了下面这个Pyecharts简化函数

## 1. 准备工作

**函数导入**

```python
from pyecharts import options as opts
from pyecharts.faker import Collector, Faker
# 保存图片 table无法保存
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot 
from pyecharts.globals import ThemeType
import pyecharts.charts as Eplot
```

**数据准备**

```python
df = pd.DataFrame({'日期':[datetime.datetime(2021,7,x).strftime("%Y-%m-%d") for x in range(1,14,1)],
             '销售额':np.random.normal(10000,500,13),
             '名片量':np.random.normal(200,50,13)})
```

## 2. 使用

先给大家看一下如何使用，可以对比一下简化前后代码区别
函数放在在最后

```python
# 查看帮助
myecharts().help_manual('轴')
myecharts().help_manual('标签')
eplot = myecharts(ptype='Bar')

# 画图
eplot = myecharts(ptype='Bar') # 条形图

eplot.plot(x = df['日期'],y = df.iloc[:,1:],mode='1',Line_style=[{'width':5},{'width':3}])\
.set_title(title='主标题',subtitle='副标题')\
.set_legend()\
.set_axis("x")\
.set_axis("y",is_scale=True,splitarea_opts=True)\
.set_VisualMap(is_show=True,type_='size')\
.set_DataZoom(Zoomnum=1,orient='vertical')\
.set_DataZoom(Zoomnum=-1)\
.set_label(position='top',color='black',font_size=10)\
.set_MarkPoint(data=[{'type_':'max','name':'最大值','symbol':'arrow'},{'type_':'min','name':'最小值'}],symbol='roundRect',label_opts = {'is_show':False})\
.set_MarkLine(data=[{'type_':'average','name':'平均值'},{'y':10000}])\
.set_MarkArea(data=[{'x':('2021-07-01','2021-07-05'),'name':'月初','itemstyle_opts':{'color':'red','opacity':0.1}}])\
.set_tooltip()\
.show()
```

**输出**：

输出分为两部分，一是简化前用pyecharts要写的参数，二是可视化图  
为了展示函数，使用了大多数参数，图片不太美观，实际使用时按需使用即可

```python
global_opts title_opts=opts.TitleOpts(
    title="主标题",
    subtitle="副标题",
    pos_left="center",
    title_textstyle_opts=opts.TextStyleOpts(color="black",font_size=30),),
    legend_opts=opts.LegendOpts(is_show=True,pos_right="10%",item_width=25,item_height=14),
    xaxis_opts=opts.AxisOpts(name="日期",splitarea_opts=opts.SplitAreaOpts(is_show=None,areastyle_opts=opts.AreaStyleOpts(opacity='0.6'))),
    yaxis_opts=opts.AxisOpts(is_scale=True,name="日期",splitarea_opts=opts.SplitAreaOpts(is_show=True,areastyle_opts=opts.AreaStyleOpts(opacity='0.6'))),
    visualmap_opts=opts.VisualMapOpts(is_show=True,type_="size",pos_right="3%",min_=99.15,max_=11148.02),
    datazoom_opts=[opts.DataZoomOpts(orient="vertical",range_start=0,range_end=100),opts.DataZoomOpts(range_start=0,range_end=100)],
    tooltip_opts=opts.TooltipOpts(is_show=True,trigger="axis",trigger_on="mousemove|click",axis_pointer_type="cross",border_width=0),
    series_opts label_opts=opts.LabelOpts(position="top",color="black",font_size=10),
    markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max",name="最大值",symbol="arrow"),opts.MarkPointItem(type_="min",name="最小值")],symbol="pin",label_opts=opts.LabelOpts(is_show=False)),
    markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average",name="平均值"),opts.MarkLineItem(y=10000)]),
    markarea_opts=opts.MarkAreaOpts(data=[opts.MarkAreaItem(x=('2021-07-01', '2021-07-05'),name="月初",itemstyle_opts=opts.ItemStyleOpts(color="red",opacity=0.1))])
```

![myecharts输出](https://raw.githubusercontent.com/analy-liu/PersonalImgaes/main/images/Pyecharts_Example.png)

## 3. 函数

最后是函数部分，如果需要，可以直接复制使用（需要先安装好pyecharts包）

```python
class myecharts(object):
    def __init__(self,ptype='Bar',theme = 'white',width=1400, height=700,page_title = 'analy_liu-pyecharts',bg_color = 'white',Echart = None):
        if Echart:
            self.eplot = Echart
        else:
            self.eplot = eval('Eplot.{}(init_opts=opts.InitOpts(theme="{}",width="{}px",height="{}px",page_title="{}",bg_color="{}"))'.format(ptype,theme,width,height,page_title,bg_color))
        
        self.ptype = ptype
        self.width = width
        self.global_opts = ''
        self.series_opts = ''
        
    def dict_transform(self,dict_):
        temp_set = ''
        for i in dict_.keys():
            if i == 'itemstyle_opts':
                dict_[i] = 'opts.ItemStyleOpts({})'.format(self.dict_transform(dict_[i]))
            if type(dict_[i])==str and '_opts'  not in i and 'data'  not in i:
                temp_set = temp_set+'{}="{}",'.format(i,dict_[i])
            elif dict_[i] != None:
                temp_set = temp_set+'{}={},'.format(i,dict_[i])
        return temp_set[0:-1]
    
    def set_TextStyle(self,TextStyle_opts = None):
#         TextStyle_opts = {'color':color,'font_style':font_style,'font_weight':font_weight,'font_family':font_family,'font_size':font_size,
#                           'align':align,'vertical_align':vertical_align,'line_height':line_height,
#                           'background_color':background_color,'border_color':border_color,
#                           'border_width':border_width,'border_radius':border_radius,'padding':padding,'shadow_color':shadow_color,'shadow_blur':shadow_blur,'width':width,'height':height,'rich':rich}
        if TextStyle_opts == None:
            return None
        else:
            temp_set = self.dict_transform(TextStyle_opts)
            return 'opts.TextStyleOpts({}),'.format(temp_set)
        
    def plot(self,x=None,y=None,data=None,mode='常规',Line_style=None):
        if str(type(x))=="<class 'pandas.core.frame.DataFrame'>":
            x = x.iloc[:,0]
            print('x类型为DataFrame,取第一列为x')
        try:
            y = y.apply(lambda x:round(x,2))
        except:
            pass
        self.x = x
        self.y = y
        
        if self.ptype in ['Bar','Line','Scatter']:
            self.eplot.add_xaxis(x.tolist())
            try:
                if Line_style!= None or self.ptype!='Line':
                    for i in y.columns:
                        self.eplot.add_yaxis(i,y.loc[:,i].tolist())
                else:
                    j=0
                    for col in y.columns:
                        temp_set = self.dict_transform(Line_style[j])
                        eval("self.eplot.add_yaxis('{}',y.loc[:,'{}'].tolist(),linestyle_opts=opts.LineStyleOpts({}))".format(col,col,temp_set))
                        j += 1
            except:
                self.eplot.add_yaxis(y.name,y.tolist())     
        elif self.ptype == 'Boxplot':
            if mode == '常规':
                # 常规方法
                self.eplot.add_xaxis(y.columns.tolist())
                temp=[]
                for i in self.y.columns:
                    temp.append(y.loc[:,i].tolist())
                self.eplot.add_yaxis("", self.eplot.prepare_data(temp))
            else:
                # 切片方法
                temp = ' '.join(['' for x in range(int((self.width*0.8)/4/len(y.columns)))])
                self.eplot.add_xaxis([temp.join(y.columns.tolist())])# 为了箱型图可切片
                for i in y.columns:
                    self.eplot.add_yaxis(i, self.eplot.prepare_data([y.loc[:,i].tolist()]))
        elif self.ptype == 'Pie':
            try:
                self.eplot.add('测试',data.values.tolist())
            except:
                self.eplot.add('测试',[list(z) for z in zip(x.tolist(), y.tolist())])
        return self
    
    def set_title(self, title=None, title_link=None, title_target=None, 
                  subtitle=None, subtitle_link=None, subtitle_target=None,
                  pos_left='center', pos_right=None, pos_top=None, pos_bottom=None,
                  padding=None,item_gap=None,
                  title_textstyle_opts={'color':'black','font_size':30}, subtitle_textstyle_opts=None):
        # 设置文字格式
        title_textstyle_opts = self.set_TextStyle(title_textstyle_opts)
        subtitle_textstyle_opts = self.set_TextStyle(subtitle_textstyle_opts)
        
        global_opts = {'title':title,'title_link':title_link,'title_target':title_target,
                      'subtitle':subtitle,'subtitle_link':subtitle_link,'subtitle_target':subtitle_target,
                      'pos_left':pos_left,'pos_right':pos_right,'pos_top':pos_top,'pos_bottom':pos_bottom,
                      'padding':padding,'item_gap':item_gap,
                      'title_textstyle_opts':title_textstyle_opts,'subtitle_textstyle_opts':subtitle_textstyle_opts}
        temp_set = self.dict_transform(global_opts)
        self.global_opts += 'title_opts=opts.TitleOpts({}),'.format(temp_set)
        return self
    
    def set_legend(self, type_=None, selected_mode=None, 
                   is_show=True, orient=None, align=None, inactive_color=None,
                   pos_left=None, pos_right="10%", pos_top=None, pos_bottom=None,
                   padding=None,item_gap=None, item_width=25, item_height=14,
                   textstyle_opts=None, legend_icon=None):
        # 设置文字格式
        textstyle_opts = self.set_TextStyle(textstyle_opts)
        
        global_opts = {'type_':type_,'selected_mode':selected_mode,
                       'is_show':is_show,'orient':orient,'align':align,'inactive_color':inactive_color,
                      'pos_left':pos_left,'pos_right':pos_right,'pos_top':pos_top,'pos_bottom':pos_bottom,
                      'padding':padding,'item_gap':item_gap, 'item_width':item_width, 'item_height':item_height, 
                      'textstyle_opts':textstyle_opts,'legend_icon':legend_icon}
        temp_set = self.dict_transform(global_opts)
        self.global_opts += 'legend_opts=opts.LegendOpts({}),'.format(temp_set)
        return self
    
    def set_tooltip(self, is_show=True, trigger='item',trigger_on='mousemove|click',axis_pointer_type='line',
                   formatter=None, 
                   background_color=None, border_color=None, border_width=0, textstyle_opts=None):
        if self.ptype in ['Bar','Line','Scatter']:
            trigger='axis'
            axis_pointer_type='cross'
        elif self.ptype in ['Pie']:
            formatter='{b} :{d}%'
        # 设置文字格式
        textstyle_opts = self.set_TextStyle(textstyle_opts)
        
        global_opts = {'is_show':is_show,'trigger':trigger,'trigger_on':trigger_on,'axis_pointer_type':axis_pointer_type,
                       'formatter':formatter,
                       'background_color':background_color,'border_color':border_color,'border_width':border_width,'textstyle_opts':textstyle_opts}
        temp_set = self.dict_transform(global_opts)
        self.global_opts += 'tooltip_opts=opts.TooltipOpts({}),'.format(temp_set)
        return self
        
    def set_axis(self,axis,type_=None, is_show=None, is_scale=None, is_inverse=None, interval=None, split_number=None, boundary_gap=None, min_=None, max_=None, min_interval=None, max_interval=None, 
                 name=None, name_location=None, name_gap=None, name_rotate=None,
                 grid_index=None, position=None, offset=None, 
                 axisline_opts=None, axistick_opts=None, axislabel_opts=None, axispointer_opts=None, textstyle_opts=None, splitarea_opts=None, splitline_opts=None):
        name = self.x.name
        name_textstyle_opts = self.set_TextStyle(textstyle_opts)
        splitarea_opts = "opts.SplitAreaOpts(is_show={},areastyle_opts=opts.AreaStyleOpts(opacity='0.6'))".format(splitarea_opts)
        
        global_opts = {'type_':type_, 'is_show':is_show, 'is_scale':is_scale, 'is_inverse':is_inverse, 'interval':interval, 'split_number':split_number, 'boundary_gap':boundary_gap, 'min_':min_, 'max_':max_, 'min_interval':min_interval, 'max_interval':max_interval,
                        'name':name, 'name_location':name_location, 'name_gap':name_gap, 'name_rotate':name_rotate,
                        'grid_index':grid_index, 'position':position, 'offset':offset, 
                        'axisline_opts':axisline_opts, 'axistick_opts':axistick_opts, 'axislabel_opts':axislabel_opts, 'axispointer_opts':axispointer_opts, 'name_textstyle_opts':name_textstyle_opts, 'splitarea_opts':splitarea_opts, 'splitline_opts':splitline_opts}
        temp_set = self.dict_transform(global_opts)
        if axis == 'x':
            self.global_opts += 'xaxis_opts=opts.AxisOpts({}),'.format(temp_set)
        elif axis == 'y':
            self.global_opts += 'yaxis_opts=opts.AxisOpts({}),'.format(temp_set)
        else:
            print('axis请输入"x"或"y"')
        return self
    
    def set_VisualMap(self,is_show=None, type_=None, orient=None, is_calculable=None, is_piecewise=None, is_inverse=None, item_width=None, item_height=None, background_color=None, border_color=None, border_width=None,
                        pos_left=None, pos_right="3%", pos_top=None, pos_bottom=None, 
                        min_=None, max_=None, range_text=None, range_color=None, range_size=None, range_opacity=None, split_number=None, pieces=None,
                        series_index=None, dimension=None, out_of_range=None, textstyle_opts=None):
        textstyle_opts = self.set_TextStyle(textstyle_opts)
        if max_ == None:
            max_ = self.y.max().max()
        if min_ == None:
            min_ = self.y.min().min()
        
        global_opts = {'is_show':is_show, 'type_':type_, 'orient':orient, 'is_calculable':is_calculable, 'is_piecewise':is_piecewise, 'is_inverse':is_inverse, 'item_width':item_width, 'item_height':item_height, 'background_color':background_color, 'border_color':border_color, 'border_width':border_width, 
                        'pos_left':pos_left, 'pos_right':pos_right, 'pos_top':pos_top, 'pos_bottom':pos_bottom, 
                        'min_':min_, 'max_':max_, 'range_text':range_text, 'range_color':range_color, 'range_size':range_size, 'range_opacity':range_opacity, 'split_number':split_number, 'pieces':pieces,
                        'series_index':series_index, 'dimension':dimension, 'out_of_range':out_of_range, 'textstyle_opts':textstyle_opts}
        
        temp_set = self.dict_transform(global_opts)
        self.global_opts += 'visualmap_opts=opts.VisualMapOpts({}),'.format(temp_set)
        return self
    
    def set_DataZoom(self,Zoomnum=0,is_show=None, type_=None, is_realtime=None, orient=None, xaxis_index=None, yaxis_index=None, is_zoom_lock=None,
                        range_start=None, range_end=None, start_value=None, end_value=None, 
                        pos_left=None, pos_top=None, pos_right=None, pos_bottom=None):
        if start_value==None and end_value==None:
            range_start=0
            range_end=100
        
        global_opts = {'is_show':is_show,'type_':type_,'is_realtime':is_realtime,'orient':orient,'xaxis_index':xaxis_index,'yaxis_index':yaxis_index,'is_zoom_loc':is_zoom_lock,
                        'range_start':range_start,'range_end':range_end,'start_value':start_value,'end_value':end_value,
                        'pos_left':pos_left,'pos_top':pos_top,'pos_right':pos_right,'pos_bottom':pos_bottom,}
        temp_set = self.dict_transform(global_opts)
        if Zoomnum==0:
            self.global_opts += 'datazoom_opts=opts.DataZoomOpts({}),'.format(temp_set)
        elif Zoomnum==1:
            self.global_opts += 'datazoom_opts=[opts.DataZoomOpts({})'.format(temp_set)
        elif Zoomnum not in [-1,0,1]:
            self.global_opts += ',opts.DataZoomOpts({})'.format(temp_set)
        elif Zoomnum == -1:
            self.global_opts += ',opts.DataZoomOpts({})],'.format(temp_set)
        return self
    
    def ItemStyle(self,color=None,color0=None,border_color=None,border_color0=None,opacity=None):
        series_opts = {'color':color,'color0':color0,'border_color':border_color,'border_color0':border_color0,'opacity':opacity}
        
        temp_set = self.dict_transform(series_opts)
        
        self.series_opts += 'itemstyle_opts=opts.ItemStyleOpts({}),'.format(temp_set)
        return self
    
    def set_label(self,is_show=None,position=None,
                    color=None,font_size=None,font_style=None,font_weight=None,font_family=None,
                    margin=None,interval=None,horizontal_align=None,vertical_align=None,vertical_alignc=None,formatter=None,rich=None):
        if self.ptype == 'Pie':
            formatter = '{b}: {d}%'
        series_opts = {'is_show':is_show,'position':position,
                        'color':color,'font_size':font_size,'font_style':font_style,'font_weight':font_weight,'font_family':font_family,
                        'margin':margin,'interval':interval,'horizontal_align':horizontal_align,'vertical_align':vertical_align,'vertical_alignc':vertical_alignc,'formatter':formatter,'rich':rich}
        
        temp_set = self.dict_transform(series_opts)
        self.series_opts += 'label_opts=opts.LabelOpts({}),'.format(temp_set)
        return self
    
    def set_MarkPoint(self,data=None,symbol=None,symbol_size=None,label_opts=None):
        if self.ptype == 'Bar':
            symbol = 'pin'
        
        temp = []
        for i in data:
            temp_set = self.dict_transform(i)
            temp_set = "opts.MarkPointItem({})".format(temp_set)
            temp.append(temp_set)
        data = '['+','.join(temp)+']'
        if label_opts != None:
            label_opts = "opts.LabelOpts({})".format(self.dict_transform(label_opts))
        
        series_opts = {'data':data,'symbol':symbol,'symbol_size':symbol_size,'label_opts':label_opts}
        temp_set = self.dict_transform(series_opts)
        self.series_opts += 'markpoint_opts=opts.MarkPointOpts({}),'.format(temp_set)
        return self
    
    def set_MarkLine(self,is_silent=None,data=[{'type_':'average','name':'平均值'}],symbol=None,symbol_size=None,precision=None,label_opts=None,linestyle_opts=None):
        temp = []
        for i in data:
            temp_set = self.dict_transform(i)
            temp_set = "opts.MarkLineItem({})".format(temp_set)
            temp.append(temp_set)
        data = '['+','.join(temp)+']'
        if linestyle_opts != None:
            linestyle_opts = "opts.LineStyleOpts({})".format(self.dict_transform(linestyle_opts))
        
        series_opts = {'data':data,'symbol':symbol,'symbol_size':symbol_size,'linestyle_opts':linestyle_opts,'is_silent':is_silent,'precision':precision}
        temp_set = self.dict_transform(series_opts)
        self.series_opts += 'markline_opts=opts.MarkLineOpts({}),'.format(temp_set)
        return self
    
    def set_MarkArea(self,is_silent=None,data=None,label_opts=None):
        temp = []
        for i in data:
            temp_set = self.dict_transform(i)
            temp_set = "opts.MarkAreaItem({})".format(temp_set)
            temp.append(temp_set)
        data = '['+','.join(temp)+']'
        if label_opts != None:
            label_opts = "opts.LabelOpts({})".format(self.dict_transform(label_opts))
        
        series_opts = {'data':data,'is_silent':is_silent,'label_opts':label_opts}
        temp_set = self.dict_transform(series_opts)
        self.series_opts += 'markarea_opts=opts.MarkAreaOpts({}),'.format(temp_set)
        return self
    
    def show(self):
        print("global_opts",self.global_opts)
        eval('self.eplot.set_global_opts({})'.format(self.global_opts[0:-1]))
        print("series_opts",self.series_opts)
        eval('self.eplot.set_series_opts({})'.format(self.series_opts[0:-1]))
        return self.eplot.render_notebook()
        
    def save(self,path = None,file_name = None):
        eval('self.eplot.set_global_opts({})'.format(self.global_opts[0:-1]))
        eval('self.eplot.set_series_opts({})'.format(self.series_opts[0:-1]))
        if not path:
            if not file_name:
                path = r'F:\sunland\data\pyecharts_html\pyecharts_{}.html'.format(self.ptype)
            else:
                path = r'F:\sunland\data\pyecharts_html\{}.html'.format(file_name)
        make_snapshot(snapshot, self.eplot.render(), path)
#         self.eplot.render(path = path)
        print('保存位置：',path)
        return self.eplot
        
    def help_manual(self,help_type=None):
        if not help_type:
            print("ptype填写pyecharts画图类型，例如'Bar'")
            print("可直接传入pandas表")
            print("目前可用类型：",['Bar','Line','Scatter','Boxplot','Pie'])
            print("更多帮助请输入：'主题','mode','标题','图例','提示框','轴','视觉','滑块'")
            print("本函数参考：https://www.heywhale.com/mw/project/5eb7958f366f4d002d783d4a")
        elif '主题' in help_type:
            print('主题列表',
                  ['chalk',
                  'dark',
                  'essos',
                  'infographic',
                  'light',
                  'macarons',
                  'purple-passion',
                  'roma',
                  'romantic',
                  'shine',
                  'vintage',
                  'walden',
                  'westeros',
                  'white',
                  'wonderland'])
        elif 'mode' in help_type:
            print('mode只影响部分图，例如箱型图，分为常规与切片')
        elif '文字' in help_type:
            print("""# 文字颜色。  
                    color: Optional[str] = None,  

                    # 文字字体的风格  
                    # 可选：'normal'，'italic'，'oblique'  
                    font_style: Optional[str] = None,  

                    # 主标题文字字体的粗细，可选：  
                    # 'normal'，'bold'，'bolder'，'lighter'  
                    font_weight: Optional[str] = None,  

                    # 文字的字体系列  
                    # 还可以是 'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei', ...  
                    font_family: Optional[str] = None,  

                    # 文字的字体大小  
                    font_size: Optional[Numeric] = None,  

                    # 文字水平对齐方式，默认自动  
                    align: Optional[str] = None,  

                    # 文字垂直对齐方式，默认自动  
                    vertical_align: Optional[str] = None,  

                    # 行高  
                    line_height: Optional[str] = None,  

                    # 文字块背景色。可以是直接的颜色值，例如：'#123234', 'red', 'rgba(0,23,11,0.3)'  
                    background_color: Optional[str] = None,  

                    # 文字块边框颜色  
                    border_color: Optional[str] = None,  

                    # 文字块边框宽度  
                    border_width: Optional[Numeric] = None,  

                    # 文字块的圆角  
                    border_radius: Union[Numeric, Sequence, None] = None,  

                    # 文字块的内边距   
                    # 例如 padding: [3, 4, 5, 6]：表示 [上, 右, 下, 左] 的边距  
                    # 例如 padding: 4：表示 padding: [4, 4, 4, 4]  
                    # 例如 padding: [3, 4]：表示 padding: [3, 4, 3, 4]  
                    padding: Union[Numeric, Sequence, None] = None,  

                    # 文字块的背景阴影颜色  
                    shadow_color: Optional[str] = None,  

                    # 文字块的背景阴影长度  
                    shadow_blur: Optional[Numeric] = None,  

                    # 文字块的宽度  
                    width: Optional[str] = None,  

                    # 文字块的高度  
                    height: Optional[str] = None,  

                    # 在 rich 里面，可以自定义富文本样式。利用富文本样式，可以在标签中做出非常丰富的效果  
                    # 具体配置可以参考一下 https://www.echartsjs.com/tutorial.html#%E5%AF%8C%E6%96%87%E6%9C%AC%E6%A0%87%E7%AD%BE  
                    rich: Optional[dict] = None, 
                    # 字符串模板 模板变量有：  
                    # {a}：系列名。  
                    # {b}：数据名。  
                    # {c}：数据值。  
                    # {d}：百分比，只在特定图表中生效，如饼图，漏斗图
                    # {@xxx}：数据中名为 'xxx' 的维度的值，如 {@product} 表示名为 'product'` 的维度的值。  
                    # {@[n]}：数据中维度 n 的值，如{@[3]}` 表示维度 3 的值，从 0 开始计数。  
                    # 示例：formatter: '{b}: {@score}'  """)
        elif '标题' in help_type or 'title' in help_type:
            print("set_title")
            print("""# 主标题文本，支持使用 \n 换行。  
                    title: Optional[str] = None,  

                    # 主标题跳转 URL 链接  
                    title_link: Optional[str] = None,  

                    # 主标题跳转链接方式  
                    # 默认值是: blank  
                    # 可选参数: 'self', 'blank'  
                    # 'self' 当前窗口打开; 'blank' 新窗口打开  
                    title_target: Optional[str] = None,  

                    # 副标题文本，支持使用 \n 换行。  
                    subtitle: Optional[str] = None,  

                    # 副标题跳转 URL 链接  
                    subtitle_link: Optional[str] = None,  

                    # 副标题跳转链接方式  
                    # 默认值是: blank  
                    # 可选参数: 'self', 'blank'  
                    # 'self' 当前窗口打开; 'blank' 新窗口打开  
                    subtitle_target: Optional[str] = None,  

                    # title 组件离容器左侧的距离。  
                    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
                    # 也可以是 'left', 'center', 'right'。  
                    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。  
                    pos_left: Optional[str] = None,  

                    # title 组件离容器右侧的距离。  
                    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
                    pos_right: Optional[str] = None,  

                    # title 组件离容器上侧的距离。  
                    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
                    # 也可以是 'top', 'middle', 'bottom'。  
                    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。  
                    pos_top: Optional[str] = None,  

                    # title 组件离容器下侧的距离。  
                    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
                    pos_bottom: Optional[str] = None,  

                    # 标题内边距，单位px，默认各方向内边距为5，接受数组分别设定上右下左边距。  
                    # // 设置内边距为 5  
                    # padding: 5  
                    # // 设置上下的内边距为 5，左右的内边距为 10  
                    # padding: [5, 10]  
                    # // 分别设置四个方向的内边距  
                    # padding: [  
                    #     5,  // 上  
                    #     10, // 右  
                    #     5,  // 下  
                    #     10, // 左  
                    # ]  
                    padding: Union[Sequence, Numeric] = 5,  

                    # 主副标题之间的间距。  
                    item_gap: Numeric = 10,  

                    # 主标题字体样式配置项，参考 `series_options.TextStyleOpts`  
                    title_textstyle_opts: Union[TextStyleOpts, dict, None] = None,  

                    # 副标题字体样式配置项，参考 `series_options.TextStyleOpts`  
                    subtitle_textstyle_opts: Union[TextStyleOpts, dict, None] = None,""")
        elif '图例' in help_type or 'lengend' in help_type:
            print("set_legend")
            print("""# 图例的类型。可选值：  
                    # 'plain'：普通图例。缺省就是普通图例。  
                    # 'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。  
                    type_: Optional[str] = None,  

                    # 图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。默认开启图例选择，可以设成 false 关闭  
                    # 除此之外也可以设成 'single' 或者 'multiple' 使用单选或者多选模式。  
                    selected_mode: Union[str, bool, None] = None,  

                    # 是否显示图例组件  
                    is_show: bool = True,  

                    # 图例组件离容器左侧的距离。  
                    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
                    # 也可以是 'left', 'center', 'right'。  
                    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。  
                    pos_left: Union[str, Numeric, None] = None,  

                    # 图例组件离容器右侧的距离。  
                    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
                    pos_right: Union[str, Numeric, None] = None,  

                    # 图例组件离容器上侧的距离。  
                    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
                    # 也可以是 'top', 'middle', 'bottom'。  
                    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。  
                    pos_top: Union[str, Numeric, None] = None,  

                    # 图例组件离容器下侧的距离。  
                    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
                    pos_bottom: Union[str, Numeric, None] = None,  

                    # 图例列表的布局朝向。可选：'horizontal', 'vertical'  
                    orient: Optional[str] = None,  

                    # 图例标记和文本的对齐。默认自动（auto）  
                    # 根据组件的位置和 orient 决定  
                    # 当组件的 left 值为 'right' 以及纵向布局（orient 为 'vertical'）的时候为右对齐，即为 'right'。  
                    # 可选参数: `auto`, `left`, `right`  
                    align: Optional[str] = None,  

                    # 图例内边距，单位px，默认各方向内边距为5  
                    padding: int = 5,  

                    # 图例每项之间的间隔。横向布局时为水平间隔，纵向布局时为纵向间隔。  
                    # 默认间隔为 10  
                    item_gap: int = 10,  

                    # 图例标记的图形宽度。默认宽度为 25  
                    item_width: int = 25,  

                    # 图例标记的图形高度。默认高度为 14  
                    item_height: int = 14,  

                    # 图例关闭时的颜色。默认是 #ccc  
                    inactive_color: Optional[str] = None,  

                    # 图例组件字体样式，参考 `series_options.TextStyleOpts`  
                    textstyle_opts: Union[TextStyleOpts, dict, None] = None,  

                    # 图例项的 icon。  
                    # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'  
                    # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。  
                    # 可以通过 'path://' 将图标设置为任意的矢量路径。  
                    legend_icon: Optional[str] = None,  """)
        elif '提示框' in help_type or 'tooltip' in help_type:
            print("set_tooltip")
            print("""# 是否显示提示框组件，包括提示框浮层和 axisPointer。  
                    is_show: bool = True,  

                    # 触发类型。可选：  
                    # 'item': 数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。  
                    # 'axis': 坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。  
                    # 'none': 什么都不触发  
                    trigger: str = "item",  

                    # 提示框触发的条件，可选：  
                    # 'mousemove': 鼠标移动时触发。  
                    # 'click': 鼠标点击时触发。  
                    # 'mousemove|click': 同时鼠标移动和点击时触发。  
                    # 'none': 不在 'mousemove' 或 'click' 时触发，  
                    trigger_on: str = "mousemove|click",  

                    # 指示器类型。可选  
                    # 'line'：直线指示器  
                    # 'shadow'：阴影指示器  
                    # 'none'：无指示器  
                    # 'cross'：十字准星指示器。其实是种简写，表示启用两个正交的轴的 axisPointer。  
                    axis_pointer_type: str = "line",  

                    # 标签内容格式器，支持字符串模板和回调函数两种形式，字符串模板与回调函数返回的字符串均支持用 \n 换行。  
                    # 字符串模板 模板变量有：  
                    # {a}：系列名。  
                    # {b}：数据名。  
                    # {c}：数据值。  
                    # {d}：百分比，只在特定图表中生效，如饼图，漏斗图
                    # {@xxx}：数据中名为 'xxx' 的维度的值，如 {@product} 表示名为 'product'` 的维度的值。  
                    # {@[n]}：数据中维度 n 的值，如{@[3]}` 表示维度 3 的值，从 0 开始计数。  
                    # 示例：formatter: '{b}: {@score}'  
                    #   
                    # 回调函数，回调函数格式：  
                    # (params: Object|Array) => string  
                    # 参数 params 是 formatter 需要的单个数据集。格式如下：  
                    # {  
                    #    componentType: 'series',  
                    #    // 系列类型  
                    #    seriesType: string,  
                    #    // 系列在传入的 option.series 中的 index  
                    #    seriesIndex: number,  
                    #    // 系列名称  
                    #    seriesName: string,  
                    #    // 数据名，类目名  
                    #    name: string,  
                    #    // 数据在传入的 data 数组中的 index  
                    #    dataIndex: number,  
                    #    // 传入的原始数据项  
                    #    data: Object,  
                    #    // 传入的数据值  
                    #    value: number|Array,  
                    #    // 数据图形的颜色  
                    #    color: string,  
                    # }  
                    formatter: Optional[str] = None,  

                    # 提示框浮层的背景颜色。  
                    background_color: Optional[str] = None,  

                    # 提示框浮层的边框颜色。  
                    border_color: Optional[str] = None,  

                    # 提示框浮层的边框宽。  
                    border_width: Numeric = 0,  

                    # 文字样式配置项，参考 `series_options.TextStyleOpts`  
                    textstyle_opts: TextStyleOpts = TextStyleOpts(font_size=14),  """)
        elif '轴' in help_type:
            print("set_axis")
            print("""# 坐标轴类型。可选：  
                    # 'value': 数值轴，适用于连续数据。  
                    # 'category': 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。  
                    # 'time': 时间轴，适用于连续的时序数据，与数值轴相比时间轴带有时间的格式化，在刻度计算上也有所不同，  
                    # 例如会根据跨度的范围来决定使用月，星期，日还是小时范围的刻度。  
                    # 'log' 对数轴。适用于对数数据。  
                    type_: Optional[str] = None,  

                    # 坐标轴名称。  
                    name: Optional[str] = None,  

                    # 是否显示 x 轴。  
                    is_show: bool = True,  

                    # 只在数值轴中（type: 'value'）有效。  
                    # 是否是脱离 0 值比例。设置成 true 后坐标刻度不会强制包含零刻度。在双数值轴的散点图中比较有用。  
                    # 在设置 min 和 max 之后该配置项无效。  
                    is_scale: bool = False,  

                    # 是否反向坐标轴。  
                    is_inverse: bool = False,  

                    # 坐标轴名称显示位置。可选：  
                    # 'start', 'middle' 或者 'center','end'  
                    name_location: str = "end",  

                    # 坐标轴名称与轴线之间的距离。  
                    name_gap: Numeric = 15,  

                    # 坐标轴名字旋转，角度值。  
                    name_rotate: Optional[Numeric] = None,  

                    # 强制设置坐标轴分割间隔。  
                    # 因为 splitNumber 是预估的值，实际根据策略计算出来的刻度可能无法达到想要的效果，  
                    # 这时候可以使用 interval 配合 min、max 强制设定刻度划分，一般不建议使用。  
                    # 无法在类目轴中使用。在时间轴（type: 'time'）中需要传时间戳，在对数轴（type: 'log'）中需要传指数值。  
                    interval: Optional[Numeric] = None,  

                    # x 轴所在的 grid 的索引，默认位于第一个 grid。  
                    grid_index: Numeric = 0,  

                    # x 轴的位置。可选：  
                    # 'top', 'bottom'  
                    # 默认 grid 中的第一个 x 轴在 grid 的下方（'bottom'），第二个 x 轴视第一个 x 轴的位置放在另一侧。  
                    position: Optional[str] = None,  

                    # Y 轴相对于默认位置的偏移，在相同的 position 上有多个 Y 轴的时候有用。  
                    offset: Numeric = 0,  

                    # 坐标轴的分割段数，需要注意的是这个分割段数只是个预估值，最后实际显示的段数会在这个基础上根据分割后坐标轴刻度显示的易读程度作调整。   
                    # 默认值是 5  
                    split_number: Numeric = 5,  

                    # 坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样。  
                    # 类目轴中 boundaryGap 可以配置为 true 和 false。默认为 true，这时候刻度只是作为分隔线，  
                    # 标签和数据点都会在两个刻度之间的带(band)中间。  
                    # 非类目轴，包括时间，数值，对数轴，boundaryGap是一个两个值的数组，分别表示数据最小值和最大值的延伸范围  
                    # 可以直接设置数值或者相对的百分比，在设置 min 和 max 后无效。 示例：boundaryGap: ['20%', '20%']  
                    boundary_gap: Union[str, bool, None] = None,  

                    # 坐标轴刻度最小值。  
                    # 可以设置成特殊值 'dataMin'，此时取数据在该轴上的最小值作为最小刻度。  
                    # 不设置时会自动计算最小值保证坐标轴刻度的均匀分布。  
                    # 在类目轴中，也可以设置为类目的序数（如类目轴 data: ['类A', '类B', '类C'] 中，序数 2 表示 '类C'。  
                    # 也可以设置为负数，如 -3）。  
                    min_: Union[Numeric, str, None] = None,  

                    # 坐标轴刻度最大值。  
                    # 可以设置成特殊值 'dataMax'，此时取数据在该轴上的最大值作为最大刻度。  
                    # 不设置时会自动计算最大值保证坐标轴刻度的均匀分布。  
                    # 在类目轴中，也可以设置为类目的序数（如类目轴 data: ['类A', '类B', '类C'] 中，序数 2 表示 '类C'。  
                    # 也可以设置为负数，如 -3）。  
                    max_: Union[Numeric, str, None] = None,  

                    # 自动计算的坐标轴最小间隔大小。  
                    # 例如可以设置成1保证坐标轴分割刻度显示成整数。  
                    # 默认值是 0  
                    min_interval: Numeric = 0,  

                    # 自动计算的坐标轴最大间隔大小。  
                    # 例如，在时间轴（（type: 'time'））可以设置成 3600 * 24 * 1000 保证坐标轴分割刻度最大为一天。  
                    max_interval: Optional[Numeric] = None,  

                    # 坐标轴刻度线配置项，参考 `global_options.AxisLineOpts`  
                    axisline_opts: Union[AxisLineOpts, dict, None] = None,  

                    # 坐标轴刻度配置项，参考 `global_options.AxisTickOpts`  
                    axistick_opts: Union[AxisTickOpts, dict, None] = None,  

                    # 坐标轴标签配置项，参考 `series_options.LabelOpts`  
                    axislabel_opts: Union[LabelOpts, dict, None] = None,  

                    # 坐标轴指示器配置项，参考 `global_options.AxisPointerOpts`  
                    axispointer_opts: Union[AxisPointerOpts, dict, None] = None,  

                    # 坐标轴名称的文字样式，参考 `series_options.TextStyleOpts`  
                    name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,  

                    # 分割区域配置项，参考 `series_options.SplitAreaOpts`  
                    splitarea_opts: Union[SplitAreaOpts, dict, None] = None,  
                    输入True即可生成分割

                    # 分割线配置项，参考 `series_options.SplitLineOpts`  
                    splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(), """)
        elif '视觉' in help_type:
            print("set_VisualMap")
            print("""# 是否显示视觉映射配置  
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
                        textstyle_opts: Union[TextStyleOpts, dict, None] = None,  """)
        elif '滑块' in help_type:
            print("set_DataZoom")
            print("""# 是否显示 组件。如果设置为 false，不会显示，但是数据过滤的功能还存在。  
                        is_show: bool = True,  

                        # 组件类型，可选 "slider", "inside"  
                        type_: str = "slider",  

                        # 拖动时，是否实时更新系列的视图。如果设置为 false，则只在拖拽结束的时候更新。  
                        is_realtime: bool = True,  

                        # 数据窗口范围的起始百分比。范围是：0 ~ 100。表示 0% ~ 100%。  
                        range_start: Numeric = 20,  

                        # 数据窗口范围的结束百分比。范围是：0 ~ 100  
                        range_end: Numeric = 80,  

                        # 数据窗口范围的起始数值。如果设置了 start 则 startValue 失效。  
                        start_value: Union[int, str, None] = None,  

                        # 数据窗口范围的结束数值。如果设置了 end 则 endValue 失效。  
                        end_value: Union[int, str, None] = None,  

                        # 布局方式是横还是竖。不仅是布局方式，对于直角坐标系而言，也决定了，缺省情况控制横向数轴还是纵向数轴  
                        # 可选值为：'horizontal', 'vertical'  
                        orient: str = "horizontal",  

                        # 设置 dataZoom-inside 组件控制的 x 轴（即 xAxis，是直角坐标系中的概念，参见 grid）。  
                        # 不指定时，当 dataZoom-inside.orient 为 'horizontal'时，默认控制和 dataZoom 平行的第一个 xAxis  
                        # 如果是 number 表示控制一个轴，如果是 Array 表示控制多个轴。  
                        xaxis_index: Union[int, Sequence[int], None] = None,  

                        # 设置 dataZoom-inside 组件控制的 y 轴（即 yAxis，是直角坐标系中的概念，参见 grid）。  
                        # 不指定时，当 dataZoom-inside.orient 为 'horizontal'时，默认控制和 dataZoom 平行的第一个 yAxis  
                        # 如果是 number 表示控制一个轴，如果是 Array 表示控制多个轴。  
                        yaxis_index: Union[int, Sequence[int], None] = None,  

                        # 是否锁定选择区域（或叫做数据窗口）的大小。  
                        # 如果设置为 true 则锁定选择区域的大小，也就是说，只能平移，不能缩放。  
                        is_zoom_lock: bool = False,  

                        # dataZoom-slider 组件离容器左侧的距离。  
                        # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
                        # 也可以是 'left', 'center', 'right'。  
                        # 如果 left 的值为 'left', 'center', 'right'，组件会根据相应的位置自动对齐。  
                        pos_left: Optional[str] = None,  

                        # dataZoom-slider 组件离容器上侧的距离。  
                        # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，  
                        # 也可以是 'top', 'middle', 'bottom'。  
                        # 如果 top 的值为 'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。  
                        pos_top: Optional[str] = None,  

                        # dataZoom-slider 组件离容器右侧的距离。  
                        # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
                        # 默认自适应。  
                        pos_right: Optional[str] = None,  

                        # dataZoom-slider组件离容器下侧的距离。  
                        # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。  
                        # 默认自适应。  
                        pos_bottom: Optional[str] = None, """)
        elif '标签' in help_type:
            print("""# 是否显示标签。  
                    is_show: bool = True,  

                    # 标签的位置。可选  
                    # 'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight'  
                    # 'insideTop'，'insideBottom'， 'insideTopLeft'，'insideBottomLeft'  
                    # 'insideTopRight'，'insideBottomRight'  
                    position: Union[str, Sequence] = "top",  

                    # 文字的颜色。  
                    # 如果设置为 'auto'，则为视觉映射得到的颜色，如系列色。  
                    color: Optional[str] = None,  

                    # 文字的字体大小  
                    font_size: Numeric = 12,  

                    # 文字字体的风格，可选：  
                    # 'normal'，'italic'，'oblique'  
                    font_style: Optional[str] = None,  

                    # 文字字体的粗细，可选：  
                    # 'normal'，'bold'，'bolder'，'lighter'  
                    font_weight: Optional[str] = None,  

                    # 文字的字体系列  
                    # 还可以是 'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei', ...  
                    font_family: Optional[str] = None,  

                    # 标签旋转。从 -90 度到 90 度。正值是逆时针。  
                    rotate: Optional[Numeric] = None,  

                    # 刻度标签与轴线之间的距离。  
                    margin: Optional[Numeric] = 8,  

                    # 坐标轴刻度标签的显示间隔，在类目轴中有效。  
                    # 默认会采用标签不重叠的策略间隔显示标签。  
                    # 可以设置成 0 强制显示所有标签。  
                    # 如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推。  
                    # 可以用数值表示间隔的数据，也可以通过回调函数控制。回调函数格式如下：  
                    # (index:number, value: string) => boolean  
                    # 第一个参数是类目的 index，第二个值是类目名称，如果跳过则返回 false。  
                    interval: Union[Numeric, str, None]= None,  

                    # 文字水平对齐方式，默认自动。可选：  
                    # 'left'，'center'，'right'  
                    horizontal_align: Optional[str] = None,  

                    # 文字垂直对齐方式，默认自动。可选：  
                    # 'top'，'middle'，'bottom'  
                    vertical_align: Optional[str] = None,  

                    # 标签内容格式器，支持字符串模板和回调函数两种形式，字符串模板与回调函数返回的字符串均支持用 \n 换行。  
                    # 模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等。   
                    # 在 trigger 为 'axis' 的时候，会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2} 这种后面加索引的方式表示系列的索引。   
                    # 不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样。 其中变量{a}, {b}, {c}, {d}在不同图表类型下代表数据含义为：  

                    # 折线（区域）图、柱状（条形）图、K线图 : {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）  
                    # 散点图（气泡）图 : {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）  
                    # 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）  
                    # 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）  
                    # 示例：formatter: '{b}: {@score}'  
                    #   
                    # 回调函数，回调函数格式：  
                    # (params: Object|Array) => string  
                    # 参数 params 是 formatter 需要的单个数据集。格式如下：  
                    # {  
                    #    componentType: 'series',  
                    #    // 系列类型  
                    #    seriesType: string,  
                    #    // 系列在传入的 option.series 中的 index  
                    #    seriesIndex: number,  
                    #    // 系列名称  
                    #    seriesName: string,  
                    #    // 数据名，类目名  
                    #    name: string,  
                    #    // 数据在传入的 data 数组中的 index  
                    #    dataIndex: number,  
                    #    // 传入的原始数据项  
                    #    data: Object,  
                    #    // 传入的数据值  
                    #    value: number|Array,  
                    #    // 数据图形的颜色  
                    #    color: string,  
                    # }  
                    formatter: Optional[str] = None,  

                    # 在 rich 里面，可以自定义富文本样式。利用富文本样式，可以在标签中做出非常丰富的效果  
                    # 具体配置可以参考一下 https://www.echartsjs.com/tutorial.html#%E5%AF%8C%E6%96%87%E6%9C%AC%E6%A0%87%E7%AD%BE  
                    rich: Optional[dict] = None,  """)
        elif 'line' in help_type:
            print("""# 是否显示  
                    is_show: bool = True,  

                    # 线宽。  
                    width: Numeric = 1,  

                    # 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。  
                    opacity: Numeric = 1,  

                    # 线的弯曲度，0 表示完全不弯曲  
                    curve: Numeric = 0,  

                    # 线的类型。可选：  
                    # 'solid', 'dashed', 'dotted'  
                    type_: str = "solid",  

                    # 线的颜色。  
                    # 颜色可以使用 RGB 表示，比如 'rgb(128, 128, 128)'，如果想要加上 alpha 通道表示不透明度，  
                    # 可以使用 RGBA，比如 'rgba(128, 128, 128, 0.5)'，也可以使用十六进制格式，比如 '#ccc'。  
                    # 除了纯色之外颜色也支持渐变色和纹理填充  
                    #   
                    # 线性渐变，前四个参数分别是 x0, y0, x2, y2, 范围从 0 - 1，相当于在图形包围盒中的百分比，  
                    # 如果 globalCoord 为 `true`，则该四个值是绝对的像素位置  
                    # color: {  
                    #    type: 'linear',  
                    #    x: 0,  
                    #    y: 0,  
                    #    x2: 0,  
                    #    y2: 1,  
                    #    colorStops: [{  
                    #        offset: 0, color: 'red' // 0% 处的颜色  
                    #    }, {  
                    #        offset: 1, color: 'blue' // 100% 处的颜色  
                    #    }],  
                    #    global: false // 缺省为 false  
                    # }  
                    #   
                    # 径向渐变，前三个参数分别是圆心 x, y 和半径，取值同线性渐变  
                    # color: {  
                    #    type: 'radial',  
                    #    x: 0.5,  
                    #    y: 0.5,  
                    #    r: 0.5,  
                    #    colorStops: [{  
                    #        offset: 0, color: 'red' // 0% 处的颜色  
                    #    }, {  
                    #        offset: 1, color: 'blue' // 100% 处的颜色  
                    #    }],  
                    #    global: false // 缺省为 false  
                    # }  
                    #   
                    # 纹理填充  
                    # color: {  
                    #    image: imageDom, // 支持为 HTMLImageElement, HTMLCanvasElement，不支持路径字符串  
                    #    repeat: 'repeat' // 是否平铺, 可以是 'repeat-x', 'repeat-y', 'no-repeat'  
                    # }  
                    color: Union[str, Sequence, None] = None,  """)
        elif '标记点' in help_type or 'MarkPoint' in help_type:
            print("""class MarkPointOpts(  
                    # 标记点数据，参考 `series_options.MarkPointItem`  
                    data: Sequence[Union[MarkPointItem, dict]] = None,  

                    # 标记的图形。  
                    # ECharts 提供的标记类型包括 'circle'圆形, 'rect'方形, 'roundRect'圆角方形, 'triangle'三角形,   
                    # 'diamond'棱形, 'pin'提示, 'arrow'箭头, 'none'  
                    # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。  
                    symbol: Optional[str] = None,  

                    # 标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，  
                    # 例如 [20, 10] 表示标记宽为 20，高为 10。  
                    # 如果需要每个数据的图形大小不一样，可以设置为如下格式的回调函数：  
                    # (value: Array|number, params: Object) => number|Array  
                    # 其中第一个参数 value 为 data 中的数据值。第二个参数 params 是其它的数据项参数。  
                    symbol_size: Union[None, Numeric] = None,  

                    # 标签配置项，参考 `series_options.LabelOpts`  
                    label_opts: LabelOpts = LabelOpts(position="inside", color="#fff"),  
                )""")
            print("""class MarkPointItem(  
                # 标注名称。  
                name: Optional[str] = None,  

                # 特殊的标注类型，用于标注最大值最小值等。可选:  
                # 'min' 最大值。  
                # 'max' 最大值。  
                # 'average' 平均值。  
                type_: Optional[str] = None,  

                # 在使用 type 时有效，用于指定在哪个维度上指定最大值最小值，可以是   
                # 0（xAxis, radiusAxis），  
                # 1（yAxis, angleAxis），默认使用第一个数值轴所在的维度。  
                value_index: Optional[Numeric] = None,  

                # 在使用 type 时有效，用于指定在哪个维度上指定最大值最小值。这可以是维度的直接名称，  
                # 例如折线图时可以是 x、angle 等、candlestick 图时可以是 open、close 等维度名称。  
                value_dim: Optional[str] = None,  

                # 标注的坐标。坐标格式视系列的坐标系而定，可以是直角坐标系上的 x, y，  
                # 也可以是极坐标系上的 radius, angle。例如 [121, 2323]、['aa', 998]。  
                coord: Optional[Sequence] = None,  

                # 相对容器的屏幕 x 坐标，单位像素。  
                x: Optional[Numeric] = None,  

                # 相对容器的屏幕 y 坐标，单位像素。  
                y: Optional[Numeric] = None,  

                # 标注值，可以不设。  
                value: Optional[Numeric] = None,  

                # 标记的图形。  
                # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle',   
                # 'diamond', 'pin', 'arrow', 'none'  
                # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。  
                symbol: Optional[str] = None,  

                # 标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，  
                # 例如 [20, 10] 表示标记宽为 20，高为 10。  
                symbol_size: Union[Numeric, Sequence] = None,  

                # 标记点样式配置项，参考 `series_options.ItemStyleOpts`  
                itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,  
            )""")
        elif '标记线' in help_type or 'MarkLine' in help_type:
            print("""class MarkLineOpts(  
                    # 图形是否不响应和触发鼠标事件，默认为 false，即响应和触发鼠标事件。  
                    is_silent: bool = False,  

                    # 标记线数据，参考 `series_options.MarkLineItem`  
                    data: Sequence[Union[MarkLineItem, dict]] = None,  

                    # 标线两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定，具体格式见 data.symbol。  
                    symbol: Optional[str] = None,  

                    # 标线两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。  
                    symbol_size: Union[None, Numeric] = None,  

                    # 标线数值的精度，在显示平均值线的时候有用。  
                    precision: int = 2,  

                    # 标签配置项，参考 `series_options.LabelOpts`  
                    label_opts: LabelOpts = LabelOpts(),  

                    # 标记线样式配置项，参考 `series_options.LineStyleOpts`  
                    linestyle_opts: Union[LineStyleOpts, dict, None] = None,  
                )""")
            print("""class MarkLineItem(  
                    # 标注名称。  
                    name: Optional[str] = None,  

                    # 特殊的标注类型，用于标注最大值最小值等。可选:  
                    # 'min' 最大值。  
                    # 'max' 最大值。  
                    # 'average' 平均值。  
                    type_: Optional[str] = None,  

                    # 相对容器的屏幕 x 坐标，单位像素。  
                    x: Union[str, Numeric, None] = None,  

                    # 相对容器的屏幕 y 坐标，单位像素。  
                    y: Union[str, Numeric, None] = None,  

                    # 在使用 type 时有效，用于指定在哪个维度上指定最大值最小值，可以是   
                    # 0（xAxis, radiusAxis），  
                    # 1（yAxis, angleAxis），默认使用第一个数值轴所在的维度。  
                    value_index: Optional[Numeric] = None,  

                    # 在使用 type 时有效，用于指定在哪个维度上指定最大值最小值。这可以是维度的直接名称，  
                    # 例如折线图时可以是 x、angle 等、candlestick 图时可以是 open、close 等维度名称。  
                    value_dim: Optional[str] = None,  

                    # 起点或终点的坐标。坐标格式视系列的坐标系而定，可以是直角坐标系上的 x, y，  
                    # 也可以是极坐标系上的 radius, angle。  
                    coord: Optional[Sequence] = None,  

                    # 终点标记的图形。  
                    # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle',  
                    #  'diamond', 'pin', 'arrow', 'none'  
                    # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。  
                    symbol: Optional[str] = None,  

                    # 标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，  
                    # 例如 [20, 10] 表示标记宽为 20，高为 10。  
                    symbol_size: Optional[Numeric] = None,  
                )""")
        elif '标记区域' in help_type or 'MarkArea' in help_type:
            print("""class MarkAreaItem(  
                    # 区域名称, 仅仅就是一个名称而已  
                    name: Optional[str] = None,  

                    # 特殊的标注类型，用于标注最大值最小值等。  
                    # 'min' 最大值。  
                    # 'max' 最大值。  
                    # 'average' 平均值。  
                    type_: Sequence[Optional[str], Optional[str]] = (None, None),  

                    # 在使用 type 时有效，用于指定在哪个维度上指定最大值最小值，可以是 0（xAxis, radiusAxis），1（yAxis, angleAxis）。  
                    # 默认使用第一个数值轴所在的维度。  
                    value_index: Sequence[Optional[Numeric], Optional[Numeric]] = (None, None),  

                    # 在使用 type 时有效，用于指定在哪个维度上指定最大值最小值。  
                    # 这可以是维度的直接名称，例如折线图时可以是 x、angle 等、candlestick 图时可以是 open、close 等维度名称。  
                    value_dim: Sequence[Optional[str], Optional[str]] = (None, None),  

                    # 相对容器的屏幕 x 坐标，单位像素，支持百分比形式，例如 '20%'。  
                    x: Sequence[Union[str, Numeric, None], Union[str, Numeric, None]] = (None, None),  

                    # 相对容器的屏幕 y 坐标，单位像素，支持百分比形式，例如 '20%'。  
                    y: Sequence[Union[str, Numeric, None], Union[str, Numeric, None]] = (None, None),  

                    # 标签配置项，参考 `series_options.LabelOpts`  
                    label_opts: Union[LabelOpts, dict, None] = None,  

                    # 该数据项区域的样式，起点和终点项的 itemStyle 会合并到一起。参考 `series_options.ItemStyleOpts`  
                    itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,  
                )""")
            print("""class MarkAreaOpts(  
                    # 图形是否不响应和触发鼠标事件，默认为 False，即响应和触发鼠标事件。  
                    is_silent: bool = False,  

                    # 标签配置项，参考 `series_options.LabelOpts`  
                    label_opts: LabelOpts = LabelOpts(),  

                    # 标记区域数据，参考 `series_options.MarkAreaItem`  
                    data: Sequence[Union[MarkAreaItem, dict]] = None,  
                )""")
```

