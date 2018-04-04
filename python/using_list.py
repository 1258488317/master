#!/usr/bin/python
#this is my shoplist
shoplist=['apple','mango','banana','carrot']
print('I have ',len(shoplist),'items to purchase')
print('These items are:',end=' ')
for item in shoplist:
    print(item,end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)
shoplist.sort()
print('sort list is:',shoplist)
olditem=shoplist[2]
del shoplist[2]
print('i bought',olditem)
print('the new shopping list is',shoplist)