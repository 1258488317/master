#!/usr/bin/python
ab={ 'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
      }
print("Swaroop's address is",ab['Swaroop'])
del ab['Spammer']
print('there are {0} contacts in the address-book'.format(len(ab)))
for name,adderss in ab.items():
    print('contacts {0} at {1}'.format(name,adderss))
ab['guido']='guido@python.org'
if 'guido' in ab:
    print("guido's address is",ab['guido'])