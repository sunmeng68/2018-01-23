# -*- coding: utf-8 -*-


class Student(object):
      def __init__(self,name,score):
          self.name=name
          self.score=score
      def print_score(self):
          return self.score
      def get_grade(self):
          if self.score >= 90:
              return 'A'
          elif self.score >= 60:
              return 'B'
          else:
              return 'C'

bart=Student('simon',99)
print(bart.name,bart.print_score())
lisa2 = Student('Lisa', 99)
print(lisa2.name, lisa2.get_grade())
print(bart.name, bart.get_grade())

class Student2(object):
    def __init__(self,name,grade):
        self.__name = name
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def set_grade(self,grade):
        if 0 <= grade <= 10:
            self.__grade=grade
        else:
            raise ValueError('bad gender')
bty = Student2('Bart', 5)
if bty.get_grade() != 5:
    print('测试失败!')
else:
    bty.set_grade(9)
    if bty.get_grade() != 9:
        print('测试失败!')
    else:
        print('测试成功!')


