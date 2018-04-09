#!/usr/bin/python
# -*- coding: utf-8 -*-
class SchoolMember:
    '''定义学校'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initializes SchoolMember:{0}'.format(self.name))
    def tell(self):
        '''告诉我细节'''
        print('Name:{0},Age:{1}'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        '''定义老师'''
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('Initialized Teacher:{0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary:"{0:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('(Initialized Student:{0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks:"{0:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividya',30,30000)
s = Student('Swaroop',25,75)
print()
members = [t,s]
for member in members:
    member.tell()