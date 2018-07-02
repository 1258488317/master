#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from tkinter import *


class Window:
    def __init__(self, title='游戏', width=300, height=120, staFunc=bool, stoFunc=bool):
        self.w = width
        self.h = height
        self.stat = True
        self.staFunc = staFunc
        self.stoFunc = stoFunc
        self.staIco = None
        self.stoIco = None
        self.root = Tk(className=title)


def drawCenter(self):
    ws = self.root.winfo_screenwidth()  # 用户屏幕宽度
    hs = self.root.winfo_screenheight()  # 用户屏幕高度
    x = int((ws / 2) - (self.w / 2))  # 距屏幕左边框的像素点数
    y = int((hs / 2) - (self.h / 2))  # 距屏幕上边框的像素点数
    self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))


def createWidgets(self):
    Label(self.root, text="实验次数：").grid(row=0, sticky=E)
    Label(self.root, text="正面出现的次数：").grid(row=1, sticky=E)
    Label(self.root, text="出现正面频率：").grid(row=2, sticky=E)
    self.e1 = Entry(self.root)
    self.hc = StringVar()
    self.e2 = Entry(self.root, textvariable=self.hc)
    self.p = StringVar()
    self.e3 = Entry(self.root, textvariable=self.p)
    self.e1.grid(row=0, column=1)
    self.e2.grid(row=1, column=1)
    self.e3.grid(row=2, column=1)
    self.btnSer = Button(self.root, command=self.click, width=3, height=1, text='运行')
    self.btnSer.grid(row=3, column=1, sticky=E)
    btnQuit = Button(self.root, text='关闭窗口', command=self.root.quit, width=8, height=1)
    btnQuit.grid(row=3, column=2)


def click(self):
    h = 0  # 正面次数
    t = 0  # 反面次数
    allcount = 0
    count = int(self.e1.get())
    for i in range(count):
        num = random.randint(0, 1)
        if num == 0:
            h = h + 1
        else:
            t = t + 1
        allcount = allcount + 1
    print(allcount)
    self.hc.set(str(h))  # 正面次数
    self.p.set(str(h / count))  # 正面概率


    def loop(self):
        self.root.resizable(False, False)  # 禁止修改窗口大小
        self.createWidgets()
        self.drawCenter()  # 窗口居中
        self.root.mainloop()


# 你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行
if __name__ == '__main__':
    w = Window(width=350, height=150)
    w.loop()
