# D55 ajax文件上传,jsonresponse,ajax弹框

## 一、ajax文件上传

- ajax文件的上传需要用到FormData,将所有要上传的数据全部塞入FormData对象中,包括csrf认证,ajax的data部分直接写FormData对象即可

-     processData: false,
      contentType: false,
      这两项配置必须写 ,与文件上传配套

- ```
  html:
  $('#sub').click(function () {
          uname = $('#uname').val()
          pwd = $('#pwd').val()
          file = $(':file')[0].files[0]  //$(':file')[00是将jquery对象转成原生js,因为只有js											有files属性
          var formdata = new FormData()    !!!!
          formdata.append('uname',uname)  !!!!
          formdata.append('pwd',pwd)
          formdata.append('file',file)
          formdata.append('csrfmiddlewaretoken', $('[name="csrfmiddlewaretoken"]').val())
          $.ajax(
              {
                  url: 'home/',
                  type: 'post',
                  processData: false,
                  contentType: false,
                  data: formdata,
                  success:function (data) {
                      console.log(data)
                  }
              }
          )
      })
  ```

  ```
  views:
  def home(request):
      if request.method == "GET":
          return render(request,"home.html")
      else:
          print(request.POST)
          file = request.FILES.get("file")
          with open(file.name,"wb") as f:
              for i in file.chunks():
                  f.write(i)
          return HttpResponse("ok")
  ```

  

## 二、JsonResponse

- 如果要将python中的字典传给js,需要先将字典序列化,然后在js端反序列化

  ```
  views:
         dic = {"name":"xiaoming","age":18}
          dic_json = json.dumps(dic)
          return HttpResponse(dic_json)
          
          如果在HttpResponse中写content_type='application/json'参数,html端得到的就是一个反序列化后的数据
          return HttpResponse(dic_json,content_type='application/json')
  ```

  

  ```
  html:
     success:function (data) {
                      
                      var dic = JSON.parse(data)
                      console.log(dic.name)
                  }
  ```

- 使用JsonResponse可以省略序列化与反序列化的过程

  ```
  JsonResponse实际上做的就是使用json传数据时的这两部:
  dic_json = json.dumps(dic)
  return HttpResponse(dic_json,content_type='application/json')
  也就是说html端收到的是反序列化后的数据类型
  ```

  ```
  views:
  from django.http import JsonResponse
  def home(request):
      if request.method == "GET":
          return render(request,"home.html")
      else:
          dic = {"name":"xiaoming","age":18}
          return JsonResponse(dic)
  ```

  ````
  html:
  success:function (data) {
  console.log(data,typeof data)
  
  }
  打印结果:name: "xiaoming", age: 18} "object"
  ````

- 如果传给js的数据类型不是字典,需要在后面加一个safe参数,设为False

  ```
  return JsonResponse(l1,safe=False)
  ```

  

## 三、json时间类型

- json本身不支持序列化时间类型(date,datetime)数据,需要重写json.JSONEncoder类的default方法

  ```
  序列化时间
  import json
  from datetime import datetime
  from datetime import date
  
  #对含有日期格式数据的json数据进行转换
  class JsonCustomEncoder(json.JSONEncoder):
      def default(self, field):
          if isinstance(field,datetime):
              return field.strftime('%Y-%m-%d %H:%M:%S')
          elif isinstance(field,date):
              return field.strftime('%Y-%m-%d')
          else:
              return json.JSONEncoder.default(self,field)
  
  
  d1 = datetime.now()
  
  dd = json.dumps(d1,cls=JsonCustomEncoder)
  print(dd)
  
  ```

## 四、弹框组件

- 组件下载地址:https://github.com/lipis/bootstrap-sweetalert

- 使用该组件需要先导入BootStrap,jquery

  ```
   $(".sub").on("click", function () {   
          ths = $(this)             //这里的$(this)是按钮
          swal({
                  title: "你确定要删除吗？",
                  text: "删除可就找不回来了哦！",
                  type: "warning",
                  showCancelButton: true,
                  confirmButtonClass: "btn-danger",
                  confirmButtonText: "我已经下定决心",
                  cancelButtonText: "容我三思",
                  closeOnConfirm: false
              },
              function () {           //如果在这里查看$(this)结果是swal对象
                  var deleteId = ths.attr('xx');
                  console.log(deleteId)
                  $.ajax({
                      url: "/app01/del/",
                      type: "post",
                      data: {"id": deleteId, csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()},
                      success: function (data) {
                          console.log(data, typeof data);
                          if (data['status'] === '1') {
                              ths.parent().parent().remove()
  
                              a = $("tr")
                              for (var i = 0; i < a.length; i++) {
                                  a.eq(i).find("td").eq(1).text(i)
                              }
  
                              swal("删除成功!", "你可以准备跑路了！", "success");
                          } else {
                              swal("删除失败", "你可以再尝试一下！", "error")
                          }
                      }
                  })
              });
      })
  ```

  