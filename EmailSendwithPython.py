# 1. 이메일 보내기 no.1

import smtplib
import getpass
import csv
# simple mail transfer protocol
# 이메일을 보내기 위한 규약

from email.message import EmailMessage
password = getpass.getpass('비번 입력:')

with open('user.csv','r')as f:
    reader = csv.reader(f)

# 이메일 내용작성
    for user in reader:
        msg = EmailMessage()
        msg['subject'] = '제목 테스트'
        msg['From'] = 'steveshin63@naver.com'
        msg['To'] = 'steveshin63@naver.com'
        if user[2]=='합':
            msg.set_content('합격')
        else:
            msg.set_content('다음 기회에')

# 네이버 서버 설정
        server = smtplib.SMTP_SSL('smtp.naver.com', 465)
        server.login('steveshin63', password)

        server.send_message(msg)
        print('이메일 전송했습니다.')

# 2. 이메일 보내기 no.2

import smtplib
import getpass
import csv
from email.message import EmailMessage
from email.mime.application import MIMEApplication

with open('image.jpg','rb')as f:
    image = f.read()
    
password = getpass.getpass('비번 입력: ')
    
msg = EmailMessage()
msg['From'] = 'steveshin63@naver.com'
msg['To'] = 'steveshin63@naver.com'
msg['Subject'] = '이메일 html'
msg.add_alternative('''
<h1>안녕하세요.</h1>
<h2>반갑습니다</h2>'
<img src="cid:image.jpg">
''',subtype='html')

# 이메일 전송 표준에 맞춰서 image 변환
attach_img = MIMEApplication(image, name='image.jpg')
attach_img.add_header('Content-ID','image.jpg')

# 첨부파일에 추가
msg.attach(attach_img)
server = smtplib.SMTP_SSL('smtp.naver.com', 465)
server.login('steveshin63', password)
server.send_message(msg)
