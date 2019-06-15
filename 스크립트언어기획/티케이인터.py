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

import telepot
import traceback
import tkinter.filedialog
from pprint import pprint

from io import StringIO
import io
from lxml.html import parse
import urllib.request
from PIL import Image, ImageTk

connect = None
Detail_url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceDetail'
List_url = "http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList"
Image_url = "https://openapi.naver.com/v1/search/image.xml"
Key = 'qmAs0ut6m%2BwM%2FJwamfdK8RkKJz5yNmI4VrT6DEUuwmm%2FW7GMClJBCltEmgQEeSo7v1poVh0ZYPSbihUbMftNUQ%3D%3D'
#Key = 'cYtnsiDywOollKA9No97lS%2B7V3H1tl2gq5F%2BJyzAxQ70dhlac0M8D84OwUrJkVVy5wC7NwpkGa05zzXUIl3BWA%3D%3D'

TOKEN = '670456876:AAGSdRbkOYrPuTlwWFJEIfd5KqLq5q_9JtY'
bot = telepot.Bot(TOKEN)
pprint( bot.getMe() )

MAX_MSG_LENGTH = 300
from datetime import date, datetime, timedelta
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
url = userURLBuilder(List_url, ServiceKey=Key, SIDO=sido[0], GUNGU=gugun)

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
        window.geometry("800x700")
        self.titleimage = PhotoImage(file="./Image/Title.png")
        TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
        Label(window, width=300, height=100, image=self.titleimage).place(x=20, y=0)

        # 시도검색 콤보박스
        self.sido = ['서울특별시', '인천광역시', '부산광역시']
        self.str = StringVar()
        self.SIDO = tkinter.ttk.Combobox(window, font=TempFont, width=10, height=15, values=self.sido,
                                         textvariable=self.str)
        self.SIDO.place(x=25, y=100)
        self.SIDO.set("시도검색")

        # 군구검색 앤트리박스
        TempFont_Search = font.Font(window, size=10, weight='bold', family='Consolas')
        self.str2 = StringVar()
        self.GUNGU = Entry(window, width=25, font=TempFont_Search, borderwidth=12, relief='ridge', textvariable=self.str2)
        self.GUNGU.place(x=20, y=160)

        # 검색 버튼
        TempFont_Button = font.Font(window, size=13, weight='bold', family='Consolas')
        # 검색의 편리함을 위해 원래 것은 주석처리했다
        # self.searchButton = Button(window, text="리스트검색", command=self.Search, font=TempFont_Button)
        self.listimage = PhotoImage(file="./Image/ListSearch.png")
        self.searchButton = Button(window, width=100, height=30,command=self. SearchList_Only_Seoul, image=self.listimage)
        self.searchButton.place(x=250, y=165)

        # 관광자원 검색 앤트리박스
        self.str3 = StringVar()
        self.SOURCE = Entry(window, width=25, font=TempFont_Search, borderwidth=12, relief='ridge', textvariable=self.str3)
        self.SOURCE.place(x=20, y=220)

        # 검색 버튼
        # 검색의 편리함을 위해 원래 것은 주석처리했다
        # self.Resource_searchButton = Button(window, text="자원검색", command=self.Source_Search, font=TempFont_Button)
        self.sourceimage = PhotoImage(file="./Image/ResourceSearch.png")
        self.Resource_searchButton = Button(window,width=100, height=30, command=self.Source_Search_Only_Seoul, image=self.sourceimage)
        self.Resource_searchButton.place(x=250, y=225)

        # 관광지 리스트 박스
        self.LIST_FONT = tkinter.font.Font(size=20)
        self.TEXTLIST = Listbox(window, width=20, height=10, borderwidth=12, relief='ridge', font=self.LIST_FONT)
        self.TEXTLIST.place(x=20, y=310)
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
        self.EXPLAIN = Text(window, width=42, height=25, borderwidth=12, relief='ridge')
        self.EXPLAIN.place(x=430, y=200)



        # 메일 주소 입력 entry
        self.Mailentry = Entry(window, width=28, borderwidth=10, relief='ridge')
        self.Mailentry.place(x=420,y=580)

        # 정보 Gmail 보내는 버튼
        TempFont_Mail = font.Font(window, size=11, weight='bold', family='Consolas')
        self.Emailimage = PhotoImage(file="./Image/EmailSend.png")
        self.Mail = Button(window, command=self.Send_Mail, width=100, height=30, image=self.Emailimage)
        self.Mail.place(x=640, y=580)

        # 위치 HTML 출력하는 버튼
        self.positimage = PhotoImage(file="./Image/Posit.png")
        self.Position = Button(window, width=100, height=30, command=self.MapOpen, image=self.positimage)
        self.Position.place(x=420, y=620)

        # 이미지 삽입
        # self.IMAGE = Label(window, width=40, height=20)
        # self.IMAGE.place(x=420, y=10)
        self.earth = PhotoImage(file="./Image/sample.png")
        self.IMAGE = Label(window, width=250, height=150, image=self.earth)
        self.IMAGE.place(x=460, y=20)

        #if self.info['posit'] != "NONE":

        self.map_image = self.GetMapImage(40.702147,-74.015794)
        self.MAP = Label(window, image = self.map_image, width=300, height=300)
        self.MAP.place(x=400, y=20)
        bot.message_loop(self.handle)
        window.mainloop()


    # 지도 html 파일 오픈하는 함수
    def MapOpen(self):
        if self.info['posit'] != "NONE":
            maplist = self.info['posit'].split(',')
            map_D_x = maplist[0].find('˚')
            map_D_y = maplist[1].find('˚')
            map_Min_x = maplist[0].find('˙')
            map_Min_y = maplist[1].find('˙')

            maplist[0] = eval(maplist[0][0:map_D_x])+(eval(maplist[0][(map_D_x+1):map_Min_x])/60)+(eval(maplist[0][(map_Min_x+1):])/3600)
            maplist[1] = eval(maplist[1][0:map_D_y])+(eval(maplist[1][(map_D_y+1):map_Min_y])/60)+(eval(maplist[1][(map_Min_y+1):])/3600)
            self.map_osm = folium.Map(location=[maplist[0], maplist[1]], zoom_start=13)
            folium.Marker([maplist[0], maplist[1]], popup=self.info['name']).add_to(self.map_osm)
            self.map_osm.save('osm.html')
            os.system("osm.html")

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
            str_name = "<" + str(i + 1) + "번>:" + DATALIST[i]['name']
            self.TEXTLIST.insert(i, str_name)

    def imageSearch(self):
        client_id = "to5NEwmlVW_cMpODwsVg"
        client_secret = "wTazqOx8Ui"
        self.Query =  self.SOURCE.get()
        self.display = 1
        self.sort = "sim"
        self.filter = "medium"
        self.url_img = userURLBuilder(Image_url, query=self.Query, display=str(self.display), sort=self.sort, filter=self.filter)
        img_request = requests.get(self.url_img)
        img_tree = ElementTree.fromstring(img_request.text)
        imageElements = img_tree.getiterator("item")
        for item in imageElements:
            img_link = item.find("link")
            print(img_link)
            self.the_image = img_link
        #print(self.the_image)
        self.EXPLAIN.insert(1.0, self.the_image)
        self.EXPLAIN.insert(1.0, "\n\n")
        self.EXPLAIN.insert(1.0, "<사진>")

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
            if phone is None:
                self.info['phone'] = "전화번호 없음"
            else:
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
        #리스트 URL 추가
        self.Explain_url = userURLBuilder(List_url, ServiceKey=Key, SIDO=self.Sido, GUNGU=self.Sigun,
                                          RES_NM=self.Source)

        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")
        self.DataList = []
        is_ex = False # NONE타입 체크변수
        for item in itemElements:
            self.info = {}
            index = item.find("ASctnNm")
            name = item.find("BResNm")
            explain = item.find("FSimpleDesc")
            phone = item.find("KPhone")
            posit = item.find("LGpsCoordinate")
            if explain is None:
                is_ex = True
            else:
                self.info['explain'] = explain.text
            self.info['index'] = index.text
            self.info['name'] = name.text
            self.info['phone'] = phone.text
            if posit is None:
                self.info['posit'] = "NONE"
            else:
                self.info['posit'] = posit.text
        #none타입인 경우 list에서 설명정보 가져옴
        if is_ex == True:
            ex_req = requests.get(self.Explain_url)
            ex_tree = ElementTree.fromstring(ex_req.text)
            ex_itemElements = ex_tree.getiterator("item")
            for item in ex_itemElements:
                explain = item.find("EPreSimpleDesc")
                if explain is None:
                    self.info['explain'] = "설명없음"
                else:
                    self.info['explain'] = explain.text
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
        self.imageSearch()

    # 리스트를 읽어오는 함수
    def getListData(self, SIDO_param, GUNGU_param):
        res_list = []
        #SIDO_ind = DATALIST.index(SIDO_param)
        #GUNGU_ind =DATALIST[SIDO_ind].index(GUNGU_param)

        for i in range(len(DATALIST)):
            str_name = "<" + str(i + 1) + "번>:" + DATALIST[i]['name']
            res_list.append(str_name)
        return res_list

    def getDetailData(self, SIDO_param, GUNGU_param, NAME_param):

        res_detail=[]

        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO=SIDO_param, GUNGU=GUNGU_param, RES_NM=NAME_param)
        self.Explain_url = userURLBuilder(List_url, ServiceKey=Key, SIDO=SIDO_param, GUNGU=GUNGU_param, RES_NM=NAME_param)
        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")

        DataList = []
        Detail_inf = {}
        is_ex = False
        for item in itemElements:
            index = item.find("ASctnNm")
            name = item.find("BResNm")
            phone = item.find("KPhone")
            posit = item.find("LGpsCoordinate")
            explain = item.find("FSimpleDesc")
            if explain is None:
                is_ex = True
                print("\nNONE타입입니다.\n")
            else:
                Detail_inf['explain'] = explain.text
            Detail_inf['index'] = index.text
            Detail_inf['name'] = name.text
            Detail_inf['phone'] = phone.text
            if posit is None:
                Detail_inf['posit'] = "NONE"
            else:
                Detail_inf['posit'] = posit.text
        if is_ex == True:
            ex_req = requests.get(self.Explain_url)
            ex_tree = ElementTree.fromstring(ex_req.text)
            ex_itemElements = ex_tree.getiterator("item")
            for item in ex_itemElements:
                explain = item.find("EPreSimpleDesc")
                if explain is None:
                    self.info['explain'] = "설명없음"
                else:
                    self.info['explain'] = explain.text
        DataList.append(Detail_inf)
        print(DataList)
        res_detail.append('<항목>\n\n'+ DataList[0]['index']+'\n\n')
        res_detail.append('<이름>\n\n' + DataList[0]['name'] + '\n\n')
        res_detail.append(DataList[0]['explain'] + '\n\n')
        res_detail.append('<전화번호>' + DataList[0]['phone'])
        return res_detail

    def replyTourList(self, SIDO_param, user, GUNGU_param):
        print(user, SIDO_param, GUNGU_param)
        res_list = self.getListData(SIDO_param, GUNGU_param)
        msg = ''
        for r in res_list:
            print(str(datetime.now()).split('.')[0], r)
            if len(r + msg) + 1 > MAX_MSG_LENGTH:
                self.sendMessage(user, msg)
                msg = r + '\n'
            else:
                msg += r + '\n'
        if msg:
            self.sendMessage(user, msg)
        else:
            self.sendMessage(user, '%s 에 해당하는 데이터가 없습니다.' % GUNGU_param)

    def replyTourDetail(self, SIDO_param, user, GUNGU_param, NAME_param):
        print(user, SIDO_param, GUNGU_param, NAME_param)
        res_Detail = self.getDetailData(SIDO_param, GUNGU_param, NAME_param)
        msg = ''
        print(str(datetime.now()).split('.')[0])
        for r in res_Detail:
            msg += r
        if msg:
            self.sendMessage(user, msg)
        else:
            self.sendMessage(user, '%s 에 해당하는 데이터가 없습니다.' % NAME_param)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return

        text = msg['text']
        args = text.split(' ')

        if text.startswith('상세') and len(args) > 1:
            print('try to 상세', args[1], args[2], args[3])
            self.replyTourDetail(args[1], chat_id, args[2], args[3])
        elif text.startswith('리스트') and len(args) > 1:
            print('try to 리스트', args[1], args[2])
            self.replyTourList(args[1], chat_id, args[2])
        else:
            self.sendMessage(chat_id, '모르는 명령어입니다.\n지역 [지역번호], 저장 [지역번호], 확인 중 하나의 명령을 입력하세요.')

    def sendMessage(self, user, msg):
        try:
            bot.sendMessage(user, msg)
        except:
            traceback.print_exc(file=sys.stdout)



    # 이메일 보내는 함수 아직 미구현
    def Send_Mail(self):
        msg = MIMEBase('multipart', 'mixed')
        msg['Subject'] = self.info['name'] + ' 정보 메일'
        msg['From'] = 'chamin1212@naver.com'
        msg['To'] = self.Mailentry.get()
        msg.attach(MIMEText("<이름> : " + self.info['name'] + "\n<항목> : "+ self.info['index'] + "\n" + self.info['explain'] + "\n<전화번호> : " + self.info['phone']))
        if self.info['posit'] != "NONE":
            maplist = self.info['posit'].split(',')
            map_D_x = maplist[0].find('˚')
            map_D_y = maplist[1].find('˚')
            map_Min_x = maplist[0].find('˙')
            map_Min_y = maplist[1].find('˙')

            maplist[0] = eval(maplist[0][0:map_D_x])+(eval(maplist[0][(map_D_x+1):map_Min_x])/60)+(eval(maplist[0][(map_Min_x+1):])/3600)
            maplist[1] = eval(maplist[1][0:map_D_y])+(eval(maplist[1][(map_D_y+1):map_Min_y])/60)+(eval(maplist[1][(map_Min_y+1):])/3600)
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

    #리스트 선택함수
    def SelectBuild_Only_Seoul(self,evt):
        i = self.TEXTLIST.curselection()[0]
        NM = DATALIST[i]['name']
        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO=sido, GUNGU=gugun, RES_NM=NM)
        self.Explain_url = userURLBuilder(List_url, ServiceKey=Key, SIDO=sido, GUNGU=gugun,
                                          RES_NM=NM)
        print(self.Explain_url)
        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")
        self.DataList = []
        is_ex=False
        for item in itemElements:
            self.info = {}
            index = item.find("ASctnNm")
            name = item.find("BResNm")
            explain = item.find("FSimpleDesc")
            phone = item.find("KPhone")
            posit = item.find("LGpsCoordinate")
            if explain is None:
                is_ex = True
                print("\nNONE타입입니다.\n")
            else:
                self.info['explain'] = explain.text
            self.info['index'] = index.text
            self.info['name'] = name.text
            if phone is None:
                self.info['phone'] = "전화번호 없음"
            else:
                self.info['phone'] = phone.text
            if posit is None:
                self.info['posit'] = "위치정보 없음"
            else:
                self.info['posit'] = posit.text
        if is_ex == True:
            ex_req = requests.get(self.Explain_url)
            ex_tree = ElementTree.fromstring(ex_req.text)
            ex_itemElements = ex_tree.getiterator("item")
            for item in ex_itemElements:
                explain = item.find("EPreSimpleDesc")
                if explain is None:
                    self.info['explain'] = "설명 없음"
                else:
                    self.info['explain'] = explain.text
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
        self.Search_Image(NM)

    def Search_Image(self, NM):
        keyword = NM
        url = 'https://www.google.co.kr/search?q=' + keyword + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'
        text = requests.get(url).text
        text_source = StringIO(text)
        parsed = parse(text_source)

        doc = parsed.getroot()
        imgs = doc.findall('.//img')
        img = imgs[3].get('src')
        urllib.request.urlretrieve(img, "./Image/Build.png")
        self.original = Image.open("./Image/Build.png")
        resized = self.original.resize((250, 150), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)

        self.IMAGE.config(image=self.image)


    def GetMapImage(self,latitude,longitude):
        BaseURL = 'https://maps.googleapis.com/maps/api/staticmap?center=LATITUDE,LONGITUDE&zoom=13&size=300x300&maptype=roadmap&markers=color:blue%7Clabel:S%LATITUDE,LONGITUDE&key='
        Key = 'AIzaSyCIwXZ_47Dyl_KmrInmMc_jAjCTsDV3goA'
        BaseURL = BaseURL.replace('LATITUDE',str(latitude))
        BaseURL = BaseURL.replace('LONGITUDE', str(longitude))
        url = BaseURL + Key

        print(url)

        u = urllib.request.urlopen(url)
        raw_data = u.read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        u.close()
        return image




TKWindow()