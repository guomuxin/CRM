# 1，尝试不使用进程池，可否实现循环创建进程并调用
# from multiprocessing import Process
#
# def func():
#     print("a")
#
# if __name__ == '__main__':
#     lst = []
#     for i in range(5):
#         lst.append(Process(target=func))
#
#     for j in lst:
#         j.start()
#
#     for z in lst:
#         z.join()

# 2，改写下列程序，分别别实现下述打印效果
# from multiprocessing import Process
# import time
# import random
# def task(n):
# time.sleep(random.randint(1,3))
# print('-------->%s' %n)
# if name == 'main':
# p1=Process(target=task,args=(1,))
# p2=Process(target=task,args=(2,))
# p3=Process(target=task,args=(3,))
# p1.start()
# p2.start()
# p3.start()
#
# print('-------->4')
# 效果一：保证最先输出-------->4
# -------->4
# -------->1
# -------->3
# -------->2
# 效果二：保证最后输出-------->4
# -------->2
# -------->3
# -------->1
# -------->4
# 效果三：保证按顺序输出
# -------->1
# -------->2
# -------->3
# -------->4

#效果一
# from multiprocessing import Process
# import time
# import random
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
# if __name__ == '__main__':
#
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#     p1.start()
#     p2.start()
#     p3.start()
#     # p1.join()
#     # p2.join()
#     # p3.join()
#     print('-------->4')

#效果二
# from multiprocessing import Process
# import time
# import random
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
# if __name__ == '__main__':
#
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     print('-------->4')

#效果三
from multiprocessing import Process
import time
import random
def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)
if __name__ == '__main__':

    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

    p3.start()

    p3.join()
    print('-------->4')