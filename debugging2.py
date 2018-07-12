# -*- coding: utf-8 -*-
def foo(s):
    n=int(s)
    print ('>>>n= %d'%n)
    return 10/n
def main():
    foo('2')
main()

#断言assert，assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#如果断言失败，assert语句本身就会抛出AssertionError：
def foo2(s):
    n=int(s)
    assert n!=0,'n is zero'
    return 10/n
def main2():
    foo2('2')
main2()

#logging ,logging不会抛出错误，可以输出到文件
import logging
logging.basicConfig(level =logging.INFO)
s ='0'
n =int(s)
logging.info('n=%d'%n)
print (10/n)
