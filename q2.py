import turtle
from turtle import Screen, Turtle

turtle.hideturtle()

height = 700
width = 700
turtle.setup(width, height)

turtle.penup()
turtle.goto(0,500)
turtle.pendown()
turtle.goto(0,-500)
turtle.penup()
turtle.goto(500,0)
turtle.pendown()
turtle.goto(-500,0)
turtle.penup()
turtle.goto(0,-60)
turtle.pendown()
turtle.pencolor('red')
turtle.circle(60)
turtle.penup()
turtle.goto(0,-120)
turtle.pendown()
turtle.pencolor('green')
turtle.circle(120)
turtle.penup()
turtle.goto(0,-180)
turtle.pendown()
turtle.pencolor('blue')
turtle.circle(180)




turtle.done()