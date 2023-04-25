from turtle import *

from random import randint

speed('fastest')

bgcolor("black")

x=1

for i in range(500):

	r=randint(0,255)	g=randint(0,255) 

	b=randint(0,255)

	colormode(255)

	pencolor(r,g,b) 

	fd(10+x)

	rt(100.578)

	x+=1

exitonclick()
