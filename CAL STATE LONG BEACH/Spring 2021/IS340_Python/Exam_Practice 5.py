print("Hello world")

import turtle

turtle.hideturtle()

turtle.dot()

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.dot()
turtle.goto(100,100)
turtle.dot()
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.dot()

turtle.goto(-100,100)
turtle.dot()

#draw top dotted line
turtle.setheading(0)
turtle.forward(21)
turtle.penup()
turtle.forward(26)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(26)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(26)
turtle.pendown()
turtle.forward(21)

turtle.setheading(270)
turtle.goto(100,-100)

#draw bottom dotted line
turtle.setheading(180)
turtle.forward(21)
turtle.penup()
turtle.forward(26)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(26)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.forward(26)
turtle.pendown()
turtle.forward(21)

turtle.setheading(90)
turtle.goto(-100,100)

turtle.done()