#number_of_books = int(input('How many books did you purchase? '))

#if number_of_books == 0:
    #print('You\'ve earned 0 points')
#elif number_of_books == 2:
    #print('You\'ve earned 5 points')
#elif number_of_books == 4:
    #print('You\'ve earned 15 points')
#elif number_of_books == 6:
    #print('You\'ve earned 30 points')
#elif number_of_books >= 8:
    #print('You\'ve earned 60 points')


#price of package

package_price = 99

quantity = float(input('Please enter quantity of packages purchased: '))

total = (package_price * quantity)

if quantity <= 9:
    print('You have no discount and your total is $',total)

elif quantity >= 10 and quantity <= 19:
    print('Your discount is 10 percent and your total is $',(total * .9))

elif quantity >= 20 and quantity <= 49:
    print('Your discount is 20 percent and your total is $',(total * .8))

elif quantity >= 50 and quantity <= 99:
    print('Your discount is 30 percent and your total is $',(total * .7))

elif quantity >= 100:
    print('Your discount is 40 percent and your total is $',(total * .6))
