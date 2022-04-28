month = input('Enter month (numeric):')
day = input('Enter day:')
year = input('Enter two digit year:')

if int(month) * int(day) == int(year):
    print ('This date is magic!')
else:
    print ('This date is not magic.')
