# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name,addr =parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))



#地址和口令 qyaehndwpjqfbcbj
#from_addr =input('From:')
from_addr='1019378099@qq.com'
#password = input('Password:')
password='qyaehndwpjqfbcbj'
#收件人地址
#to_addr=input('To:')
to_addr='sunmeng@tanchengiot.com'
#SMTP服务器地址
#smtp_server = input('Smtp server:')
smtp_server='smtp.qq.com'

#第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
#msg = MIMEText('hello,send by python ','plain','utf-8')
#如果发送HTML邮件，在构造MIMEText时，把HTML字符串，再把第二个参数由plain变为html
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候。。。','utf-8').encode()

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
#打印交互信息
server.set_debuglevel(1)
#登陆SMTP服务器
server.login(from_addr, password)
#发邮件
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

