# -*- coding: utf-8 -*-
from enum import Enum,unique

Month = Enum('Month',('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

@unique #装饰器帮助检查保证没有重复值
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
day1=Weekday.Mon
print (day1)
print (day1.value)
print (Weekday(1))


#Test 把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
    Male=0
    Female=1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')