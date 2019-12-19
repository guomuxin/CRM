# 1.
# 请写出下列代码的执行结果：
# 例一：
#
# def func1():
#     print('in func1')
#
#
# def func2():
#     print('in func2')
#
#
# ret = func1
#
# ret()
#
# ret1 = func2
#
# ret1()
#
# ret2 = ret
#
# ret3 = ret2
#
# ret2()
#
# ret3()
# 执行结果：
# in func1
# in funv2
# in func1
# in func1
# 例二：
#
# def func1():
#     print('in func1')
#
#
# def func2():
#     print('in func2')
#
#
# def func3(x, y):
#     x()
#
#     print('in func3')
#
#     y()
#
#
# print(111)
# func3(func2, func1)
# print(222)
# 执行结果：
111
# in func2
# in func3
# in func1
# 222
# 例三（选做题）：
#
# def func1():
#     print('in func1')
#
#
# def func2(x):
#     print('in func2')
#     return x
#
#
# def func3(y):
#     print('in func3')
#     return y
#
#
# ret = func2(func1)
# ret()
# ret2 = func3(func2)
# ret3 = ret2(func1)
# ret3()
# 执行结果：

# in func2
# in func1
# in func3
# in funv2
# in func1
# 看代码写结果：
# 例四:
#
#
# def func(arg):
#     return arg.replace('alex', '****')


# def run():
#     msg = "Alex和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
#
# run()
# data = run()
# print(data)
# Alex和大家都是好朋友
# Alex和大家都是好朋友
# None
# 看代码写结果：
# 例五:
# data_list = []
#
#
# def func(arg):
#     return data_list.insert(0, arg)
#
#
# data = func('绕不死你')
# print(data)
# print(data_list)
# None
# ['绕不死你']

# 看代码写结果：
# 例六:
#
#
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for item in func_list:
#     val = item()
#     print(val)
# "你好呀"
# "好你妹呀"
# "你好呀"
# "好你妹呀"
# "你好呀"
# "好你妹呀"
# 看代码写结果：
# 例七:
#
#
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)
# "你好呀"
# "好你妹呀"
# "你好呀"
# "好你妹呀"
# "你好呀"
# "好你妹呀"
# 看代码写结果：
# 例八:
#
#
# def func():
#     return '大烧饼'
#
#
# def bar():
#     return '吃煎饼'
#
#
# def base(a1, a2):
#     return a1() + a2()
#
#
# result = base(func, bar)
# print(result)
# "大烧饼吃煎饼"
# 看代码写结果：
# 例九:
#
#
# def func():
#     for item in range(10):
#         pass
#         return item
#
#
# func()
# ? 0
# 看代码写结果：
# 例十:
#
#
# def func():
#     for item in range(10):
#         pass
#         yield item
#
#
# func()

# 看代码写结果：
# 例十一:
item = '老男孩'


# def func():
#     item = 'alex'
#
#     def inner():
#         print(item)
#
#     for inner in range(10):
#         pass
#     inner()
#
#
# func()
# 报错
# 看代码写结果：
# 例十二:
# l1 = []
#
#
# def func(args):
#     l1.append(args)
#     return l1
#
#
# print(func(1))
# print(func(2))
# print(func(3))
# [1]
# [1,2]
# [1,2,3]
# 看代码写结果：
# 例十三:
# name = '宝元'
#
#
# def func():
#     global name
#     name = '男神'
#
#
# print(name)
# func()
# print(name)
# 宝元
# 男神
# 看代码写结果：
# 例十四:
# name = '宝元'
#
#
# def func():
#     print(name)
#
#
# func()
# 宝元
# 看代码写结果：
# 例十五: (选做题)
# name = '宝元'
#
#
# def func():
#     print(name)
#     name = 'alex'
#
#
# func()
# 报错
# 看代码写结果：
# 例十六:
#
#
# def func():
#     count = 1
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#
#     print(count)
#     inner()
#     print(count)
#
#
# func()
# 1
# 2
# 2
# 看代码写结果：
# 例十七: (选做题)
#
#
# def extendList(val, list=[]):
#     print(list)
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3)

# list1=[10,"a"]
# list2=[123]
# list3=[10,"a"]
# 看代码写结果：
# 例十八:
#
#
def extendList(val, list=[]):
    list.append(val)
    return list


print('list1=%s' % extendList(10),print(id(extendList(10))))
print('list2=%s' % extendList(123, []))
print('list3=%s' % extendList('a'),print(id(extendList('a'))))


# 2.
# 用你的理解解释一下什么是可迭代对象，什么是迭代器。

# 可迭代对象就是可以用for进行循环，有__iter__()方法，迭代器是迭代对象的进一步扩展，有__next__()方法
# 3.
# 使用while循环实现for循环的本质(面试题)
# s = "abcdd"
# s = s.__iter__()
# while True:
#     try:
#         print(s.__next__())
#     except StopIteration:
#         break