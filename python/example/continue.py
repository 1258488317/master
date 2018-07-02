#!/usr/bin/python
# -*- coding: UTF-8 -*-
# while True:
#     s =input('enter something:')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print('too samall')
#     else:
#         print('input is of suffivient length')
# print('done')
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
