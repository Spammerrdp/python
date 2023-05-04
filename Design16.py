import colorsys

from turtle import *

bgcolor('black')

tracer(100)

pensize(8)

h = 0.5

n=100

for i in range(600):

	c=colorsys.hsv_to_rgb(h,1,0.9)

	h += 0.5/n

	color(c)

	fillcolor('black')

	begin_fill()

	circle(90,43)

	circle(18)

	rt(20)

	bk(45)

	up()

	goto(0,0)

	down()

	circle(1,203)

	rt(50)

	end_fill()

done()
