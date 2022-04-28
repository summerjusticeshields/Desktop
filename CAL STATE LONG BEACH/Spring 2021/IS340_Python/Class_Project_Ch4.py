import turtle

#for x in range (5):
    #turtle.forward(100)
    #turtle.right(72)



#SIDES = 5
#LEN = 100

#angle = 360 / SIDES

#angle = 144 #star angle

#for side in range(SIDES):
   # turtle.forward(100)
    #turtle.right(angle)

import turtle

RADIUS = 100
NUMBER_OF_CIRCLES = 1000
angle = 360 / NUMBER_OF_CIRCLES

turtle.speed(0)
colors = ["red", "green", "blue", 'yellow', 'purple', 'orange']
number_colors = len(colors)

for index in range(NUMBER_OF_CIRCLES):

    color = colors[index % number_colors]
    turtle.color(color)

    turtle.circle(RADIUS)
    turtle.right(angle)

turtle.done()