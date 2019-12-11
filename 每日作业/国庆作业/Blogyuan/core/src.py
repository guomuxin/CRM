
dic = {}
login_dic = {
    "using_name": "1",
    "logined": True
}
from lib import commom
from conf.setting import *
import json
import time
# File_PATH = setting.FILE_PATH
# COMMENT_PATH = setting.COMMENT_PATH
# LOGGING_PATH = setting.LOGGING_PATH
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


f = open(FILE_PATH, "a+", encoding="utf-8")
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
@commom.logined_check
def title():
    print(f"欢迎{login_dic['using_name']}进入文章页面")
@commom.logined_check
def comment():
    print(f"欢迎{login_dic['using_name']}进入评论页面")
    floor = 0
    with open(COMMENT_PATH,"a+",encoding="utf-8") as f1:
        f1.seek(0)
        for i in f1:
            print(json.loads(i))
            floor = int(i[2])
        comment_if = input("是否要评论,请输入是/否")
        if comment_if == "是":
            your_comment = input("请评论")
            f1.write("\n"+json.dumps({str(floor+1)+"楼"+" - "+login_dic["using_name"]:your_comment},ensure_ascii=False))
        else:
            return

@commom.logined_check
def logging():
    print(f"欢迎{login_dic['using_name']}进入日记页面")
    with open(LOGGING_PATH,"a+",encoding="utf-8") as f2:
        for i in f2:
            print(json.loads(i))
        logging_if = input("是否要记录日记,请输入是/否")
        if logging_if == "是":
            your_logging = input("请记录日记")
            f2.write("\n"+json.dumps({"time":time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),"content":your_logging},ensure_ascii=False))
@commom.logined_check
def shoucang():
    print(f"欢迎{login_dic['using_name']}进入收藏页面")
def run():
    # using_name = ""
    # logined = True

    while True:
        choice_func = {
            1:login,
            2:register,
            3:title,
            4:comment,
            5:logging,
            6:shoucang,
        }
        choice = int(input(msg))
        if 0 < choice < 7:
            choice_func[choice]()
        elif choice == 8:
            exit()
        elif choice == 7:
            login_dic["logined"] = True
        else:
            print("输入有误")
