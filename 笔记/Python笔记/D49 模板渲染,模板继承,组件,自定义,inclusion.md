# D49 模板渲染,模板继承,组件,自定义,inclusion

## 一、模板渲染

- for标签渲染

  ```
  示例:
  <ul>
      {% for i in l1 %}  #循环列表
          <li>{{ i }}</li>
      {% endfor %}
  </ul>
  
  <ul>
      {% for i in l1 reversed %}  #翻转循环列表时
          <li>{{ i }}</li>
      {% endfor %}
  </ul>
  
  <ol>
      {% for key in d1.keys %}  #循环字典的键
          <li>{{ key }}</li>
  
      {% endfor %}
      {% for key in d1.values %} #循环字典的值
          <li>{{ key }}</li>
  
      {% endfor %}
      {% for key,value in d1.items %} #循环字典的键值对
  {#        {{ forloop.counter }}#}
          <li>{{ forloop.last }}>>>>{{ key }}---{{ value }}</li>
          {% for foo in d1.hobby %}
              {{ forloop.parentloop.counter }}---{{ forloop.counter }}<a href="">{{ foo }}</a>
  
          {% endfor %}
  
      {% endfor %}
  
  </ol>
  
  
  forloop计数
      forloop.counter            当前循环的索引值(从1开始)，forloop是循环器，通过点来使用功能
      forloop.counter0           当前循环的索引值（从0开始）
      forloop.revcounter         当前循环的倒序索引值（从1开始）
      forloop.revcounter0        当前循环的倒序索引值（从0开始）
      forloop.first              当前循环是不是第一次循环（布尔值）
      forloop.last               当前循环是不是最后一次循环（布尔值）
      forloop.parentloop         本层循环的外层循环的对象，再通过上面的几个属性来显示外层循环的计数等
  
  
  
  empty
      {% for i in l1 %} #当没有数据时,会生成empty的内容
          <li>{{ i }}</li>
      {% empty %}
          <p>啥数据也没有!</p>
      {% endfor %}
  ```

- if标签:	if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断，注意条件两边都有空格

  ```
  {% if num == 11 %}
      <a href="">详细些</a>
  {% else %}
      <p>hahahhahah</p>
  {% endif %}
  
  多条件判断
      {% if num > 100 or num < 0 %}
          <p>无效</p>  <!--不满足条件，不会生成这个标签-->
      {% elif num > 80 and num < 100 %}
          <p>优秀</p>
      {% else %}  <!--也是在if标签结构里面的-->
          <p>凑活吧</p>
      {% endif %}
      
  结合过滤来使用
      {% if user_list|length > 5 %}  <!--结合过滤器来使用-->
        七座豪华SUV
      {% else %}
          黄包车
      {% endif %}
  ```

- with:给较长的数据调用起别名,只能在with内部使用

  ```
  dic = {"name":"guo","age":20,"hobby":["抽烟","喝酒","烫头"]}
  方式一:
      {% with dic.hobby.2 as c %}
          <h1>{{ c }}</h1>
      {% endwith %}
  方式二:
  	{% with c=dic.hobby.2 %}
          <h1>{{ c }}</h1>
      {% endwith %}		
  ```

- csrf_token:用于跨站请求伪造保护,django只允许自己在自己的页面中提交post请求,不是来自自己的页面的post请求会被拒绝,而标识是否是自己页面的方式就是csrf认证

  ```
  在form表单中的任何位置写上{% csrf_token %},模板渲染时会替换成<input type="hidden" name="csrfmiddlewaretoken" value="8J4z1wiUEXt0gJSN59dLMnktrXFW0hv7m4d40Mtl37D7vJZfrxLir9L3jSTDjtG8">,value是动态变换的
  ```

  

## 二、模板继承

- Django模版引擎中最强大也是最复杂的部分就是模版继承了。模版继承可以创建一个基本的“骨架”模版，它包含站点中的全部元素，并且可以定义能够被子模版覆盖的 blocks 。

  ```
  模板的定义:可以在任意位置定义block,包括css,js
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
  
      <style>
          .top{
              height: 100px;
              width: 100%;
              background-color: red;
          }
  
      </style>
      {% block css %}
          <style>
                  .bloc{
              background-color: black;
          }
          </style>
      {% endblock %}
  
  </head>
  <body>
  <div class="top">
      <a href="http://127.0.0.1:8000/menu1/">菜单1</a>
  </div>
  <div class="content bloc">
      {% block content %}
          base
      {% endblock %}
  </div>
  </body>
  
  {% block js %}
  
  {% endblock %}
  
  </html>
  ```

  ```
  继承模板:所有模板中block定义的地方都可以进行替换,需要先extends继承,然后对每个block分别进行替换,名称要一一对应
  {% extends "base.html" %}
  {% block css %}
          <style>
                  .bloc{
              background-color: blue;
          }
          </style>
  {% endblock %}
  {% block content %}
  
      menu1
  
  {% endblock %}
  {% block js %}
      <script>
      alert("welcome")
      </script>
  {% endblock %}
  ```

  ```
  block.super:可以在被替换的block内使用模板中的原内容:
  {% block content %}
      {{ block.super }}
      menu1
  
  {% endblock %}
  这样的效果就是既有模板中的base,也有新页面中的menu1
  ```

- 为了增强可读性,endblock也可以写名字

## 三、组件

- 组件就是使用某个页面中写好的功能直接用

  ```
  组件的引用:会导入目标文件中的所有内容
  {% include "zujian.html" %}
  ```

## 四、自定义过滤器和标签

- 自定义过滤器:

  - 1.在app应用文件夹内创建templatetags文件,并且名字必须是这个

  - 2.创建py文件,任意名字

  - 3.定义过滤器

    ```
    from django import template
    register = template.Library()  //变量名必须是这个,注意Library的L是大写
    
    @register.filter
    def filter01(v1):			//如果过滤器需要参数,函数形参写两个,第二个就是参数,最多
        return str(v1)+"xx"		//两个
    ```

  - 4.使用过滤器

    ```
    {% load my_tags %}
    <h1>{{ num|filter01 }}</h1>
    
    ```

- 自定义标签

  - 与自定义过滤器基本一样,只是使用的装饰器不同,以及使用方法不同,还有就是标签的参数不限个数

  - 标签的定义

    ```
    @register.simple_tag
    def tag01(v1,v2,v3):
        return v1+v2+v3+"xx"
    ```

  - 标签的使用

    ```
    {% load my_tags %}
    <h1>{% tag01 num "a" "bss" %}</h1>
    ```

- inclusion_tag

  ```
  定义组件:具体标签数量用循环表示,循环的内容从外部获取
  <div class="menu">
      {% for i in data %}
          <div class="item">
              <a href="">{{ i }}</a>
          </div>
      {% endfor %}
  </div>
  ```

  ```
  在my_tags中定义inclusion_tags:
  @register.inclusion_tag("base_menu.html")//参数为组件所在html
  def set_menu(l):
      return {"data":l} //这里键要和组件中循环的数据名字一致
  ```

  ```
  views函数:从后台传入要循环的数据,也就是真正要显示的数据
  def base_menu(request):
      l = ["菜单1","菜单2","菜单3"]
      return render(request,"base_menu.html",{"data":l})
  
  def menu_1(request):
      l = ["商城","后台","个人中心"]
      return render(request,"menu_1.html",{"data":l})
  ```

  ```
  使用组件的页面:
  <body>
      {% load my_tags %}
      {% set_menu data %} 
  </body>
  ```

  ![1574163256541](C:\Users\WO\AppData\Roaming\Typora\typora-user-images\1574163256541.png)

