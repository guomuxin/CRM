# class JianShuError(Exception):
#     def __init__(self, n):
#         self.n = n
#
# def func():
#     a = input("请输入被减数")
#     b = input("请输入减数")
#
#     try:
#         if a < b:
#             raise JianShuError("被减数小于减数")
#
#     except JianShuError as e:
#         print(e)
# func()

# 2，info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm'....]
# 任意多的网址.定义一个方法get_page(listindex) listindex为下标的索引，类型为整数。 函数调用：任意输入一个整数，
# 返回列表下标对应URL的内容，用try except 捕获列表下标越界
# info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm']
# def get_page(listindex):
#     try:
#         return info[listindex]
#     except IndexError:
#         print("数组越界")
#
# get_page(3)

# 3，让一个人类对象，可以使用len（）方法获得一个整数值
# class Person:
#     def __len__(self):
#         return 10
#
#     def run(self):
#         print("a")
# p = Person()
# print(len(p))

# 4，定义人类对象，用print直接打印时可以获得该对象的属性信息
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#
#         return f"{self.name}{self.age}"
#
# p = Person("a",12)

# 5，尝试捕获IOError
try:
    open("a","r",encoding="utf-8")
except IOError:
    print("io错误")

try:
    dic = {'name': 'shang'}
    print(dic[1])
except NameError:
    print('出现了NameError错误....')
finally:
    print('执行结束')