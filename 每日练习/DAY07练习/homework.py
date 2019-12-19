# 1.看代码写结果
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v1.append(6)
# print(v1)     [1,2,3,4,5,6]
# print(v2)        [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]

# 2.看代码写结果
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)         [222,2,3,4,5]
# print(v2)         [[222,2,3,4,5],[222,2,3,4,5],[222,2,3,4,5]]
# 3.看代码写结果，并解释每一步的流程。
# v1 = [1,2,3,4,5,6,7,8,9]
# v2 = {}
# for item in v1:
#     if item < 6:          筛选v1中大于6的值
#         continue
#     if 'k1' in v2:                如果v2里已经有k1这个键,则追加
#         v2['k1'].append(item)
#     else:                     没有k1这个键就创建
#         v2['k1'] = [item ]
# print(v2)
{"k1":[6,7,8,9]}
# 4.简述赋值和深浅拷贝？
#赋值后两者就是一个东西,都指向同一个地址
# 5.看代码写结果
# import copy
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)           True
# print(v1 is v3)           True
# 6.看代码写结果
# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)           False
# print(v1 is v3)            False
# 7.看代码写结果
# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# ​
# print(v1[0] is v2[0])     True
# print(v1[0] is v3[0])       True
# print(v2[0] is v3[0])         True


# 8.看代码写结果
# import copy
# ​
# v1 = [1,2,3,4,[11,22]]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# ​
# print(v1[-1] is v2[-1])       True
# print(v1[-1] is v3[-1])       False
# print(v2[-1] is v3[-1])       False
# 9.看代码写结果
# import copy
# # ​
# # v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
# # v2 = copy.copy(v1)
# # ​
# # print(v1 is v2)             False
# # ​
# # print(v1[0] is v2[0])          True
# # print(v1[3] is v2[3])           True
# # ​
# # print(v1[3]['name'] is v2[3]['name'])           True
# # print(v1[3]['numbers'] is v2[3]['numbers'])         True
# # print(v1[3]['numbers'][1] is v2[3]['numbers'][1])      True

# 10.看代码写结果
# import copy
# v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
# v2 = copy.deepcopy(v1)
# print(v1 is v2)               False
# print(v1[0] is v2[0])          True
# print(v1[3] is v2[3])            False
#
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])


# 11.请说出下面a,b,c三个变量的数据类型。
# a = ('太白金星')
# b = (1,)
# c = ({'name': 'barry'})
# a:字符串
# b:元组
# c:字典

# 12.按照需求为列表排序：
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# # 从大到小排序
# # 从小到大排序
# # 反转l1列表
l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
l1.sort(reverse=True)
print(l1)
l1.sort()
print(l1)
l1.reverse()
print(l1)
# 13.利用python代码构建一个这样的列表(升级题)：
# [['_','_','_'],['_','_','_'],['_','_','_']]
lst = []
lst1 = []
for j in range(3):

    lst1.append("_")
    lst.append(lst1)
print(lst)
# 14.看代码写结果：
# l1 = [1,2,]
# l1 += [3,4]
# print(l1)
[1,2,3,4]

# 15.看代码写结果：
# dic = dict.fromkeys('abc',[])
# dic['a'].append(666)
# dic['b'].append(111)
# print(dic)
{"a":[666,111],"b":[666,111],"c":[666,111]}

# 16.l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除
l1 = [11, 22, 33, 44, 55]
l1 = l1[::2]
print(l1)
# 17.dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删除.
dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
dic1 = dic.copy()
for k in dic1:
    if "k" in k:
        dic.pop(k)
print(dic)
# 18.完成下列需求：
# s1 = '宝元'
# 将s1转换成utf-8的bytes类型。
# 将s1转化成gbk的bytes类型。
# b = b'\xe5\xae\x9d\xe5\x85\x83\xe6\x9c\x80\xe5\xb8\x85'
# b为utf-8的bytes类型，请转换成gbk的bytes类型。
s1 = '宝元'
b = b'\xe5\xae\x9d\xe5\x85\x83\xe6\x9c\x80\xe5\xb8\x85'
print(s1.encode("utf-8"))
print(s1.encode("gbk"))
print(b.decode().encode("gbk"))


# 19.用户输入一个数字，判断一个数是否是水仙花数。
# 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数,
# 例如: 153 = 1**3 + 5**3 + 3**3
x = input("请输入一个数字:")
sum = 0
for i in str(x):
    sum += int(i)**3
if sum == int(x):
    print(f"{x}是水仙花数")
else:
    print(f"{x}不是水仙花数")
# 20.把列表中所有姓周的⼈的信息删掉(此题有坑, 请慎重):
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# 结果: lst = ['麻花藤']
lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
lst1 = lst.copy()
for i in lst1:
    if "周" in i:
        lst.remove(i)
print(lst)
# 21.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (选做题)
# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
# locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
# 结果: {'⿊⻰江':2, '⼭东': 2, '上海': 1}
cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}

result = {}
for i in cars:
    s = i[0]
    if s in locals:
        if locals[s] not in result:
            result[locals[s]] = 1
        else:
            result[locals[s]] += 1
print(result)