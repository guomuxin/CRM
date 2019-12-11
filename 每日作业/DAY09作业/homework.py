# 1.整理函数相关知识点,将课上的代码敲3遍
#
# 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def func(s):
    lst = []
    for i in s[1::2]:
        lst.append(i)
    return lst
l = (1,2,3,4,5)
print(func(l))
# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def func01(s):
    return len(s) > 5

# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def func02(s):
    return s[:2]
print(func02([1]))
# 5.写函数，计算传入函数的字符串中,[数字]、[字母和中文]以及 [其他]的个数，并返回结果。
def func03(s):
    count_int = 0
    count_alpha = 0
    count_other = 0
    for i in s:
        if i.isdecimal():
            count_int += 1
        elif i.isalpha():
            count_alpha += 1
        else:
            count_other += 1
    return count_int,count_alpha,count_other
print(func03("dasdadaf1133??"))
# 6.写函数，接收两个数字参数，返回比较大的那个数字。
def func04(a,b):
    if a < b:
        a,b = b,a
    else:
        pass
    return a
print(func04(4,1))
# 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
def func05(d):
    for i in d:
        d[i] = d[i][:2]
    return d
print(func05({"k1": "v1v1", "k2": [11,22,33,44]}))
# 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
def func06(l):
    if type(l) != list:
        return False
    else:
        dic = {}
        for i in l:
            dic[l.index(i)] = i
    return dic
print(func06([11,22,33]))
# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
def func07(name,sex,age,sc):
    with open("student_msg","a",encoding="utf-8") as f:
        f.write(f"{name},{sex},{age},{sc}")
func07("guo","男",21,"bk")
# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
def func08(name,age,sc,sex="男"):
    with open("student_msg", "a", encoding="utf-8") as f:
        f.write(f"{name},{sex},{age},{sc}")
while True:
    info = input("请输入信息(姓名,年龄,学历,性别):")
    if info == "q" or info == "Q":
        break
    else:
        j = info.split(",")
        func08(j[0],j[1],j[2],j[3])
# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
def func09(file_name,opretion):
    with open(file_name,"r",encoding="utf-8") as f, \
        open("file","w",encoding="utf-8") as f1:
        for i in f:
            i = i.replace(opretion[0],opretion[1])
            f1.write(i)
        import os
    os.rename(file_name,"file01")
    os.rename("file",file_name)
func09("student_msg",["女","男"])
