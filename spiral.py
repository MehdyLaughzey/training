import turtle
from turtle import Screen
import math
import time
import random as rnd
#sets up the window and main turtle t
turtle.tracer(0,0)
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.setup(1900,1040,0,0)
t.hideturtle()
# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)

   
#turtle extends out to 3000 but breaks when outside of window boundaries, this varies depending on the rotation
for i in range(0,6000):
    t.color(rnd.randint(1, 255),rnd.randint(1, 255),rnd.randint(1, 255))
    t.rt(int(i/3))
    t.fd(i)
    
    width = (turtle.window_width() / 2) + 200
    abs_x = abs(t.xcor())
    #checks if turtle is drawing outside window width and breaksstop
    if abs_x > width:
        break
turtle.update()

        
# t.reset()
# t.hideturtle()
# turtle.tracer(0,0)


screen.exitonclick()