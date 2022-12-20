
import urllib, urllib2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Sender address, created in the console
username = 'xxx@xxx.com'
# Sender password, created in the console
password = 'XXXXXXXX'

# Recipient address list, supports up to 30 recipients
rcptlist = ['to1@to.com', 'to2@to.com']
receivers = ','.join(rcptlist)

# Build multipart mail message
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Test Email'
msg['From'] = username
msg['To'] = receivers

# Build text/plain part of multipart/alternative
alternative = MIMEMultipart('alternative')
textplain = MIMEText ('plain text part')
alternative.attach(textplain)

# Build text/html part of multipart/alternative
textplain = MIMEText ('hyper text part')
alternative.attach(texthtml)

# Add alternative into mixed
msg.attach(alternative)

# Attachment type
# xlsx type attachment
xlsxpart = MIMEApplication(open('1.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='1.xlsx')
msg.attach(xlsxpart)

# jpg type attachment
jpgpart = MIMEApplication(open('2.jpg', 'rb').read())
jpgpart.add_header('Content-Disposition', 'attachment', filename='2.jpg')
msg.attach(jpgpart)

# mp3 type attachment
mp3part = MIMEApplication(open('3.mp3', 'rb').read())
mp3part.add_header('Content-Disposition', 'attachment', filename='3.mp3')
msg.attach(mp3part)

# Send mail
try:
    client = smtplib.SMTP()
    # SSL may be needed to create a client in python 2.7 or later
    #client = smtplib.SMTP_SSL()

    client.connect('smtpdm.aliyun.com')
    client.login(username, password)
    # Sender has to match the authorized address
    client.sendmail(username, rcptlist, msg.as_string())
    client.quit()
    Print ('Email delivered successfully!')
except smtplib.SMTPRecipientsRefused:
    Print 'Email delivery failed, invalid recipient'
except smtplib.SMTPAuthenticationError:
    Print 'Email delivery failed, authorization error'
except smtplib.SMTPSenderRefused:
    Print 'Email delivery failed, invalid sender'
except smtplib.SMTPException,e:
    Print 'Email delivery failed, ' e.message