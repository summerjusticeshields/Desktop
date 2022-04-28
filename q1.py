import turtle


turtle.hideturtle()

#setup screen

height = 700
width = 700
turtle.setup(width, height)

#draw the intersection of two lines

turtle.penup()
turtle.goto(0,500)
turtle.pendown()
turtle.goto(0,-500)
turtle.penup()
turtle.goto(500,0)
turtle.pendown()
turtle.goto(-500,0)


#draw the red circle about the intersection

turtle.penup()
turtle.goto(0,-60)
turtle.pendown()
turtle.pencolor('red')
turtle.circle(60)

#draw the green circle about the intersection 

turtle.penup()
turtle.goto(0,-120)
turtle.pendown()
turtle.pencolor('green')
turtle.circle(120)

#draw the blue circle about the intersection

turtle.penup()
turtle.goto(0,-180)
turtle.pendown()
turtle.pencolor('blue')
turtle.circle(180)

turtle.done()