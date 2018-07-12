# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
#collections
from collections import namedtuple,deque

now=datetime.now()
print (now)

dt=datetime(2018,6,8,12,59,59)
print (dt)
print (dt.timestamp())

#str转化为datetime使用datetime.strptime()
today=datetime.strptime('2018-06-28 14:08:00','%Y-%m-%d %H:%M:%S')
print (today)

#datetime 转str strftime()
now =datetime.now()
print (now.strftime('%a,%b %d %H:%M'))

#对时间加减 导入timedelta 类
n=datetime.now()
n=n+timedelta(hours=10)
print(n)


#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
point=namedtuple('point',['x','y'])
p=point(1,2)
print (p.x)

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print (q)