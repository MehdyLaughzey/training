import pygame


gravity = 2 #or whatever constant value you want for the gravity acceleration
screen = pygame.display.set_mode((x, y)) #x and y here is the resolution
while True:
    object.time += 1
    gravity_speed = gravity * object.time
    object.rect.y += gravity_speed
    screen.blit(object.image, object.rect)
    pygame.display.update()
    pygame.time.delay(50) #add a delay before the next loop, otherwise things happens really fast.
