# D32 socketsever,粘包,远程执行命令

## 一、socketsever

- socketsever作用:可以使用socketserver来创建socket用来简化并发服务器

- socketserver可以实现和多个客户端通信（实现并发处理多个客户端请求的Socket服务端）

  它是在socket的基础上进行了一层封装，也就是说底层还是调用的socket

- 处理过程:收到处理请求->实例化请求处理程序(服务器类的实例)->根据服务器类和请求处理类调用处理方法(handle)

  例如:基本请求程序类（BaseRequestHandler）调用方法 handle 。此方法通过属性 self.request 来访问客户端套接字

  ```
  创建请求处理类:
  import socketsever
  class Mysever(socketsever.BaseRequestHandler): #自定义请求处理类,必须继承																BaseRequestHandler类
  	def handle(self):             #一定要实现handle方法
  		print(self.request.recv(1024))  #handle方法内部可以通过self.request获取套接字对象
  										对请求的处理都在handle方法内部实现
  					
  ```

  ```
  实例化请求处理程序(服务器类):
  s1 = socketsever.ThreadingTCPSever((ip,端口号),Mysever) #参数为地址,自定义的请求处理类,这样#ForkingTCPServer 用于创建进程,只能在linux中使用
  														就可以在建立连接时自动调用请求处理类															中的handle()方法
  ```

  ```
  设置地址可重用:
  socketsever.TCPSever.allow_reuse_address = True
  ```

  ```
  开启服务端:
  s1.sever_forever() #此方法可以处理多个请求,永远执行
  s1.handle_request()#此方法只能处理一个请求,估不常用
  ```

## 二、subprocess远程执行命令

- Python可以通过实例化subprocess模块中的Popen类,使用其中的方法来执行命令

  ```
  创建Popen类对象:
  import subprocess
  from socket import *
  s = socket(AF_INET, SOCK_STREAM)
  cmd = s.recv(1024).decode()        #要执行的命令
  obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)   #创建Poen对象,stdout和stderr参数这么设置是把信息丢在管道中,让原本在							终端显示的信息显示在控制台
  ```

  ```
  读取正确结果和错误结果:
  correct_msg = obj.stdout.read().decode("gbk") #命令正确时打印的结果
  error_msg = obj.stderr.read().decode("gbk")		#命令有误时打印的结果
  												#在windows端read的结果是gbk编码的
  ```

## 三、解决粘包问题

- 粘包:TCP协议传输数据时会在发送端和接收端都设置缓冲区,以减少网络速率对数据传输的影响,当多次发送的数据被一次接收,或一次接收没能全部接收发送的数据就是粘包,这样会出现结果不完整或异常的情况

- 只有TCP中会出现粘包,因为UDP是面向消息的协议,每个UDP段都是一条消息,以消息为接收单位,不会出错,而TCP是以数据流为接收单位,所以会出现粘包的情况

- 产生粘包的根本原因:不管是recv还是send都不是直接向对方接收数据(一个send不一定对应一个recv),而是操作自己的缓冲区

  例如基于tcp的套接字客户端往服务端上传数据，发送时数据内容是按照一段一段的字节流发送的，

  在接收方看了，根本不知道该文件的字节流从何处开始，在何处结束

- 所谓粘包问题主要还是因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的

- 粘包不一定会发生

  如果发生了：1.可能是在客户端已经粘了

  　　　　　　2.客户端没有粘，可能是在服务端粘了

- 发送端粘包:发送数据量小,时间间隔短的情况下,TCP优化算法会把他们当作一个包发送,产生粘包

- 接收端粘包:接收方没能及时(或没能完整)接收全部数据,这样下次接收实际上是从上次没有被接收的地方开始

- 解决方法:

  - 问题的根源在于：接收端不知道发送端将要传送的字节流的长度

  - 所以解决粘包的方法就是发送端在发送数据前，发一个头文件包，告诉发送的字节流总大小，然后接收端来一个死循环接收完所有数据

    ```
    服务器端:
    from socket import *
    import subprocess
    import struct
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("192.168.34.150", 8083))
    s.listen(5)
    
    while True:
        conn, addr = s.accept()
        while True:
            cmd = conn.recv(1024).decode("utf-8")
            ret = subprocess.Popen(cmd, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            correct_msg = ret.stdout.read()
            error_msg = ret.stderr.read()
            total_data = correct_msg + error_msg  
            print(len(total_data))
            print(struct.pack("i",len(total_data)))  #将数据长度打包先发送给客户端
            conn.send(struct.pack("i",len(total_data))) 
            conn.send(total_data)  
    ```

    ```
    客户端:
    from socket import *
    import struct
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("192.168.34.150", 8090))
    while True:
        cmd = input("请输入:")
        s.send(cmd.encode())    
        total_size = struct.unpack("i", s.recv(4))[0]  #首先接收4字节的报头,里面说明了数据的														长度
        total_data = b""
        while len(total_data) < total_size:			#只要目前接收到的数据长度小于真正的数据长												度就一直接收
            if total_size - len(total_data) < 1024:#为了防止最后一次接收将后续传入的数据也接												收到,要判断一下
                total_data += s.recv(total_size - len(total_data))
            else:
                total_data += s.recv(1024)
        print(total_data.decode("gbk"))
    
    ```

    /