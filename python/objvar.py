#!/usr/bin/python
# -*- coding: utf-8 -*-
class Robot:
    '''Represents a robot, with a name'''
    population = 0

    def __init__(self,name):
        '''Initializes the data'''
        self.name=name
        print('Initializes {0}'.format(self.name))
        Robot.population += 1

    def __del__(self):
        '''I am dying'''
        print('{0} is desdroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the lst one'.format(self.name))
        else:
            print('There are still {0:d} robots working'.format(Robot.population))
    def sayHi(self):
        '''Greeting by the robots.'''
        print('Greetings, my master calls me {0}'.format(self.name))
    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    howMany=staticmethod(howMany)
droid1=Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3P0')
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")
print("Robots have finished their works.So let`s gestroyed them.")

del droid1
del droid2
Robot.howMany()

