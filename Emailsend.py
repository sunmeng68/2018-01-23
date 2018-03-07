# -*- coding: utf-8 -*-
import smtplib
#加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
import ConfigParser
import string, os, sys
yw = ConfigParser.ConfigParser()
try:
    yw.read("yunwei.ini")
#读取配置文件
#kvs = cf.items("email")
#获取section的所有option
#print 'email:', kvs
#获取option的值
    my_sender = yw.get("email", "my_sender")
    print(my_sender)
    my_sender_pass = yw.get("email", "my_sender_pass")
    print(my_sender_pass)
    my_user = yw.get("email", "my_user")
    print(my_user)
except Exception as e:
    print(e)
def mail(logstr):
    try:
        msg=MIMEText(logstr,'plain','utf-8')
        msg['From']=formataddr(["系统监测",my_sender])
        msg['To']=formataddr(["杜军",my_user])
        msg['Subject']="python监测通知"
        server=smtplib.SMTP("smtp.163.com",25)
        server.login(my_sender,my_sender_pass)
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.quit()
    except Exception as e:
        print(e)