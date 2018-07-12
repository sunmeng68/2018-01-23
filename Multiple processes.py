# -*- coding: utf-8 -*-
from multiprocessing import  Process
from multiprocessing import Pool
from multiprocessing import Queue
import os,time,random,subprocess
#print('Process (%s) start...' % os.getpid())
#子进程执行代码
def run_proc(name):
    print('Run child process %s (%s)...' %(name,os.getpid()))
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Process(target =run_proc,args=('test',))
    print ('Child process will start')
    p.start()
    p.join()
    print ('Child process end')

def long_time_task(name):
    print ('Run task %s (%s)' %(name,os.getpid()))
    start =time.time()
    time.sleep(random.random()*3)
    end =time.time()
    print ('Task %s runs %0.2f seconds'% (name,(end-start)))
#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
if __name__=='__main__':
    print ('Parent process %s' %os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print ('Waiting for all subprocesses done')
    p.close()
    p.join()
    print ('All subprocesses dong')

#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
#在代码中运行命令 nslookup www.4008812356.com
if __name__=='__main__':
    print('$ nslookup www.4008812356.com')
    r=subprocess.call(['nslookup','www.4008812356.com'])
    print ('Exit code:',r)

#进程之间的通信
#multiprocessing模块提供了Queue、Pipes等方式交换数据
def write(q):
    print ('Process to write:%s' %os.getpid())
    for value in['A','B','C']:
        print ('Put %s to queue'%value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print ('Process to read:%s'%os.getpid())
    while True:
        value=q.get(True)
        print ('Get %s from queue'%value)
if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
