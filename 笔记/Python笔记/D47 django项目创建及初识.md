# D47 django项目创建及初识

## 一、django项目的创建

- 命令行创建:

  下载安装
  	pip install django==1.11.9
  创建项目(找到一个文件夹,切换到这个文件夹下执行下面的指令)
  	django-admin startproject 项目名称
  创建应用
  	python manage.py startapp 应用名称
  在和项目同名的那个文件夹里面的settings配置文件中找到下面的配置:
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  	'app01',  #加上咱们项目文件夹下面的这个应用名称,将项目和应用关联到一起
  ]
  启动项目:
  	python manage.py runserver 127.0.0.1:8001
  	#如果端口不写,默认是8000
  	#如果ip地址和端口号都不写,默认是127.0.0.1:8000

- pycharm创建:

  注意事项:

  - 解释器部分要选择Exisiting interpreter,可以在More Settings中自动创建第一个app
  - 默认地址为主机地址,默认端口为8000,修改主机地址和端口号:runserver 127.0.0.1:8001

  

- 项目文件夹:
      manage.py ----- Django项目里面的工具，通过它可以调用django shell和数据库，启动关闭项目与项目交互等，不管你将框架分了几个文件，必然有一个启动文件，其实他们本身就是一个文件。
      settings.py ---- 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
      urls.py ----- 负责把URL模式映射到应用程序。
      wsgi.py ---- runserver命令就使用wsgiref模块做简单的web server，后面会看到renserver命令，所有与socket相关的内容都在这个文件里面了，目前不需要关注它。



## 二、MVC和MTV模式

- MVC:

  - M:model,模型,业务对象与数据库的映射(ORM)
  - V:view:视图,视图负责与用户的交互(页面)
  - C:controller:控制器:控制器接受用户的输入调用模型和视图完成用户的请求

- MTV:本质与MVC其实一样,django中使用这种模式

  - M:模型,业务对象与数据库的映射(ORM)

  - T:template,模板,html页面存放,展示给用户的页面

  - V:负责业务逻辑，并在适当时候调用Model和Template。

    ![1573818954510](C:\Users\WO\AppData\Roaming\Typora\typora-user-images\1573818954510.png)

  执行过程:用户输入url通过url控制器找到视图中的函数,函数通过models与数据库进行交互获取数据,再将数据发送到template中获取的html页面中,最后发送给用户

### 三、url控制器

- url格式:url(正则,函数名,参数,别名)

- url工作流程:将接受到的url循环与存储的正则表达式进行匹配,只要匹配到就执行后面的函数,且不再向后匹配

- 若要从url中捕获一个值,只需要在它周围放置一对圆括号进行分组匹配

  ```
  两种传参的方式:
  1.位置参数:
  url(r'^home/(\d+)/(\d+)', views.home),
  这种方式会按顺序将url中的参数传给views中的函数
  2.关键字参数:
  url(r'^home/(?P<year>\d+)/(?P<month>\d+)', views.home),
  这种方式会按照关键字将参数传给views中的函数,并且形参必须与名字匹配
  ```

### 四、request

- request代表着请求所包含的所有信息,例如:request.path可以获取路径,request.method可以获取form表达提交的方法	

- ```
  #     print(request.path)  #request.path当前请求路径
  #     print(request.method) #当前请求方法(get,post...)
  #     print(request.GET)
  #     print(request.POST)
  #     print(request.body)
  #     # request.GET 获取所有get请求携带过来的数据
  #     # request.POST 获取所有post请求携带过来的数据
  #     # request.body 获取所有post请求携带过来的数据的原始格式
  ```

- ```
  验证post请求时,记得改一下配置,在settings配置文件中
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      # 'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]
  
  ```

- request.POST.dict():将post请求获取的数据转成字典类型,且需要删除del data["csrfmiddlewaretoken"]

- request.GET或request.POST这样的数据类型类似与字典,可以通过get方法按键取值,如果值是列表需要用getlist方法才能完整取到