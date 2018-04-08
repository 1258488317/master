#!/usr/bin/python
#while 循环语句
number=23
running= True
while running:
    guess=int(input('Enter an integer:'))
    if guess==number:
        print('Congratulations, you guessed it.')
        running=False
    elif guess<number:
        print('No,it is litter higher.')
    else:
        print('no,it is a litter lower.')
else:
    print('the while is over.')
print('done')
