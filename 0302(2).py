# -*- coding: utf-8 -*-
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
