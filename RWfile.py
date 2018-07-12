# -*- coding: utf-8 -*-
#read 后必须用close,'r'表示读取
try:
    f=open('F:\相关地址及密码.txt','r')
    print(f.read())
finally:
    if f:
        f.close()

#with语句可以自动调用close()方法
with open('F:\相关地址及密码.txt','r') as f2:
    print (f2.read())

#read()会一次性读取全部内容，保险起见，可以反复调用read(size)方法，readline()可以每次读取一行
f2=open('F:\相关地址及密码.txt','r')
for line in f2.readlines(5):
    print(line.strip(' '))#去除首尾字符
f2.close()

#二进制文件如图片视频 用'rb'打开
p=open('F:\桌面.jpg','rb')
print (p.read())
p.close()

#读取非UTF-8编码的文本文件，需要给open（）函数传入encoding参数，如有非法字符，还可传入errors参数
#例：f=open('F:\gbk.txt','r',encoding='gbk',errors='ignore')

#写文件时，传入参数‘w’或者‘wb’表示写文本文件或写二进制文件
f3=open('F:\test.txt','w')
f3.write('hello')
print (f3.write())
f3.close()


