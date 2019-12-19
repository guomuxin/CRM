# D56 cookie,session,中间件

## 一、cookie

- cookie的作用:由于http协议是无状态的,即每次连接不会保留期间产生的数据,也不会保留任何状态,这就造成某些我们需要的数据会无法保留,还有就是我们访问一个网站的不同页面时如果没有记录我们的登录状态就会导致每次访问都需要进行登录验证.为了避免以上问题,我们使用cookie来保存某些数据,以及记录我们的一些状态

- 什么是cookie:cookie是浏览器的技术,具体来说是服务器发给浏览器,并存储在本地的键值对,保存了我们需要的数据,浏览器每次访问服务器都会携带这些数据,服务器可以从请求中提取到这些信息

- cookie工作原理:浏览器第一次访问服务器会携带一个空的cookie,服务器产生数据后发送给浏览器,浏览器将其存在cookie中并保存在本地,下次访问服务器时就会带着这些数据一起访问,服务器可以通过这些数据判断浏览器的身份

- 一个浏览器对于同一个服务器来说只能保存20条cookie内的具体数据,本地cookie总共可以保存300个cookie,总大小不超过4kb

- django操作cookie

  ```
  设置cookie内容:通过HttpResponse对象进行设置(render,redirect本质也是HttpResponse对象),cookie可以设置多条,但都存在一个cookie中,以多个键值对的形式保存
      ret = HttpResponse("ok")
      普通cookie:ret.set_cookie(键,值)
      带签名的cookie:ret.set_signed_cookie(键,值,盐)
      return ret
      
      其他参数:max_age=5:超时时间设置为5秒
      		expires=具体时间:有效期至该时间
  ```

  ```
  获取cookie:由于cookie中的内容要经过网络传输,所以都经过json序列化,最终的到的数据无论之前是什么类型现在都是字符串,例如发送时的键值对为is_login:True,最终得到的is_login是'True'
  	普通cookie:request.COOKIE.get(键)     //request.COOKIE是一个字典类型的数据
  	带签名的cookie:request.get_signed_cookie(键,盐)
  ```

  ```
  删除cookie:
  	ret.delete_cookie(键)
  ```

  ```
  对登录状态进行记录的实例:
  def login(request):
  
      if request.method == "POST":
          uname = request.POST.get("uname")
          pwd = request.POST.get("pwd")
          if uname == "alex" and pwd == "123":
              ret = redirect("/home/")
              ret.set_cookie("is_login",True)
              return ret
          else:
              return render(request,"login.html")
      else:
          return render(request,"login.html")
  
  def home(request):
      print(request.COOKIES)
      is_login = request.COOKIES.get("is_login")
      if is_login == "True":
          return render(request,"home.html")
      else:
          return redirect("/login/")
  ```

  

## 二、session

- session是基于cookie,在后端进行某些加工后的技术,本质是将本要存储在本地的数据存在服务器的数据库上,并且只发送给浏览器一个随机字符串,作用类似于钥匙,浏览器下次请求服务器时通过钥匙找到属于自己的数据

- session的优势:非明文显示,长度不限

- django中使用session

  ```
  设置session:
      服务器端需要进行的操作:
      1.生成随机字符串sessionid
      2.将字符串发送给浏览器
      3.将字符串和数据(加密后的)存入数据库中的django_session表中
      django对以上过程进行了封装,使用时直接通过以下代码就可以完成以上功能:
      request.session[键] = 值 
  ```

  ```
  获取session:由于经过网络传输的内容只有sessionID,所以数据还是原类型
  	服务器端需要进行的操作:
  	1.取出cookie中携带随机字符串sessionid
  	xx = request.COOKIES.get('sessionid')
  	2.根据sessionid到数据库中查找对应的数据
  	data = select session_data from django_session where session_key = xx;
  	3.拿出记录中的session_data,并对其解密
  	dic = sss(data) -- {'is_login':True}
      dic.get('is_login') -- True
  	django封装后:
  	data = request.session.get(键)
  	data就是保存的数据键值对的值
  ```

  ```
  注销session:
  	服务器端需要进行的操作:
  	1.删除cookie中的sessionid这个键值对
  	2.数据库中删除这条数据
  	request.session.flush()
  	
  ```

  ```
  session验证登录实例:
  def login(request):
  
      if request.method == "POST":
          print(11)
          uname = request.POST.get("uname")
          pwd = request.POST.get("pwd")
          if uname == "alex" and pwd == "123":
              request.session['is_login']=True
              return redirect("/home/")
          else:
              return render(request,"login.html")
  
      else:
          return render(request,"login.html")
  
  def home(request):
      print(request.COOKIES)
      is_login = request.session.get("is_login")
      if is_login == True:
          return render(request,"home.html")
      else:
          return redirect("/login/")
  
  def logout(request):
      request.session.flush()
      return HttpResponse("ok")
  ```

  

- cookie和session对比:

  - cookie:
    - 作用:保持会话
    - 有大小限制
    - 有个数限制
  - session:
    - 比cookie安全
    - 没有大小限制
    - 可以配置多个存储方案,可以配置到缓存中以加快读取速度

## 三、中间件

- django请求的生命周期
  - 1.浏览器接收到请求后在wsgi文件中将其封装成socket,并将信息封装成request对象
  - 2.请求被提交给中间件,按照列表从上到下的顺序依次执行每个中间件的process_request方法
  - 3.请求被发送到url控制器中查找对应的views函数
  - 4.执行对应的views函数,并进行数据库,模板相关的操作
  - 5.执行完毕后将响应发送给中间件,从下到上依次执行每个中间件的process_response方法,如果没有则跳过该中间件,每个process_response方法都应该将response对象返回,否则下一个中间件接收不到响应,如果都没有process_方法则直接交给wsgi
  - 6.wsgi将响应读取并交给浏览器显示
  - ![img](https://img2018.cnblogs.com/blog/988061/201903/988061-20190307152249812-1922952163.png)

- 中间件:request和response处理之间的一道处理过程,作用就是在视图函数执行前后进行一些额外的操作,本质是一个自定义类,django会在特定时间去执行其中的一些方法

- MIDDLEWARE配置项是一个列表，列表中是一个个字符串，这些字符串其实是一个个类，也就是一个个中间件。

- 自定义中间件:

  - 中间件的五个方法:(常用的是process_request),参数必须给全

    - process_request(self,request)
    - process_view(self, request, view_func, view_args, view_kwargs)
    - process_template_response(self,request,response)
    - process_exception(self, request, exception)
    - process_response(self, request, response)

    以上方法如果返回值是None就会继续向后执行,如果是HttpResponse对象则返回给用户,不会直接返回给用户,而是通过process_response方法返回.process_response中.当用户发起请求的时候会依次经过所有的的中间件，这个时候的请求时process_request,最后到达views的函数中，views函数处理后，在依次穿过中间件，这个时候是process_response,最后返回给请求者。

  - 自定义的中间件是一个继承了MiddlewareMixin的类

    ```
    例:自定义中间件达到登录验证的效果
    新创建文件夹mymiddleware,新建文件login_check:
    from django.utils.deprecation import MiddlewareMixin
    from django.shortcuts import redirect,render,HttpResponse
    
    class LoginCheck(MiddlewareMixin):
        white_list = ['/login/']     //白名单,避免无限重定向
        def process_request(self,request):
            if request.path in self.white_list:
                return None
            if request.session.get("is_login"):
                pass
            else:
                return redirect("/login/")
    ```

    ```
    MIDDWARE中添加该类:
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'app01.mymiddleware.login_check.LoginCheck', !!!!//新添加的类路径及类名
    ]
    ```

    ```
    views中函数:
    def home(request):
    
            return render(request,"home.html")
    
    ```

  - process_response方法:响应时会执行的方法

  - process_view(self, request, view_func, view_args, view_kwargs)方法:在url找到路径执行views函数前会执行这里,view_func就是对应的view函数,后面两个分别为给view函数的位置参数和关键字参数

    ![img](https://images2018.cnblogs.com/blog/877318/201805/877318-20180523150722556-373788290.png)

  - 方法的执行顺序

    - 1.按照MIDDLEWARE列表中的顺序正序执行所有的process_request方法
    - 2.按照MIDDLEWARE列表中的顺序正序执行所有的process_view方法
    - 3.执行view函数中的方法
    - 4.按照MIDDLEWARE列表中的顺序倒序执行所有的process_response方法