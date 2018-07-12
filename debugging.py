# -*- coding: utf-8 -*-
import logging#logging模块可以记录错误信息,打印完错误信息后会继续执行，并正常退出
from functools import reduce

try:
    print ('try..')
    r=10/int('a')
    print ('result:',r)
except ZeroDivisionError as e:
    print ('except:',e)
except ValueError as e:
    print ('ValueError:',e)
finally:
    print ('finally..')
print ('END')


def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('2')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')
main()
#抛出错误,可以抛出我们自己定义的错误
class FooError(ValueError):
    pass
def foo2(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s'%s)
    return 10/n
#捕获了错误后也可以通过raise给抛出去
def bar2():
    try:
        foo2('0')
    except ValueError as e:
        print ('Error:',e)
#       raise
bar2()

#测试
def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except ValueError as e:
        print('ValueError:',e)
main()

def str2num(s):
    try:
        return int(s)
    except:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
main()