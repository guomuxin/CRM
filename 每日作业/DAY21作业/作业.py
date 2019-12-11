# 1 定义宠物类（ Pet ），猫类（Cat）和狗类（Dog）
# 宠物都有属性姓名（name）和年龄(age)
# 宠物都有吃（eat）、喝（drink）、叫（shout）的方法
# 猫除了具有宠物类的方法，还有爬树（ climbTree ）的方法
# 狗除了具有宠物类的方法，还有警戒（ police）的方法
'''
class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃东西")

    def drink(self):
        print("跑")

    def shout(self):
        print("叫")


class Cat(Pet):
    def climbTree(self):
        print("爬树")


class Dog(Pet):
    def police(self):
        print("警戒")
'''

# 2 建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性，至少要求 汽车能够加速 减速 停车。 再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD属性，并且重新实现方法覆盖加速、减速的方法

'''
class Auto(object):
    def __init__(self, color, weight, speed = 0, num_lt=4,):
        self.num_lt = num_lt
        self.color = color
        self.weight = weight
        self.speed = speed

    def add_speed(self, num_add_speed):
        self.speed += num_add_speed
        print(f"汽车加速{num_add_speed}km/h,当前时速{self.speed}km/h")
    def low_speed(self,num_low_speed):
        self.speed -= num_low_speed
        print(f"汽车减速{num_low_speed}km/h,当前时速{self.speed}km/h")


class CarAuto(Auto):
    def __init__(self,air,CD,*args,**kwargs):
        self.air = air
        self.CD = CD
        super().__init__(*args,**kwargs)

    def add_speed(self, num_add_speed):
        self.speed += num_add_speed
        print(f"小汽车加速{num_add_speed}km/h,当前时速{self.speed}km/h")

    def low_speed(self, num_low_speed):
        self.speed -= num_low_speed
        print(f"小汽车减速{num_low_speed}km/h,当前时速{self.speed}km/h")

car1 = CarAuto("海尔","好音响","红色","1000kg")
print(car1.__dict__)
car1. add_speed(10)
car1. add_speed(10)
car1.low_speed(10)
'''

# 3 银行卡类（BankCard）有余额（balance）属性和存款（deposit）取款（draw）的方法，只要取款金额小于余额即可完成取款操作
# 信用卡类（CreditCard）继承自银行卡类，信用卡多了透支额度（overdraft）属性，如果卡中余额和透支额度的和大于取款金额即可完成取款。如果透支，显示透支金额

'''
class BankCard(object):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, num):
        if self.balance >= num:
            self.balance -= num
            print(f"取款{num}元,余额:{self.balance}")
        else:
            print("余额不足")

    def draw(self, num):
        self.balance += num
        print(f"存款{num}元,余额:{self.balance}")


class CreditCard(BankCard):
    def __init__(self,overdraft,*args):
        super().__init__(*args)
        self.overdraft = overdraft

    def deposit(self, num):
        if self.balance >= num:
            self.balance -= num
            print(f"取款{num}元,余额:{self.balance}")
        elif self.balance + self.overdraft >= num:
            self.overdraft -= (num-self.balance)
            print(f"已透支{num-self.balance}元")
            self.balance = 0
        else:
            print("余额不足")

    def draw(self, num):
        self.balance += num
        print(f"存款{num}元,余额:{self.balance}")


cc1 = CreditCard(1000,2000)
cc1.deposit(2500)
'''

# 4 编写程序, A 继承了 B, 两个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法

'''
class B(object):
    def handle(self):
        print("B的handle方法")


class A(B):
    def handle(self):
        super().handle()

a = A()
a.handle()
'''