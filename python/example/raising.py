#!/usr/bin/python
# -*- coding: utf-8 -*-
class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text) <3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex :
    print('ShortInputException the input was {0} long,excepted atleast {1}'.format(ex.length,ex.atleast))
else:
    print('No exception was raised.')