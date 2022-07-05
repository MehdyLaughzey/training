import turtle
import math
import time
import random as rnd
#sets up the window and main turtle t
# turtle.tracer(0,0)
# t = turtle.Turtle()
# turtle.bgcolor('black')
# turtle.setup(1900,1040,0,0)
# t.hideturtle()
# # Creating the screen object
screen = turtle.Screen()
# p=3.14
# # Setting the screen color-mode
screen.colormode(255)
# # for j in range(360,0,-1):
# # #turtle extends out to 3000 but breaks when outside of window boundaries, this varies depending on the rotation
# for x in range(180,0,-1):
#     for y in range(180):
#         t.color((x+y)%255,3*(x+y)%255,6*(x+y)%255)
#         t.goto(math.sin(x)*(x),math.cos(y)*y)
#         turtle.update()
#        # t.reset()


def drawLogarithmicSpiral(a, b):

    
    for i in range(1, 720, 5):
    # Draw a spiral 
        t = math.radians(i)
        x = a*math.exp(b*t)*math.cos(t)
        y = a*math.exp(b*t)*math.sin(t)

        # Since our turtle is down, we'll be drawing the spiral as we move positions.
        tt.color(rnd.randint(120, 240),rnd.randint(120, 240),rnd.randint(120, 240))
        tt.goto(x,y)
        width = (turtle.window_width() / 2) + 200
        abs_x = abs(tt.xcor())
        if abs_x > width:
            break
    turtle.update()
    turtle.tilt(30)


        

# These two values for a and b are very arbitrary, change them up and see what happens!
screen = turtle.Screen()
screen.colormode(255)
tt=turtle.Turtle()
turtle.setup(1900,1040,0,0)
turtle.bgcolor('black')
tt.hideturtle()
for h in range(1,6):
    drawLogarithmicSpiral(.3, .6)
    
# The turtle.mainloop() function prevents the program from quitting after the drawing has been made.
turtle.mainloop()



# for i in range(0,360):
#     width = (turtle.window_width() / 2) + 200
#     #checks if turtle is drawing outside window width and breaksstop
#     if abs_x > width:
#         break
#     turtle.update()
#     # t.reset()
# # t.reset()
# # t.hideturtle()
# # turtle.tracer(0,0)


screen.exitonclick()