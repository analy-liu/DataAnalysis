---
title:  python-环境配置
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# python环境配置

换电脑是一件麻烦的事情，每次配置环境都需要各种查资料，本篇文章记录一下python环境配置的过程，方便以后换电脑时查看，快速把环境搭建起来。

## anaconda安装与常用命令

### 1. 安装

Anaconda 主要用于管理包，安装运行升级管理都很方便，本篇只介绍windows下的安装

1. 下载安装包
   清华源：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
   官网：https://www.anaconda.com/ （官网已经需要付费了）
2. 安装过程注意
   1. 打开安装包>> next >> I agree 
   2. just ME 和 All Users 都可以（最好选All users)
   3. 安装路径最好在某个盘下新建一个Anaconda文件夹，例如D:\Anaconda
   4. 不勾选Add PATH 环境变量后面自己加，选resigter python 
   5. 安装过程中弹出cmd 不要关掉，等待完成
   6. skip
   7. 两个Learn都不选，点击finish结束
3. 环境变量配置
   此电脑-属性-高级系统设置-环境变量-系统变量-新建
   1. D:\Anaconda
   2. D:\Anaconda\Scripts
4. 检查是否安装成功
   1. 打开Anaconda Prompt
   2. 输入conda --version，出现版本号即为成功

### 2. 安装升级包

安装包时，最好关闭网络代理，并且关掉防火墙

有时安装包比较老旧，需要对包升级一下  
update 和 upgrade 都可以互换试试

conda命令
```
# 升级conda(升级Anaconda前需要先升级conda)
conda update conda
conda update --force conda
conda update -n base conda -c conda-forge
# 升级anaconda
conda update anaconda
# 升级spyder
conda update spyder

# 更新所有包（二选一）
conda update --all
conda upgrade --all
# 搜索包：conda search [package]
conda search matplotlib
# 安装包
conda install package
conda install -c conda-forge package
# 更新包
conda update package
# 查看现有包版本
conda list

# 添加国内镜像源
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
# 设置启动设置好的国内镜像源
conda config --set show_channel_urls yes
# 查看添加的镜像
conda config --get channelsconda config --get channels
# 查看是否添加上了源
conda config --show channels
# 添加镜像源后，清除索引缓存，确保用的是镜像站提供的索引
conda clean -i
# 删除指定镜像源：conda config --remove channels [channel]
conda config --remove channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --remove channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
# 删除所有镜像并恢复默认镜像
conda config --remove-key channels

# SSL与代理
# 设置不通过代理
conda config --set ssl_verify no
conda config --set ssl_verify false
```
pip命令
```
# 查看版本
pip --version
# 升级
python -m pip install --upgrade pip

# 列出当前环境下安装的包, 非常常用
pip list  

# 实验过程中，如果发现某些包没有，直接安装
pip install package_name  # 也可以带版本号

# 如果发现装错版本了，想要卸载掉包
pip uninstall package_name  

# 更新包
conda update package_name
```

### 3. 管理虚拟环境env

```
# 查看已经有的虚拟环境 常用
conda env list

# 新建虚拟环境 可以指定python版本和一些包的版本
conda create -n env_names package_names   
# conda create -n tfenv python=3.8

# 进入虚拟环境,这时候面临着对一些包的操作，就是上面包的相关命令了
activate tfenv

# 离开虚拟环境
conda deactivate

# 删除虚拟环境
conda env remove -n env_name

# 共享环境
## conda
conda env export > environment.yaml # 导出环境
conda env update -f=/path/to/environment.yaml # 导入环境
## pip
pip freeze > requirements.txt  # 导出环境
pip install -r /path/requirements.txt # 导入环境
```

### 4.数据挖掘常用包安装

```
conda install pandas # 自动会安装好依赖包，例如numpy
conda install scikit-learn
conda install mat
```

## jupyter配置 

jupyter主要是插件配置，让jupyter更好用

```
# 共3个插件需要安装
 
1.安装 nbextensions
pip install jupyter_contrib_nbextensions
conda install -c conda-forge jupyter_contrib_nbextensions
 
2.安装 javascript and css files
jupyter contrib nbextension install --user
 
3.安装 configurator
pip install jupyter_nbextensions_configurator
conda install -c conda-forge jupyter_nbextensions_configurator

```

### 错误解决

如果遇到类似 
```
ERROR: Cannot uninstall 'terminado'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall. 
```
这样的报错信息，执行下面的语句
```
pip install terminado --ignore-installed
```

如果jupyter首页为正常，打开ipynb文件报错500，尝试下面代码
pip install --upgrade nbconvert