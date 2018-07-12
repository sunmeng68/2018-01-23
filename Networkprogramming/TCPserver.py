# -*- coding: utf-8 -*-
import socket
import threading,time

#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#指定端口后
s.bind(('127.0.0.1',9999))
#启动监听，参数是等待连接的最大数量
s.listen(5)
print('Waiting for connection')

#每个连接都必须创建新线程或者进程来处理
def tcplink(sock,addr):
    print ('Accept new collections from %s:%s'%addr)
    sock.send(b'welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print ('Connection from %s:%s closed' %addr)

#通过一个永久循环接受来自客户端的连接
while True:
    #接受一个新连接
    sock,addr=s.accept()

    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
