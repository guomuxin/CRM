# 1.
# 有如下
# v1 = {'郭宝元', 'alex', '海绵', '王二麻子'}
# v2 = {'alex', '王二麻子'}
# 请得到
# v1和v2的交集并输出
# 请得到v1和v2的并集并输出
# 请得到v1和v2的差集并输出
#请得到v2和v1的差集并输出
v1 = {'郭宝元', 'alex', '海绵', '王二麻子'}
v2 = {'alex', '王二麻子'}
print(v1 | v2)
print(v1 - v2)
print(v2 - v1)
# 2.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
# lst = []
# while True:
#     s = input("请输入:")
#     if s == "N" or s == "n":
#         break
#     else:
#         lst.append(s)
# print(lst)

# 3.写代码实现
# v1 = {'alex', '武sir', '黑哥'}
# v2 = []
# ​循环提示用户输入，如果输入的内容在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
v1 = {'alex', '武sir', '黑哥'}
v2 = []
while True:
    s = input("请输入")
    if s in v1:
        v2.append(s)
    else:
        v1.append(s)
# 4.
# 通过观察判断以下值那个能做字典的key？那个能做集合的元素？
# 1     能
# -1    能
# ""    能
# None  不能
# [1, 2]    不能
# (1,)      不能
# {11, 22, 33, 4}   不能
# {'name': 'wupeiq', 'age': 18} 不能

# 5. is 和 == 的区别？
is判断两者是不是一个东西， == 判断两边的值是否相等
# 6.type使用方式及作用？
type(变量)：判断该变量的类型
# 7.id的使用方式及作用？
id（变量）：查找该变量的地址
# 8.看代码写结果并解释原因
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
# ​
# result1 = v1 == v2        t
# result2 = v1 is v2
# print(result1)            True：两者值完全一样
# print(result2)            False，变量名不同，即内存地址不同

# 9.看代码写结果并解释原因
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
# ​
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)           True     v2是v1赋值过去的，所以两者共享空间
# print(result2)            True


# 10.
# 看代码写结果并解释原因
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
# ​
# v1['k1'] = 'meet'
# print(v2)             {'k1': 'meet', 'k2': [1, 2, 3]} v2被赋值为v1与v1共享地址空间
# 11.
# 看代码写结果并解释原因
# v1 = '人生苦短，我用Python'
# v2 = [1, 2, 3, 4, v1]
# v1 = "人生苦短，用毛线Python"
# print(v2)         [1, 2, 3, 4, "人生苦短，用毛线Python"]   v2保存的是v1的地址，但是v1重新赋值等于重新开辟空间
# 12.
# 看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
# ​
# info.append(9)
# print(userinfo)           {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}，userinfo保存的是info的地址，info修改是原地修改
# ​
# info = "题怎么这么多"
# print(userinfo)           {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]} 与上题一样

# 13.
# 看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
# ​
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo)             ['不仅多，还特么难呢', 2, 3] [['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3]]
# 14.
# 看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
# ​
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)     ['闭嘴', 2, 3] [['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3]]  他们都指向info这个数据本身的地址，所有的修改都会发生
# 15.
# 看代码写结果并解释原因
# info = [1, 2, 3]
# user_list = []
# for item in range(10):
#     user_list.append(info)
#
# info[1] = "是谁说Python好学的？" 十个[1,"是谁说Python好学的？",3]       循环增加10遍，且所有user_list里的info都指向info的地址，把info[1]改了则都改
# ​
# print(user_list)
# 16.
# 看代码写结果并解释原因
# data = {}
# for i in range(10):
#     data['user'] = i
# print(data)               {"user":9} 字典的修改，会覆盖之前的值

# 17.
# 看代码写结果并解释原因
# data_list = []
# data = {}
# for i in range(10):
#     data['user'] = i
#     data_list.append(data)
# print(data_list)              [{'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}]和上题一样，只不过每次都要append，所以会更新
# 18.
# 看代码写结果并解释原因
# data_list = []
# for i in range(10):
#     data = {}
#     data['user'] = i
#     data_list.append(data)
# print(data_list)              [{'user': 0}, {'user': 1}, {'user': 2}, {'user': 3}, {'user': 4}, {'user': 5}, {'user': 6}, {'user': 7}, {'user': 8}, {'user': 9}] 每次循环前data都会变为空
# 19.
# 使用循环打印出一下效果：
# 格式一
# *
# **
# ** *
# ** **
# ** ** *
s = ""
for i in range(5):

    if i % 2 == 0:
        s += " *"
    else:
        s += "*"
    print(s)
# 格式二
# ** **
# ** *
# **
# *

s = ""
lst = []
for i in range(5):

    if i % 2 == 0:
        s += " *"

    else:
        s += "*"
    lst.append(s)
    print(lst)
for j in range(len(lst)-1,0,-1):
    print(lst[j])
# 格式三
# *
# ** *
# ** ** *
# ** ** ** *
# ** ** ** ** *
s = ""
for i in range(9):

    if i % 2 == 0:
        s += " *"
    else:
        s += "*"
    print(s)
# 20.
# 敲七游戏.从1开始数数.遇到7或者7的倍数（不包含17, 27, 这种数）要在桌上敲⼀下.编程来完成敲七.给出⼀个任意的数字n.从1开始数.数到n结束.把每个数字都放在列表中, 在数的过程中出现7或
# 者7的倍数（不包含17, 27, 这种数）.则向列表中添加⼀个
# '咣'
# 例如, 输⼊10.
# lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
s = int(input("请输入："))
lst = []
for i in range(s):
    if i % 7 == 0:
        lst.append("咣")
    else:
        lst.append(i)
# 21.模拟购物车
# 要求:
# 1,用户先给自己的账户充钱：比如先充3000元。
# 2,有如下的一个格式:
# goods = [{"name": "电脑", "price": 1999},
# {"name": "鼠标", "price": 10},
# {"name": "游艇", "price": 20},
# {"name": "美女", "price": 998},]
# 3,页面显示 序号 + 商品名称 + 商品价格，如：
# 1 电脑 1999
# 2 鼠标 10
# …
# 4,用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车(自己定义购物车)，用户还可继续添加商品。
# 5,如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 6,用户输入N为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
# 7,用户输入Q或者q退出程序。
# 8,退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少，并将购买信息显示。

goods = [{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},]
money = int(input("请输入要充值的金额:"))
shop_car = []
num = []
count = 0
for i in goods:
    print(goods.index(i) + 1, i["name"], i["price"])
while True:

    choice = input("请输入商品序号或其他信息:")

    if choice == "N":
        print(shop_car)
        for j in shop_car:
            s = "商品名称:" + j[0] + " " + "单价:" + str(j[1]) + " " + "数量:" + str(shop_car.count(j))
            num.append(s)
            count += j[1]
        print(num)
        num_set = set(num)
        for x in num_set:
            print(x)
        print(count)
        while count > money:
            need_del = input("余额不足,请输入要删除的商品名称")
            for y in shop_car:
                if need_del in y:
                    shop_car.remove(y)
                    count -= y[1]
                    for z in num_set:
                        if need_del in z:
                            num_set = list(num_set)
                            num_set.remove(z)
                            type(num_set)
                            num_set = set(num_set)

            print(count)
        money -= count
        print("购买成功")
    elif choice == "q" or choice == "Q":
        print("购买记录:",num_set)
        print("此次消费:",count)
        print("账户余额:",money)
    elif 0 < int(choice ) < 5:
        shop_car.append([goods[int(choice)-1]["name"],goods[int(choice)-1]["price"],0])

