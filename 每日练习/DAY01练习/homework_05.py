#5.利用if语句写出猜大小的游戏：


answer = 66

while True:
    guess_number = int(input("请输入猜测结果："))
    if guess_number > answer:
        print("太大了")
        continue
    elif guess_number < answer:
        print("太小了")
        continue
    else:
        print("猜对了")
        break