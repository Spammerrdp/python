from turtle import*

import colorsys 

bgcolor("black")

tracer(2)

n = 36

h = 0.5

for i in range (200):

	k= colorsys.hsv_to_rgb (h,0.9,1)	
  h+=1/n

	color(k)

	left(50)

	for j in range (5):

		forward (250)

		left(889)
