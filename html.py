import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "제목"
msg['From'] = "yud02150@naver.com"
msg['To'] = "yud02150@gmail.com" 
# msg.set_content('!!!!!!')
msg.add_alternative('''
<h1>안녕하세요!!!</h1>
<p>저는 박나원입니다.</p>
''',subtype="html")
smtp_url ='smtp.naver.com'
smtp_port = 465
s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('yud02150', 'cv3140cv..')
s.send_message(msg)