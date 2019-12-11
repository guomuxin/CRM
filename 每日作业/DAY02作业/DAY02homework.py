#1.判断下列逻辑语句的结果,一定要自己先分析 (3<4这种是一体)

1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
1 > 1 or 3 < 4 or False and 9 > 8 or 7 < 6
1 > 1 or 3 < 4 or False or 7 < 6
True or False or 7 < 6
True

not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
8 or 3 and 4 or 2 and 0 or 9 and 7
8 or 4 or 0 or 7
8 or 0 or 7
8 or 7
8

#2.求出下列逻辑语句的值,一定要自己分析

8 or 3 and 4 or 2 and 0 or 9 and 7
8 or 4 or 0 or 7
8 or 0 or 7
8

0 or 2 and 3 and 4 or 6 and 0 or 3
0 or 3 and 4 or 6 or 0 or 3
0 or 4 or 6 or 0 or 3
4

1 and 0 or 8 and 9 and 5 or 2
0 or 8 and 9 and 5 or 2
0 or 9 and 5 or 2
0 or 5 or 2
5

4 or 8 and not False and 8 or 9
4 or 8 and True and 8 or 9
4 or True and 8 or 9
4 or 8 or 9
4

#3.下列结果是什么? (2>1这种是一体)

6 or 2 > 1
6

3 or 2 > 1
3

0 or 5 < 4
False

5 < 4 or 3
3

2 > 1 or 6
True

3 and 2 > 1
True

0 and 3 > 1
0

2 > 1 and 3
3

3 > 1 and 0
0

3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
2 or 2 < 3 and 3 and 4 or 3 > 2
2 or 3 and 4 or 3 > 2
2 or 4 or 3 > 2
2

#4.简述ASCII、Unicode、utf-8编码
'''
- ASCII码：不支持中文，一个字符占8位
- unicode：英文和中文都是一个字符占4个字节，32位
- utf-8：目前最流行的编码方式
  - 英文：一个字符占1字节
  - 欧洲：一个字符占2字节
  - 中国：一个字符占3字节
'''

#5.简述位和字节的关系？
'''
一字节= 8位
'''

#6.while循环语句基本结构？
'''
while 条件：
    循环体
'''

#7.利用while语句写出猜大小的游戏：
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


#8.在7题的基础上进行升级：
answer = 66
count = 0
while count<3:

    count += 1
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

else:
    print("太笨了。。。")


#09 使用while循环输出 1 2 3 4 5 6 8 9 10

count01 = 0

while count01 < 10:
    count01 += 1
    if count01 != 7:
        print(count01)
    else:
        continue


#10 求1-100的所有数的和

count02 = 1
sum = 0
while count02 <= 100:
    sum += count02
    count02 += 1
print(sum)

#11.输出 1-100 内的所有奇数

count03 = 1

while count03 <= 100:
    if count03 % 2 != 0:
        print(count03)
    count03 += 1

#12.输出 1-100 内的所有偶数

count04 = 1

while count04 <= 100:
    if count04 % 2 == 0:
        print(count04)
    count04 += 1

#13.求1-2+3-4+5 ... 99的所有数的和

count05 = 1
sum = 0
while count05 <= 99:
    if count05 % 2 == 0:
        sum -= count05
    else:
        sum += count05
    count05 += 1
print(sum)

#14.⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
count06 = 3
while count06 >= 1:
    name = input("请输入用户名：")
    if name == "guo":
        print("登录成功")
        break
    else:
        count06 -= 1
        print( f"输入错误，还剩下{count06}次机会")
