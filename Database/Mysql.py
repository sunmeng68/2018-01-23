# -*- coding: utf-8 -*-
import mysql.connector

conn=mysql.connector.connect(host='tchztest.mysql.rds.aliyuncs.com',port=3316,user='tchztest',password='admin111!@#',database='tanchengwulian')
cursor=conn.cursor()
cursor.execute('select * from customerinfo where customer_id=%s',('107',))
values=cursor.fetchall()
print (values)
cursor.close()
conn.close()