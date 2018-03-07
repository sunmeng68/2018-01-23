# -*- coding: utf-8 -*-
from command import Myobject
computer = Myobject()

def run(x):
    inp=input('method>')
    if hasattr(computer,inp):
        func=getattr(computer,inp)
        print(func())
    else:
        setattr(computer,inp,lambda x:x+1)
        func=getattr(computer,inp)
        print(func(x))
if __name__=='__main__':
    run(10)
