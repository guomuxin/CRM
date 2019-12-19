# 1.有变量name = "aleX leNb" 完成如下操作：
# 移除 name 变量对应的值两边的空格,并输出处理结果
# 判断 name 变量是否以 "al" 开头,并输出结果
# 判断name变量是否以"Nb"结尾,并输出结果
# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# 将name变量对应的值根据第一个"l"分割,并输出结果。
# 将 name 变量对应的值变大写,并输出结果
# 将 name 变量对应的值变小写,并输出结果
# 判断name变量对应的值字母"l"出现几次，并输出结果
# 如果判断name变量对应的值前四位"l"出现几次,并输出结果
# 请输出 name 变量对应的值的第 2 个字符?
# 请输出 name 变量对应的值的前 3 个字符?
# 请输出 name 变量对应的值的后 2 个字符?

name = "aleX leNb"
print(name.strip())
print(name.startswith("al"))
print(name.endswith("Nb"))
print(name.replace("l","p"))
print(name.replace("l","p",1))
print(name.split("l"))
print(name.split("l",1))
print(name.upper())
print(name.lower())
print(name.count("l"))
print(name.count("l",0,4))
print(name[1])
print(name[:3])
print(name[-2:])

# 2.有字符串s = "123a4b5c"
# 通过对s切片形成新的字符串s1,s1 = "123"
# 通过对s切片形成新的字符串s2,s2 = "a4b"
# 通过对s切片形成新的字符串s3,s3 = "1345"
# 通过对s切片形成字符串s4,s4 = "2ab"
# 通过对s切片形成字符串s5,s5 = "c"
# 通过对s切片形成字符串s6,s6 = "ba2"

s = "123a4b5c"

s1 = s[:3]
print(s1)
s2 = s[3:6]
print(s2)
s3 = s[::2]
print(s3)
s4 = s[1:-1:2]
print(s4)
s5 = s[-1]
print(s5)
s6 = s[-3::-2]
print(s6)

# 3.使用while和for循环分别打印字符串s="asdfer"中每个元素。

s = "asdfer"
count = 0
while count < len(s):
    print(s[count])
    count += 1

for i in s:
    print(i)

#4.使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
s = "asdfer"
for i in s:
    print(s)

#5.使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
s = "abcdefg"

for i in s:
    print(i + "sb")

#6.使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。

s = "321"
for i in s:
    print(f"倒计时{i}秒")
print("出发！")

#7.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。

content = input("请输入内容：")
nums = content.split("+")
print(int(nums[0].strip()) + int(nums[1].strip()))

#8.选做题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。

content = input("请输入内容：")
nums = content.split("+")
sum = 0
for i in nums:
    sum += int(i.strip())
print(sum)


# 9.计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla

content = input("请输入内容")
count = 0
for i in content:
    if i.isdigit():
        count += 1
    else:
        continue

print(f"有{count}个整数")

#10.写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
sum = 0
for i in range(1,100):
    if i == 88:
        continue
    else:
        if i % 2 == 1:
            sum += i
        else:
            sum -= i
print(sum)

#11.选做题：写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。

while True:
    chocie_01 = input("输入A走大路，输入B走小路,输入C绕道回家")
    if chocie_01 == "A":
        print("走大路回家")
        choice_02 = input("公交车or步行")
        if choice_02 == "公交车":
            print("10分钟到家")
            break
        elif choice_02 == "步行":
            print("20分钟到家")
            break
        else:
            print("输入错误")
            continue
    elif chocie_01 == "B":
        print("走小路回家")
        break
    elif chocie_01 == "C":
        print("绕道回家")
        choice_03 = input("游戏厅or网吧")
        if choice_03 == "游戏厅":
            print("一个半小时到家，爸爸在家，拿棍等你")
            continue
        elif choice_03 == "网吧":
            print("两个小时到家，妈妈已做好了战斗准备")
            continue
        else:
            print("输入错误")
            continue
    else:
        print("输入错误")
        continue

#12.选做题：判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海⾃来⽔来⾃海上

content = input("请输入内容：")
if content == content[::-1]:
    print("是回文")
else:
    print("不是回文")
#13.制作趣味模板程序(使用字符串格式化)需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进行任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
name = input("请输入名字：")
addr = input("请输入地址：")
hobby = input("请输入爱好：")
print(f"敬爱可亲的{name},最喜欢在{addr}干{hobby}")