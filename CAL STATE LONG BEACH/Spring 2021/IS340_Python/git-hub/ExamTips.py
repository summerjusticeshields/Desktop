#Tips
#1. Make sure you understand the question/problem
#2. come with a solution (no coding yet) that divide the solution in multiple subtasks
#3. incrementally work on subtask, test/verify it, then the next task
#4. tools: VS code, run it, debud it 

# 1 Set the window size to 600 x 600
# 2 Draw a square with length of 25 px, lower left (100, 250)
# 3 Ask the user to type an angle and a distance
# 4 Launch the arrow to the specialized angle
# 5 check if the arrow hit the target (inside the square)
# 6 display message (hit or miss)

import turtle

pen = turtle.Pen()

# 1 Set the window size to 600 x 600
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# 2 Draw a square with length of 25 px, lower left (100, 250)

TARGET_WIDTH = 25
TARGET_LOW_LEFT_X = 100
TARGET_LOW_LEFT_Y = 250

pen.up()
pen.goto(TARGET_LOW_LEFT_X, TARGET_LOW_LEFT_Y)
pen.down()
pen.forward(TARGET_WIDTH)

NORTH = 90
pen.setheading(WEST)
pen.forward(TARGET_WIDTH)

WEST = 180
pen.setheading(WEST)
pen.forward(TARGET_WIDTH)

SOUTH = 270
pen.setheading(SOUTH)
pen.forward(TARGET_WIDTH)

# go back home
pen.up()
pen.home()
pen.down()

# 3 Ask the user to type an angle and a distance

angle = float(input('Type in an angle: '))
distance = float(input('Type a distance: '))

pen.setheading(angle)
pen.forward(distance)

# 5 check if the arrow hit the target (inside the square)

xcor = pen.xcor()
ycor = pen.ycor

##check

left = TARGET_LOW_LEFT_X
right = TARGET_LOW_LEFT_X + TARGET_WIDTH

is_x_in = xcor >= left and xcor <= right

bottom = TARGET_LOW_LEFT_Y
top = bottom + TARGET_WIDTH

is_y_in = ycor >= bottom and xcor <= top

if is_hit:
    print('Hit the target')
else:
    print('Miss the target')


turtle.done()








