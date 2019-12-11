# 1，写一个程序，线程C在线程B后执行，线程B在线程A之后进行
'''
import threading

def funA():
    mutex1.acquire()
    print("线程A")
    mutex2.release()
def funB():
    mutex2.acquire()
    print("线程B")
    mutex3.release()
def funC():
    mutex3.acquire()
    print("线程C")
    mutex1.release()
if __name__ == '__main__':
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    mutex2.acquire()
    mutex3 = threading.Lock()
    mutex3.acquire()

    tA = threading.Thread(target=funA)
    tB = threading.Thread(target=funB)
    tC = threading.Thread(target=funC)

    tA.start()
    tB.start()
    tC.start()
'''
# 2，编写一个程序，开启3个线程，这3个线程的name分别为A、B、C，每个线程将自己的name在屏幕上打印10遍，要求输出结果必须按ABC的顺序显示；如：ABCABC….依次递推

import threading
count = 10
def funA():
    global count
    while count:
        mutex1.acquire()
        print(tA.name)
        count -= 1
        mutex2.release()

def funB():
    while True:
        mutex2.acquire()
        print(tB.name)
        mutex3.release()
def funC():
    while True:
        mutex3.acquire()
        print(tC.name)
        mutex1.release()
if __name__ == '__main__':
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    mutex2.acquire()
    mutex3 = threading.Lock()
    mutex3.acquire()

    tA = threading.Thread(target=funA, name="A")
    tB = threading.Thread(target=funB, name="B")
    tC = threading.Thread(target=funC, name="C")

    tA.start()
    tB.start()
    tC.start()

# from greenlet import greenlet
# count = 10
# def funA():
#     while True:
#         if count:
#             print("A")
#             g2.switch()
#         else:
#             return
# def funB():
#     while True:
#         if count:
#             print("B")
#             g3.switch()
#         else:
#             return
#
# def funC():
#     while True:
#         if count:
#             print("C")
#             g1.switch()
#         else:
#             return
#
#
# g1 = greenlet(funA)
# g2 = greenlet(funB)
# g3 = greenlet(funC)
# g1.switch()
# 3，简述生产者与消费者模式（用自己的话默写）
# 参考建议：生产者与消费者模式是通过一个容器来解决生产者与消费者的强耦合关系，生产者与消费者之间不直接进行通讯，而是利用阻塞队列来进行通讯，
# 生产者生成数据后直接丢给阻塞队列，消费者需要数据则从阻塞队列获取，实际应用中，生产者与消费者模式则主要解决生产者与消费者生产与消费的速率不一致的问题，
# 达到平衡生产者与消费者的处理能力，而阻塞队列则相当于缓冲区。