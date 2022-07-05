# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math
import random

FibArray = [0, 1]
 
def fibonacci(n):
   
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is less
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:       
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]



n=13

t = turtle
t.tracer(0,0)
screen = t.Screen()
screen.colormode(255)
t.hideturtle()
t.bgcolor('black')
t.setup(1900,1040,0,0)

for i in range(0,n-1):
    t.penup()
    t.goto(0,n*50)
    t.pendown()
    t.goto(50,n*50)
t.update()
screen.mainloop()


# def fiboPlot(n,angel):
#     a = 0
#     b = 1
#     square_a = a
#     square_b = b
 
   
 
#     # Bringing the pen to starting point of the spiral plot
#     x.setposition(factor, 0)
#     x.setheading(angel)
#     # Setting the colour of the plotting pen to red
    
 
#     # Fibonacci Spiral Plot
#     x.left(90)
#     for i in range(n):
#         fdwd = math.pi * b * factor / 2
#         fdwd /= 90
#         for j in range(90):
#             # x._rotate(angel)
#             x.forward(fdwd)
#             x.left(1)
#         temp = a
#         a = b
#         b = temp + b
#     x.tilt(angel)
 
# # Here 'factor' signifies the multiplicative
# # factor which expands or shrinks the scale
# # of the plot by a certain factor.
# factor = 1
 
# # Taking Input for the number of
# # Iterations our Algorithm will run
# n = 14
 
# # Plotting the Fibonacci Spiral Fractal
# # and printing the corresponding Fibonacci Number



# turtle.tracer(0,0)
# screen = turtle.Screen()
# screen.colormode(255)
# x = turtle.Turtle()
# x.hideturtle()

# turtle.bgcolor('black')
# turtle.setup(1900,1040,0,0)

# for j in range(0,360,5):
    
    

#     # x.turtlesize(5,2)

#     x.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
#     fiboPlot(n,j)

# # for turtle in screen.turtles():
# #     turtle.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
# turtle.update()
# screen.mainloop()

# x.done()