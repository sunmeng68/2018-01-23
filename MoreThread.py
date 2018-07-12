# -*- coding: utf-8 -*-
import time,threading


#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
#current_thread()函数永远返回当前线程的实例。子线程的名字在创建是指定，没有其他意义
def loop():
    print ('thread %s is running..'%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print ('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print ('thread %s ended'%threading.current_thread().name)

print ('thread %s is running'%threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print ('thread %s ended'%threading.current_thread().name)


#lock
balance =0
lock = threading.Lock()
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
#当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
def run_thread(n):
    for i in range(10):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #修改完释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)