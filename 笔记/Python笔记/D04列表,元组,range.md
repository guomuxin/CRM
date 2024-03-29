# Python基础DAY04

## 一、列表

- 格式：变量名["内容1","内容2","内容3"...]，每个元素之间用逗号分隔。列表是是python中的数据结构之一
- 作用：1.用于存储大量数据。本质上是一个容器。2.用于存储不同类型的数据
- 注意:可变类型的数据进行操作后不需要重新赋值,图中第二种方法会输出None![1568194363888](.\Python基础DAY04.assets\1568194363888.png)
- 列表的存储方式（简要版):![1568103020796](.\Python基础DAY04.assets\1568103020796.png)
- 列表的增加：（定义一列表为names = ["guo","mu","xin"]）
  - names.append（内容）:添加到列表最后
  - names.insert(索引，"内容")：将内容插入到指定位置
  - names.extend(可迭代对象)：迭代添加
- 列表内容的删除：
  - names.remove(内容)：从左往右开始删除第一个该内容元素
  - names.pop（）:默认删除列表的最后一个，可以加索引参数删除指定位置的元素,返回值是被删除的元素
  - names.clear():清空整个列表
  - del names[索引]：删除指定位置的元素，可用于删除多个元素
  - del names:删除整个列表
  - ![1568103150028](\Python基础DAY04.assets\1568103150028.png)
- 列表内容的修改：
  - 就是切片的使用。例如：names[2],names[1:4]
  - 使用切片时，获取内容的数据类型就是其本身的数据类型，例如print("fasfas"[1:3])获取的内容是字符串，print(names[1:3])获取的内容还是列表，每个元素都是其本身的类型
  - 切片获得的内容空间是连续的时候，修改的内容可以多也可以少
  - 切片获得的内容空间是不连续的时候，必须一一对应
  - ![1568103127849](.\Python基础DAY04.assets\1568103127849.png)
- 总结：
  - 列表是可变数据类型，可迭代数据类型，有序的数据结构
  - 用于存储大量数据，存储不同类型的数据
  - 列表就是一个容器



## 二、元组

- 定义：元组本质上就是不可变的列表
- 元组的应用场景：
  - 用于配置文件当中
  - 为了防止误操作时修改数据，元组用于存放一些重要信息
- 面试题：
  - a(10):这是一个整型数据，a("fdsf")：这是一个字符串类型数据。当括号中没有逗号出现时，其类型就是该数据本身的类型
  - a(10,):这是一个元组
  - a():这也是元组
- 总结：元组是一个有序，不可变，可迭代数据类型



## 三、range

- 定义：范围

- 作用：可以将不可迭代的整型数据进行迭代操作

- python2和python3中的range的区别：

  - python2中打印range获取的是一个列表
  - python3中打印range就是range本身

- range与切片用法大致相似，只是在range中要用逗号分隔，同样是顾头不顾尾

  - 一般情况下可以直接写一个终止位置，使用步长时要添加起始位置，例如range(10)表示从第一个元素到第十10个元素，不包括第10个

  - 输出1-50内的偶数：

    for i in range(0,51,2)

  - 输出1-50内的奇数：

    for i in range(1,51,2)

- range是一个可迭代对象