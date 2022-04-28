# Ask user to input amoount between 0.01 and 0.99

user_amount = float(input('Enter amount between 0.01 and 0.99: '))

#calculate the relative amounts

quarter = (user_amount)//.25
user_amount = user_amount%(.25)

dime = (user_amount)//.1
user_amount = user_amount%(.1)

penny = (user_amount)*100

#print the totals
print(f' Your change is {quarter} quarter(s), {dime} dime(s), and {penny} penny.')
