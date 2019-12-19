# D36 多表查询,python操作数据库

用到的表:

![1572437616526](C:\Users\WO\AppData\Roaming\Typora\typora-user-images\1572437616526.png)

## 一、交叉连接

- 交叉连接:不适应任何匹配条件,生成笛卡儿积

  ```
  交叉连接:
  select * from employee,department;
  +----+------------+--------+------+--------+------+----------+
  | id | name       | sex    | age  | dep_id | id   | name     |
  +----+------------+--------+------+--------+------+----------+
  |  1 | egon       | male   |   18 |    200 |  200 | 技术     |
  |  1 | egon       | male   |   18 |    200 |  201 | 人力资源 |
  |  1 | egon       | male   |   18 |    200 |  202 | 销售     |
  |  1 | egon       | male   |   18 |    200 |  203 | 运营     |
  |  2 | alex       | female |   48 |    201 |  200 | 技术     |
  |  2 | alex       | female |   48 |    201 |  201 | 人力资源 |
  |  2 | alex       | female |   48 |    201 |  202 | 销售     |
  |  2 | alex       | female |   48 |    201 |  203 | 运营     |
  |  3 | wupeiqi    | male   |   38 |    201 |  200 | 技术     |
  |  3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源 |
  |  3 | wupeiqi    | male   |   38 |    201 |  202 | 销售     |
  |  3 | wupeiqi    | male   |   38 |    201 |  203 | 运营     |
  |  4 | yuanhao    | female |   28 |    202 |  200 | 技术     |
  |  4 | yuanhao    | female |   28 |    202 |  201 | 人力资源 |
  |  4 | yuanhao    | female |   28 |    202 |  202 | 销售     |
  |  4 | yuanhao    | female |   28 |    202 |  203 | 运营     |
  |  5 | liwenzhou  | male   |   18 |    200 |  200 | 技术     |
  |  5 | liwenzhou  | male   |   18 |    200 |  201 | 人力资源 |
  |  5 | liwenzhou  | male   |   18 |    200 |  202 | 销售     |
  |  5 | liwenzhou  | male   |   18 |    200 |  203 | 运营     |
  |  6 | jingliyang | female |   18 |    204 |  200 | 技术     |
  |  6 | jingliyang | female |   18 |    204 |  201 | 人力资源 |
  |  6 | jingliyang | female |   18 |    204 |  202 | 销售     |
  |  6 | jingliyang | female |   18 |    204 |  203 | 运营     |
  +----+------------+--------+------+--------+------+----------+
  ```

## 二、内连接

- 内链接:只有匹配条件的才匹配,相当于从笛卡儿积中筛选出了符合条件的数据,后面还可以加where筛选

  ```
  select * from employee inner join department on employee.dep_id = department.id;
  #inner join 表示内连接,on后的条件为匹配条件,可以加多条
  #以上语句与下述语句效果一样
  select * from employee,department where employee.dep_id = department.id;
  +----+-----------+--------+------+--------+------+----------+
  | id | name      | sex    | age  | dep_id | id   | name     |
  +----+-----------+--------+------+--------+------+----------+
  |  1 | egon      | male   |   18 |    200 |  200 | 技术     |
  |  2 | alex      | female |   48 |    201 |  201 | 人力资源 |
  |  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源 |
  |  4 | yuanhao   | female |   28 |    202 |  202 | 销售     |
  |  5 | liwenzhou | male   |   18 |    200 |  200 | 技术     |
  +----+-----------+--------+------+--------+------+----------+
  ```

## 三、外连接

- 左连接:以左边为基准,即找出所有左表的信息,右表没有的为NULL,本质是在内连接的基础上增加左边有右边没有的结果

  ```
  select * from employee left join department on employee.dep_id = department.id;
  +----+------------+--------+------+--------+------+----------+
  | id | name       | sex    | age  | dep_id | id   | name     |
  +----+------------+--------+------+--------+------+----------+
  |  1 | egon       | male   |   18 |    200 |  200 | 技术     |
  |  5 | liwenzhou  | male   |   18 |    200 |  200 | 技术     |
  |  2 | alex       | female |   48 |    201 |  201 | 人力资源 |
  |  3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源 |
  |  4 | yuanhao    | female |   28 |    202 |  202 | 销售     |
  |  6 | jingliyang | female |   18 |    204 | NULL | NULL     |
  +----+------------+--------+------+--------+------+----------+
  ```

- 右连接:以右边为基准,即找出所有右表的信息,右表没有的为NULL,本质是在内连接的基础上增加右边有左边没有的结果

  ```
  select * from employee right join department on employee.dep_id = department.id;
  +------+-----------+--------+------+--------+------+----------+
  | id   | name      | sex    | age  | dep_id | id   | name     |
  +------+-----------+--------+------+--------+------+----------+
  |    1 | egon      | male   |   18 |    200 |  200 | 技术     |
  |    2 | alex      | female |   48 |    201 |  201 | 人力资源 |
  |    3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源 |
  |    4 | yuanhao   | female |   28 |    202 |  202 | 销售     |
  |    5 | liwenzhou | male   |   18 |    200 |  200 | 技术     |
  | NULL | NULL      | NULL   | NULL |   NULL |  203 | 运营     |
  +------+-----------+--------+------+--------+------+----------+
  ```

- 全外连接:mysql本身不支持全外连接,在其他数据库中有full join,mysql只能通过将左连接和右连接结合的方式做到全外连接

  ```
  select * from employee left join department on employee.dep_id = department.id
  union
  select * from employee right join department on employee.dep_id = department.id;
  +------+------------+--------+------+--------+------+----------+
  | id   | name       | sex    | age  | dep_id | id   | name     |
  +------+------------+--------+------+--------+------+----------+
  |    1 | egon       | male   |   18 |    200 |  200 | 技术     |
  |    5 | liwenzhou  | male   |   18 |    200 |  200 | 技术     |
  |    2 | alex       | female |   48 |    201 |  201 | 人力资源 |
  |    3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源 |
  |    4 | yuanhao    | female |   28 |    202 |  202 | 销售     |
  |    6 | jingliyang | female |   18 |    204 | NULL | NULL     |
  | NULL | NULL       | NULL   | NULL |   NULL |  203 | 运营     |
  +------+------------+--------+------+--------+------+----------+
  ```

# 四、子查询

- 1：子查询是将一个查询语句嵌套在另一个查询语句中。
  2：内层查询语句的查询结果，可以为外层查询语句提供查询条件。
  3：子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字

  ```
  带in关键字的查询:
  select id,name from department
      where id in 
          (select dep_id from employee group by dep_id having avg(age) > 25);
          
  +------+----------+
  | id   | name     |
  +------+----------+
  |  201 | 人力资源 |
  |  202 | 销售     |
  +------+----------+
  ```

  ```
  带exists关键字的子查询:
  EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。
  而是返回一个真假值。True或False
  当返回True时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询
  select * from employee
           where exists
               (select id from department where id=200);
               
  +----+------------+--------+------+--------+
  | id | name       | sex    | age  | dep_id |
  +----+------------+--------+------+--------+
  |  1 | egon       | male   |   18 |    200 |
  |  2 | alex       | female |   48 |    201 |
  |  3 | wupeiqi    | male   |   38 |    201 |
  |  4 | yuanhao    | female |   28 |    202 |
  |  5 | liwenzhou  | male   |   18 |    200 |
  |  6 | jingliyang | female |   18 |    204 |
  +----+------------+--------+------+--------+
  
  select * from employee
           where exists
               (select id from department where id=204);
  Empty set (0.00 sec)
  
  ```

  

  4：还可以包含比较运算符：= 、 !=、> 、<等

  ```
  带比较运算符的子查询:
  select name,age from emp where age > (select avg(age) from emp);
  +---------+------+
  | name    | age  |
  +---------+------+
  | alex    |   48 |
  | wupeiqi |   38 |
  +---------+------+
  ```

- 查询结果如果进行拼接必须起别名
- 查询结果中如果有聚合函数得出的结论,且在连表之后使用,必须给字段起名字

## 五、从sql文件中导入导出数据

- 导出数据(在cmd初始界面,不是mysql):mysqldump -uroot -p密码 要导出的db名字 > 一个.sql文件的路径

- 导入数据:mysql>soource 文件路径

## 六、python操作数据库

- 安装并导入PyMySQL模块

- 连接数据库

  ```
  conn = pymysql.connect(ip,用户名,密码,[数据库名])
  本质是实例化了一个connection对象
  ```

- 创建游标:之后操作数据库就是通过游标

  ```
  cur = conn.cursor()
  ```

- 执行sql语句:

  ```
  cur.execute(sql语句)
  ```

- 查看执行结果:

  ```
  print(cur.fetchone()):获取一条数据
  print(cur.fetchmany(参数)):获取指定条数的数据
  print(cur.fetchall()):获取所有数据
  ```

- 在进行插入,更新,删除操作时要提交,否则不生效,注意是连接对象进行提交

  ```
  cur.execute("update table1 set age = 20 where age = 18")
  conn.commit()
  ```

- 关闭连接:

  ```
  conn.close()
  ```

- sql注入:在sql语句中使用占位符占位时,有可能会插入一些带有结束符或其他含义的符号,导致绕开后面的判断

  ```
  例如登录验证时:
  sql = ' select * from user where username = "alex"; -- "and password = "1233";'
  这样的sql语句会在alex 后结束,--后被当作注释内容而不判断
  ```

  所以通常将占位符所代替的字段传入execute()方法中:

  ```
  sql = 'select * from user where username = %s and password = %s'
  ret = cur.execute(sql,(username,password))
  ```

  