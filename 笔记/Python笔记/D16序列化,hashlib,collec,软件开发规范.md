# Python基础DAY16

## 一、序列化

- 什么是序列化:序列化就是将列表,字典等数据结构的数据转换成字符串或字节就是序列化

- 什么是反序列化:将符合格式的字符串或字节转回到列表和字典的过程就是反序列化

- 序列化的作用:当我们需要在文件中或网络上存储列表和字典格式的数据时,普通方法是不能写入的.这时就需要用到序列化将他们转换成字符串存入,需要时再转换成原数据类型使用,同时由于不同语言的数据类型不同,当要在不同语言间进行数据传输,就需要json这个中间人,先转换成字符串,再转换成字节, 然后发送.

  总结来说序列化有两个作用:

  1.文件读写数据

  2.网络传输

- 进行序列化的两种方式:

  - json:序列化后是字符串,所有语言通用
  - pickle:序列化后是字节,支持python中的大部分对象,但是只有python有

- json:

  - 支持的数据结构:dict,list, tuple,str,int, float,True,False,None

  - dumps和loads,dump和load必须成对使用

  - 作用:文件读写数据:dump,load

    ​		 网络传输:dumps,loads

  - dumps,loads:

    - 序列化:json.dumps(其他数据类型)

    - 反序列化:json.loads(字符串)

      ```
      a = json.dumps({"a":"AA"})
      print(a,type(a))
      b = json.loads(a)
      print(b,type(b))
      输出结果:
      {"a": "AA"} <class 'str'>
      {'a': 'AA'} <class 'dict'>
      ```

  - 其他参数:ensure_ascii:当它为True时,所有非ascii码字符显示为\uxxx序列,只需在dump时将改参数改为False即可,此时存入json中的中文就可以正常显示

  - json中的dump在写入多行数据时不会换行,所以再次load时会报错,可以采用以下方式:

    ```
  import json
    f = open("a.txt","a+",encoding="utf-8")
    f.seek(0)
    s = ["果","ad",12]
    f.write(json.dumps(s))
    for i in f:
        print(json.loads(i))
    #使用dumps先将数据转换成字符串,然后再写入
    ```
  
    
  
- pickle:

  - 支持大部分数据结构
  - 使用方法与json类似,但pickle的一个好处是dump读入多行时会自动换行

## 二、hashlib

- 什么是hashlib:可以叫做摘要算法,加密算法,哈希算法,散列算法,就是用来加密和校验

- 工作原理:通过一个函数,将一个任意长度的数据转换成一个固定长度的数据串(通常是16进制的字符串)

- 为什么要使用hashlib:如果把每个用户的密码都以明文的形式存储在数据库中,当数据库遭到入侵时所有用户的密码都一览无遗的展现给入侵者,账号的安全系数非常低,所以通常使用密文的方式存储密码,这样即使数据库被入侵黑客也无法获取我们的密码信息,而hashlib就是用来将明文数据转换为密文数据

- hashlib的特征以及使用要点:

  - 1.只能将bytes类型转换,所以要先encode
  - 2.bytes数据类型->hashlib算法->固定长度的字符串
  - 3.不同的bytes转换后的结果一定不同
  - 4.相同的bytes转换后的结果一定相同
  - 5.此转化过程不可逆

- 加密:

  - 加密方式现在常用的有md5,sha1,sha256,sha512

  - 普通的md5加密方式:

    ```
    import hashlib
    md5 = hashlib.md5()
    md5.update("1234".encode("utf-8"))  ## 必须是bytes类型才能够进行加密
    print(md5.hexdigest())
    输出结果:
    81dc9bdb52d04dc20036dbd8313ed055
    ```

  - 普通的md5加密方式其实不是特别安全,比如黑客比较常用的破解密码方法:撞库,将一些常见的密码md5加密后的算法保存,与你输入的密码对比,有几率破解你的密码,所以提出了"加盐"的方式提高安全性

    ```
    import hashlib
    md5 = hashlib.md5("name".encode("utf-8"))  #参数就是加的盐,本质就是在被保护的数据前面加一													上一个其他数据,然后将整体进行md5加密
    md5.update("1234".encode("utf-8"))
    print(md5.hexdigest())
    输出结果:
    a00f94d2c469ff7e3e9d708b8ac6ed30
    ```

  - 动态加盐:

    ```
    import hashlib
    name = input("请输入用户名")
    md5 = hashlib.md5(name.encode("utf-8"))
    md5.update("1234".encode("utf-8"))
    print(md5.hexdigest())
    
    输出结果:
    8aa777ce3fd59e27934a9d983c3f21f9
    ```

- 文件的一致性校验

  copy from:宝哥博客

  hashlib模块除了可以用于密码加密之外，还有一个常用的功能，那就是文件的一致性校验

  ​    linux讲究：一切皆文件，我们普通的文件，是文件，视频，音频，图片，以及应用程序等都是文件。我们都从网上下载过资源，比如我们刚开学时让大家从网上下载Python解释器，当时你可能没有注意过，其实你下载的时候都是带一个MD5或者shax值的，为什么？ 我们的网络世界是很不安全的，经常会遇到病毒，木马等，有些你是看不到的可能就植入了你的电脑中，那么他们是怎么来的？ 都是通过网络传入来的，就是你在网上下载一些资源的时候，趁虚而入，当然大部分被我们的浏览器或者杀毒软件拦截了，但是还有一部分偷偷的进入你的磁盘中了。那么我们自己如何验证我们下载的资源是否有病毒呢？这就需要文件的一致性校验了。在我们下载一个软件时，往往都带有一个MD5或者shax值，当我们下载完成这个应用程序时你要是对比大小根本看不出什么问题，你应该对比他们的md5值，如果两个md5值相同，就证明这个应用程序是安全的，如果你下载的这个文件的MD5值与服务端给你提供的不同，那么就证明你这个应用程序肯定是植入病毒了（文件损坏的几率很低），那么你就应该赶紧删除，不应该安装此应用程序。 

  我们之前说过，md5计算的就是bytes类型的数据的转换值，同一个bytes数据用同样的加密方式转化成的结果一定相同，如果不同的bytes数据（即使一个数据只是删除了一个空格）那么用同样的加密方式转化成的结果一定是不同的。所以，hashlib也是验证文件一致性的重要工具。

## 三、collections

- 统计:统计可迭代对象中每个元素出现了多少次,以字典格式存储,元素为key,出现次数为value

  ```
  import collections
  lst = [1,1,1,2,3,3,4]
  print(collections.Counter(lst))
  输出结果:
  Counter({1: 1, 2: 1, 3: 1, 4: 1})
  ```

- 命名元组nametuple:生成可以用名字来访问的元组,例如时间元组

  ```
  
  ```

- 队列与栈:

  - 队列:先进先出,例如排队取款
  - 栈:先进后出:例如坐电梯

- 双向队列deque:实现高效插入和删除,可以双向进出,效率高

  ```
  双向添加:
  q = collections.deque([1,2,3,4])
  q.append("a")
  q.appendleft("b")
  print(q)
  输出结果:
  deque(['b', 1, 2, 3, 4, 'a'])
  双向删除:
  print(q.pop())
  print(q.popleft())
  print(q)
  输出结果:
  a
  b
  deque([1, 2, 3, 4])
  ```

- 有序字典OrderedDict:此类型专用于python2中,因为python3中的字典已经改成默认按照添加顺序排列,而python2中的字典是完全无序的,排序顺序是插入顺序

  ```
  od = collections.OrderedDict([("a","aa"),("b","bb")])
  print(od)
  输出结果:
  OrderedDict([('a', 'aa'), ('b', 'bb')])
  ```

- 默认字典defaultDict:

  ```
  如果有一个列表,希望将所有大于66的元素用一个键值对表示,其余的用另一个键值对表示
  values = [11, 22, 33,44,55,66,77,88,99,90]
  my_dict = defaultdict(list)
  
  for value in  values:
      if value>66:
          my_dict['k1'].append(value)
      else:
          my_dict['k2'].append(value)
  ```


四、软件的开发规范

- 为什么要有软件开发规范:

  在后期真正写项目的时候,代码量巨大,如果还都放在一个py文件下,无论是让别人查看,还是排查bug都会非常困难,所以要将代码份文件处理,规范你的项目目录结构，代码规范，遵循PEP8规范,这样就会变得更加清晰

- 具体的文件存放位置

  bin:存放启动文件(start.py)

  conf:存放固定的配置文件(setting.py)

  db:存放和程序有关的一些数据

  core:存放主逻辑代码(src.py)

  lib:存放公用的函数,即公共组件代码(commom.py)

  log:存放日志

  

  