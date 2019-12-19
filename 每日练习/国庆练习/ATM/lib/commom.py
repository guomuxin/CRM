from core import src
import os
from conf import setting
Logging_PATH = setting.Logging_PATH
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

                login_dic['logined'] = True
                login_dic['using_name'] = name
                src.f.close()
                break
            else:
                print(f"用户名或密码错误,,错误次数{count}")
                count += 1
        else:
            print(f"用户名或密码错误,错误次数{count}")
            count += 1


def logined_check(f):
    def inner(*args,**kwargs):
        if login_dic["logined"] == True:
            ret = f(*args,**kwargs)
            return ret
        else:
            login()
            ret = f(*args,**kwargs)
            return ret
    return inner



def log(file_name,opretion,num):
    import logging
    logger = logging.getLogger() #创建一个空架子
    fh = logging.FileHandler(os.path.join(Logging_PATH,file_name+".log"),mode="a",encoding="utf-8")

    ch = logging.StreamHandler()
    f_str = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)s %(message)s")
    logger.level = 10
    fh.setFormatter(f_str)
    ch.setFormatter(f_str)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info(f"{file_name} {opretion} 当前余额:{num}")
    logger.removeHandler(fh)