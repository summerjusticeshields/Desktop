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

turtle.setup(500,600)

turtle.penup()
turtle.hideturtle()

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

#Draw stars

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()

#Display the star names

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('Betelgeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('Rigel')


# Draw a line from the left shoulder to the left belt star

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()


turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

turtle.done()

