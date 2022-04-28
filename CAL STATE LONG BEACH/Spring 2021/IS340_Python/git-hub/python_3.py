question = 'Please input your birth year: '

answer = input(question) # all inputs are strings

birth_year = int(answer) # int is another builtin function

age = 2021 - birth_year

#print ('Your age is', age, 'years old')

message = f'Your age is {age} years old'

print(message)

#get the number of cookies
cookies = input ('Enter number of cookies:')

x = int(cookies)*1.5/48
y = int(cookies)*1.0/48
z = int(cookies)*2.75/48

message = f'You need {x} cups of sugar, {y} cups of butter, and {z} cups of flour.'
print (message)


m = input ('Enter number of males: ')

f = input ('Enter number of females: ')

print(int(m/f))

male = f'{m/(m+f)}'
female = f'{f/(m+f)}'

print(f'Percent males: {male}')
print(f'Percent females:{female}')
