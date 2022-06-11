import pygame
import numpy as np
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
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
 


for i in range(9):
    print(fibonacci(i))

# Driver Program


# verticies = (
#     (1, -1, -1),
#     (1, 1, -1),
#     (-1, 1, -1),
#     (-1, -1, -1),
#     (1, -1, 1),
#     (1, 1, 1),
#     (-1, -1, 1),
#     (-1, 1, 1)
#     )
# x=tuple()
# verticies.__add__()

# edges = (
# (0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),
# (0,1),(1,2),(2,3),(3,0),
# (4,6),(5,7),(7,6),(5,4)
#     )


# def Cube():
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(verticies[vertex])
#     glEnd()


# def main():
#     pygame.init()
#     display = (800,600)
#     pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

#     gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

#     glTranslatef(0.0,0.0, -5)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         glRotatef(1, 3, 1, 1)
#         glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#         Cube()
#         pygame.display.flip()
#         pygame.time.wait(10)


# main()
