# D46手写web框架

## 一、http协议

- http:超文本传输协议(**H**yper**T**ext **T**ransfer **P**rotocol),目前使用最广泛的是http1.1版本

- http是客户端与服务器端进行请求和应答时的协议标准,基于tcp/ip协议的应用层协议.客户向80端口发送请求报文,这个客户端被称为"用户代理",服务端发送的信息中包含用户代理信息("user agent"),从而判断消息来源.例如是来自浏览器还是手机客户端,或者是其他方式

- http默认端口:80

- http工作原理:

  - 客户端发送请求报文,包含:请求的方法,URL,协议版本,请求头部和请求数据
  - 服务端回复状态行以响应请求,包含:协议版本,状态码,服务器信息,响应头部,响应数据
  - 请求/响应步骤:
    - 1.客户端(通常是浏览器)与web服务器端(端口80)建立TCP连接
    - 2.客户端通过TCP套接字发送情求报文
    - 3.服务器端接受请求,解析请求,定位资源并通过TCP套接字返回响应
    - 4.释放TCP连接
      - 若连接模式为无连接(close),则每次服务器端发送完客户端请求的数据后就主动断开连接,以保证资源不被长期占用
      - 若连接模式为短连接(keepalive),则每次服务器端发送完客户端情求的数据后保持连接一段时间,以免客户连续多次发送请求导致需要频繁建立,断开连接
    - 5.客户端浏览器解析html内容:首先解析状态行,查看状态码,之后解析每一个响应头,最后读取响应数据html,对其进行格式化

- http协议是无状态协议,也就是说不会保存之前连接留下的数据,每次建立都要把所有数据都传输一遍,不能做持久化处理,可以使用cookie或session技术进行保存

- http请求方法:

  - get:向服务器发出查看资源的请求,只用在读取数据时,因为get请求会将form表单中的内容拼接到url后面发送到客户端,以?分隔,数据与数据之间用&分隔不够安全,由于URL长度有限制,所以get方法提交数据有大小限制
  - post:向指定资源提交数据,请求服务器进行处理(例如表单提交,上传文件等),数据在请求文本中,这个请求可能会创建新的资源或修改现有资源
  - head:和get一样,也是发出指定资源的请求,只不过服务器将不传回资源的本文部分。它的好处在于，使用这个方法可以在不必传输全部内容的情况下，就可以获取其中“关于该资源的信息”（元信息或称元数据)
  - put:向指定资源位置上传其最新内容
  - delete:请求服务器删除Request-URI所标识的资源。
  - trace:回显服务器收到的请求，主要用于测试或诊断。
  - options:这个方法可使服务器传回该资源所支持的所有HTTP请求方法。用'*'来代替资源名称，向Web服务器发送OPTIONS请求，可以测试服务器功能是否正常运作。
  - connect:HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。通常用于SSL加密服务器的链接（经由非加密的HTTP代理服务器）

- http状态码:

  所有HTTP响应的第一行都是状态行，依次是当前HTTP版本号，3位数字组成的状态代码，以及描述状态的短语，彼此由空格分隔。

  - 1xx消息——请求已被服务器接收，继续处理
  - 2xx成功——请求已成功被服务器接收、理解、并接受
  - 3xx重定向——需要后续操作才能完成这一请求
  - 4xx请求错误——请求含有词法错误或者无法被执行
  - 5xx服务器错误——服务器在处理某个正确请求时发生错误

## 二、URL

- URL:统一资源定位符,访问资源的完整地址,包含以下信息:
  - 传送协议:http
  - 层级URL标记符号://
  - 访问资源需要的凭证信息,可省略
  - 服务器:通常为域名,也可为ip地址
  - 端口号:默认80,若为80可省略
  - 路径:服务器下资源的具体位置,目录之间以/分隔
  - 查询:get模式下的参数,以?为起点
  - 片段:以#为起点

## 三、报文格式

- 请求格式:

  ![img](https://images2018.cnblogs.com/blog/867021/201803/867021-20180322001733298-201433635.jpg)

- 响应格式:

  ![img](https://images2018.cnblogs.com/blog/867021/201803/867021-20180322001744323-654009411.jpg)

## 四、简易手写web框架

```
from socket import *
import threading
import time
s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",8081))
s.listen(5)

def html(conn):
    with open("login.html","rb") as f:
        send_to_client = f.read().decode()
    send_to_client = send_to_client.replace("%xxoo",str(time.time()))  #动态页面
    conn.send(send_to_client.encode())
    conn.close()

def html2(conn):
    with open("setting.html","rb") as f:
        send_to_client = f.read()
    conn.send(send_to_client)
    conn.close()

def css(conn):
    with open("login.css","rb") as f:
        send_to_client = f.read()
    conn.send(send_to_client)
    conn.close()

def js(conn):
    with open("login.js","rb") as f:
        send_to_client = f.read()
    conn.send(send_to_client)
    conn.close()

def img(conn):
    with open("1.jpeg","rb") as f:
        send_to_client = f.read()
    conn.send(send_to_client)
    conn.close()

def icon(conn):
    with open("1.png","rb") as f:
        send_to_client = f.read()
    conn.send(send_to_client)
    conn.close()

url_pattern = {
    "/":html,
    "/login.css":css,
    "/login.js":js,
    "/1.jpeg":img,
    "/favicon.ico":icon,
    "/setting.html":html2
}
while True:
    conn,addr = s.accept()
    info = conn.recv(1024).decode()
    print(info)
    action = info.split(" ")[1]   
    
    conn.send(b"HTTP/1.1 200 ok \r\n\r\n")   
    if action in url_pattern:    #通过判断请求的内容响应不同数据
        t = threading.Thread(target=url_pattern[action],args=(conn,))
        t.start()
```

五、