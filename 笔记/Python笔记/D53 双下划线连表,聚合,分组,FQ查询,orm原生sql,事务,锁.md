# D53 双下划线连表,聚合,分组,FQ查询,orm原生sql,事务,锁

## 一、基于双下划线的跨表查询(join)

- values除了对输出内容进行限定为还有一个重要作用就是连表时使用,正向查询时通过外键属性名加双下划线就可取到关联表的信息,反向查询则是通过小写类名加双下划线

- 一对一:

  ```
  例:查询姓名为小明的作者电话
  ret = models.Author.objects.filter(name="小明").values("ad__telephone")
  or
  ret = models.AuthorDetail.objects.filter(author__name="小明").values("telephone")
  ```

- 一对多:

  ```
  例:查询太原出版社出版了哪些书
  ret = models.Publish.objects.filter(name="太原出版社").values("book__title")
  or
  ret = models.Book.objects.filter(publishs__name="太原出版社").values("title")
  ```

- 多对多:

  ```
  例:查询小明出版的书
  ret = models.Book.objects.filter(author__name="小明").values("title")
  or
  ret = models.Book.objects.filter(author__name="小明").values("title")
  ```

# 二、聚合查询

- 使用聚合查询首先要从django.db.models模块中导入相应的功能,例如Avg,Max,Min,Count,Sum

- 聚合查询的关键字:aggregate(),在其中使用聚合查询

- 结果是普通字典,queryset的结束符,也就是说通常用在最后,常与分组连用

  ```
  例:查询最贵的书的价格
  ret = models.Book.objects.aggregate(Max("price"))
  ```

## 三、分组

- 关键字:annotate(),在其中使用聚合查询

- 方式一:单表分组,依照表中的某个字段进行分组.values写在annotate前面,意思是以values括号内的字段作为分组的依据,annotate里面是你要做的统计结果,这样,返回结果为queryset类型数据,里面是字典,每个属性就是一个键值对,{'publishs_id':1,'m':100}.聚合查询可以赋别名,显示时以别名为键,这个别名也会作为表中的一个临时属性名,values时可以显示该属性

  ```
  例:以publishs进行分组查询出版的书的平均价格
  ret = models.Book.objects.values("publishs").annotate(Avg("price"))
  结果:<QuerySet [{'publishs': 1, 'price__avg': 123.5}, {'publishs': 2, 'price__avg': 74.8}, {'publishs': 3, 'price__avg': 100.0}]>
  
  ret = models.Book.objects.values("publishs").annotate(m=Avg("price"))
  结果:<QuerySet [{'publishs': 1, 'm': 123.5}, {'publishs': 2, 'm': 74.8}, {'publishs': 3, 'm': 100.0}]>	
  
  ```

- 方式二:连表后将主表的每一行(主键)作为分组依据,然后对连表后的整张表进行分组.annotate直接写在了objects后面,意思是按照前面表的所有的数据(默认是id值)作为分组依据,结果返回的是前面这个表的所有models对象(model对象中包含了每个对象自己的统计结果),在通过values来取值,取值时可以直接写字段和统计结果的别名,也是queryset类型,里面是字典{'m':100,'name':'东京出版社'},这里必须起别名,因为annotate后的结果是一个对象,通过values才能获取其中的具体内容, 而想查看聚合查询就需要在values中指定

    ```
  例:查询每个作者的姓名以及出版的书的最高价格
  ret = models.Author.objects.annotate(m=Max("book__price")).values("name","m")
  结果:<QuerySet [{'name': '郭沐鑫', 'm': Decimal('123.50')}, {'name': '小明', 'm': Decimal('99.00')}, {'name': '红红', 'm': Decimal('123.50')}, {'name': '黑黑', 'm': None}, {'name': '黑黑', 'm': None}]>
  
  该例使用方式一的写法:
  ret = models.Book.objects.values("author__id").annotate(m=Max("price")).values("author__name","m")
    ```

## 四、F查询和Q查询

- F查询:

  - 在orm中不能直接对一个表中的两个字段进行比较,例如

    models.Book.objects.filter(age>id),这样的写法在orm中是不可行的,通过F修饰后就可以进行这样的比较

  ```
  例:查询年龄大于id值的作者
  ret = models.Author.objects.filter(age__gt=F('id'))
  ```

  - 进行更新时想要以原数据为基础,进行四则运算:

    ```
    例:所有书的价钱上涨20
    models.Book.objects.all().update(
    price = F('price') + 20
    )
    ```

- Q查询:

  - 进行逻辑查询时需要用到Q关键字

  - 与(and):&

  - 或(or):|

  - 非(not):~

    ```
    例:作者id为1或2的作者写的书
    ret = models.Book.objects.filter(Q(author__id=1) | Q(author__id=2)).values("title")
    例:作者是98年出生且地址是山西的作者姓名
    ret = models.AuthorDetail.objects.filter(Q(birthday__year=1998) & Q(addr='山西')).values("author__name")
    例:查询年龄不是20岁的作者姓名
    ret = models.Author.objects.filter(~Q(age=20)).values("name")
    ```

## 五、orm执行原生sql语句(了解)

```
# 方式1
    # ret = models.Book.objects.raw('select * from app01_book;')
    # for i in ret:
    #     print(i.title)
    # print(ret)
    
    #方式2 django自带的连接通道(配置的pymysql)
    from django.db import connection
    import pymysql
    # conn = pymysq.connect()
    # cursor = connection.cursor()
    # cursor.execute('select * from app01_book;')
    # print(cursor.fetchall())
    #
    
    # 方式3 pymysql
    # conn = pymysql.connect(
    #     host='127.0.0.1',
    #     port=3306,
    #     user='root',
    #     password='123',
    #     database='orm02',
    #     charset='utf8'
    # 
    # )
    # cursor = conn.cursor(pymysql.cursors.DictCursor)
    # cursor.execute('select * from app01_book;')
    # print(cursor.fetchall())
```



## 六、django外部脚本调用models数据库操作

```

import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm02.settings")
    import django
    django.setup()
    
	from app01 import models
    ret = models.Book.objects.all().values('title')
    print(ret)

```



## 七、ORM事务和锁

- 锁:

  ```
  models.Book.objects.select_for_update().filter(id=1)
  ```

- 事务:

  ```
  方式1 全局配置
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'mxshop',
          'HOST': '127.0.0.1',
          'PORT': '3306',
          'USER': 'root',
          'PASSWORD': '123',
          "ATOMIC_REQUESTS": True, #全局开启事务，绑定的是http请求响应整个过程当中的sql
      }
  }
  
  
  方式2: 视图函数加装饰器
  	from django.db import transaction
      @transaction.atomic
      def viewfunc(request):
          # This code executes inside a transaction.
          do_stuff()
  方式3: 上下文加装饰器
  	from django.db import transaction
      def viewfunc(request):
          # This code executes in autocommit mode (Django's default).
          do_stuff()
  
          with transaction.atomic():   #保存点
              # This code executes inside a transaction.
              do_more_stuff()
  
          do_other_stuff()
  ```

  

