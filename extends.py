# -*- coding: utf-8 -*-
class Student():
    def grade(self):
        print('哇要考试啦！')
class goodStudent(Student):
    def grade(self):
        print('哇满分！')
class badStudent(Student):
    def grade(self):
        print('哇零分')
class Pig():
    def grade(self):
        print('精品猪肉！')
def kind(student):
    student.grade()
student = Student()
good = goodStudent()
bad = badStudent()
pig = Pig()
kind(student)
kind(good)
kind(bad)
kind(pig)