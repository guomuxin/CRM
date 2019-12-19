# D50 url别名,反向解析,orm增删改查

## 一、url别名和反向解析

- url别名:url中的地址可能是会变换的,比如版本更新或其他情况等,如果修改地址之后一个一个去函数或者html页面中修改就会非常麻烦,如果使用别名就可以避免这种情况

  - 写法:url(r'^login/v2/', views.login,name='xx'),

- 反向解析:从别名解析出地址的过程

  - 从视图中反向解析:

    ```
    from django.urls import reverse
    
    ...
    addr = reverse(别名) //这样得到的结果就是当前的地址,可以用于返回页面
    ...
    ```

  - html模板渲染时的反向解析:

    ```
    ...
    {% url "别名" %} django会自动将别名对应的地址传给前端,无需在views中再写
    ```

- include分发路由:如果一个项目中有多个app,为了便于管理通常在每个app文件夹下都建立urls文件,项目的urls只负责将请求发送到指定app中,具体使用哪个函数由app内的urls决定

  ```
  项目urls:不需要admin了,要导入include,原本写函数的地方现在写include("app.urls",namespace="")
  from django.conf.urls import url,include
  
  
  urlpatterns = [
      url(r'^app01/',include("app01.urls",namespace="app01")),
      url(r'^app02/',include("app02.urls",namespace="app02")),
  
  ]
  django匹配url过程,先找到url中的url,取走这部分再拿后面的部分匹配后面的具体路径
  ```

  ```
  app01的urls:
  from django.conf.urls import url,include
  from django.contrib import admin
  from app01 import views
  urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^home/',views.home,name="home")
  
  ]
  ```

- 不同app之间的函数,路径可以相同,但是如果有别名的话都会指向最后一个app的内容,所以需要使用命名空间来区分,也就是namespace

  ```
  例如:
  app01的views:
  def home(request):
      if request.method == "GET":
          print(reverse("home"))
          return render(request,"app01_home.html")
          
  app02的views:
  def home(request):
      if request.method == "GET":
          print(reverse("home"))
          return render(request,"app02_home.html")
  
  由于app01和app02中都有别名为home的内容,最终都会指向后创建的app02
  ```

  

- 命名空间namespace:将每个应用自己的url路径划分一个空间,将来通过别名反向解析时,通过空间名称可以找到对应应用下面的路径

  ```
  项目urls:
  urlpatterns = [
      url(r'^app01/',include("app01.urls",namespace="app01")),
      url(r'^app02/',include("app02.urls",namespace="app02")),
  
  ]
  
  app01的views:
  def home(request):
      if request.method == "GET":
          print(reverse("app01:home"))
          return render(request,"app01_home.html")
          
  app02中的views:
  def home(request):
      if request.method == "GET":
          print(reverse("app02:home"))
          return render(request,"app02_home.html")
          
  打印结果:
  /app01/home/
  /app02/home/
  ```

  - html中使用命名空间:{% url 'app01:home' %}

## 二、数据库操作orm

- orm:object relational mapping  对象关系映射

- 使用orm:

  ```
  1.在models文件内创建类,继承自models.Model,django会自动将类转换为数据库中的一个表
  class UserInfo(models.Model):
      id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=10,null=False,unique=True)
      password = models.CharField(max_length=32,null=False)
  2.setting中配置数据库
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'orm01',
          'HOST':"127.0.0.1",
          'PORT':3306,
          'USER':"root",
          'PASSWORD':"123456"
      }
  }
  
  3.在项目中的__init__文件中指定pymysql作为连接客户端
  import pymysql
  pymysql.install_as_MySQLdb()
  
  4.在终端执行数据库同步指令
  python manage.py makemigrations  #在migrations文件夹下面生成记录文件
  python manage.py migrate         #执行记录文件
  
  5.表名为:应用名_类名全小写
  6.decimal:max_digits    总位数(不包括小数点和符号)
          decimal_places    小数位数
  
  ```

- 表中的增删改查

  - 增:create会返回新创建的对象

    ```
    方式一:
    obj = models.UserInfo(
    	name="xiaoming",
    	password="123"
    )
    obj.save()
    
    方式二:
    models.UserInfo.objects.create(
    	name="xiaohei",
    	password="hhh"
    )
    ```

  - 删:

    ```
    models.UserInfo.objects.filter(id=1).delete()
    ```

  - 改:

    ```
    models.UserInfo.objects.filter(id=1).update(
    	name="xxx",
    	password="hhh"
    )
    ```

  - 查:

    ```
    1.all():获取所有内容,结果是一个QuerySet,类似列表,可以用索引取值
    ret = models.UserInfo.objects.all()
    
    2.get(条件):能且只能获取一条数据,若没有符合条件的数据或有多条符合条件的数据都会报错,获取的结果是一个对象,可以直接通过.来取详细内容
    ret = models.UserInfo.objects.get(id=1)
    print(ret.name)
    结果:xiaoming
    如果是all或者filter获取的结果.name会报错
    
    3.filter(条件):获取所有符合条件的数据,返回一个QuerySet
    
    4.enclude():排除符合条件的数据,返回QuerySet

    ```

- 批量创建

  ```
  
  
  ​	list_obj = []
  ​    for i in range(10):
  ​        obj = models.UserInfo(
  ​            username='xx%s'%i,
  ​            password='66%s'%i,
  ​        )
  ​        list_obj.append(obj)
  ​    print(list_obj)
  ​    models.UserInfo.objects.bulk_create(list_obj)
  
  update_or_create 有就更新,没有就创建
      a,b = models.UserInfo.objects.update_or_create(
          username='alex',
          defaults={
              'id':20,
              'password':'ooooo',
              'age':84,
          }
      )
  ```

  

  ```
  print(a)  # 当前更新后的model对象,或者是你新增的记录的model对象
  print(b)  # 新增就是True,查询就False
  ```

- 

  