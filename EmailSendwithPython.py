# 1. �̸��� ������ no.1

import smtplib
import getpass
import csv
# simple mail transfer protocol
# �̸����� ������ ���� �Ծ�

from email.message import EmailMessage
password = getpass.getpass('��� �Է�:')

with open('user.csv','r')as f:
    reader = csv.reader(f)

# �̸��� �����ۼ�
    for user in reader:
        msg = EmailMessage()
        msg['subject'] = '���� �׽�Ʈ'
        msg['From'] = 'steveshin63@naver.com'
        msg['To'] = 'steveshin63@naver.com'
        if user[2]=='��':
            msg.set_content('�հ�')
        else:
            msg.set_content('���� ��ȸ��')

# ���̹� ���� ����
        server = smtplib.SMTP_SSL('smtp.naver.com', 465)
        server.login('steveshin63', password)

        server.send_message(msg)
        print('�̸��� �����߽��ϴ�.')

# 2. �̸��� ������ no.2

import smtplib
import getpass
import csv
from email.message import EmailMessage
from email.mime.application import MIMEApplication

with open('image.jpg','rb')as f:
    image = f.read()
    
password = getpass.getpass('��� �Է�: ')
    
msg = EmailMessage()
msg['From'] = 'steveshin63@naver.com'
msg['To'] = 'steveshin63@naver.com'
msg['Subject'] = '�̸��� html'
msg.add_alternative('''
<h1>�ȳ��ϼ���.</h1>
<h2>�ݰ����ϴ�</h2>'
<img src="cid:image.jpg">
''',subtype='html')

# �̸��� ���� ǥ�ؿ� ���缭 image ��ȯ
attach_img = MIMEApplication(image, name='image.jpg')
attach_img.add_header('Content-ID','image.jpg')

# ÷�����Ͽ� �߰�
msg.attach(attach_img)
server = smtplib.SMTP_SSL('smtp.naver.com', 465)
server.login('steveshin63', password)
server.send_message(msg)
