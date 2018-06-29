#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
guess = ''
while guess not in ('heads','tails'):
    print('Guess the coin toss!Enter heads or tails:')
    guess = input()
toss = random.randint(0,1)
if toss ==0:
    toss='tails'
else:
    toss='heads'
if toss==guess:
    print('You got it!')
else:
    print('Nope!Guess again!')
    guess= input()
    toss= random.randint(0,1)
    if toss == 0:
        toss = 'tails'
    else:
        toss = 'heads'

    if toss == guess:
        print('You got it!')
    else:
        print('Nope.You are really bad at this game.')