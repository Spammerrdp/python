from turtle import*

import colorsys

tracer (40)

bgcolor('black')

pensize (4)

h=0.4

for i in range (299):

	c = colorsys.hsv_to_rgb (h,1,1)	color(c)

	h+=0.002

	rt(200)

	for j in range (5):

		fd(i)

		rt(10)

		rt(50)

	rt(1180)

done()
