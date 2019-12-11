
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
import json

def register():
    while True:
        name = input("请输入用户名：")
        pwd = input("请输入密码：")
        import hashlib
        md5 = hashlib.md5(name.encode("utf-8"))
        md5.update(pwd.encode("utf-8"))
        pwd_md5 = md5.hexdigest()
        if name in dic:
            print("用户已存在")
        else:
            f.write(json.dumps({name: [pwd,pwd_md5, 0]}) + "\n")
            # login()
            break
def login():
    while True:
        name = input("请输入用户名：")
        if name not in dic:
            print("请先注册")
            register()
            break
        pwd = input("请输入密码：")
        f1.seek(0, 0)
        if name in f1.read():
            print("你的账户已被锁定,请联系管理员")
            continue
        import hashlib
        md5 = hashlib.md5(name.encode("utf-8"))
        md5.update(pwd.encode("utf-8"))
        if md5.hexdigest() == dic[name][1]:
            print("登录成功")
            break
        else:
            print("用户名或密码错误")
            dic[name][2] += 1
            if dic[name][2] == 3:
                f1.write(f"{name} + \n")
while True:
    msg = """
1.注册
2.登录
请输入序号：
    """
    choice = input(msg)
    if choice == "1" or choice == "2":
        break
    else:
        print("请重新输入")
with open("lock.txt","a+",encoding="utf-8") as f1:
    with open("userinfo.txt","a+",encoding="utf-8") as f:
        dic = {}
        f.seek(0,0)
        for i in f:
            info = json.loads(i)
            dic.update(info)
        if choice == "1":
            register()
        elif choice == "2":
            login()
