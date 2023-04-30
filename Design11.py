from turtle import *

import colorsys 

tracer (90)

bgcolor("black")

h=1

c=colorsys.hsv_to_rgb(h,1,1) 

pensize(2)

def Draw():

	global h	

	for i in range(4):

	

		c=colorsys.hsv_to_rgb(h,1,1)

		

		fillcolor(c)

		

		h+=1.009

		

		begin_fill()

		

		fd(50)

		

		right(20)

		

		fd(400)

	

		right (9)

		

		end_fill()

for i in range(400):

	Draw()

	

	goto(0,0)

	

	rt(1)
