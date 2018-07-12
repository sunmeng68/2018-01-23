# -*- coding: utf-8 -*-
#最大类
class Animal(object):
    pass
#哺乳类和鸟类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
#各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
#添加动物功能
class Runnable(object):
    def run(self):
        print('Running')
class Flyable(object):
    def fly(self):
        print('Flying')
#多继承
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
#example
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass
#mro,解析方法调用的顺序
#多重继承按照拓扑排序：从DAG途中选择一个没有前驱(即入度为0)的顶点并输出
#从图中删除该顶点和所有以它为起点的有向边。
#重复1和2直到当前DAG图为空或当前途中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。
if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()