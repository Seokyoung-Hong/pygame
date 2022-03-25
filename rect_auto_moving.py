import pygame
from pygame.locals import *
from pygame.rect import *
import pyc

size = width, height = 800,600
screen = pygame.display.set_mode(size)


rect1 = Rect(50,50,50,75)
rect2 = Rect(75,100,75,75)

speed = [2,8]
speed0 = [7,2]

clock = pygame.time.Clock()

pygame.init()


running =True
while running :
    clock.tick(60)
    for ev in pygame.event.get():
        if ev.type == QUIT :
            running = False
        
    rect1.move_ip(speed)
    rect2.move_ip(speed0)
    
    if rect1.left < 0:
        speed[0] *= -1
    if rect2.left < 0:
        speed0[0] *= -1
    if rect1.right > width :
        speed[0] *= -1
    if rect2.right > width :
        speed0[0] *= -1
    if rect1.top < 0:
        speed[1] *= -1
    if rect2.top < 0 :
        speed0[1] *= -1
    if rect1.bottom > height :
        speed[1] *= -1 
    if rect2.bottom > height :
        speed0[1] *= -1
    
    screen.fill(pyc.GRAY)
    pygame.draw.rect(screen,pyc.GREEN, rect1)
    pygame.draw.ellipse(screen,pyc.BLUE,rect2)
    pygame.display.flip()


pygame.quit()