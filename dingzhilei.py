# -*- coding: utf-8 -*-
#__str__方法
class student(object):
    def __init__(self,name):
        self.name =name

    def __str__(self):
        return 'name:%s' % self.name
a=student('sun')
print(a)

#__iter__方法
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化两个计数器

    def __iter__(self):
        return self #实例本身就是迭代对象，所以返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b #计算下一个值
        if self.a>1000:
            raise StopIteration()
        return self.a
for n in Fib():
    print (n)

#__getitem__,按照下标取出元素
class Fib2(object):
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib2()
print(f[3])

class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b =1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start =n.start
            stop =n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a,b=b,a+b
            return L
f =Fib3()
print(f[1:3])

class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __call__(self,param):
        return Chain('%s/:%s' % (self._path,param))
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
print(Chain().status.user.timeline.list)
print (Chain().users('michael').repos)

