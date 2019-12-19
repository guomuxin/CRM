# D54 AJAX,文件上传

## 一、AJAX

- 特点:局部刷新,异步请求

- 作用:代替浏览器进行数据的接发,避免每次发送数据都刷新页面,使用ajax后浏览器的请求实际上是发送给ajax程序,然后由ajax发送给服务端,服务端也将回复发送给ajax然后转给浏览器

- 写法:

  ```
  <script>
      $('#sub').click(function () {
          uname = $('#uname').val()   //要发送的请求数据先取出来
          pwd = $('#pwd').val()
          csrfmiddlewaretoken = $('[name=csrfmiddlewaretoken]').val()
              $.ajax(
          {
              url:"/login/",
              type:'post',
              data:{'uname':uname,'pwd':pwd,'csrfmiddlewaretoken':csrfmiddlewaretoken},
              //如果是get方法或者没有数据时此项可不写
              success:function (res) {  //请求成功后进行的操作,参数是拿到的响应数据,无论服务端怎么发接受到的都是字符串
                  if(res == "ok"){
                      console.log("a")
                  }
                  else {
                      $("span").text("用户名..")
                  }
              }
          }
      )
      })
  ```

- ajax通过csrf_token认证

  - 方式一:

    ```
    hmtl:
    		!!!!{% csrf_token %} 
            用户名: <input type="text" id="uname">
            密码: <input type="password" id="pwd">
            <button id="sub">提交</button>
    	
    	js代码:
                $('#sub').click(function () {
    
                var uname = $('#uname').val();
                var pwd = $('#pwd').val();
                # 获取到{% csrf_token %}这个模板渲染语法渲染之后的input标签对应的值
                !!!!var xxx = $('[name="csrfmiddlewaretoken"]').val();
    
                $.ajax({
                    url:'{% url "login" %}',  // 127.0.0.1:8000/login/
                    type:'post',
                    # 给post请求提交的数据中添加上csrf_token认证所需要的键值对
                   !!! data:{'uname':uname,'pwd':pwd,'csrfmiddlewaretoken':xxx},
                    success:function (res) {
                        console.log('>>>>',res);
                        if (res !== 'ok'){
                            $('#error').text('用户名或者密码有误!')
    
                        }else {
                            location.href='/home/';
                        }
    
                    }
    
                })
    
    
            })
    
    ```

  - 方式二:

    ```
    tml
                用户名: <input type="text" id="uname">
                密码: <input type="password" id="pwd">
                <button id="sub">提交</button>
            js代码:
            	$('#sub').click(function () {
    
            var uname = $('#uname').val();
            var pwd = $('#pwd').val();
            // var xxx = $('[name="csrfmiddlewaretoken"]').val();
    
            $.ajax({
                url:'{% url "login" %}',  // 127.0.0.1:8000/login/
                type:'post',
                # data数据部分的csrf_token认证的键值对的值直接写{{ csrf_token }} ,经过模板渲染之后,它直接就是那个input标签的value值
                data:{'uname':uname,'pwd':pwd,'csrfmiddlewaretoken':'{{ csrf_token }}'},
                success:function (res) {
                    console.log('>>>>',res);
                    if (res !== 'ok'){
                        $('#error').text('用户名或者密码有误!')
    
                    }else {
                        location.href='/home/';
                    }
    
                }
    
            })
    
        })
    ```

    

## 二、form表单上传文件

```
html代码:  注意:form表单标签的 enctype="multipart/form-data"这个属性要写才能上传文件,content-type请求头中的携带数据的消息格式
    <form action="" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        用户名:<input type="text" name="username">
        头像: <input type="file" name="file_obj">
        <input type="submit">
    </form>

views:
    def upload(request):
        if request.method == 'GET':
            return render(request,'upload.html')
        else:
            print(request.POST)
            print(request.FILES)
            file_obj = request.FILES.get('file_obj')  //这个file_obj是一个文件句柄
            # f = open('xx','rb')
            # for i in f:
            #     print(i)
            print(file_obj.name)
            with open(file_obj.name,'wb') as f:
                # for i in file_obj:
                #     f.write(i)
                for i in file_obj.chunks():  #65536字节  //普通的循环文件时是按行操作,使用chunks可以做到每次操作65536字节的数据
                    f.write(i)
            return HttpResponse('ok')
```

