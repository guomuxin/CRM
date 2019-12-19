#11.用户输入一个分数.根据分数来判断用户考试成绩的输出不同的档次


score = int(input("请输入分数："))
if score < 60 and score > 0:
    print("不及格")
elif score > 60 and score <= 70:
    print("D")
elif score > 70 and score <= 80:
    print("C")
elif score >80 and score <= 90:
    print("B")
elif score > 90 and score <= 100:
    print("A")
else:
    print("请输入正确的成绩")