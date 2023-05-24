from turtle import*

import colorsys 

bgcolor("black")

speed(0)

n = 36

h = 0.5

for i in range (80):

	k= colorsys.hsv_to_rgb (h,0.9,1)	
  h+=1/n

	color(k)

	left(50)

	for j in range (5):

		forward (2500)

		left(144)
