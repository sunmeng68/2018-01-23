# -*- coding: utf-8 -*-
from datetime import datetime
import os

print(os.name)
#环境变量
print(os.environ)
#获取环境变量的值,调用os.environ.get('')
print (os.environ.get('PATH'))
#操作文件和目录
#查看当前目录的绝对路径
print (os.path.abspath('.'))
#在某目录下创建一个目录，首先把完整路径表示,join()函数
print (os.path.join('F:\\','Testdir'))
#然后创建一个目录
os.mkdir('F:\Testdir')
#删除一个目录
os.rmdir('F:\Testdir')

#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
#split()函数可以把路径拆分为两部分，后一部分事最后级别的目录或文件名
print (os.path.split('F:\相关地址及密码.txt'))
#splitext()可以直接获得文件扩展名
print (os.path.splitext('F:\相关地址及密码.txt'))

#例，过滤文件：列出当前目录下所有目录
print ([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有.py文件
print ([x for x in os.listdir('.') if os.path.isfile(x)and os.path.splitext(x)[1]=='.py'])

# 实现 dir -l
pwd = os.path.abspath('.')
print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

