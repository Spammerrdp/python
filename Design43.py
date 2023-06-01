from turtle import *
tracer(10)
left(90)
backward(100)
bgcolor('black')
color('brown')
def tree(l):
          if l<10:
                  return
          else:
                 forward(l)
                 color('pink')
                 pensize(6)
                 circle(2)
                 pensize(1)
                 color('brown')
                 left(30)
                 tree(3*l/4)
                 right(60)
                 tree(3*l/4)
                 left(30)
                 backward(l)
                 hideturtle()
tree(100)
exitonclick()
