#!/usr/bin/python
#if 条件语句
number=23
guess=int(input('Enter an integer:'))
if guess == number:
    print('Congratulations ,you guess it .')
elif guess < number:
    print('No,it is a litter higher than that.')
else:
    print('No,it is litter lower than that.')
print('Done')
