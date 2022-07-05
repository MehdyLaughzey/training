import pygame.midi
import time
import numpy
import random
pygame.midi.init()
player = pygame.midi.Output(2)

player.set_instrument(0)

minlenth=0.1
slicel=random.randint(1, 3)*3
for p in range(1,slicel):




# while True:
#     for i in range(24,120,3):
#         player.note_on(i+3,int(numpy.sin(i)*random.randint(30, 60)))
#         time.sleep(0.1)
#         player.note_off(i+3,int(numpy.sin(i)*random.randint(30, 60)))




# for j in range(i-12,i+12,3):
#     player.note_on(j, i)
#     # player.note_on(j+3,i)
#     # player.note_on(j-3,i)
#     time.sleep()


time.sleep(1)
player.note_off(64, 64)
del player
pygame.midi.quit()