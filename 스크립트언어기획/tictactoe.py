from tkinter import *
import random

class hh:
    #def again(self):
    #    for i in range(9):
    #        self.labelList[i].configure(image=self.imageList[random.randint(0, 1)])

    def select(self, num):
        tmp = 3
        if self.turn == 8:
            tmp = 2
        if self.ButtonList[num]['text'] == "off":
            self.ButtonList[num].configure(image=self.imageList[(self.turn % 2)])
            if self.turn % 2 == 0:
                self.ButtonList[num].configure(text="o")
                if num < 3:
                    if self.ButtonList[0]['text'] =="o" and self.ButtonList[1]['text'] =="o" and self.ButtonList[2]['text'] =="o":
                        tmp = 0
                    for k in range(3):
                        if self.ButtonList[k+0]['text'] == "o" and self.ButtonList[k+3]['text'] == "o" and self.ButtonList[k+6]['text'] == "o":
                            tmp = 0
                elif num >= 3 and num <6:
                    if self.ButtonList[3]['text'] =="o" and self.ButtonList[4]['text'] =="o" and self.ButtonList[5]['text'] =="o":
                        tmp = 0
                    for k in range(3):
                        if self.ButtonList[k+0]['text'] == "o" and self.ButtonList[k+3]['text'] == "o" and self.ButtonList[k+6]['text'] == "o":
                            tmp = 0
                else:
                    if self.ButtonList[6]['text'] == "o" and self.ButtonList[7]['text'] == "o" and self.ButtonList[8]['text'] == "o":
                        tmp = 0
                    for k in range(3):
                        if self.ButtonList[k + 0]['text'] == "o" and self.ButtonList[k + 3]['text'] == "o" and self.ButtonList[k + 6]['text'] == "o":
                            tmp = 0
                if num % 2 == 0:
                    if self.ButtonList[0]['text'] == "o" and self.ButtonList[4]['text'] == "o" and self.ButtonList[8]['text'] == "o":
                        tmp = 0
                    elif self.ButtonList[2]['text'] == "o" and self.ButtonList[4]['text'] == "o" and self.ButtonList[6]['text'] == "o":
                        tmp = 0
            else:
                self.ButtonList[num].configure(text="x")
                if num < 3:
                    if self.ButtonList[0]['text'] =="x" and self.ButtonList[1]['text'] =="x" and self.ButtonList[2]['text'] =="x":
                        tmp = 1
                    for k in range(3):
                        if self.ButtonList[k+0]['text'] == "x" and self.ButtonList[k+3]['text'] == "x" and self.ButtonList[k+6]['text'] == "x":
                            tmp = 1
                elif num >= 3 and num <6:
                    if self.ButtonList[3]['text'] =="x" and self.ButtonList[4]['text'] =="x" and self.ButtonList[5]['text'] =="x":
                        tmp = 1
                    for k in range(3):
                        if self.ButtonList[k+0]['text'] == "x" and self.ButtonList[k+3]['text'] == "x" and self.ButtonList[k+6]['text'] == "x":
                            tmp = 1
                else:
                    if self.ButtonList[6]['text'] == "x" and self.ButtonList[7]['text'] == "x" and self.ButtonList[8]['text'] == "x":
                        tmp = 1

                    for k in range(3):
                        if self.ButtonList[k + 0]['text'] == "x" and self.ButtonList[k + 3]['text'] == "x" and self.ButtonList[k + 6]['text'] == "x":
                            tmp = 1
                if num % 2 == 0:
                    if self.ButtonList[0]['text'] == "x" and self.ButtonList[4]['text'] == "x" and self.ButtonList[8]['text'] == "x":
                        tmp = 1
                    elif self.ButtonList[2]['text'] == "x" and self.ButtonList[4]['text'] == "x" and self.ButtonList[6]['text'] == "x":
                        tmp = 1
            self.turn += 1
        if tmp != 3:
            self.result(tmp)
    def result(self,num):
        if num == 0:
            Label(self.frame2, text="O 승리! 게임이 끝났습니다.").pack()
        elif num == 1:
            Label(self.frame2, text="X 승리! 게임이 끝났습니다.").pack()
        elif num == 2:
            Label(self.frame2, text="비김! 게임이 끝났습니다.").pack()
    def __init__(self):
        window = Tk()
        window.title("틱택토")
        self.turn = 0
        self.imageList = []
        self.ButtonList = []
        self.imageList.append(PhotoImage(file='imageo.gif'))
        self.imageList.append(PhotoImage(file='imagex.gif'))
        self.imageList.append(PhotoImage(file='empty.gif'))
        frame = Frame(window)
        frame.pack()
        for i in range(9):
            self.ButtonList.append(Button(frame, text="off", image=self.imageList[2], command=lambda tmp=i: self.select(tmp)))
            self.ButtonList[i].grid(row=i//3, column=i % 3)
        self.frame2 = Frame(window)
        self.frame2.pack()
        #Button(frame2, text="다시생성", command=self.again).pack()

        window.mainloop()

hh()