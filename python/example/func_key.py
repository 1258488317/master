#!/usr/bin/python
def func(a,b=5,c=10):
    print('a is',a,'b is',b,'c is',c)
func(3,9)
func(20,c=24)
func(c=30,a=199)