# 1.请实现一个装饰器，限制该函数被调用的频率，如10秒一次（面试题）

# #上次该函数执行的时间
# time_last = 0
# import time
# #参数为需要限制的频率时间
# def outter(x):
#     def wrapper(f):
#         def inner(*args,**kwargs):
#             global time_last
#             #如果当前时间与上次执行时间间隔大于传入的时间则继续执行
#             if time.time() - time_last > x:
#                 #将这次调用函数的时间覆盖掉上次函数执行的执行,即下次执行时以这次时间为参照
#                 time_last = time.time()
#                 ret = f(*args,**kwargs)
#                 return ret
#             else:
#                 print("距离上次调用间隔不到十秒")
#         return inner
#     return wrapper
# #设置间隔时间需在6秒以上
# @outter(6)
# def func():
#
#     print("执行成功")
#     # time.sleep(1)
# def f():
#     time.sleep(7)
# func()
# f()
# func()

# 2.请写出下列代码片段的输出结果：
# def say_hi(func):
#   def wrapper(*args,**kwargs):
#       print("HI")
#       ret=func(*args,**kwargs)
#       print("BYE")
#       return ret
#   return wrapper
#
# def say_yo(func):
#   def wrapper(*args,**kwargs):
#       print("Yo")
#       return func(*args,**kwargs)
#   return wrapper
# @say_hi
# @say_yo
# def func():
#   print("ROCK&ROLL")
# func()


# HI
# Yo
# ROCK&ROLL
# BYE


# 3.编写装饰器完成下列需求:
# 用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
# 设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
# 启动程序后,呈现用户的选项为:
# 1,京东首页
# 2,京东超市
# 3,淘宝首页
# 4,淘宝超市
# 5,退出程序
# 四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,只要输入一次京东账号和密码并成功,则这两个函数都可以任意访问;用户选择淘宝超市或者淘宝首页,只要输入一次淘宝账号和密码并成功,则这两个函数都可以任意访问.
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。
flag = {"京东":False,"淘宝":False}
def log(file_name,f,app):
    '''
    用于验证登录
    :param file_name: 京东或淘宝用户信息的文件名
    :param f: 和装饰器的f一样
    :return:
    '''
    with open(file_name, 'r', encoding="utf-8") as f1:
        if flag[app[0:3]] == True:
            ret = f()
            return ret
        else:
            name = input("请输入用户名:")
            pwd = input("请输入密码:")
            f1.seek(0, 0)
            dic = {}
            for i in f1:
                dic[i.split(":")[0]] = i.split(":")[1].strip()
            if name in dic and pwd == dic[name]:
                ret = f()
                flag[app[0:3]] = True
                return ret
            else:
                print("账号或密码错误")

def login(app):
    def wrapper(f):
        def inner(*args,**kwargs):
            if "京东" in app:
                return log("jd.txt",f,app)
            elif "淘宝" in app:
                return log("tb.txt",f,app)
        return inner
    return wrapper
@login("京东")
def jdpage():
    print("京东首页")
@login("京东")
def jdmall():
    print("京东商城")
@login("淘宝")
def tbpage():
    print("淘宝首页")
@login("淘宝")
def tbmall():
    print("淘宝商城")
dic = {
    "京东首页":jdpage,
    "京东商城":jdmall,
    "淘宝首页":tbpage,
    "淘宝商城":tbmall
}
msg = """
京东商城
京东首页
淘宝商城
淘宝首页
请选择要进入的页面:
"""
while True:
    app = input(msg)
    dic[app]()

# 4.给l1 = [1,1,2,2,3,3,6,6,5,5,2,2]去重，不能使用set集合（面试题）。
l1 = [1,1,2,2,3,3,6,6,5,5,2,2]
# def func(l1):
#     for i in l1:
#         if l1.count(i) > 1:
#             l1.remove(i)
#             func(l1)
# func(l1)
# print(l1)

# # 5.用递归函数完成斐波那契数列（面试题）：
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(1,8):
#     print(fib(i))
# 斐波那契数列：1，1，2，3，5，8，13，21..........(第三个数为前两个数的和，但是最开始的1，1是特殊情况，可以单独讨论)
# 6.用户输入序号获取对应的斐波那契数字：比如输入6，返回的结果为8.
# 1 1 2 3 5 8
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(6))