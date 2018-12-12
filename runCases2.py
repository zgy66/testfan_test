#!/usr/bin/env python

import unittest
import HTMLTestRunner
from mytestcases import trybaidu
from mytestcases import tryTestfan
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(trybaidu.Baidu))
mysuite.addTest(unittest.makeSuite(tryTestfan.Testfan))

filename = 'result2.html'
fp = open(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
#执行测试套件
# runner = unittest.TextTestRunner()
runner.run(mysuite)
sleep(3)


# 只需要改这些即可，开始
smtpserver = 'smtp.qq.com'
username = '489292988@qq.com'
password = 'nmbdzcpvzrakbgid'     # 设置客户端授权码 的 密码
sender = '489292988@qq.com'
# 收件人为多个收件人
receiver = ['489292988@qq.com']
subject = 'Python email test'
mailbody = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.testfan.cn"
attachfile = filename
# 只需要改这些即可，结束


msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = 'zgy_answer@163.com <zgy_answer@163.com>'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)


# 构造文字内容

text_plain = MIMEText(mailbody, 'plain', 'utf-8')
msg.attach(text_plain)


# 构造附件
sendfile = open(attachfile, 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# 附件可以重命名成aaa.txt，最好用原来文件名
# text_att["Content-Disposition"] = 'attachment; filename="smail.py"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename=attachfile)
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()