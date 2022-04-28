#Please use Turtle module to draw the following picture: 

#-	(25 points) Draw X-axis and Y-axis with length of 500.
#-	Draw three circles whose centers are in the (0, 0)
#o	(25 points) First circle in “red” color, radius is 70.
#o	(10 points) First circle in “green” color, radius is 140.
#o	(10 points) First circle in “blue” color, radius is 210.

# import turtle
import turtle

screen_w = 1000
screen_h = 1000

turtle.setup(screen_w, screen_h)

#draw y-axis

turtle.penup()
turtle.goto(0,125)
turtle.pendown()
turtle.goto(0,-125)

#draw x-axis

turtle.penup()
turtle.goto(-125,0)
turtle.pendown()
turtle.goto(125,0)
turtle.penup()

#draw red circle

radius = 45
turtle.goto(0,-45)
turtle.pendown()
turtle.pencolor('red')
turtle.pensize(1)
turtle.circle(radius)

#draw green circle

radius = 70
turtle.goto(0,-70)
turtle.pendown()
turtle.pencolor('green')
turtle.pensize(1)
turtle.circle(radius)

#draw blue circle

radius = 105
turtle.goto(0,-105)
turtle.pendown()
turtle.pencolor('blue')
turtle.pensize(1)
turtle.circle(radius)

turtle.done()