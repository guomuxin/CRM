
dic = {}
login_dic = {
    "using_name": "1",
    "logined": True
}
from lib import commom
from conf import setting
File_PATH = setting.FILE_PATH
login = commom.login
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

f = open(File_PATH, "a+", encoding="utf-8")
f.seek(0, 0)
for i in f:
    j = i.strip().split(",")
    dic[j[0]] = [j[1],j[2]]
def register():
    while True:

        name = input("请输入用户名:")
        pwd = input("请输入密码:")
        import hashlib
        md5 = hashlib.md5(name.encode("utf-8"))
        md5.update(pwd.encode("utf-8"))
        pwd_md5 = md5.hexdigest()
        if name in dic:
            print("用户已存在")
        elif name.isalnum() != True:
            print("用户名不符合要求")
        elif 6 > len(pwd) or len(pwd) > 14:
            print("密码长度不符合要求")
        else:
            f.write(f"{name},{pwd},{pwd_md5}\n")
            choice = "1"
            print("请登录")
            f.close()
            break
def title():
    print(f"欢迎{login_dic['using_name']}进入文章页面")
def comment():
    print(f"欢迎{login_dic['using_name']}进入评论页面")
def run():
    # using_name = ""
    # logined = True

    while True:
        choice = input(msg)
        if choice == "1" or choice == "2":
            while True:
                if choice == "2":
                   register()
                   break
                else:
                    login()
                    break
        elif 3 <= int(choice) <= 7:
            if login_dic['logined'] == False:
                if choice == "3":
                    title()
                if choice == "4":
                    comment()
                if choice == "5":
                    break
                if choice == "6":
                    print(f"欢迎{login_dic['using_name']}进入收藏页面")
                    break
                if choice == "7":
                    logined = True
            else:
                print("请先登录")
                login()
        else:
            break