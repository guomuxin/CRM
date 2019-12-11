# 1．首先程序启动，显示下面内容供用户选择：
# 1.请登录
# 2.请注册
# 3.进入文章页面
# 4.进入评论页面
# 5.进入日记页面
# 6.进入收藏页面
# 7.注销账号
# 8.退出整个程序
# 2．必须实现的功能：
# 1.注册功能要求：
# a.用户名、密码要记录在文件中。
# b.用户名要求：不能有特殊字符并且确保用户名唯一。
# c.密码要求：长度要在6~14个字符之间。
#
# 2.登录功能要求：
# a.用户输入用户名、密码进行登录验证。
# b.登录成功之后，才可以访问3 - 7选项，如果没有登录或者登录不成功时访问3 - 7选项，不允许访问,提示用户进行登录!
# c.超过三次登录还未成功，则退出整个程序。
# 3.进入文章页面要求：
# 提示欢迎xx进入文章页面。(xx是当前登录的用户名)
# 4.进入评论页面要求：
# ​ 提示欢迎xx进入评论页面
# 5.进入日记页面要求：
# 提示欢迎xx进入日记页面。
# 6.进入收藏页面要求：
# 提示欢迎xx进入收藏页面。
# 7.注销账号要求：
# 不是退出整个程序，而是将已经登录的状态变成未登录状态（在次访问3~7选项时需要重新登录）
# 8.退出整个程序要求：
# 就是结束整个程序

msg = """
1.请登录
2.请注册 
3.进入文章页面
4.进入评论页面
5.进入日记页面
6.进入收藏页面
7.注销账号
8.退出整个程序
请输入序号:
"""
dic = {}

using_name = ""

logined = True
def login():
    count = 1
    while count < 4:
        name = input("请输入用户名:")
        pwd = input("请输入密码:")
        if name in dic:
            if pwd == dic[name]:
                print("登录成功")
                global logined
                logined = False
                using_name = name
                break
            else:
                print(f"用户名或密码错误,,错误次数{count}")
                count += 1
        else:
            print(f"用户名或密码错误,错误次数{count}")
            count += 1

def register():
    while True:
        name = input("请输入用户名:")
        pwd = input("请输入密码:")
        if name in dic:
            print("用户已存在")
        elif name.isalnum() != True:
            print("用户名不符合要求")
        elif 6 > len(pwd) or len(pwd) > 14:
            print("密码长度不符合要求")
        else:
            f.write(f"{name},{pwd}\n")
            choice = "1"
            print("请登录")
            break
def title():
    print(f"欢迎{using_name}进入文章页面")
def comment():
    print(f"欢迎{using_name}进入评论页面")

while True:
    choice = input(msg)
    if choice == "1" or choice == "2":
        while True:
            f = open("info.txt","a+",encoding="utf-8")
            f.seek(0,0)
            for i in f:
                j = i.strip().split(",")
                dic[j[0]] = j[1]
            if choice == "2":
               register()
               break
            else:
                login()
                break


    elif 3 <= int(choice) <= 7:
        if logined == False:
            if choice == "3":
                title()

            if choice == "4":
                comment()
            if choice == "5":

                break
            if choice == "6":
                print(f"欢迎{using_name}进入收藏页面")
                break
            if choice == "7":
                logined = True
        else:
            print("请登录")
    else:
        break
# 四.用代码实现三次用户登录及锁定(选做题,这是一个单独的程序)
# 项目分析:
# 一.首先程序启动,显示下面内容供用户选择:
# 1.注册
# 2.登录
# a.用户选择登录的时候,首先判断用户名在userinfo.txt表中存在不在,存在就不能进行注册
# b.当注册的用户名不存在的时候将用户名和密码写入到userinfo.txt文件中
# c.用户选择登录的时候,判断用户输入的账号和密码是否userinfo.txt存储的一致
# d.用户名和密码一致就终止循环,并提示用户登录成功!
# e.用户名和密码不一致,只有三次登录机会,三次过后提示用户名被锁定,请联系管理员!并终止循环
# f.当用户名错误三次,再次运行程序.登录锁定的账号继续提示用户名被锁定,请联系管理员!

# while True:
#     msg = """
# 1.注册
# 2.登录
# 请输入序号：
#     """
#     choice = input(msg)
#     if choice == "1" or choice == "2":
#         break
#     else:
#         print("请重新输入")
# with open("lock.txt","a+",encoding="utf-8") as f1:
#     with open("userinfo.txt","a+",encoding="utf-8") as f:
#         dic = {}
#         f.seek(0,0)
#         for i in f:
#             j = i.split(",")
#             dic[j[0].strip()] = j[1].strip()
#         if choice == "1":
#             while True:
#                 name = input("请输入用户名：")
#                 pwd = input("请输入密码：")
#                 if name in dic:
#                     print("用户已存在")
#                 else:
#                     f.write(f"{name},{pwd}\n")
#                     break
#
#         elif choice == "2":
#             count = 1
#             while count<4:
#                 name = input("请输入用户名：")
#                 pwd = input("请输入密码：")
#                 f1.seek(0,0)
#                 if name in f1.read():
#                     print("你的账户已被锁定,请联系管理员")
#                     break
#                 if name in dic:
#                     if pwd == dic[name]:
#                         print("登录成功")
#                         break
#                     else:
#                         print("用户名或密码错误")
#                 else:
#                     print(f"用户名或密码错误,错误次数{count}")
#                     count += 1
#                 if count == 4:
#
#                         f1.write(f"{name}")

