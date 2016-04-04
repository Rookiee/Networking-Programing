import smtplib
#from  email.miee.text import MIMEText
#msg = MIMEText("this is  a test message", "plain", "utf-8")

fromMail = '82154915@qq.com'
toMail = '82154915@qq.com'

server = smtplib.SMTP()
server.connect('smtp.qq.com',587)
server.starttls()
server.login('82154915@qq.com', 'Xie.Haoyang86052')
print "login success!"

server.sendmail(fromMail, toMail, "123, this is the second")

server.quit()
