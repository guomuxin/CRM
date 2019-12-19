# D51 orm的查询

## 一、补充:静态文件的另一种配置方法

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{% static 'bootstrap-3.3.7-dist/css/bootstrap.min.css' %}">
</head>
<body>

</body>
<script src="{% static 'jquery.js' %}"></script>
<script src="{% static 'bootstrap-3.3.7-dist/js/bootstrap.min.js' %}"></script>
</html>
```

## 二、编辑按钮携带数据

```
<a href="{% url 'book_edit' %}?book_id={{ book.id }}" class="btn btn-warning btn-sm">编辑</a>#}

{#   <a href="/book/edit/{{ book.id }}/" class="btn btn-warning btn-sm">编辑</a>#}

<a href="{% url 'book_edit' book.id %}" class="btn btn-warning btn-sm">编辑</a>
```

url别名反向解析时 如果需要参数怎么搞:

```
html
	{% url '别名' 3 %}         url(r'^index/(\d+)/',views.index,name='index');
	-- /index/3/
	
views视图
	reverse('index',args=(3,))    -- /index/3/
```

## 三、13个查询接口

```
1.all():获取所有内容,结果是一个QuerySet,类似列表,可以用索引取值
ret = models.UserInfo.objects.all()

2.get(条件):能且只能获取一条数据,若没有符合条件的数据或有多条符合条件的数据都会报错,获取的结果是一个对象,可以直接通过.来取详细内容
ret = models.UserInfo.objects.get(id=1)
print(ret.name)
结果:xiaoming
如果是all或者filter获取的结果.name会报错

3.filter(条件):queryset或objects调用,获取所有符合条件的数据,返回一个QuerySet
ret = models.UserInfo.objects.all().exclude(id=2)
返回QuerySet

4.exclude(条件):queryset或objects调用,排除符合条件的数据
返回QuerySet

5.order_by(属性):queryset类型数据调用,按某种属性排序,如需降序,在属性前加"-",默认按照id升序
ret = models.UserInfo.objects.all().order_by("age","-id"):先按照年龄升序排列,再按照id降序排列
返回QuerySet

6.reverse():queryset类型数据调用,对已经排序过的QuerySet类型数据反转,必须是经过order_by排序后才能使用reverse()
ret = models.UserInfo.objects.all().order_by("age").reverse()
返回QuerySet

7.count():queryset类型的数据来调用，返回数据库中匹配查询(QuerySet)的对象数量。

8.first():queryset类型数据或objects调用,返回第一条记录

9.last(),queryset类型数据或objects调用,返回最后一条数据

10.exists():queryset或objects调用,只有结果中有数据就返回True,没有返回False

11.values():返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列,只要是返回的queryset类型，就可以继续链式调用queryset类型的其他的查找方法，其他方法也是一样的。也就是说values()后的值可以继续调用其他方法
values()可以指定只要部分元素
ret = models.UserInfo.objects.all().values("id","name")
<QuerySet [{'id': 5, 'name': 'huhu'}, {'id': 2, 'name': 'xiaohei'}, {'id': 3, 'name': 'xiaohong'}, {'id': 4, 'name': 'xiaohuang'}]>

12.values_list(*field):它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列

13.distinct():values和values_list得到的queryset类型的数据来调用，从返回结果中剔除重复纪录,通常与values()一起用
ret = models.UserInfo.objects.all().values("age").distinct()

```

## 四、模糊查询

```
1.age__in[10,32]:age属性在列表内的所有数据
2.age__gt=15:age大于15的所有数据
3.age__lt=15:age小于15的所有数据
4.age__gte=10:age大于等于15的所有数据
5.age__lte=10:age小于等于15的所有数据
6.age__range=[10,28]:大于等于10,小于等于28
7.name__contains="xiao":名字中包含xiao的数据
8.name__icontains="X":名字中包含X或x的数据
9.name__startwith="x":名字以x开头的数据
10.name__istartwith="X":名字以X或x开头的数据
11.name__endwith="i":名字以i结尾的数据
12.name__iendwith="I:名字以I结尾或i结尾的数据
13.date__year=2012:日期是2012年的数据
14.date__month=1:日期是1月的数据
15.date__day=2:日期是2号的数据
```

## 五、关于时间类型的问题

- 如果input的type为date时,传输的数据需要先经过date过滤器设置成YYYY-mm-dd格式才能正常显示
- 传时间类型数据时可以直接以YYYY-mm-dd格式上传,会自动转成时间格式



## 六、request获取数据写入数据库的简便方法

```
data = request.POST.dict()
del data["csrfmiddlewaretoken"]

models.book.objects.create(
**data
)
```

