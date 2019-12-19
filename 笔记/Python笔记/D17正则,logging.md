# Python基础DAY17

## 一、re正则表达式

- 什么是正则:

  正则就是用一些具有特殊含义的符号组合到一起（称为正则表达式）来描述字符或者字符串的方法。或者说：正则就是用来描述一类事物的规则。

- 贪婪匹配与非贪婪匹配:个人理解就是只要还能取就继续取,直到达到最大要求不能再取元素就是贪婪匹配

- 元字符:

  - \w:匹配字母数字中文下划线	

    ```
    s = "1a,23ggsg分割4啊"
    print(re.findall("\w",s))
    输出结果:
    ['1', 'a', '2', '3', 'g', 'g', 's', 'g', '分', '割', '4', '啊']
    ```

  - \W:匹配特殊字符,即非字母数字中文下划线	

    ```
    s = "1a,23ggsg分割4啊"
    print(re.findall("\W",s))
    输出结果:
    [',']
    ```

  - \s:匹配空白符

    ```
    s = "1a,23g gsg 分割4啊"
    print(re.findall("\s",s))
    输出结果:
    [' ', ' ']
    ```

  - \S:匹配非空白符

    ```
    s = "1a,23g gsg 分割4啊"
    print(re.findall("\S",s))
    输出结果:
    ['1', 'a', ',', '2', '3', 'g', 'g', 's', 'g', '分', '割', '4', '啊']
    ```

  - \d:匹配数字

    ```
    s = "1a,23g gsg 分割4啊"
    print(re.findall("\d",s))
    输出结果:
    ['1', '2', '3', '4']
    ```

  - \D:匹配非数字

    ```
    s = "1a,23g gsg 分割4啊"
    print(re.findall("\D",s))
    输出结果:
    ['a', ',', 'g', ' ', 'g', 's', 'g', ' ', '分', '割', '啊']
    
    ```

  - \A:匹配字符串开头

    ```
    s = "1a,23g gsg 分割4啊"
    print(re.findall("\A1a",s))
    输出结果:
    ['1a']
    ```

  - ^:匹配字符串开头

    ```
    s = "1a,23g gsg 分割4啊"
    print(re.findall("^1a",s))
    输出结果:
    ['1a']
    ```

  - \z:匹配字符串结尾,除换行符外

    ```
    小写z实测会出错,原因不详
    s = "1a,23g gsg 分割4啊"
    print(re.findall("啊\Z",s))
    输出结果:
    ['啊']
    ```

  - $:匹配字符串结尾,除换行符外

    ```
    s = "1a,23g gsg 分割4啊"
    print(re.findall("啊\Z",s))
    输出结果:
    ['啊']
    ```

  - \n:匹配一个换行符

    ```
    s = """
    aaadada
    asd
    """
    print(re.findall("\n",s))
    输出结果:
    ['\n', '\n', '\n']
    ```

  - \t:匹配一个制表符

  - .:匹配所有,除换行符,当re.DOTALL标记被指定

    ```
    print(re.findall(".","""abc,.
    """,re.DOTALL))
    输出结果:
    ['a', 'b', 'c', ',', '.', '\n']
    
    print(re.findall(".","""abc,.
    """))
    输出结果:
    ['a', 'b', 'c', ',', '.']
    ```

  - *:匹配多个或0个左边的元素(贪婪匹配)

    ```
    s = "1a,23g gsgg 分割4啊"
    print(re.findall("g*",s))
    输出结果:
    ['', '', '', '', '', 'g', '', 'g', '', 'gg', '', '', '', '', '', '']
    ```

  - +:匹配1个或多个左边的元素(贪婪匹配)

    ```
    s = "1a,23g gsgg 分割4啊"
    print(re.findall("g+",s))
    输出结果:
    ['g', 'g', 'gg']
    ```

  - ?:匹配0个或一个左边的元素(非贪婪匹配),一个重要的用途就是与+或*一起使用防止贪婪匹配

    ```
    s = "1a,23g gsgg 分割4啊"
    print(re.findall("g?",s))
    输出结果:
    ['', '', '', '', '', 'g', '', 'g', '', 'g', 'g', '', '', '', '', '', '']
    ```

  - {n}:匹配n个前面的元素

    ```
    s = "1a,23g gsgg 分割ggg4啊"
    print(re.findall("g{2}",s))
    输出结果:
    ['gg', 'gg']
    ```

  - {n,m}:匹配n-m次前面的元素(贪婪匹配)

    ```
    s = "1a,23g gsgg 分割gggggg,gggg4啊"
    print(re.findall("g{0,5}",s))
    输出结果:
    ['', '', '', '', '', 'g', '', 'g', '', 'gg', '', '', '', 'ggggg', 'g', '', 'gggg', '', '', '']
    ```

  - {a|b}:匹配a或者b

    ```
    s = "1a,23g gsgg 分割g,gggg4啊"
    print(re.findall("1|g",s))
    输出结果:
    ['1', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
    ```

  - ():匹配括号内的表达式,也表示一个组

    ```
    s = "1a23ggsgg 分割g,gggg4啊"
    print(re.findall("a(2\w)g",s))
    输出结果:
    ['23']
    ```

  - []:指定匹配范围(多个范围之间不需要加空格)

    ```
    s = "1a23ggsgg 分割g,gggg4啊"
    print(re.findall("[1-9a-z]",s))
    输出结果:
    ['1', 'a', '2', '3', 'g', 'g', 's', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '4']
    ```

- 匹配方式:

  - .*:匹配0个或多个任意字符

    ```
    s = "1a23ggsgg 分割g,gggg4啊啊啊啊啊啊啊啊啊啊"
    print(re.findall(".*",s))
    输出结果:
    ['1a23ggsgg 分割g,gggg4啊啊啊啊啊啊啊啊啊啊', '']
    ```

  - .+:匹配一个或多个任意字符

    ```
    s = "1a23ggsgg 分割g,gggg4啊啊啊啊啊啊"
    print(re.findall(".+",s))
    输出结果:
    ['1a23ggsgg 分割g,gggg4啊啊啊啊啊啊']
    ```

  - a*:匹配0个或多个a字符:

    ```
    s = "1a23gg啊sgg 分啊割g,gggg4啊啊啊"
    print(re.findall("啊*",s))
    输出结果:
    ['', '', '', '', '', '', '啊', '', '', '', '', '', '啊', '', '', '', '', '', '', '', '', '啊啊啊', '']
    ```

  - a+:匹配1个或多个a字符:

    ```
    s = "1a23gg啊sgg 分啊割g,gggg4啊啊啊"
    print(re.findall("啊+",s))
    输出结果:
    ['啊', '啊', '啊啊啊']
    ```

- 常用方法:

  - findall:全部找到返回到一个列表

  - search:从字符串的任意位置匹配查找,找到就返回一个对象,里面span就是查找元素的位置范围.想要查看取到的值必须用group方法,找不到返回None

    ```
    s = "1a23gg啊sgg 分啊割g,gggg4啊啊啊"
    print(re.search("sg",s))
    print(re.search("sg",s).group())
    输出结果:
    <re.Match object; span=(7,9), match='g'>
    sg
    
    s = "1a23gg啊sgg 分啊割g,gggg4啊啊啊"
    print(re.search("b",s))
    输出结果:
    None
    ```

  - match:从字符串的开头进行匹配查找,找到就返回一个对象,里面span就是查找元素的位置范围.想要查看取到的值必须用group方法,找不到返回None

    ```
    s = "1a23gg啊sgg 分啊割g,gggg4啊啊啊"
    print(re.match("1a",s))
    print(re.match("1a",s).group())
    输出结果:
    <re.Match object; span=(0, 2), match='1a'>
    1a
    ```

  - split:按照列表里的元素分割,可以写多个,中间不需要空格或,分隔

    ```
    s = "1a23gg啊,s,gg. 分啊,,割g,gggg4啊啊啊"
    print(re.split('[,.]',s))
    输出结果:
    ['1a23gg啊', 's', 'gg', ' 分啊', '', '割g', 'gggg4啊啊啊']
    ```

  - sub(被替换的元素,新元素,字符串对象):将旧元素全部替换成新元素

    ```
    s = "1a23gg啊,s,gg. 分啊,,割g,gggg4啊啊啊"
    print(re.sub("啊","a",s))
    输出结果:
    1a23gga,s,gg. 分a,,割g,gggg4aaa
    ```

  - compile:自定义匹配规则

    ```
    obj = re.compile("\d{2}")
    s = "1a23gg啊,s,gg. 分啊,,割g,gggg4啊啊啊"
    print(obj.findall(s))
    输出结果:
    ['23']
    ```

  - findfilter:返回一个迭代器,每个元素都是一个Match对象,用group才可以取到内容

    ```
    g = re.finditer("\d",s)
    print(g)
    print(next(g))
    print(next(g).group())
    输出结果:
    <callable_iterator object at 0x03B3EE50>
    <re.Match object; span=(0, 1), match='1'>
    2
    ```

    

## 三、logging日志

- 作用:

  1.记录程序的运行状态,例如时间,文件名,报错行数,错误信息等

  2.分析用户的喜好操作

  3.流水记录,例如银行

- 日志的级别:

   1.debug 调试  10 

   2.info 信息      20

   3.warning 警告   30

   4.error 错误    40

   5.critical 危险  50

- 基础版logging

  ```
  import logging
  logging.basicConfig(
      level=10,
      format = "%(asctime)s %(name)s %(filename)s %(lineno)s %(message)s",
      datefmt="%Y-%m-%d %H:%M:%S",
      filename="test.log",
      filemode="a",
  )
  logging.debug("这是调试")
  logging.info("这是信息")
  logging.warning("这是警告")
  logging.error("这是错误")
  logging.critical("这是危险")
  ```

  基础版的缺陷:1.编码不能修改.2.屏幕和文件不能同时有

- 进阶版logging

  ```
  import logging
  looger = logging.getLogger() # 创建一个空架子
  fh = logging.FileHandler('test1.log',mode="a",encoding="utf-8")
  # 创建一个文件句柄,用来记录日志(文件流)
  ch = logging.StreamHandler()
  # 创建一个屏幕流,打印记录的内容
  f_str = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)s %(message)s")
  # 定义一个记录日志的格式
  looger.level = 10
  # 设置一个记录级别
  
  fh.setFormatter(f_str)  # 给文件句柄设置记录内容的格式
  ch.setFormatter(f_str)  # 给中控台设置打印内容的格式
  looger.addHandler(fh)   # 将文件句柄添加的looger对象中
  looger.addHandler(ch)   # 将中控台添加的looger对象中
  
  looger.debug(1234)     # 咱们二次开发实现的
  looger.info(1234)      # 咱们二次开发实现的
  looger.warning(1234)   # 咱们二次开发实现的
  looger.error(1234)     # 咱们二次开发实现的
  looger.critical(1234)  # 咱们二次开发实现的
  ```

  