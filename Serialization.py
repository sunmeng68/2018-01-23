# -*- coding: utf-8 -*-
import pickle
import json

#pickle.dumps()方法把任意对象序列化成一个bytes
d=dict(name='Bob',age=20,score=86)
#print (pickle.dumps(d))
f=open('dump.txt','wb')
print(pickle.dump(d,f))
f.close()

#python对象变成json
d2=dict(name='Sun',age=22,score=80)
print(json.dumps(d2))
#json反序列化为python对象
json_str='{"age":20,"score":90,"name":"sun"}'
print (json.loads(json_str))

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
#python无法把类实例化为json，需要写一个转换函数
    def student2dict(self,std):
        return {'name':std.name,
                 'score':std.score,
                 'age':std.age}
s=Student('Yuan',22,90)
print (json.dumps(s,default=s.student2dict))

#练习：对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print (s)