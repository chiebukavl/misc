# -*- coding: utf-8 -*-

_userName = ''

while not _userName:
    print('Enter your username: ')
    if _userName == False:
        print('Invalid username. Try again.')
    _userName = input()
    


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
