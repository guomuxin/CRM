# 1有一个男人类和一个女人类
# 创建男女朋友之间互相关联的关系
# 例如男人类的对象调用看电影的方法时，需要用到女人类的对象，女人类的对象调用逛街的方法时也需要用到男人类的对象（相互关联）
'''
class Man(object):
    def __init__(self,name):
        self.name = name
    def watch_movie(self,woman):
        print(f"{self.name}和{woman.name}一起看电影")
class Woman(object):
    def __init__(self,name):
        self.name = name
    def shopping(self,man):
        print(f"{self.name}和{man.name}一起逛街")

m1 = Man("guo")
w1 = Woman("mou")
m1.watch_movie(w1)
w1.shopping(m1)
'''

# 2创建一个学生类和一个背包类，将背包类的对象组合到学生类中
'''
class Student(object):
    def __init__(self,name,bag):
        self.name = name
        self.bag = bag
class Bag(object):
    def __init__(self,name):
        self.name = name
bag1 = Bag("Nike")
s1 = Student("guo",bag1)
print(s1.bag.name)
'''

# 3创建客船类/货船类和油船类，三个类都需要组合发动机类/船体类/甲板类/船舱类对象
'''
class FaDongJi(object):
    def __init__(self,name):
        self.name = name
class ChuanTi(object):
    def __init__(self,name):
        self.name = name
class JiaBan(object):
    def __init__(self,name):
        self.name = name
class ChuanCang(object):
    def __init__(self,name):
        self.name = name

class Ke_Ship(object):
    def __init__(self,name,fadongji,chuanti,jiaban,chuancang):
        self.name = name
        self.fadongji = fadongji
        self.chuanti = chuanti
        self.jiaban = jiaban 
        self.chuancang = chuancang
class Huo_Ship(object):
    def __init__(self,name,fadongji,chuanti,jiaban,chuancang):
        self.name = name
        self.fadongji = fadongji
        self.chuanti = chuanti
        self.jiaban = jiaban 
        self.chuancang = chuancang
class You_Ship(object):
    def __init__(self,name,fadongji,chuanti,jiaban,chuancang):
        self.name = name
        self.fadongji = fadongji
        self.chuanti = chuanti
        self.jiaban = jiaban 
        self.chuancang = chuancang
        
        
fdj1 = FaDongJi("发动机1")
ct1 = ChuanTi("船体1")
jb1 = JiaBan("甲板1")
cc1 = ChuanCang("船舱1")
ks1 = Ke_Ship("客船1",fdj1,ct1,jb1,cc1,ks1)
hs1 = Huo_Ship("货船1",fdj1,ct1,jb1,cc1,ks1)
s1 = You_Ship("油船1",fdj1,ct1,jb1,cc1,ks1)
'''

# 4士兵类（Soldier）具有名字，和枪支（gun）两个属性
# 枪支属性默认为None值
# 士兵可以使用枪支开火(fire)，如果没有获得枪则提示“还没有枪”
# 枪类（Gun）有型号(model)和子弹数量（bullet_count）属性
# 枪能够发射子弹(shoot)，也可以装填子弹(add_bullet)，如果子弹数为0则不能继续发射

'''
class Soldier(object):
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun:
            self.gun.shoot()
        else:
            print("还没有枪")


class Gun(object):
    def __init__(self, model, bullet_count=5):
        self.model = model
        self.bullet_count = bullet_count

    def shoot(self):
        if self.bullet_count > 0:
            print("biu")
            self.bullet_count -= 1
            print(f"剩余子弹:{self.bullet_count}")
        else:
            print("装填子弹")
            self.add_bullet()

    def add_bullet(self):
        self.bullet_count += 5
        print(f"装填完毕,当前剩余子弹:{self.bullet_count}")


g1 = Gun("AK")
s1 = Soldier("guo", g1)
for i in range(20):
    s1.fire()
'''
