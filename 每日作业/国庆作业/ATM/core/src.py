login_dic = {
    "using_name" : '',
    "logined" : False
}
dic = {}
import json
import time
import logging
import os
from conf import setting
from lib import commom
login = commom.login
log = commom.log
USERINFO_PATH = setting.USERINFO_PATH
logined_check = commom.logined_check
User_PATH = setting.User_PATH
Logging_PATH = setting.Logging_PATH
msg = """
1.登录
2.注册 
3.查看余额
4.存钱
5.转账
6.查看用户流水
7.退出
请输入序号:
"""
f = open(USERINFO_PATH,"a+",encoding="utf-8")
f.seek(0)
for i in f:
    if i != "\n":
        dic.update(json.loads(i))
def register():
    '''
    注册账号
    :return:
    '''
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
            f.write(json.dumps({name:[pwd,pwd_md5]})+"\n")
            f1 = open(os.path.join(User_PATH,name+".json"),"a+",encoding="utf-8")
            f1.write(json.dumps({name:[pwd_md5,0]},ensure_ascii=False)+"\n")
            f2 = open(os.path.join(Logging_PATH,name+".log"),"a+",encoding="utf-8")
            print("请登录")
            f.close()
            f1.close()
            break

@logined_check
def check_money():
    '''
    查看账户余额
    :return:
    '''
    f1 = open(os.path.join(User_PATH,login_dic["using_name"]+".json"),"r",encoding="utf-8")
    f1.seek(0)
    data = json.load(f1)
    print("您的余额是:"+str(data[login_dic["using_name"]][1]))
    log(login_dic["using_name"],"查看余额",data[login_dic["using_name"]][1])
    f1.close()
@logined_check
def save_money():
    '''
    存钱
    :return:
    '''
    num_of_save = int(input("请输入要存入的数量:"))
    f1 = open(os.path.join(User_PATH, login_dic["using_name"] + ".json"), "r+", encoding="utf-8")
    data = json.load(f1)
    data[login_dic["using_name"]][1] += num_of_save
    print("存入成功,当前余额:"+str(data[login_dic["using_name"]][1]))
    f1.seek(0)
    f1.write(json.dumps(data))
    log(login_dic["using_name"],f"存入{num_of_save}元",data[login_dic["using_name"]][1])
@logined_check
def trans():
    '''
    转帐
    :return:
    '''
    while True:
        target_name = input("请输入对方的用户名:")
        if target_name in dic and target_name != login_dic["using_name"]:
            num_of_trans = int(input("请输入要转账的数目:"))
            f1 = open(os.path.join(User_PATH, login_dic["using_name"] + ".json"), "r+", encoding="utf-8")
            data = json.load(f1)
            f2 = open(os.path.join(User_PATH, target_name + ".json"), "r+", encoding="utf-8")
            data1 = json.load(f2)
            if data[login_dic["using_name"]][1] >= num_of_trans:
                data[login_dic["using_name"]][1] -= num_of_trans
                data1[target_name][1] += num_of_trans
                print("转账成功,当前余额:" + str(data[login_dic["using_name"]][1]))
                f1.seek(0)
                f1.write(json.dumps(data))
                f2.seek(0)
                f2.write(json.dumps(data1))
                log(login_dic["using_name"],f"转账给{target_name}{num_of_trans}元,",data[login_dic["using_name"]][1])
                log(target_name,f"收到来自{login_dic['using_name']}的转账{num_of_trans}元",data1[target_name][1])
                return
            else:
                print("余额不足")
        else:
            print("用户名不合法")
@logined_check
def show_logging():
    '''
    查看流水
    :return:
    '''
    with open(os.path.join(Logging_PATH,login_dic["using_name"]+".log"),"r",encoding="utf-8") as f:
        for i in f:
            print(i)
def run():
    while True:
        choice_func = {
            1: login,
            2: register,
            3: check_money,
            4: save_money,
            5: trans,
            6: show_logging,
        }
        choice = int(input(msg))
        if 0 < choice < 7:
            choice_func[choice]()
        elif choice == 7:
            exit()
        else:
            print("输入有误")