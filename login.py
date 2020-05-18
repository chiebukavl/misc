# -*- coding: utf-8 -*-

_userName = ''

while not _userName:
    print('Enter your username: ')
    _userName = input()
    
print('Your username is \'' + _userName + '\'')


_counter = 0
print('Enter your password: ')

# start while loop
while _counter < 3:

    _userPassword = input()

    if _userPassword != 'pbjelly':
        
        print('Invalid password.')
        _counter += 1
        
        if _counter == 3:
            print('Login unsuccessful. Please try again in 15 minutes.')
        continue
        
    else:
        print('Login successful.')
        break
# end while loop
