# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font
import tkinter.ttk
import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import re
import folium

import smtplib
import mimetypes
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

connect = None
Detail_url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceDetail'
List_url = "http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList"
Key = 'qmAs0ut6m%2BwM%2FJwamfdK8RkKJz5yNmI4VrT6DEUuwmm%2FW7GMClJBCltEmgQEeSo7v1poVh0ZYPSbihUbMftNUQ%3D%3D'
#Key = 'cYtnsiDywOollKA9No97lS%2B7V3H1tl2gq5F%2BJyzAxQ70dhlac0M8D84OwUrJkVVy5wC7NwpkGa05zzXUIl3BWA%3D%3D'

from xml.etree import ElementTree

# 서비스키, 공공데이터포털링크, 시도, 군구 합쳐서 URL생성해주는 함수
def userURLBuilder(url, **user):
    str = url + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    print(str)
    return str


# 종로구만 검색하기위해 사용된 곳
sido = "서울특별시"
gugun = "종로구"
url = userURLBuilder(List_url, ServiceKey=Key, SIDO=sido, GUNGU=gugun)

req = requests.get(url)
tree = ElementTree.fromstring(req.text)
itemElements = tree.getiterator("item")
DATALIST = []

for item in itemElements:
    DATA = {}
    tag = item.find("ASctnNm")
    name = item.find("BResNm")
    DATA['tag'] = tag.text
    DATA['name'] = name.text
    DATALIST.append(DATA)
# 여기까지


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('murder49@gmail.com', 'murderas')





class TKWindow:
    def __init__(self):
        window = Tk()
        window.title("관광자원프로그램")
        window.geometry("800x670")
        TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
        Label(window, text="관광자원 프로그램", font=TempFont).place(x=20, y=0)

        # 시도검색 콤보박스
        self.sido = ['서울특별시', '인천광역시', '부산광역시']
        self.str = StringVar()
        self.SIDO = tkinter.ttk.Combobox(window, font=TempFont, width=10, height=15, values=self.sido,
                                         textvariable=self.str)
        self.SIDO.place(x=20, y=50)
        self.SIDO.set("시도검색")

        # 군구검색 앤트리박스
        TempFont_Search = font.Font(window, size=10, weight='bold', family='Consolas')
        self.GUNGU = Entry(window, width=25, font=TempFont_Search, borderwidth=12, relief='ridge')
        self.GUNGU.place(x=20, y=100)

        # 검색 버튼
        TempFont_Button = font.Font(window, size=13, weight='bold', family='Consolas')
        # 검색의 편리함을 위해 원래 것은 주석처리했다
        # self.searchButton = Button(window, text="리스트검색", command=self.Search, font=TempFont_Button)
        self.searchButton = Button(window, text="리스트검색", command=self. SearchList_Only_Seoul, font=TempFont_Button)
        self.searchButton.place(x=260, y=100)

        # 관광자원 검색 앤트리박스
        self.SOURCE = Entry(window, width=25, font=TempFont_Search, borderwidth=12, relief='ridge')
        self.SOURCE.place(x=20, y=160)

        # 검색 버튼
        # 검색의 편리함을 위해 원래 것은 주석처리했다
        # self.Resource_searchButton = Button(window, text="자원검색", command=self.Source_Search, font=TempFont_Button)
        self.Resource_searchButton = Button(window, text="자원검색", command=self.Source_Search_Only_Seoul, font=TempFont_Button)
        self.Resource_searchButton.place(x=280, y=160)

        # 관광지 리스트 박스
        self.TEXTLIST = Listbox(window, width=45, height=23, borderwidth=12, relief='ridge')
        self.TEXTLIST.place(x=20, y=220)
        # 검색의 편리함을 위해 원래 것은 주석처리했다
        # self.TEXTLIST.bind('<<ListboxSelect>>', self.SelectBuild)
        self.TEXTLIST.bind('<<ListboxSelect>>', self.SelectBuild_Only_Seoul)

        # # 페이지 넘기기 버튼 과연 필요할까?
        # TempFont_direction = font.Font(window, size=12, weight='bold', family='Consolas')
        # PageButton1 = Button(window, font= TempFont_direction, text="◀", command=Going_Prev_Page)
        # PageButton1.place(x=50, y=710)
        #
        # PageButton2 = Button(window, font= TempFont_direction, text="▶", command=Going_Next_Page)
        # PageButton2.place(x=350, y=710)

        # 관광지 설명 텍스트 박스
        self.EXPLAIN = Text(window, width=42, height=40, borderwidth=12, relief='ridge')
        self.EXPLAIN.place(x=420, y=20)

        # 메일 주소 입력 entry
        self.Mailentry = Entry(window, width=28, borderwidth=10, relief='ridge')
        self.Mailentry.place(x=420,y=570)

        # 정보 Gmail 보내는 버튼
        TempFont_Mail = font.Font(window, size=11, weight='bold', family='Consolas')
        self.Mail = Button(window, text="이메일보내기", command=self.Send_Mail, font=TempFont_Mail)
        self.Mail.place(x=640, y=570)

        window.mainloop()

    # 시도, 군구 받아 파싱하는 함수
    def Search(self):
        self.Sido = self.SIDO.get()
        self.Sigun = self.GUNGU.get()
        self.url = userURLBuilder(List_url, ServiceKey=Key, SIDO=self.Sido, GUNGU=self.Sigun)
        print(self.url)
        self.SearchList()

    # 파싱한 함수를 기반으로 리스트 출력하는 함수
    def SearchList(self):
        self.DATALIST = []
        if len(self.DATALIST) > 0:
            self.TEXTLIST.delete(1.0, END)
            self.TEXTLIST.update()

        req = requests.get(self.url)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")

        for item in itemElements:
            self.DATA = {}
            tag = item.find("ASctnNm")
            name = item.find("BResNm")
            self.DATA['tag'] = tag.text
            self.DATA['name'] = name.text
            self.DATALIST.append(self.DATA)

        for i in range(len(self.DATALIST)):
            str_name = "<" + str(i + 1) + "번> 시설이름 : " + self.DATALIST[i]['name']
            self.TEXTLIST.insert(i, str_name)

    def  SearchList_Only_Seoul(self):
        for i in range(len(DATALIST)):
            str_name = "<" + str(i + 1) + "번> 시설이름 : " + DATALIST[i]['name']
            self.TEXTLIST.insert(i, str_name)


    # 자원 직접 검색 함수 아직 미구현
    def Source_Search(self):
        self.Sido = self.SIDO.get()
        self.Sigun = self.GUNGU.get()
        self.Source = self.SOURCE.get()
        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO=self.Sido, GUNGU=self.Sigun, RES_NM=self.Source)

        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")
        self.DataList = []
        for item in itemElements:
            self.info = {}
            index = item.find("ASctnNm")
            name = item.find("BResNm")
            explain = item.find("FSimpleDesc")
            phone = item.find("KPhone")
            posit = item.find("LGpsCoordinate")
            if explain is None:
                self.info['explain'] = "설명없음"
            else:
                self.info['explain'] = explain.text
            self.info['index'] = index.text
            self.info['name'] = name.text
            self.info['phone'] = phone.text
            if posit is None:
                self.info['posit'] = "NONE"
            else:
                self.info['posit'] = posit.text
            self.DataList.append(self.info)
        print(self.DataList)
        self.EXPLAIN.delete(1.0, END)
        self.EXPLAIN.update()
        self.EXPLAIN.insert(1.0, self.DataList[0]['phone'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<전화번호> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['explain'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['name'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<이름> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['index'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<항목>")

    def Source_Search_Only_Seoul(self):
        self.Sido = self.SIDO.get()
        self.Sigun = self.GUNGU.get()
        self.Source = self.SOURCE.get()
        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO="서울특별시", GUNGU="종로구", RES_NM=self.Source)

        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")
        self.DataList = []
        for item in itemElements:
            self.info = {}
            index = item.find("ASctnNm")
            name = item.find("BResNm")
            explain = item.find("FSimpleDesc")
            phone = item.find("KPhone")
            posit = item.find("LGpsCoordinate")
            if explain is None:
                self.info['explain'] = "설명없음"
            else:
                self.info['explain'] = explain.text
            self.info['index'] = index.text
            self.info['name'] = name.text
            self.info['phone'] = phone.text
            if posit is None:
                self.info['posit'] = "NONE"
            else:
                self.info['posit'] = posit.text
            self.DataList.append(self.info)
        print(self.DataList)
        self.EXPLAIN.delete(1.0, END)
        self.EXPLAIN.update()
        self.EXPLAIN.insert(1.0, self.DataList[0]['phone'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<전화번호> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['explain'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['name'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<이름> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['index'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<항목>")

    # 이메일 보내는 함수 아직 미구현
    def Send_Mail(self):
        msg = MIMEBase('multipart', 'mixed')
        msg['Subject'] = self.info['name'] + ' 정보 메일'
        msg['From'] = 'chamin1212@naver.com'
        msg['To'] = self.Mailentry.get()
        msg.attach(MIMEText("<이름> : " + self.info['name'] + "\n<항목> : "+ self.info['index'] + "\n" + self.info['explain'] + "\n<전화번호> : " + self.info['phone']))
        if self.info['posit'] != "NONE":
            mapXY = self.info['posit'].replace('.', '')
            mapXY = mapXY.replace('˙', '')
            mapXY = mapXY.replace('˚', '.')
            maplist = mapXY.split(', ')
            self.map_osm = folium.Map(location=[maplist[0], maplist[1]], zoom_start=13)
            folium.Marker([maplist[0], maplist[1]], popup=self.info['name']).add_to(self.map_osm)
            self.map_osm.save('osm.html')
            path = 'osm.html'
            part = MIMEBase("application", "octet-stream")
            part.set_payload(open(path, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(path))
            msg.attach(part)
        s.sendmail('chamin1212@naver.com', self.Mailentry.get(), msg.as_string())
        #naver_server.close()

    # 페이지 넘기기 함수 아직 미구현
    def Going_Prev_Page(self):
        pass

    def Going_Next_Page(self):
        pass

    # 설명창 기입 함수
    def SelectBuild(self,evt):
        i = self.TEXTLIST.curselection()[0]
        NM = self.DATALIST[i]['name']
        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO=self.Sido, GUNGU=self.Sigun, RES_NM=NM)

        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")
        self.DataList = []
        for item in itemElements:
            self.info = {}
            index = item.find("ASctnNm")
            name = item.find("BResNm")
            explain = item.find("FSimpleDesc")
            phone = item.find("KPhone")
            posit = item.find("LGpsCoordinate")
            if explain is None:
                self.info['explain'] = "설명없음"
            else:
                self.info['explain'] = explain.text
            self.info['index'] = index.text
            self.info['name'] = name.text
            self.info['phone'] = phone.text
            if posit is None:
                self.info['posit'] = "NONE"
            else:
                self.info['posit'] = posit.text
            self.DataList.append(self.info)
        print(self.DataList)
        self.EXPLAIN.delete(1.0, END)
        self.EXPLAIN.update()
        self.EXPLAIN.insert(1.0, self.DataList[0]['phone'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<전화번호> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['explain'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['name'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<이름> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['index'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<항목>")

    def SelectBuild_Only_Seoul(self,evt):
        i = self.TEXTLIST.curselection()[0]
        NM = DATALIST[i]['name']
        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO=sido, GUNGU=gugun, RES_NM=NM)

        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")
        self.DataList = []
        for item in itemElements:
            self.info = {}
            index = item.find("ASctnNm")
            name = item.find("BResNm")
            explain = item.find("FSimpleDesc")
            phone = item.find("KPhone")
            posit = item.find("LGpsCoordinate")
            if explain is None:
                self.info['explain'] = "설명없음"
            else:
                self.info['explain'] = explain.text
            self.info['index'] = index.text
            self.info['name'] = name.text
            self.info['phone'] = phone.text
            if posit is None:
                self.info['posit'] = "NONE"
            else:
                self.info['posit'] = posit.text
            self.DataList.append(self.info)
        print(self.DataList)
        self.EXPLAIN.delete(1.0, END)
        self.EXPLAIN.update()
        self.EXPLAIN.insert(1.0, self.DataList[0]['phone'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<전화번호> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['explain'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['name'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<이름> ")
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, self.DataList[0]['index'])
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<항목>")



TKWindow()