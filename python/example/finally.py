#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end=" ")
        time.sleep(2)
except KeyboardInterrupt:
    print('!! You cancelled the reading from the line.')
finally:
    f.close()
    print('(Cleaning up: close the file.)')