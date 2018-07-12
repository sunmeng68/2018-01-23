# -*- coding: utf-8 -*-
import psutil

#获取CPU数量
print(psutil.cpu_count())
#获取CPU物理核心
print (psutil.cpu_count(logical=False))
#统计CPU的用户，系统，空闲时间
print (psutil.cpu_times())
#CPU使用率，每秒刷新一次，累计十次
#for x in range(10):
#    print (psutil.cpu_percent(interval=1,percpu=True))

#物理内存
print (psutil.virtual_memory().percent)
#交换内存
print (psutil.swap_memory())

#获取磁盘信息
print (psutil.disk_partitions())
#磁盘使用情况
print (psutil.disk_usage('F:/'))

#网络接口信息
print (psutil.net_if_stats())
#网络连接信息
print (psutil.net_connections())

#所有进程
print (psutil.pids())
p=psutil.Process(5056)
print (p.name())