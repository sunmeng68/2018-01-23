# -*- coding: utf-8 -*-

import math
from collections import Iterable
from functools import reduce

a1=abs(-12)
a2=max(1,2,3,4)
print(a1,a2)

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

def move(x,y,step,angel=0):
    nx=x+step * math.cos(angel)
    ny=y-step * math.sin(angel)
    return nx,ny

#def trim(s):
#    i=0
#    for i in range(len(s)):
#        if s[i] is ' ':
#            return i
#        else:
#            return s
def trim(s):
    l=[]
    for i in range(len(s)):
        if s[i]!=' ':
            l.append(i)#获得第一个不为空的顺序
#            return l
    if l==[]:
        return ''
    else:
        return s[l[0]:(l[-1]+1)]#切片起始位置为l[0]，终止位置为l[-1]+1

a='  hello HE   '
print(trim(a))
#迭代
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)

#判断对象是否是可迭代对象，通过collections模块的Iterable类型
print(isinstance('abc',Iterable))

for x,y in [(1,2),(2,3),(3,4)]:
    print(x,y)
#迭代 取数组中极值
def findMinAndMax(L):
    if L!=[]:
        max=L[0]
        min=L[0]
        for x in L:
            if x>=max:
                max=x
            if x<=min:
                min=x
        return(min,max)
    else:
        return(None,None)
print(findMinAndMax([7,1,3,5,6]))

#列表生成式
L1=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L1 if isinstance(s,str)==True]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


#生成器 generator,遇到yield就退出，通常使用for循环返回对象，
def yanghui(l):
    n=0
    s=[1]
    while n<l:
        yield s
        news =[1]
        for i in range(1,len(s)):
            news.append(s[i-1]+s[i])
        news.append(1)
        s=news[:]
        n=n+1
a=yanghui(5)
for i in a:
    print(i)

#用map返回首写字母为大写，其余小写
def normalize(name):
    return name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#一个list并利用reduce()求积
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


