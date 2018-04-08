#!/usr/bin/python
name = 'Swaroop'  #这是一个字符串
if name.startswith('Swa'):
    print('yes,the string starts with "Swa"')
if 'a' in name:
    print('yes, it contains the string "a"')
if name.find('war')!=-1:
    print('yes ,it contains the string "war"')
delimiter = '_*_'
mylist = ['brazil','russia','india','china']
print(delimiter.join(mylist))