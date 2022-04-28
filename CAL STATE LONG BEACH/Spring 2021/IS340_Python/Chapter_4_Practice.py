#You're a swimmer, and you want to compare all of your race 
#times to find the fastest one. Write a program that continuously 
#takes race times as doubles from standard input, until the 
#input is "no more races," at which point it should print out the 
#time of your fastest race.

#input race times

import math

times = input()

list = [times]
# list.sort()

while times != 'no more races':
    times = input()

else:
    if times == 'no more races':
        print (max(list))







