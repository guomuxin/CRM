# D61 crm-建表及显示

## Models:

- ```
  qq = models.CharField(verbose_name='QQ', max_length=64, unique=True, help_text='QQ号必须唯一')
  
  
  verbose_name:对应modelform自动生成时的label值
  help_text:admin添加表内容时的提示信息
  ```

- ```
  sex_type = (('male', '男'), ('female', '女'))
  sex = models.CharField("性别", choices=sex_type, max_length=16, default='male', blank=True, null=True)
  
  choices:在表中存储对应元组的第一项,在视图函数或html页面中通过get_sex_display()方法可以获取元组第二项的内容
  blank=True:对应modelform自动生成时required验证条件
  ```

- ```
  date = models.DateTimeField("咨询日期", auto_now_add=True)
  
  auto_now_add=True:自动添加当前时间
  ```

- ```
  delete_status = models.BooleanField(default=False)
  
  用于假删除,展示内容时只展示此项为真的数据
  ```

- ```
  class Meta:    
  ordering = ['id',]    
  verbose_name='客户信息表'    
  verbose_name_plural = '客户信息表'
  
  
  Meta类是对此类进行一些配置
  ordering:默认以此项排序,可设置多个,也可倒序(加负号)
  verbose_name:在admin页面中显示的表名为此
  verbose_name_plural:在admin页面中显示的表名会自动加s,这个可以定制复数形式的展示内容
  ```

- ```
  def __str__(self):    
  	return self.name+":"+self.qq
  	
  admin添加数据后显示的信息
  ```

## 配置方面:

- 要在admin中操作表,需要现在admin.py中配置

  ```
  from django.contrib import admin
  
  # Register your models here.
  from app01 import models
  admin.site.register(models.Userinfo)
  admin.site.register(models.Customer)
  admin.site.register(models.Campuses)
  admin.site.register(models.ClassList)
  ```

- 添加超级用户:

  ```
  终端处输入命令:
  python manage.py createsuperuser
  ```

## Meta类常用参数:

```
model = models.Book  # 对应的Model中的类
fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
exclude = None  # 排除的字段  内容为列表
labels = None  # 提示信息
help_texts = None  # 帮助提示信息
widgets = None  # 自定义插件
error_messages = None  # 自定义错误信息
```

 

```
error_messages = {    'title':{'required':'不能为空',...} #每个字段的所有的错误都可以写，...是省略的意思，复制黏贴我代码的时候别忘了删了...}
```

## urlencode:

- 用于原样输出url中的内容(带&)
- 也可用于对url进行编码, 将&,/,?等转成特殊格式
- 需要使用QueryDict调用