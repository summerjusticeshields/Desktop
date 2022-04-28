print('Reboot the computer and try to connect.')

problem = input('Did that fix the problem? ')

string1 = 'NO'
string2 = 'no'

if problem == 'no':
        print('Reboot the router and try to connect.')
        problem = input('Did that fix the problem? ')
        if problem == 'no':
                print('Make sure the cables between the router and modem are plugged in firmly.')
                problem = input('Did that fix the problem? ')
                if problem == 'no':
                        print('Move the router to a new location.')
                        problem = input('Did that fix the problem? ')
                        if problem == 'no':
                            print('Get a new router.')

else:
    breakpoint









