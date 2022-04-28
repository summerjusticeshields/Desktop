Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:44:01) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print('Reboot the computer and try to reconnect')
step1 = input('Did that fix the problem? ')

if step1 == 'no':
    print('Reboot the router.')
    step2 = input('Did that fix the problem? ')
elif step2 == 'no':
    print('Make sure the cables between the router and modem are plugged in firmly')
    step3 = input('Did that fix the problem? ')
elif step3 == 'no':
    print('Move the router to a new location and try to connect.')
    step4 = input('Did that fix the problem? ')
elif step4 == 'no':
    print('Get a new router')
else:
    print('')