import smtplib
from email.message import EmailMessage

email_list = ['neon858@hanmail.net', 'yud02150@gmail.com']

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "제목"
    msg['From'] = "yud02150@naver.com"
    msg['To'] = email 
    msg.set_content('!!!!!!') 
    smtp_url ='smtp.naver.com'
    smtp_port = 465
    s = smtplib.SMTP_SSL(smtp_url, smtp_port)
    s.login('yud02150', password)
    s.send_message(msg)


