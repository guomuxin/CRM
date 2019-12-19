# 1，写一个程序，实现3个进程间通信，传递一个字符串
'''
from multiprocessing import Process,Queue
def w(que):
    s = "被传递的字符串"
    que.put(s)
    print("传递的字符串是:",s)

def r(que, que2):
    while True:
        temp = que.get()
        print(temp)
        que2.put(temp)

def r1(que2):
    while True:
        print(que2.get())

if __name__ == '__main__':
    que = Queue(3)
    que2 = Queue(3)
    p1 = Process(target=w, args=(que,))
    p2 = Process(target=r, args=(que, que2))
    p3 = Process(target=r1, args=(que2,))

    [i.start() for i in [p1,p2,p3]]
    [i.join() for i in [p1,p2,p3]]
'''
# 2，写一个包含10个线程的程序，，每一个子线程执行的时候都需要打印当前线程名、当前活跃线程数量
'''
import threading
def func():
    print("线程名:",threading.current_thread().name)
    print("活跃线程数量:",len(threading.enumerate()))

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
'''
# 3，已知列表 info = [1,2,3,4,55,233]生成6个线程对象,每次线程输出一个值，最后输出："the end"
'''
import threading

def func(n):
    print(n)

if __name__ == '__main__':
    info = [1,2,3,4,55,233]
    for i in info:
        t = threading.Thread(target=func, args=(i,))
        t.start()
    print("the end")
'''
# 4，有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共刷100次。账户原有500块。所以当天最后的总账应该为1500
'''
count = 500
def Pos():
    global count
    for i in range(100):
        count += 1

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=Pos)
        t.start()
    print(count)
'''