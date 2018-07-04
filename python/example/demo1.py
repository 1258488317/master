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




