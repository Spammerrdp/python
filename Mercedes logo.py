from turtle import *

shape("circle")

speed(2)

bgcolor('black')

color("#CCCCCC")

pensize(7)

circle(154)

left(90)

penup()

pensize(15)

forward(150)

for _ in range(3):

    pendown()

    forward(150)

    penup()

    forward(-150)

    left(120)

hideturtle()

done()
