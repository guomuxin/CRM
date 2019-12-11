class Hero(object):
    def __init__(self,blood,blue):
        self.blood = blood
        self.blue = blue
    def ziChan(self):
        self.blood -= 1
        print(self.blood)

gaiLun = Hero(100,50)
gaiLun.ziChan()
gaiLun.ziChan()

def eat(self):
    print("吃")
yasuo = Hero(100,100)

class Dog(object):
    def __init__(self,name,color,type,age,sex):
        self.name = name
        self.color = color
        self.type = type
        self.age = age
        self.sex = sex
    def bark(self):
        print("汪汪汪")
    def watch(self):
        print("看家")
        self.bark()
d = Dog("niu","红","泰迪",6,"公")
d.bark()
d.watch()

'''
定义一个学生类。有下面的类属性：
1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
zm = Student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100
'''
class Student(object):
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.grade)
zm = Student('zhangming',20,[69,88,100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())


'''
定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
'''
class DictClass(object):
    def __init__(self,dic):
        self.dic = dic
    def del_dict(self,key):
        self.dic.pop(key)
    def get_dict(self,key):
        if key in self.dic:
            return dic[key]
        else:
            return "not found"
    def get_key(self):
        lst = []
        for i in dic.keys():
            lst.append(i)
        return lst
dic = {'a':"aa",'b':"bb"}
dicc = DictClass(dic)



'''
定义一个列表的操作类：Listinfo
包括的方法:
1 列表元素添加: add_key(keyname) [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list) [list:列表类型]
4 删除并且返回最后一个元素：del_key()
list_info = Listinfo([44,222,111,333,454,'sss','333'])
'''
class ListInfo(object):
    def __init__(self,lst):
        self.lst = lst
    def add_key(self,keyname):
        self.lst.append(keyname)
    def get_key(self,num):
        return self.lst[num]
    def update_list(self,lst1):
        self.lst.extend(lst1)
        return self.lst
    def del_key(self):
        return self.lst.pop()
list_info = ListInfo([44,222,111,333,454,'sss','333'])
