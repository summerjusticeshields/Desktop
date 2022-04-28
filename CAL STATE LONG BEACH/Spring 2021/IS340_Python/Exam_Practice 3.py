import turtle
#turtle.hideturtle()
#turtle.begin_fill()
#turtle.fillcolor('pink')
#turtle.goto(120, 120)
#turtle.goto(200, -100)
#turtle.goto(0,0)
#turtle.end_fill()

#variable = turtle.numinput(title, prompt, default=x, minval=y, maxval=z)

#num = turtle.numinput('Input Needed', 'Enter a value in the range 1-10', 
#default=5, minval=1, maxval=10)

#turtle.done()

Name = input('Enter name: ')
Address = input ('Enter your address (i.e. 3066 Olive Ave., Altadena, CA 91001)')
Telephone = input ('Enter your phone number: ')
Degree = input ('Enter your college major: ')

print(Name)
print(Address)
print(Telephone)
print(Degree)

Area = int(input('Please enter the total square feet in your tract of land: '))


Acres = Area/43560

print(f'You have {Acres:.0f} acres.')

P = float(input('Enter the principal amount: '))
r = float(input('Enter the annual interest rate: '))
n = float(input('Enter the number of times per year the interest is compunded: '))
t = float(input('Enter number of years: '))

A = P*(1 + (r/n))**(n*t)

print(f'You will have {A:.2f}')