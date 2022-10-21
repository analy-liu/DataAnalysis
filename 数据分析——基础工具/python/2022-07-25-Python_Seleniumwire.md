---
title:  seleniumwire爬虫
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/07/05/Python_Index.html)

# selenium使用

准备工作：
1. 安装：pip install selenium
2. 下载浏览器驱动
  Firefox浏览器驱动：[geckodriver](https://github.com/mozilla/geckodriver/releases)  
  Chrome浏览器驱动：[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home) 需要开全局代理、[taobao镜像](http://npm.taobao.org/mirrors/chromedriver/)  
  IE浏览器驱动：[IEDriverServer](http://selenium-release.storage.googleapis.com/index.html)  
  Edge浏览器驱动：[MicrosoftWebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver)  
  Opera浏览器驱动：[operadriver](https://github.com/operasoftware/operachromiumdriver/releases)  
  PhantomJS浏览器驱动：[phantomjs](http://phantomjs.org/)  
3. 设置环境变量

## 1. 基本操作

```python
from selenium import webdriver
# 打开浏览器
driver = webdriver.Edge(executable_path='MicrosoftWebDriver位置')

# 打开目标网页
target_url = ""
driver.get(target_url)

# 页面操作
driver.set_window_size(480, 800) # 页面大小
driver.back()# 后退 
driver.forward()# 前进 
driver.refresh() # 刷新
driver.save_screenshot("保存位置")# 页面截图

# 寻找元素
element = driver.find_element_by_xpath("")
# function
find_element_by_id()
find_element_by_name()
find_element_by_class_name()
find_element_by_tag_name()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_xpath()
find_element_by_css_selector()
find_elements_by...()

# 元素操作
element.click()# 点击元素
element.clear() # 清除文本
element.send_keys('')# 在元素中输入
element.screenshot('保存位置')# 元素截图
element.send_keys('').submit()# 输入并回车提交
element.send_keys('D:\\upload_file.txt')# 文件上传

# 元素判断
element.is_displayed()# 判断元素用户是否可见
element.is_enabled()# 元素是否可以点击
EC.presence_of_element_located((By.ID,"kw"))   #查看某个元素是否存在
EC.element_to_be_clickable()         #查看元素是否可点击
EC.element_located_to_be_selected((By.ID,"kw")) #某个预期元素是否被选中
element.get_attribute(name)# 获得属性值
element.text # 获取元素的文本
element.size # 获取元素的尺寸

# 键盘操作
send_keys(Keys.BACK_SPACE) #删除键（BackSpace）
send_keys(Keys.SPACE) #空格键(Space)
send_keys(Keys.TAB) #制表键(Tab)
send_keys(Keys.ESCAPE) #回退键（Esc）
send_keys(Keys.ENTER) #回车键（Enter）
send_keys(Keys.CONTROL,'a') #全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') #复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') #剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') #粘贴（Ctrl+V）
send_keys(Keys.F1) #键盘 F1
# ……
send_keys(Keys.F12) #键盘 F12

# 鼠标操作
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element_by_link_text("设置")# 设置元素
ActionChains(driver).move_to_element(element).perform()# 悬停操作
# function
perform()# 执行所有 ActionChains 中存储的行为；
context_click()# 右击；
double_click()# 双击；
drag_and_drop()# 拖动；
move_to_element()# 鼠标悬停。

# 关闭浏览器
driver.close()
```

## 2. 页面等待

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
element = WebDriverWait(driver, 5, 0.5).until(
                      EC.presence_of_element_located((By.ID, "kw"))
                      )
```
**函数**

```python
WebDriverWait(
    driver, # 浏览器驱动。
    timeout, # 最长超时时间，默认以秒为单位。
    poll_frequency=0.5, # 检测的间隔（步长）时间，默认为0.5S。
    ignored_exceptions=None # 超时后的异常信息，默认情况下抛NoSuchElementException异常。
    )
"""
WebDriverWait()一般由until()或until_not()方法配合使用，
下面是until()和until_not()方法的说明。
"""
until(method, message=‘’) # 调用该方法提供的驱动程序作为一个参数，直到返回值为True。
until_not(method, message=‘’) # 调用该方法提供的驱动程序作为一个参数，直到返回值为False。
```

**应用**

```python
WebDriverWait(driver,10).until(EC.title_is(u"百度一下，你就知道"))
# 判断title,返回布尔值

WebDriverWait(driver,10).until(EC.title_contains(u"百度一下"))
# 判断title，返回布尔值

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
# 判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'su')))
# 判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0

WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')))
# 判断元素是否可见，如果可见就返回这个元素

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
# 判断是否至少有1个元素存在于dom树中，如果定位到就返回列表

WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.mnav')))
# 判断是否至少有一个元素在页面中可见，如果定位到就返回列表

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='u1']/a[8]"),u'设置'))
# 判断指定的元素中是否包含了预期的字符串，返回布尔值

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#su'),u'百度一下'))
# 判断指定元素的属性值中是否包含了预期的字符串，返回布尔值

#WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
#  判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False注意这里并没有一个frame可以切换进去

WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#swfEveryCookieWrap')))
# 判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素注意#swfEveryCookieWrap在此页面中是一个隐藏的元素

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='u1']/a[8]"))).click()
# 判断某个元素中是否可见并且是enable的，代表可点击
driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()

WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element(By.ID,'su')))
# 等待某个元素从dom树中移除

WebDriverWait(driver,10).until(EC.element_to_be_selected(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]")))
# 判断某个元素是否被选中了,一般用在下拉列表

WebDriverWait(driver,10).until(EC.element_selection_state_to_be(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]"),True))
# 判断某个元素的选中状态是否符合预期

WebDriverWait(driver,10).until(EC.element_located_selection_state_to_be((By.XPATH,"//*[@id='nr']/option[1]"),True))
# 判断某个元素的选中状态是否符合预期
driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()

instance = WebDriverWait(driver,10).until(EC.alert_is_present())
# 判断页面上是否存在alert,如果有就切换到alert并返回alert的内容
instance.accept()
# 关闭弹窗
```

## 3. 警告框处理

```python
alert = driver.switch_to_alert()
```

text：返回 alert/confirm/prompt 中的文字信息。  
accept()：接受现有警告框。  
dismiss()：解散现有警告框。  
send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。  

### 下拉框选择

```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('50')  # 显示50条
```

## 4. cookie操作

**selenium**

```python
#WebDriver操作cookie的方法：

driver.get_cookies() #获得所有cookie信息。
driver.get_cookie(name)# 返回字典的key为“name”的cookie信息。
driver.add_cookie(cookie_dict) # 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。
driver.delete_cookie(name,optionsString)# 删除cookie信息。“name”是要删除的driver.cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。
driver.delete_all_cookies()# 删除所有cookie信息

# 使用cookie登录
for item in cookies:
    driver.add_cookie(item)
```

**seleniumwire**

seleniumwire有requests函数，可以获取用selenium获取不到的返回值

```python
# 输出指定cookie
for i in driver.requests:
    try:
        if i.headers['Host'] in host and 'SESSION' in i.headers['Cookie']:
            cookie = i.headers['Cookie']
            cookie = re.findall(r'(SESSION.*(?=;))', cookie)[0]
            self.cookies[i.headers['Host']] = cookie
```

## 5. 设置无界面

```python
from selenium import webdriver # 模拟登录
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"D:\chrome\chromedriver.exe", chrome_options=chrome_options)
```