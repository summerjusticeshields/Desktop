male = int(input('Enter number of males:'))
female = int(input('Enter number of females:'))

percent_m = (male / (female + male))*100
percent_f = (female / (female + male))*100

print(f'Percent males: {percent_m:.0f}%')
print(f'Percent females: {percent_f:.0f}%')
