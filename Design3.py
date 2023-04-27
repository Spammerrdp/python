from turtle import *

bgcolor('black')

tracer (100)

colour = ['cyan', 'white'] 

for i in range(1200):

	color(colour[i%2])	up()

	fd(i)

	down()

	rt(1)

	for j in range(5):

		fd(j*25)

		lt(20000)
