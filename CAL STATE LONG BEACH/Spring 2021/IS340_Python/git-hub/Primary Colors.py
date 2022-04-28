color_1 = input('Enter first primary color:')
color_2 = input('Enter second primary color: ')
 
if color_1 == 'red' and color_2 == 'blue' or color_1 == 'blue' and color_2 == 'red':
 	print ('When you mix red and blue, you get purple.')
 
elif color_1 == 'red' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'red':
	print ('When you mix red and yellow, you get orange.')
	
elif color_1 == 'blue' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'blue':
	print ('When you mix blue and yellow, you get green.')
else:
	print: ('You didn\'t input two primary colors.')
