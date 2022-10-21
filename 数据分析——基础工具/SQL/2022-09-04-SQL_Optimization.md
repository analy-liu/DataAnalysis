---
title:  SQL优化
layout: default
---
[![返回](/assets/images/back.png)](../../../../2022/06/01/SQL_Index.html)

# 1. SQL查询语句优化

本节会介绍一些不依赖具体数据库实现，而且简单易行的优化方法  

很多时候，使用不同的查询语句可以得出相同的结果，虽然有查询优化器的存在，但很遗憾，查询优化器生成的执行计划很大程度上要受查询语句结构的影响。  

不过查询语句，也是要考虑可读性的，当可读性高时，代码执行速度也很快，有时就没必要优化成时间空间复杂度最高的代码。  

## 1.1 使用EXISTS替代IN

在IN用于子查询时，用EXISTS替代IN，速度往往会有所提升。例如下面的两段代码  

```SQL
-- 查询表A中id存在于表B中的行
-- 慢
SELECT *
FROM Table_A
WHERE id IN (SELECT id
             FROM Table_B);
-- 快
SELECT *
FROM Table_A A
WHERE EXISTS (SELECT *
              FROM Table_B B
              WHERE A.id = B.id);
```

为什么呢？  
简而言之就是降低了时间与空间复杂度  
- 降低空间复杂度：如果连接列（id）上建立了索引，那么查询B表时不用查询实际的表，只查询索引就可以了。因为当 IN 的参数是子查询时，数据库首先会执行子查询，然后将结果存储在一张临时的工作表里（内联视图），然后扫描整个视图。很多情况下这种做法都非常耗费资源。使用 EXISTS 的话，数据库不会生成临时的工作表  
- 降低时间复杂度：如果使用EXISTS ，那么只要查到一行数据满足条件就会终止查询，不用像使用 IN 时一样扫描全表。在这一点上 NOT EXISTS 也一样。

当然，除了用EXISTS，还可以用联结优化。

```SQL
SELECT A.id, A.name
FROM Table_A A INNER JOIN Table_B B
ON A.id = B.id;
```

## 1.2 避免无谓的排序

学过排序的同学都知道，在排序算法中，时间复杂度最快的也是O(nlogn)，所以尽量避免无谓的排序，能提高代码速度  

会进行排序的代表性语句有下面这些：

- GROUP BY
- ORDER BY
- 聚合函数（SUM、COUNT、AVG、MIN、MAX）
- DISTINCT
- 集合运算符（UNION 、INTERSECT 、EXCEPT ）
- 窗口函数（RANK 、ROW_NUMBER 等）

**解决办法：**

- GROUP BY
  能写在WHERE中的条件就不要写在HAVING中，这样能减少进入GROUP BY语句的行，减轻排序负担

- DISTINCT
  
  使用 EXISTS 代替 DISTINCT

  ```SQL
  -- 用联结查询一对多时，会产生重复列，需要去重
  SELECT DISTINCT A.id
  FROM Table_A A I INNER JOIN Table_B B
  ON A.id = B.id;

  -- 用EXISTSS代替 DISTINCT，可以避免排序
  SELECT A.id
  FROM Table_A A
  WHERE EXISTS
  (SELECT *
  FROM Table_B B
  WHERE A.id = B.id);
  ```

- 集合运算符（UNION 、INTERSECT 、EXCEPT ）
  如果不在乎结果中是否有重复数据，或者事先知道不会有重复数据，加上 ALL 能避免排序

## 1.3 使用索引  

都知道使用索引能提高速度，但你真的使用了索引吗？

下面是几种以为用了，但没真的用的情况

1. 条件表达式中，左边不是原始字段，例如 ID+1 > 100，改成ID>99即可  
2. 在索引字段使用IS NULL谓词，例如 ID IS NULL ，会使得索引无法使用  
3. 表达式中使用否定形式不能用到索引（<>、NOT IN），会进行全表扫描  
4. 使用OR连接联合索引
5. 使用 LIKE 谓词时，使用‘%a'这样开头模糊的形式，‘a%’这样才能用到索引
6. 进行默认的类型转换

## 1.4 减少中间表

中间表会产生额外的开销，尽量减少中间表的产生能提高效率

下面是几种减少中间表的方法

1. GROUP BY后，用HAVING进行筛选，而不是把结果作为子表，用WHERE进行筛选
2. 优化条件逻辑中产生子表的次数  
   
3. 是