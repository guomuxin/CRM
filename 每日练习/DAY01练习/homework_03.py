#.if条件语句的基本结构？


age = 19
sex = "男"
if age > 18:
    print("ok")
#二选一
if age < 18:
    print("未成年")
else:
    print("成年")
#多选一或零
if age > 25:
    print("大于25")
elif age > 22:
    print("大于22")
elif age > 18:
    print("大于18")

#多选一
if age > 25:
    print("大于25")
elif age > 22:
    print("大于22")
elif age > 19:
    print("大于19")
else:
    print("不详")

#多选多
if age > 18:
    print("大于18")
if age > 15:
    print("大于15")
if age > 12:
    print("大于12")

#if嵌套
if age > 18:
    if sex == "男":
        print("ok")