#!/usr/bin/python
 -*- coding: UTF-8 -*-
import random
from tkinter import *
class Windows:
    def _init_(self,title='游戏',width=300,height=120,staFunc=bool,stoFunc=bool):
        self.w=width
        self.h=height
        self.stat=True