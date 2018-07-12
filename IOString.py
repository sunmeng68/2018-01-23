# -*- coding: utf-8 -*-
from io import StringIO
#getvalue（)方法用于获得写入后的str
f=StringIO()
f.write('Hello')
f.write(',')
f.write('MY Baby')
print (f.getvalue())

#可以初始化一个StringIO,像读文件一样读取
f1=StringIO('Hello!\nHi!\nGoodbye')
while True:
    s=f1.read()
    if s=='':
        break
    print (s.strip())

#BytesIO
#StringIO操作的只能是str，操作二进制的数据要用BytesIO
#传入的值是经过utf-8编码的bytes
from io import BytesIO
b=BytesIO()
b.write('中文'.encode('utf-8'))
print (b.getvalue())


