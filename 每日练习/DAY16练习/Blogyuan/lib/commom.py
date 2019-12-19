from core import src
login_dic = src.login_dic
dic = src.dic
def login():
    count = 1
    while count < 4:
        name = input("请输入用户名:")
        pwd = input("请输入密码:")
        if name in dic:
            import hashlib
            md5 = hashlib.md5(name.encode("utf-8"))
            md5.update(pwd.encode("utf-8"))
            if md5.hexdigest() == dic[name][1]:
                print("登录成功")

                login_dic['logined'] = False
                login_dic['using_name'] = name
                src.f.close()
                break
            else:
                print(f"用户名或密码错误,,错误次数{count}")
                count += 1
        else:
            print(f"用户名或密码错误,错误次数{count}")
            count += 1