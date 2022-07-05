import turtle
import math
import time
import random as rnd
#sets up the window and main turtle t
turtle.tracer(0,0)
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.setup(1900,1040,0,0)
t.hideturtle()
t.width=2
# Creating the screen object
screen = turtle.Screen()
t.pensize(1)
# Setting the screen color-mode
screen.colormode(255)
for fram in range(60,120):
    for j in range(0,60):
    #turtle extends out to 3000 but breaks when outside of window boundaries, this varies depending on the rotation
        t.tilt(j)
        for i in range(0,360):
            t.color(int(math.sin(i+j)*i)%255,int(math.cos(i+j)*i)%255,int(math.sin(i+j+fram)*i)%255)
            # t.rt(i)
            # t.fd(j)
            # t.penup()
            t.goto(math.sin(i+j+fram)*i,math.cos(i+j+fram)*i)
            t.pendown()
            t.dot()
            width = (turtle.window_width() / 2) + 200
            abs_x = abs(t.xcor())
            #checks if turtle is drawing outside window width and breaksstop
            if abs_x > width:
                break
    turtle.update()
turtle.clear()

        # t.reset()
# t.reset()
# t.hideturtle()
# turtle.tracer(0,0)


screen.exitonclick()