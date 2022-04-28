length1 = int(input('Enter length of first rectangle: '))
width1 = int(input('Enter width of first rectangle: '))

length2 = int(input('Enter length of second rectangle: '))
width2 = int(input('Enter width of second rectangle: '))

A1 = length1 * width1
A2 = length2 * width2

if A1 > A2:
    print('The area of rectangle one is greater.')
elif A2 > A1:
    print('The area of rectangle two is greater.')
elif A2 == A1:
    print('The area of both rectangles is equal.')