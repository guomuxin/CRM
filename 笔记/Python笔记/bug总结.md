1.TypeError: unsupported operand type(s) for +: 'int' and 'str'

​	不支持对这样的对象类型进行+操作，一个int一个str

![1567671820586](.\bug总结.assets\1567671820586.png)

2.ValueError: invalid literal for int() with base 10: 'q'

不能用int()转换"q"这样的字符串

![1568123067660](.\bug总结.assets\1568123067660.png)

3. 大于号不可以比较字符串和int

![1568123199569](.\bug总结.assets\1568123199569.png)

4.RecursionError: maximum recursion depth exceeded

python中限定了最大的递归次数,10000左右,如果调用函数时不小心出错有可能会超过最大递归次数,从而报错

![1568814986211](C:\Users\WO\Desktop\Python笔记\bug总结.assets\1568814986211.png)

5.json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

​	load读不到数据,通常是由于格式错误,或者文件中的光标没有移到开头导致

![1569664132484](.\bug总结.assets\1569664132484.png)