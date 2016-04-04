

import smtplib

from email.header import Header 
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

content = '''
We are sorry for your computer is being affected by our testing programe.
You have reinstall your computer to restore the normal email system, 
otherwise this test email will send by 'yourself' forever.
Sorry for that.

Please reinstall your OS right now and unplugin your Internet connectiong.
GB Teams
'''

msg = MIMEText(content, 'plain', 'utf-8')
msg['Subject'] = Header("Testing Program Email",'utf-8').encode()

fromMail = 'gbteams@outlook.com'
toMail = '82154915@qq.com'

server = smtplib.SMTP()
server.connect('smtp-mail.outlook.com',587)
server.starttls()
server.login('gbteams@outlook.com', 'Tyler_XCCFO')
print "Login Success"

# server.sendmail(fromMail, toMail, msg.as_string())
server.sendmail(fromMail, toMail, content)
server.quit()