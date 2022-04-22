# 了解SQL
## 学习SQL三个层次目标
1. 熟悉基本的增删改查语句及函数，包括select、where、group by、having、order by、delete、insert、join、update等，可以做日常的取数或简单的分析（该水平已经超过90%非IT同事）;
2. 掌握并熟练使用高阶语法，比如集合、分组聚合、子查询、条件逻辑、字符串函数、算术函数、日期时间函数，并且知道MySQL、Oracle、SQL Server等数据库的语法差异；
3. 熟悉如何优化SQL语句，以期达到最高查询效率，了解事务、锁、索引、约束、视图、元数据等概念，并且学会使用hive sql、spark sql、pymysql等工具；

## SQL简介

SQL，全称Structured Query Language，即结构化查询语句，它的主要作用是设计，创建和管理关系数据库，**关系数据库**的表是类似excel的二维表，由行列组成，每列代表一个字段。换句话说，SQL是用于与关系数据库进行通信的编程语言。

关系数据库有很多，比如Oracle把自己扩展的SQL称为PL/SQL，Microsoft把自己扩展的SQL称为T-SQL等，每个数据库都使用自己的SQL方言，但是它们都共享相同的基本语法。

## SQL的能力
DDL：Data Definition Language

DDL允许用户定义数据，也就是创建表、删除表、修改表结构这些操作。通常，DDL由数据库管理员执行。

DML：Data Manipulation Language

DML为用户提供添加、删除、更新数据的能力，这些是应用程序对数据库的日常操作。

DQL：Data Query Language

DQL允许用户查询数据，这也是通常最频繁的数据库日常操作。

# MySQL

## MySQL介绍
安装完MySQL后，除了MySQL Server，即真正的MySQL服务器外，还附赠一个MySQL Client程序。MySQL Client是一个命令行客户端，可以通过MySQL Client登录MySQL，然后，输入SQL语句并执行。

MySQL Client的可执行程序是mysql，MySQL Server的可执行程序是mysqld。

在MySQL Client中输入的SQL语句通过TCP连接发送到MySQL Server。默认端口号是3306，即如果发送到本机MySQL Server，地址就是127.0.0.1:3306。

也可以只安装MySQL Client，然后连接到远程MySQL Server。假设远程MySQL Server的IP地址是10.0.1.99，那么就使用-h指定IP或域名：
## 打开MySQL客户端
安装完成后，打开cmd，输入mysql -u root -p后输入密码。  
命令行程序mysql实际上是MySQL客户端，真正的MySQL服务器程序是mysqld，在后台运行。

## 使用操作
以下操作在cmd中运行
```cmd
# 登录操作
>mysql -u root -p
Enter password

# 提示符
mysql> # 准备好接受新的命令。
-> # 等待多行的下一行，或等待以分号（;）结束。
'> # 等待多行的下一行，或等待以单引号（'）结束。
"> # 等待多行的下一行，或等待以双引号（"）结束。
`> # 等待多行的下一行，或等待以反斜点（`）结束。
/*> # 等待多行的下一行，或等待以注释终止符（*/）结束。
```