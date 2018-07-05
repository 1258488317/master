#!/usr/bin/python
#first
# url = input('Please enter the URL:')
# domain = url[11:-4]
# print("domain name:" + domain)



#second
# sentence = input('Sentence:')
#
# screen_width = 80
# text_width = len(sentence)
# box_width = text_width + 6
# left_margin = (screen_width - box_width)//2
#
# print()
# print(''*left_margin + '+' + '-'*(box_width-2) + '+')
# print(''*left_margin + '|' + ' '*text_width     + '|' )
# print(''*left_margin + '|' +    sentence       +'|')
# print(''*left_margin + '|' + ' '*text_width     + '|')
# print(''*left_margin + '+' + '-'*(box_width-2) + '+')
# print()

#third
# name = input('What`s your name?')
# if name.endswith('Gumby'):
#     if name.startswith('Mr.'):
#         print('Hello,Mr.Gumby')
#     elif name.startswith('Mrs.'):
#         print('Hello.Mrs.Gumby')
#     else:
#         print('Hello,Gumby')
# else:
#     print('Hello,stranger')



#four
# def story(**kwds):
#     return 'Once upon a time ,there was a {job} called {name}.'.format_map(kwds)
#
# def power(x,y,*others):
#     if others:
#         print('received redndant parameters:',others)
#     return pow(x,y)
#
# def interval(start,stop=None,step=1):
#     'Imitates rang() for step >0'
#     if stop is None:
#         start,stop = 0,start
#     result = []
#
#     i = start
#     while i <stop:
#         result.append(i)
#         i += step
#     return  result
# print(story(job='king',name='Gumby'))
# params = {'job':'language','name':'python'}
# print(story(**params))
# a=power(2,3)
# print(a)
# b = power(3,3,'hello , world')
# print(b)


#five
# from math import sqrt
# for n in range (99,81,-1):
#     root =sqrt(n)
#     if root == int(root):
#         print(n)
#         break
# else:
#     print('didn`t find it!')

#six
# def fibs(num):
#     result = [0,1]
#     for i in range(num -2):
#         result.append(result[-2]+result[-1])
#     return result
#
#
# print(fibs(20))


#seven


def init(data):#初始化数据
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storage = {}
init(storage)
print(storage)

#获取人员姓名
def lookup(data,label,name):
    return data[label].get(name)


#将人员存储到数据结构
def store(data,full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1,' ')
    labels = 'first','middle','last'

    for label ,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames,'Magnus Lie Hetland')
print('打印中间名称：',lookup(MyNames,'middle','Lie'))

store(MyNames,'Robin Hood')
store(MyNames,'Robin Lockslev')
print('打印姓：',lookup(MyNames,'first','Robin'))

store(MyNames,'bi qi')
store(MyNames,'fu qi qi')
print(lookup(MyNames,'last','qi'))

