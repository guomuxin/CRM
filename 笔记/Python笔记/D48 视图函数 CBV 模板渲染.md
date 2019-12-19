# D48 视图函数 CBV 模板渲染

## 一、视图函数补充

- redirect:将请求交给目标url,例如

  ```
  retuurn redirect("/page")
  将会从urls中查找"/page"路径,执行其后的函数
  ```

  与render的区别:render是直接提交一个html页面,redirect是执行目标的函数

## 二、CBV和FBV

- FBV:function based view :基于函数的视图逻辑

- CBV:class based view :基于类的视图逻辑

- FBV在urls中直接写函数名即可

- CBV在urls中的写法:

  ```
  urls(r"^home/",views.类名.as_view()):注意as_view后加括号
  ```

- CBV视图写法

  ```
  from django.views import View
  class LoginView(View):
      def dispatch(self, request, *args, **kwargs): //可以重写dispatch方法以实现在分
          print(11)								//	前后进行操作
          ret = super().dispatch(request,*args,**kwargs)
          print(22)
          return ret
      
      def get(self,request):						//函数名为请求方法名中的内容就行,不
          return render(request,"login.html")		//再判断request.method的内容
      
      def post(self,request):
          print(request.POST)
          return HttpResponse("登录失败")
  ```

- as_view源码分析

![1574059865818](C:\Users\WO\AppData\Roaming\Typora\typora-user-images\1574059865818.png)



## 三、CBV和FBV中的装饰器

- FBV中的装饰器就是正常的函数使用装饰器

- CBV中的装饰器:需要先导入from django.utils.decorators import method_decorator,使用method_decorator(装饰器名,name)添加装饰器

  - 在类中普通函数前使用:

    ```
    @method_decorator(wrapper)
        def get(self,request):
            return render(request,"login.html")
    ```

  - 在dispatch前使用

    ```
    @method_decorator(wrapper)
        def dispatch(self, request, *args, **kwargs):
            print(11)
            ret = super().dispatch(request,*args,**kwargs)
            print(22)
            return ret
    ```

  - 在类前声明使用装饰器的函数:name属性只能写一个函数名

    ```
    @method_decorator(wrapper,name="get")
    class LoginView(View):
     ....
    ```

## 四、模板渲染

- setting设置:用命令行创建的应用没有template模板,需要手动创建,并在setting中设置

  ```
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')]  #别忘了配置这个路径
          ,
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

- 模板语法

  - {{变量}}
  - {%逻辑%}

- 万能的据点:

  ```
  views函数:
  def testTemplate(request):
      num = 100
      lst = [1,2,3,4]
      dic = {"a":1,"b":2}
      class A:
          b = 10
          def run(self):
              return "run"
      return render(request,"testTemplate.html",{"num":num,"lst":lst,"dic":dic,"A":A})
      
  html页面:
  <h1>{{ num }}</h1>
  <h1>{{ lst.2 }}</h1>
  <h1>{{ dic.a }}</h1>
  <h1>{{ A.b }}</h1>
  <h1>{{ A.run }}</h1>  //调用方法时不可加括号,所以不能调用需要参数的函数
  ```

- 过滤器:

  - 用法:

    - 无参数:{{变量|过滤器}}
    - 有参数:{{变量|过滤器:"参数"}}

  - 内置过滤器:

    - default:当变量值为空或没有被传值的显示的内容

      ```
      <h1>{{ data|default:"没有数据" }}</h1>:当data为空或没赋值时显示没有数据
      ```

    - length:获取数据的长度

      ```
      以上述代码为例:
      <h1>{{ lst|length }}</h1>:显示结果:4
      ```

    - slice:切片

      ```
      <h1>{{ lst|slice:"0:3" }}</h1>:显示结果:[1,2,3]
      ```

    - date:日期格式化

      ```
      views代码:
      time = datetime.now()
      html代码:
      <h1>{{ time|date:"Y-m-d H:i:s" }}</h1>
      显示结果:2019-11-18 16:07:59
      ```

    - safe:Django的模板中在进行模板渲染的时候会对HTML标签和JS等语法标签进行自动转义，原因显而易见，这样是为了安全，django担心这是用户添加的数据，比如如果有人给你评论的时候写了一段js代码，这个评论一提交，js代码就执行啦，这样你是不是可以搞一些坏事儿了，写个弹窗的死循环，那浏览器还能用吗，是不是会一直弹窗啊，这叫做xss攻击，所以浏览器不让你这么搞，给你转义了。但是有的时候我们可能不希望这些HTML元素被转义，比如我们做一个内容管理系统，后台添加的文章中是经过修饰的，这些修饰可能是通过一个类似于FCKeditor编辑加注了HTML修饰符的文本，如果自动转义的话显示的就是保护HTML标签的源文件。为了在Django中关闭HTML的自动转义有两种方式，如果是一个单独的变量我们可以通过过滤

    - truncatechars:限制显示的字符个数,剩余内容用...表示,参数表示显示内容加...总共的长度

      ```
      views代码:
      s = "hello world my name is"
      html代码:
      <h1>{{ s|truncatechars:"4" }}</h1>
      显示内容:h...
      ```

    - truncatewords:限制显示的单词个数,以空格为分隔,剩余内容以...表示

      ```
      <h1>{{ s|truncatewords:"2" }}</h1>
      显示内容:hello world...
      ```

    - cut:去除指定元素

      ```
      <h1>{{ s|cut:"e" }}</h1>
      显示内容:hllo world my nam is
      ```

    - join:使用指定元素拼接

      ```
      <h1>{{ lst|join:"-" }}</h1>
      显示内容:1-2-3-4
      <h1>{{ s|join:"-" }}</h1>
      显示内容:h-e-l-l-o- -w-o-r-l-d- -m-y- -n-a-m-e- -i-s
      ```

      

## 四、静态文件配置

- 在项目中,css/js/img等都被称为静态项目,在django中直接把这些文件放到html的同级文件夹下并不能生效

- 静态文件的配置:

  ```
  setting文件中添加以下内容:
  STATIC_URL = '/statics/'
  
  STATICFILES_DIRS = (
      os.path.join(BASE_DIR, "放置静态文件的文件夹名"),
  )
  ```

  ```
  html文件中使用:
  <link href="/static/文件路径"   注:无论配置的路径是什么,这里都是static
  ```

  static其实是放置静态文件的文件夹的别名,当浏览器收到url中文件地址的内容是以/static开头时,就会去该文件夹下去查找静态文件,所以static前必须加/,如果不加就是在原页面的url后拼接static....进行请求,这样是找不到文件的

## 五、url斜杠

```
url(r'^home/', views.home),  #前置导航斜杠不需要写,后面的斜杠是根据django的配置来的,如果在settings配置文件中我们设置了
# APPEND_SLASH = False,那么浏览器发送来的请求如果没有带着后面的斜杠,也是可以正常请求的,但是如果没有这个配置的话,django要求浏览器必须带着路径后面的斜杠来进行访问,如果你输入路径的时候没有加/,那么django让你的浏览器发一个重定向请求带上/.
```

