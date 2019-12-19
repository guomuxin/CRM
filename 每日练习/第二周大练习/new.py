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