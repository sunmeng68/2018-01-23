# -*- coding: utf-8 -*-
import  socket

#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接,参数是一个tuple,包含地址和端口号
s.connect(('www.sina.com',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer=[]
while True:
    #每次最多接收1K字节
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data =b''.join(buffer)
s.close()
#HTTP头和网页分离
header,html=data.split(b'\r\n\r\n',1)
print (header.decode('utf-8'))
#把接收的数据写入文件
with open('sina.html','wb') as f:
    f.write(html)


