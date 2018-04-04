#!/usr/bin/python
zoo=('python','elephant','penguin')
print('zoo is',len(zoo))
new_zoo =('monkey','camel',zoo)
print('new zoo is',len(new_zoo))
print('All new zoo is:',new_zoo)
print('old zoo is',new_zoo[2])
print('the last is',new_zoo[2][2])
print('the numbers is',len(new_zoo)-1+len(new_zoo[2]))