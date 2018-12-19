import csv
import smtplib

f = open('pygj.csv', 'r', encoding='utf-8')
read_csv = csv.reader(f)

from email.message import EmailMessage

smtp_url ='smtp.naver.com'
smtp_port = 465
s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login("yud02150@naver.com",password) #traceback방지하기 위해 로그인정보 밖으로 뺌

for line in read_csv:
    msg = EmailMessage()
    msg['Subject'] = "안녕하세요 저는 박나원입니다"
    msg['From'] = 'yud02150@naver.com' #from의 정보와 email정보의 따옴표 일치
    msg['To'] = line[1]
    msg.set_content(line[0] +'에게 보냄')
    s.send_message(msg)
    
f.close() #리소스가 남아있을 수도 있으니 파일을 열고 닫아줌
