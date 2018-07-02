#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time

source=['"D:\\text"','D:\\Code']
target_dir='D:\\backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.rar'