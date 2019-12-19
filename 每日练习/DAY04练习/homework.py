# 1.写代码，有如下列表，按照要求实现每一个功能
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
# 列表中追加元素"seven",并输出添加后的列表
# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# 请删除列表中的元素"ritian",并输出添加后的列表
# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# 请删除列表中的第2至4个元素，并输出删除元素后的列表

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
print(len(li))
li.append("seven")
print(li)
li.insert(1,"Tony")
print(li)
li[2] = "Kelly"
print(li)
l2=[1,"a",3,4,"heart"]
li.extend(l2)
print(li)
s = "qwert"
li.extend(s)
print(li)
print(li.pop(1))
print(li)
del li[1:4]
print(li)


# 2.写代码，有如下列表，利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# 通过对li列表的切片形成新的列表l5,l5 = ["c"]
# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]

li = [1, 3, 2, "a", 4, "b", 5,"c"]
l1 = li[0:3]
print(l1)
l2 = li[3:6]
print(l2)
l3 = li[::2]
print(l3)
l4 = li[1:-2:2]
print(l4)
l5 = li[-1]
print(l5)
l6 = li[-3::-2]
print(l6)

# 3.写代码，有如下列表，按照要求实现每一个功能。
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"tt"变成大写（用两种方式）。
# 将列表中的数字3变成字符串"100"（用两种方式）。
# 将列表中的字符串"1"变成数字101（用两种方式）。

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 方式1
lis[3][2][1][0] = lis[3][2][1][0].upper()
print(lis)
#方式2
lis[3][2][1][0] = lis[3][2][1][0].replace("t","T")
print(lis)

#方式1
lis[1] = "100"
list[3][2][1][1] = "100"
print(lis)

#方式2
lis[3][2][1].pop(1)
lis.pop(1)
lis.insert(1,"100")
lis[3][2][1].insert(1,"100")
print(lis)

#方式1
lis[3][2][1][2] = 101

#方式2
lis[3][2][1].pop(2)
lis[3][2][1].insert(2,101)
print(lis)

# 4.请用代码实现：
# li = ["alex", "wusir", "taibai"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
li = ["alex", "wusir", "taibai"]

s = li[0] + "_" + li[1] + "_" + li[2]
print(s)
# 5.利用for循环和range打印出下面列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for i in li:
    print(li.index(i))

# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
o_list = []
for i in range(2,101,2):
    o_list.append(i)
print(o_list)


# 7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
three_list = []
for i in range(1,50):
    if i % 3 == 0:
        three_list.append(i)

print(three_list)

# 8.利用for循环和range从100~1，倒序打印。

for i in range(100,0,-1):
    print(i)

# 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
os_list = []
for i in range(100,9,-2):
    os_list.append(i)
for j in os_list:
    if j % 4 != 0:
        os_list.remove(j)
print(os_list)

# 10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。

one_list = []
count = 0
for i in range(1,31):
    one_list.append(i)

for j in one_list:
    if j % 3 == 0:
        one_list[count] = "*"
    count += 1
print(one_list)


# 11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]

li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
count = 0
l1 = []
for i in li:
    li[count] = li[count].strip()
    if (li[count].startswith("A") or li[count].startswith("a")) and li[count].endswith("c"):
        l1.append(li[count])
    count += 1
print(l1)

# 12.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["老师苍", "东京比较热", "武兰", "波多"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（老师苍就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。

li = ["老师苍", "东京比较热", "武兰", "波多"]
coments = input("请输入评论内容：")
for i in li:
    if i in coments:
        coments = coments.replace(i,"*"*len(i))
print(coments)

# 13.有如下列表（选做题）
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# 1
# 3
# 4
# alex
# 3
# 7
# 8
# taibai
# 5
# ritian
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
for i in li:
    if type(i) == list:
        for j in i:
            if type(j) == str:
                j = j.lower()
            print(j)
    else:
        if type(i) == str:
            i = i.lower()
        print(i)