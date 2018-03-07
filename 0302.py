# -*- coding: utf-8 -*-
class Student(object):
    count=0

    def __init__(self,name):
        self.name=name
        Student.count=Student.count+1
if Student.count!=0:
    print('false')
else:
    bart=Student('Bart')
    if Student.count != 1:
        print('false')
    else:
        lisa = Student('Lisa')
        if Student.count != 2:
            print('false')
        else:
            print('Students:',Student.count,bart.name)
            print('success')
