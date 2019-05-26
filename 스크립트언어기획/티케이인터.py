from tkinter import *
from tkinter import font
import tkinter.ttk
import http.client
import urllib.parse
from tkinter import messagebox

import json
from xml.etree import ElementTree

import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("800x650+500+100")
DataList = []

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="관광자원 프로그램")
    MainText.pack()
    MainText.place(x=20)

def sido_click():
    #print(str.get())
    pass


def gungu_click():
    global RenderText1
    Search_TourPlace()


    RenderText1.place_forget()
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText1 = Listbox(g_Tk, width=49, height=22, borderwidth=12,
                       relief='ridge', font=TempFont)
    RenderText1.place(x=10, y=215)

    for i in range(len(DataList)):
        RenderText1.insert(i, DataList[i]["이름"])


def InitSido():
    sido = ['서울특별시', '인천광역시', '부산광역시']

    gungu = [['중구', '종로구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구'],
             ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구'],
             ['중구', '동구', '남구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군']]

    global str
    global str1
    str = StringVar()
    str1 = StringVar()

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    TempFont1 = font.Font(g_Tk, size=10, weight='bold', family='Consolas')

    ComboBox = tkinter.ttk.Combobox(g_Tk, font=TempFont, width=10, height=15, values = sido, textvariable = str)
    Click_button = Button(text="선택", command = sido_click, font=TempFont1)
    ComboBox.pack()
    ComboBox.place(x=20,y=50)
    Click_button.pack()
    Click_button.place(x=170, y =50)
    ComboBox.set("시도검색")



    ComboBox1 = tkinter.ttk.Combobox(g_Tk, font=TempFont, width=10, height=15, values=gungu[0], textvariable = str1)
    Click_button1 = Button(text="선택", command=gungu_click, font=TempFont1)
    ComboBox1.pack()
    ComboBox1.place(x=20, y=100)
    Click_button1.pack()
    Click_button1.place(x=170, y=100)
    ComboBox1.set("시군구검색")



def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=150)

def InitSearchButton():
    str_search = StringVar()
    TempFont = font.Font(g_Tk, size=14, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=155)

def Search_TourPlace():
    conn = http.client.HTTPConnection("openapi.tour.go.kr")
    URL = "/openapi/service/TourismResourceService/getTourResourceList?serviceKey=cCHEHEp%2BWRwV%2FfoF1u%2FVeQGoxigy9y%2FrGH8XHy3oN11YntHkyn3zf8fpQiLDIKWuVY6qT9MUkLU8yQ1naKv%2BFw%3D%3D&numOfRows=50&SIDO=main&GUNGU=sub&pageNo=PageNumber"
    URL = URL.replace("main", urllib.parse.quote(str.get()))#urllib.parse.quote(main))
    URL = URL.replace("sub", urllib.parse.quote(str1.get()))#urllib.parse.quote(sub))
    URL = URL.replace("PageNumber", '1')
    print(str.get())
    print(str1.get())
    print(URL)
    conn.request("GET", URL)
    req = conn.getresponse()

    tree = ElementTree.fromstring(req.read().decode("UTF-8"))
    itemElements = tree.getiterator("item")  # item 엘리먼트 리스트 추출
    for item in itemElements:
        info = dict()
        result = item.find('ASctnNm')
        if result !=None:
            info["카테고리"] = result.text
        result = item.find('BResNm')
        if result !=None:
            info["이름"] = result.text
        result = item.find('CSido')
        if result !=None:
            info["시도"] = result.text
        result = item.find('DGungu')
        if result !=None:
            info["군구"] = result.text
        result = item.find('EPreSimpleDesc')
        if result !=None:
            info["상세정보"] = result.text
        DataList.append(info)



def SearchButtonAction():
    pass


def InitSearchList():
    global RenderText1

    RenderText1 = Listbox(g_Tk, width=49, height=22, borderwidth=12,
                       relief='ridge')  # , yscrollcommand=RenderTextScrollbar.set
    RenderText1.pack()
    RenderText1.place(x=10, y=215)

    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    PageButton1 = Button(g_Tk, font=TempFont, text="◀", command=Going_Prev_Page)
    PageButton1.pack()
    PageButton1.place(x=30, y=600)

    PageButton2 = Button(g_Tk, font=TempFont, text="▶", command=Going_Next_Page)
    PageButton2.pack()
    PageButton2.place(x=330, y=600)


def Going_Prev_Page():
    pass

def Going_Next_Page():
    pass

def InitDetailExplain():

    # RenderTextScrollbar = Scrollbar(g_Tk)
    # RenderTextScrollbar.pack()
    # RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=40, borderwidth=12,
                         relief='ridge', font = TempFont)  # , yscrollcommand=RenderTextScrollbar.set)

    for i in range(len(DataList)):
        RenderText.insert(i, DataList[i]["이름"])

    RenderText.place(x=400, y=10)
    # RenderTextScrollbar.config(command=RenderText.yview)
    # RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')



    RenderText1.configure(state='disabled')


InitTopText()
InitSido()
InitInputLabel()
InitSearchButton()
InitSearchList()
InitDetailExplain()
g_Tk.mainloop()


