#6.提⽰⽤户输入他的年龄, 通过程序进⾏判断.


age = int(input("请输入年龄："))
if age <= 10:
    print("小屁孩")
elif age > 10 and age <= 20:
    print("青春叛逆期的小屁孩")
elif age > 20 and age <= 30:
    print("开始定性")
elif age > 30 and age <= 40:
    print("看老老大不了,赶紧结婚小屁孩儿")
elif age > 40 and age <= 50:
    print("家里有个不听话的小屁孩儿")
elif age > 50 and age <= 60:
    print("自己马上变成不听话的老屁孩儿")
elif age > 60 and age <= 70:
    print("活着还不错的老屁孩儿")
elif age > 70 and age <= 90:
    print("人生就快结束了的一个老屁孩儿")
else:
    print("再见了这个世界")