color_1 = input('Enter primary color:')
color_2 = input('Enter primary color:')

if (color_1 == 'red' and color_2 == 'blue' or color_1 == 'blue' and color_2 == 'red'):
    print ('When you mix blue and red, you get purple.')
elif (color_1 == 'red' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'red'):
    print ('When you mix yellow and red, you get orange.')
elif (color_1 == 'blue' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'blue'):
    print ('When you mix yellow and blue, you get green.')
else: (print('You didn\'t input two primary colors.'))
