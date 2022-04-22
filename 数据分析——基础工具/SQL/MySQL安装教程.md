# 下载MySQL
* https://dev.mysql.com/downloads/mysql/ 
这个是压缩包   
下载第一个，解压后需要配置

* https://dev.mysql.com/downloads/installer/
这个是安装包  
下载第二个，第一个是在线安装，第二个是离线安装。  


# 安装MySQL

1. 打开安装包
2. Choosing a Setup Type: 选择Server only (只安装MySQL),点击next
3. Check Requirements: 点击需要安装的版本，如果显示需要安装Microsoft Visual C++ 2019 Redistributable Package (x64)，则先点击Execute，安装完对应需求后点击next
4. instalation: 点击Execute，安装完成后点击next
5. Product Configuration: 点击next
6. Type and Networking: 默认，点击next。如果3306端口被占用，打开cmd，输入netstat -ano|findstr "3306"后回车，记住PID，打开任务管理器选择“服务”，找到对应进程关闭后即可继续安装。
7. Authentication Method: 选择第二个，点击next
8. Accounts and Roles: 设置密码，需要牢记，登陆用户名是root
9. Windows Service: 选择是否开机自启，用户名可以修改，点击next
10. Apply Configuration: 点击next，应用前面的设置，安装完后点Finish
11. Product Configuration: 点击next
12. Finish

# 配置环境变量

1. 右键我的电脑->属性->高级系统设置->环境变量
2. 选择系统变量中的Path，编辑->新建，把MySQL安装目录放入后保存，例如“C:\Program Files\MySQL\MySQL Server 8.0\bin”

# 测试

打开cmd，输入mysql -u root -p  
输入密码后显示welcome to MySQL, 并有具体版本号

# 异常处理
## win10中MySQL出现 ERROR 1045 (28000): Access denied for user 'root'@'localhost'
1. 用管理员权限打开cmd，输入net stop mysql
2. 删除mysql文件夹中的data文件夹
3. 在MySQL安装目录的 bin 目录下执行命令mysqld --initialize --console
4. 输出结果中有 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: password 记住password
5. 之后输入mysql -u root -p登录
6. 修改初始密码alter user 'root'@'localhost' identified by 'youpassword';
参考连接：https://blog.csdn.net/BigData_Mining/article/details/104539934
# 参考链接
https://zhuanlan.zhihu.com/p/37152572
https://blog.csdn.net/zhouzezhou/article/details/52446608

