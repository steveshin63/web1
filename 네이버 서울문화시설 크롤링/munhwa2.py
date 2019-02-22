import cx_Oracle
#db연동
connection = cx_Oracle.connect("java", "1234", "localhost")
cursor = connection.cursor()
cnt = 0

#-*-coding:utf-8-*-
import requests
from urllib import parse
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd

name = []

place = cursor.execute("""select contentname from munhwa2""")

place = place.fetchall()

for r in place :
    name.append(r[0])
    
for a in name:
    req = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="+a)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    
    tag = soup.find_all("ul",{"class":"type01 _content"})
 
    review = []
    image = []
    title = []
    link = []

    for i in tag:
        print(a)
        j = i.find('div',class_="review_txt")
        j = j.text
        review.append(j)
        print(review)
    
        p = i.find('a',class_="review_tit")
        p = p.text
        title.append(p)
        print(title)
        
        m = i.find('img',class_="thumb_img")
        image.append(m.get('src'))
        print(image)
        
        l = i.find('a',class_="review_tit")
        link.append(l.get('href'))
        print(link)
        
        #db 업데이트
        cursor.execute("""INSERT into data3(name, review, title, image, link) values(:name, :review, :title, :image, :link)""",name = a, review = j, title=p, image=m.get('src'), link = l.get('href'))
        #cursor.execute("""commit""")
        print(cnt)
        cnt+=1
    connection.commit();
    #connection.close()