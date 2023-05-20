from turtle import*

from colorsys import*

bgcolor('black')

tracer(400)

h = 0

n = 210

for i in range(2,290):

		c = hsv_to_rgb(h,1,1)		
    h += 120/n

		color (c)

		pensize(7)

		up()

		goto(0,0)

		down()

		circle(i,405)

		for j in range(2,1,100):

			circle(i/3,45)

done()
