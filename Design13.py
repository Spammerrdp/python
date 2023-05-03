from turtle import*

import colorsys

speed('fastest')

s=0.9

for i in range(100):

	col=colorsys.hsv_to_rgb(s, 1, 1)

	s+=1

	fillcolor (col)

	begin_fill()

	circle(130-1,100)

	lt(90)

	circle(130-i,100)

	lt(20)

	rt (79)

	end_fill()

done()
