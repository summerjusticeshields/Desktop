#get the number of cookies
cookies = input ('Enter number of cookies: ')

a = 1.5
b = 1
c = 2.75

amount_of_sugar = int(f'(1.5/48)*{cookies:.1f}')
amount_of_butter = (f'(1/48)*{cookies:.1f}')
amount_of_flour =  (f'(2.75/48)*{cookies:.1f}')

#display ingrdients
print (f'({amount_of_sugar} cups of sugar, {amount_of_butter} cups of butter, and {amount_of_flour} cups of flour')

#For every 1 cookie you need: 1.5/48 cups of sugar, 1/48 cups of butter, 2.75/48 cups of flour

#x * 48 = 1.5
#1.5/48 = x
#x =
