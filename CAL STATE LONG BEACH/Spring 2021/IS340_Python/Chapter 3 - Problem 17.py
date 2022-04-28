

print('Reboot the computer and try to reconnect')
problem = input('Did that fix the problem? ')


if problem == 'no' or 'No' or 'NO':
    print('Reboot the router.')
    problem = input('Did that fix the problem? ')
    if problem == 'no' or 'No' or 'NO':
        print('Make sure the cables between the router and modem are plugged in firmly')
        problem = input('Did that fix the problem? ')
        if problem == 'no' or 'No' or 'NO':
            print('Move the router to a new location and try to connect.')
            problem = input('Did that fix the problem? ')
            if problem == 'no' or 'No' or 'NO':
                print('Get a new router')
else:
    
