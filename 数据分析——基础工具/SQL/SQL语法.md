 # SQL语法
- [SQL语法](#sql语法)
  - [1. 关系模型](#1-关系模型)
    - [1.1. 主键](#11-主键)
    - [1.2. 外键](#12-外键)
    - [1.3. 索引](#13-索引)
  - [2. MySQL基础](#2-mysql基础)
    - [2.1. 数据库](#21-数据库)
    - [2.2. 表](#22-表)
    - [2.3. 数据类型与新建变量](#23-数据类型与新建变量)
    - [2.4. 内置函数（未完善）](#24-内置函数未完善)
    - [2.5. 窗口函数(未完善)](#25-窗口函数未完善)
    - [2.6. 自定义函数（未完善）](#26-自定义函数未完善)
  - [3. 查找数据](#3-查找数据)
    - [3.1. 基本查询](#31-基本查询)
    - [3.2. 投影查询(筛选列) SELECT与 去重DISTINCT](#32-投影查询筛选列-select与-去重distinct)
    - [3.3. 先过滤数据(筛选行) WHERE](#33-先过滤数据筛选行-where)
    - [3.4. 后过滤数据HAVING](#34-后过滤数据having)
    - [3.5. 聚合查询与分组GROUP BY](#35-聚合查询与分组group-by)
    - [3.6. 排序 ORDER BY](#36-排序-order-by)
    - [3.7. 多表查询](#37-多表查询)
      - [3.7.1. 笛卡尔查询](#371-笛卡尔查询)
      - [3.7.2. 连接查询 JOIN](#372-连接查询-join)
    - [3.8. 分页 LIMIT OFFSET](#38-分页-limit-offset)
    - [3.9. 综合查询(综合使用以上方法)](#39-综合查询综合使用以上方法)
    - [3.10. 查询思路](#310-查询思路)
  - [4. 修改数据](#4-修改数据)
    - [4.1. 增加数据 INSERT INTO](#41-增加数据-insert-into)
    - [4.2. 修改数据 UPDATE](#42-修改数据-update)
    - [4.3. 删除数据 DELETE](#43-删除数据-delete)
  - [5. 常见问题](#5-常见问题)
## 1. 关系模型

关系数据库是建立在关系模型上的。而关系模型本质上就是若干个存储数据的二维表，可以把它们看作很多Excel表。

表的每一行称为记录（Record），记录是一个逻辑意义上的数据。  
表的每一列称为字段（Column），同一个表的每一行记录都拥有相同的若干字段。

**NULL**：  
字段定义了数据类型（整型、浮点型、字符串、日期等），以及是否允许为NULL。注意NULL表示字段数据不存在。一个整型字段如果为NULL不表示它的值为0，同样的，一个字符串型字段为NULL也不表示它的值为空串''。  
通常情况下，字段应该避免允许为NULL。不允许为NULL可以简化查询条件，加快查询速度，也利于应用程序读取数据后无需判断是否为NULL。

**表之间的关系**：  
和Excel表有所不同的是，关系数据库的表和表之间需要建立“一对多”，“多对一”和“一对一”的关系，这样才能够按照应用程序的逻辑来组织和存储数据。

“一对多”：班级表对学生表，每个班级对应多个学生  
“多对一”：学生表对班级表，多个学生对应一个班级  
“一对一”：班级表对教师表，一个班级对应一个班主任  

### 1.1. 主键
**主键**：一张表中能**区分**不同记录（行）的字段（列），例如ID  
**联合主键**：两个或更多的字段都设置为主键，允许一列有重复，只要不是所有主键列都重复即可。**尽量不使用联合主键**，会使关系表复杂度上升。

**选主键的原则**：不使用任何业务相关的字段作为主键。主键最好不要再修改，修改会造成一系列的影响。  
**常见主键**：ID。  
**可作为ID的类型**：自增整数类型、全局唯一GUID类型  

### 1.2. 外键
**主要内容**：关系数据库通过外键可以实现一对多、多对多和一对一的关系。外键既可以通过数据库来约束，也可以不设置约束，仅依靠应用程序的逻辑来保证。

**外键**：在一张表中能**关联**另一张表的字段（列），一般是关联另一张表的主键  

**外键约束**：  
通过定义外键约束，关系数据库可以保证无法插入无效的数据。  
即如果classes表不存在id=99的记录，students表就无法插入class_id=99的记录。  
外键约束会降低数据库的性能，可不设置外键约束，依靠应用程序自身保证逻辑的正确性。

**外键约束的实现与删除**：  
```SQL
# 实现
ALTER TABLE students #(需要定义外键的表)
ADD CONSTRAINT fk_class_id #(外键的约束名称)
FOREIGN KEY (class_id) #(外键的列明)
REFERENCES classes (id); #(关联到classes表中的id字段)
# 删除
ALTER TABLE students
DROP FOREIGN KEY fk_class_id;
```
**一对多**：  
通过一个表的外键关联到另一个表，我们可以定义出一对多关系
**多对多**：  
多对多关系实际上是通过两个一对多关系实现的，即通过一个中间表，关联两个一对多关系，就形成了多对多关系。  
**一对一**：  
一对一关系是指，一个表的记录对应到另一个表的唯一一个记录。  
多用于存储可能有缺失值的字段，也用于将经常读取和不经常读取的字段分开，提升性能。

### 1.3. 索引
**索引**：索引是关系数据库中对某一列或多个列的值进行预排序的数据结构。  
通过使用索引，可以让数据库系统不必扫描整个表，而是直接定位到符合条件的记录，这样就大大加快了查询速度。

**主要内容**：
通过对数据库表创建索引，可以提高查询速度。

通过创建唯一索引，可以保证某一列的值具有唯一性。

数据库索引对于用户和应用程序来说都是透明的。

**添加索引**：
```SQL
-- 创建索引
CREATE INDEX index_name
ON table_name (column_name)

-- 增加索引
ALTER TABLE students

ADD INDEX idx_score (score);
# 将students表里的score创建为名为idx_score的索引

ADD UNIQUE INDEX uni_name (name);
# 将name添加为唯一索引

ADD CONSTRAINT uni_name UNIQUE (name);
# 对name添加唯一约束，但不创建唯一索引

-- 删除索引
ALTER TABLE table_name DROP INDEX index_name # MySQL中
DROP INDEX index_name # DB2/Oracle中
```
可以对一张表创建多个索引。索引的优点是提高了查询效率，缺点是在插入、更新和删除记录时，需要同时修改索引，因此，索引越多，插入、更新和删除记录的速度就越慢。  
对于主键，关系数据库会**自动对其创建主键索引**。使用主键索引的效率是最高的，因为主键会保证绝对唯一。
## 2. MySQL基础

### 2.1. 数据库
```SQL
-- 查看数据库
SHOW DATABASE;
-- 创建新数据库
CREATE DATABASE dbname;
CREATE DATABASE IF NOT EXISTS test;

-- 修改数据库
ALTER DATABASE - 修改数据库

-- 删除数据库
DROP DATABASE database_name
```
### 2.2. 表
```SQL
-- 查看表
show tables;
-- 创建新表
CREATE TABLE table_name
(
id BIGINT NOT NULL AUTO_INCREMENT, # 自增加
column_name2 data_type(size) constraint_name,# 增加约束
column_name3 data_type(size),
....
PRIMARY KEY (id) # 设置主键
)ENGINE=InnoDB DEFAULT CHARSET=utf8; # 编码

-- 变更（改变）数据库表
ALTER TABLE table_name
-- 增加列
ADD column_name data_type
-- 删除列
DROP COLUMN column_name
-- 修改列的数据类型
MODIFY COLUMN column_name datatype

-- 约束
NOT NULL - 指示某列不能存储 NULL 值。
UNIQUE - 保证某列的每行必须有唯一的值。
PRIMARY KEY - NOT NULL 和 UNIQUE 的结合。确保某列（或两个列多个列的结合）有唯一标识，有助于更容易更快速地找到表中的一个特定的记录。
FOREIGN KEY - 保证一个表中的数据匹配另一个表中的值的参照完整性。
CHECK - 保证列中的值符合指定的条件。
DEFAULT - 规定没有给列赋值时的默认值。

-- 清空表数据，但不删除表
TRUNCATE TABLE table_name
-- 删除表
DROP TABLE table_name
```
### 2.3. 数据类型与新建变量
主要数据类型
|类型|用途|格式|
|:-|:-|:-|
|INT|整数||
|FLOAT|单精度浮点数值||
|DOUBLE|双精度浮点数值||
|DATE|日期值|YYYY-MM-DD|
|TIME|时间值或持续时间|HH:MM:SS|
|YEAR|年份值|YYYY|
|DATETIME|混合日期和时间值|YYYY-MM-DD HH:MM:SS|
|TIMESTAMP|混合日期和时间值，时间戳|YYYYMMDD HHMMSS|
|VARCHAR|变长字符串||
|BLOB|二进制形式的长文本数据||
|TEXT|长文本数据||

```SQL
-- 声明变量类型
declare m INT;
-- 设置变量值
set m=N-1; 
```
### 2.4. 内置函数（未完善）
1. 条件判断

|函数|描述|用法|
|:-|:-|:-|
|if(expr,true,false)|满足expr，返回ture的值，否则返回false的值||
|ifnull(v1,v2)|如果v1的值不位NULL，则返回v1，否则返回v2||
```SQL
-- CASE表示函数开始，END表示函数结束
CASE 
　　WHEN e1
　　THEN v1
　　WHEN e2
　　THEN e2
　　...
　　ELSE vn
END
-- 有一个成立后，后面的都不执行了
```
2. 数学函数

|函数|描述|用法|
|:-|:-|:-|
|ABS(x)|返回x绝对值||
|CEIL(x)|x向上取整||
|FLOOR(x)|x向下取整||
|RAND(x)|返回0-1的随机数，x为种子，x相同时返回随机数相同|
|SIGN(x)|返回x的符号，x为负数，0，正数分别返回-1,0,1|
|POW(x,y)|返回x的y次方|
|SQRT(x)|返回x平方根|
|EXP(x)|返回e的x次方|

3. 字符串函数

|函数|描述|用法|
|:-|:-|:-|
4. 日期时间函数
5. 系统信息函数
6. 加密函数
7. 其他函数

### 2.5. 窗口函数(未完善)
窗口函数用法：

    函数名（[expr]） over子句
    原则上一般写在select子句中

over() 用来指定函数执行的窗口
```SQL
-- over 写法
SELECT *,
# start
窗口函数()
over (
ORDER BY score # 排序
partition by class_id # 按字段分组
ROWS 2 preceding # frame分区
)
AS result 
# end
FROM test;

-- frame分区写法
ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING

时间点可以表示为：

n PRECEDING : 前n行
n FOLLOWING：后n行
CURRENT ROW ： 当前行
UNBOUNDED PRECEDING：窗口第一行
UNBOUNDED FOLLOWING：窗口的最后一行

```

1. 序号函数(排名问题)

|函数|描述|用法(参数)|
|:-|:-|:-|
|row_number()|排序，同数不同名，相当于行号|3、2、2、1排名后为1、2、3、4|
|rank()|同数同名，有跳级|3、2、2、1排名后为1、2、2、4|
|dense_rank()|同数同名，无跳级|3、2、2、1排名后为1、2、2、3|
```SQL
-- 例子：178分数排名
select Score, dense_rank() over(ORDER BY Score DESC) AS "Rank"
from Scores;
```

2. 分布函数

|函数|描述|用法(参数)|
|:-|:-|:-|
|percent_rank()|百分比排名||
|cume_dist()|分组内小于等于当前rank值的行数/分组内总行数||
3. 前后函数

|函数|描述|用法(参数)|
|:-|:-|:-|
|lag(列名,n)|分区中位于当前行后n行(lag)的记录值|
|lead(列名,n)|分区中位于当前行前n行的记录值|
1. 头尾函数

|函数|描述|用法(参数)|
|:-|:-|:-|
|first_val()|得到分区中的第一个指定参数的值|
|last_val()|得到分区中的最后一个指定参数的值|
1. 其他函数

|函数|描述|用法(参数)|
|:-|:-|:-|
|nth_value(expr,n)|返回窗口中第N个expr的值，expr可以是表达式，也可以是列名|
|nfile(n)|将分区中的有序数据分为n个桶，记录桶号。|
### 2.6. 自定义函数（未完善）
```SQL
-- 语法基础
-- 例子：177返回第N高薪水
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare m INT;
    set m=N-1; 
  RETURN (
      # Write your MySQL query statement below.
      select 
      ifnull(
          (select distinct Salary from Employee order by Salary desc limit m,1),null
          )
  );
END
```
## 3. 查找数据
**准备数据**：  
使用廖雪峰老师提供的数据：
https://raw.githubusercontent.com/michaelliao/learn-sql/master/mysql/init-test-data.sql
将文件内容复制，在本地创建txt，将文本粘贴进去，在第一行加入
set character set utf8;  
保存为UTF-8编码并改名为init-test-data.sql
cmd先cd到sql文件所在目录  
再登录MySQL，在输入密码后输入：\\. init-test-data.sql  

### 3.1. 基本查询

```SQL
-- 显示所有数据库
show databases;

-- 切换到数据库test
use test;

-- 查询表所有数据
SELECT * FROM students;
--SELECT 表示要执行一个查询 * 表示所有列 FROM表示将要从哪个表查询

-- 使用SELECT进行计算
SELECT 100+200
-- 虽然SELECT可以用作计算，但它并不是SQL的强项
-- 不带FROM子句的SELECT语句常用于：判断当前到数据库的连接是否有效
-- 许多检测工具会执行一条SELECT 1;来测试数据库连接。

-- 统计行数
select count(id) from students;

```
### 3.2. 投影查询(筛选列) SELECT与 去重DISTINCT
1. SELECT 语句基础
```SQL
-- 按照列名筛选
SELECT id, score, name FROM students;
-- 按照列名筛选的同时给列起别名
SELECT id, score points, name FROM students;
SELECT 列1 别名1, 列2 别名2 FROM ...

-- 只列出不同的值
SELECT DISTINCT column_name,column_name
FROM table_name;
```
2. UNION 操作符
```SQL
-- 默认地，UNION 操作符选取不同的值。如果允许重复的值，请使用 UNION ALL。
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
-- UNION 结果集中的列名总是等于 UNION 中第一个 SELECT 语句中的列名。
SELECT column_name(s) FROM table1
WHERE condition
UNION ALL
SELECT column_name(s) FROM table2
WHERE condition;
```
UNION 操作符用于合并两个或多个 SELECT 语句的结果集。  
请注意，UNION 内部的每个 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每个 SELECT 语句中的列的顺序必须相同。

### 3.3. 先过滤数据(筛选行) WHERE
WHERE在GROUP BY分组和聚合函数之前对数据行进行过滤
WHERE子句中不能使用聚合函数
1. WHERE 语句基础
```SQL
-- 单条件查询
SELECT * FROM students WHERE score >= 80;
-- 在students中的所有数据中，找到score字段值大于等于80的

-- AND条件查询
SELECT * FROM students WHERE score >= 80 AND gender = 'M';

-- OR条件查询
SELECT * FROM students WHERE score >= 80 OR gender = 'M';

-- NOT条件查询
SELECT * FROM students WHERE NOT class_id = 2;
SELECT * FROM students WHERE class_id <> 2;# 等价于上一句，NOT语句不常用
-- 多条件查询，使用括号
SELECT * FROM students WHERE (score < 80 OR score > 90) AND gender = 'M';
```
2. LIKE+通配符
```SQL
-- LIKE条件查询
SELECT * FROM students WHERE name LIKE '小%'; 
-- %表示任意字符，'ab%'将匹配ab'，'abc'，'abcd'
```
3. IN 操作符
```SQL
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1,value2,...);
```
IN 操作符允许您在 WHERE 子句中规定多个值。

4. BETWEEN 操作符
```SQL
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```
BETWEEN 操作符选取介于两个值之间的数据范围内的值。这些值可以是数值、文本或者日期。

|通配符|描述|
|:-|:-|
|%|替代 0 个或多个字符|
|_|替代一个字符|
|[charlist]|字符列中的任何单一字符|
|[^charlist]或[!charlist]|不在字符列中的任何单一字符|

运算优先级：NOT、AND、OR  
加上括号可以改变优先级

### 3.4. 后过滤数据HAVING
HAVING子句对GROUP BY分组和聚合函数之后的数据行进行过滤  
HAVING子句中不能使用除了分组字段和聚合函数之外的其他字段
```sql
SELECT SUM(score)
FROM students
GROUP BY class
HAVING SUM(population)>500
# 总成绩超过500的班级
```
### 3.5. 聚合查询与分组GROUP BY
|聚合函数|说明|
|:-|:-|
|COUNT|计数|
|SUM|求和，该列必为数值类型|
|AVG|求平均值，该列必须位数值类型|
|MAX|求某一列最大值，如果是字符类型，返回排序最后的字符|
|MIN|求某一列最小值，如果是字符类型，返回排序最前的字符|
```SQL
-- 统计男性人数，并将列名命名为boys
SELECT COUNT(id) boys FROM students
WHERE gender = 'M';

-- 求男性成绩平均值，并将列名命名为average
SELECT AVG(score) average FROM students
WHERE gender = 'M';
-- 要特别注意：如果聚合查询的WHERE条件没有匹配到任何行
-- COUNT()会返回0，而SUM()、AVG()、MAX()和MIN()会返回NULL：

--分组统计
--单分组
SELECT class_id, COUNT(*) num
FROM students
GROUP BY class_id;
--多重分组统计
SELECT class_id, gender, COUNT(*) num
FROM students
GROUP BY class_id, gender;
--分组时，SELECT只能放入分组的列
```
### 3.6. 排序 ORDER BY
ORDER BY 语句
```SQL
-- 升序排序
SELECT * FROM students ORDER BY score;

-- 降序排序
SELECT * FROM students ORDER BY score DESC;

-- 多重排序
SELECT * FROM students ORDER BY score DESC, id;
-- 如果score有相同分数，再按id排序，实现绝对排序
-- 排序值相同的行位置是随机的，在分页时会出错
```



### 3.7. 多表查询
#### 3.7.1. 笛卡尔查询
```SQL
SELECT
    s.id sid,
    s.name,
    s.gender,
    s.score,
    c.id cid,
    c.name cname
FROM students s, classes c
WHERE s.gender = 'M' AND c.id = 1;
```
查询结果是students表和classes表的“乘积”  
即结果集的列数是students表和classes表的**列数之和**，行数是students表和classes表的**行数之积**。
使用笛卡尔查询时要非常小心，因为是乘积，很容易返回数据过多
笛卡尔积主要是用来查看连续缺失的数据。
#### 3.7.2. 连接查询 JOIN
```SQL
-- 内连接(INNER JOIN)
SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
FROM students s # 主表
INNER JOIN classes c # 连接的附表
ON s.class_id = c.id; # 主表附表连接条件

-- 左外连接, 选出左表存在的记录
LEFT OUTER JOIN classes c
-- 右外连接, 选出右表存在的记录
RIGHT OUTER JOIN classes c
-- 全外连接, 选出左右表都存在的记录
FULL OUTER JOIN classes c

```
### 3.8. 分页 LIMIT OFFSET
LIMIT OFFSET语句
LIMIT OFFSET后面只接受正整数与单一变量，不能时负数、0、表达式
```SQL
SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 0;
-- 对结果集从0号记录开始，最多取3条。
-- 注意SQL记录集的索引从0开始

-- 语句
LIMIT <pageSize> OFFSET <N>;
-- N = pageSize * (pageIndex - 1)
-- 只写LIMINT时，相当于OFFSET设置为0
-- N越大，查询速度越慢

-- MySQL中简写
LIMIT <index>, <pageSize>;
```
### 3.9. 综合查询(综合使用以上方法)
```SQL
-- 连接多表，查询数值，筛选行列，排序，分页
SELECT DISTINCT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
FROM students s # 主表
INNER JOIN classes c # 连接的附表
ON s.class_id = c.id # 主表附表连接条件
WHERE gender = "M" # 筛选条件
ORDER BY score DESC, id # 按指定列排序
LIMIT 3 OFFSET 0; # 分页
-- ORDER 语句要放在 WHERE 后面

-- 聚合查询，条件查询并分组
SELECT class_id, AVG(score) num
FROM students
WHERE gender = "M"
GROUP BY class_id
HAVING AVG(score)>80;
-- 聚合查询时，WHERE要在GROUP BY前
```

### 3.10. 查询思路

1. 某些带聚合功能的查询需求应用窗口函数是一个最优选择。（如果版本允许）
2. 优先单表查询：
   即便是需要用group by、order by、limit等，效率一般也比多表高
3. 不能用单表时优先用连接：
   连接是SQL中非常强大的用法，小表驱动大表+建立合适索引+合理运用连接条件，基本上连接可以解决绝大部分问题。但join级数不宜过多，毕竟是一个接近指数级增长的关联效果
4. 尽量不使用子查询与笛卡尔积
5. 自定义变量在复杂SQL实现中会很有用
## 4. 修改数据
### 4.1. 增加数据 INSERT INTO
```SQL
-- 基本语法
INSERT INTO <表名> (字段1, 字段2, ...) VALUES (值1, 值2, ...);
-- 例子
INSERT INTO students (class_id, name, gender, score)
VALUES (2, '大牛', 'M', 80);

-- 一次添加多条
INSERT INTO students (class_id, name, gender, score)
VALUES
(1, '大宝', 'M', 87),
(2, '二宝', 'M', 81);

-- 插入其他表数据
INSERT INTO table2 (column_name(s))
SELECT column_name(s)
FROM table1;
```
插入记录时不需要考虑id字段，这是因为id字段是一个自增主键，它的值可以由数据库自己推算出来。此外，如果一个字段有默认值，那么在INSERT语句中也可以不出现。

要注意，字段顺序不必和数据库表的字段顺序一致，但值的顺序必须和字段顺序一致。也就是说，可以写  
INSERT INTO students  
(score, gender, name, class_id) ...，  
但是对应的VALUES就得变成  
(80, 'M', '大牛', 2)。

### 4.2. 修改数据 UPDATE
```SQL
-- 基本语法
UPDATE <表名> SET 字段1=值1, 字段2=值2, ... WHERE ...;

-- 例子
UPDATE students
SET name='大牛', score=66
WHERE id=1;
-- 修改多条
UPDATE students
SET name='小牛', score=77
WHERE id>=5 AND id<=7;
-- 表达式修改多条
UPDATE students
SET score=score+10
WHERE score<80;

-- 注意，不加WHERE条件会更新整个表的数据
UPDATE students SET score=60;
```
如果WHERE条件没有匹配到任何记录，UPDATE语句不会报错，也不会有任何记录被更新。例如：
### 4.3. 删除数据 DELETE
```SQL
-- 基本语句
DELETE FROM <表名> WHERE ...;

-- 例子
DELETE FROM students WHERE id=1;
-- 删除多条
DELETE FROM students WHERE id>=5 AND id<=7;
DELETE FROM students WHERE id IN (1,3,5)
-- 不带WHERE条件会删除整个表
DELETE FROM students;
```
当删除的是主表时
无外键：相当于没有任何关联数据
有外键：
1. 创建外键时定义了ON DELETE CASCADE，关联数据被自动删除
2. 没有定义ON DELETE CASCADE，有关联数据时报错
## 5. 常见问题
**中文出现乱码时的解决办法**

修改cmd默认编码格式：
1. win键+R，输入regedit，确定。
2. 按顺序找到HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor。
3. 点击右键-新建，选择“字符串值”。
4. 命名为“autorun”, 点击右击修改，数值数据填写“chcp 65001”，确定。

修改mysql编码格式：
https://blog.csdn.net/u012410733/article/details/61619656
```SQL
-- 显示当前字符串编码
show variables like '%char%';
-- 修改服务器与数据库编码格式
set character_set_server=utf8;
set character_set_database=utf8;
```