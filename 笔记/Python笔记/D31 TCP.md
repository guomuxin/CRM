# D31 TCP

## 一、TCP

- TCP(传输控制协议):一种面向连接,提供可靠传输,速度比UDP稍慢的传输层协议,提供稳定性,保证数据一定能够收到,使用频率高于UDP,web服务器都用TCP
- TCP中,任何一方收到对方的数据后一定会回复一个确认包
- TCP通信模型:
  - 传输数据前必须先建立连接
  - ![1571816790768](.\D31 TCP.assets\1571816790768.png)

## 二、TCP的三次握手,四次挥手

- 三次握手:用于客户端与服务器建立连接:
  - 第一次握手:客户端向服务器发送一个SYN(请求同步)包,提出连接请求,里面包含数据包序号seq x,这时客户端进入SYN_SENT(请求连接)状态
  - 第二次握手:服务器收到请求包后返回一个确认包ACK,数据包序号为x+1,客户端会将收到的ACK包序号与之前自己发出的SYN包序号x对比,如果对比结果是SYN包序号x+1就接收.服务器同时发出自己的SYN包,里面也包含一个数据包序号y,此时服务器进入SYN_RECV(请求派遣)状态
  - 第三次握手:客户端发出针对刚才收到的来自服务器的SYN包的ACK包,包序号为y+1,服务器收到ACK包再与自己之前发出的SYN包序号对比,如果是y+1就接收,连接建立成功
  - 理想状态下,只要双方都没有主动断开连接,连接就会一直保持下去
  - ![1571817473422](.\D31 TCP.assets\1571817473422.png)

- 四次挥手:用于断开连接
  - 第一次挥手:主动关闭方(通常是客户端)调用close方法,发出一个长度为0的数据包和FIN(结束标志)
  - 第二次挥手:被动关闭方收到FIN后,会返回给主动关闭方一个ACK包,序号为收到的包的序号+1
  - 第三次挥手:被动关闭方发送一个FIN包
  - 第四次挥手:主动关闭方收到FIN包后回复一个ACK包.序号为收到包的序号+1,连接正式断开
  - ![1571817841984](.\D31 TCP.assets\1571817841984.png)

## 三、TCP服务器

- 长连接:三次握手四次挥手之间分多次传递完数据(看网络视频,玩在线游戏时),长时间占用某个套接字

- 短链接:三次握手四次挥手之间传递少部分数据,多次握手多次挥手才传递完所有数据(例如浏览器),短时间占用套接字

- TCP服务器流程:

  - 1.创建套接字
  - 2.绑定ip,端口
  - 3.listen监听连接请求,可以设置最大排队数(不是最大连接数,最大连接数不能设置)
  - 4.accept等待客户端连接,接收客户端请求,返回新套接字对象和客户端地址,服务器绑定的端口只是用于接收客户端连接,具体的操作要交给新创建的套接字对象,且端口随机.以保证能够接收下一个连接请求
  - 5.recv/send接收发送数据
  - 6.关闭新建的临时套接字,结束当前连接
  - 也可以close()关闭主套接字,但通常不需要

- 客户端服务流程:

  - 1.创建套接字

  - 2.可以绑定ip,端口,也可以不绑定

  - 3.connect连接服务器,会将自己的ip和端口发送给服务器

  - 4.send/recv接收发送数据

  - 5.close关闭套接字,断开连接

    ```
    from socket import *
    
    s = socket(AF_INET, SOCK_STREAM)
    
    s.connect(("192.168.34.150",7788))
    while True:
        msg = input("发送:")
        s.send(msg.encode())
    s.close()
    ```

    

## 四、并发服务器

- serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1）:

  - 在多进程服务器中,这个设置可以允许该套接字的端口连接多个客户端,因为在多进程中,主套接字接收到连接请求后会将请求分发给子进程执行,所以该端口同时连接多个客户端没有影响
  - 在多线程服务器中,当一个端口被使用释放后,操作系统会将其锁定几分钟,这时其他线程就无法立即使用这个端口,而SO_REUSEADDR可以使得刚端口被释放后不被锁定

- 多进程服务器:

  ```
  from socket import *
  from multiprocessing import Process
  def handelClient(conn,addr):
      while True:
          data = conn.recv(1024)
          if len(data) > 0:	#如果收到的数据包长度为0,说明客户端发出了断开连接请求(发送空内容也
              print(data)		会有相同状况)
          else:
              print("已关闭连接")
              break
      conn.close()			#可关可不关,因为函数执行结束会销毁所有空间
  
  def main():
      s = socket(AF_INET, SOCK_STREAM)
      s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
      local_addr = ("192.168.34.150", 7788)
      s.bind(local_addr)
      s.listen(5)
      try:
          while True:
              conn,addr = s.accept()
              p = Process(target=handelClient, args=(conn,addr))
              p.start()
              conn.close()  #在函数内和这里都要关闭一次conn,因为子进程和主进程都保留了一份conn
      except Exception as e:	内容,而主线程的conn只是为了获取该套接字并传给子进程,所以可以立即
          print(e)			关闭,这里必须关闭,因为只要不close该套接字就会一直存在占用内存
      finally:
          s.close()		
  if __name__ == '__main__':
      main()
  ```

- 多线程服务器:

  ```
  from socket import *
  import threading
  def handelClient(conn,addr):
      while True:
          data = conn.recv(1024)
          if len(data) > 0:
              print(data.decode())
          else:
              print("已关闭连接")
              break
      conn.close()
  
  def main():
      s = socket(AF_INET, SOCK_STREAM)
      s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
      local_addr = ("192.168.34.150", 7788)
      s.bind(local_addr)
      s.listen(5)
      try:
          while True:
              conn,addr = s.accept()
              t = threading.Thread(target=handelClient, args=(conn,addr))
              t.start()			#这里不close conn由于线程间共享空间,一个关闭则该程序内都不能
      except Exception as e:		使用
          print(e)
      finally:
          s.close()
  if __name__ == '__main__':
      main()
  ```

- 多线程和多进程服务器的主要区别就是在于是否需要关闭conn