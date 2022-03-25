import pygame
from pygame.locals import *
from pygame.rect import *
import pyc


size = width, height = 800,600
screen = pygame.display.set_mode(size)

rect1 = Rect(50,60,300,150)
moving = False

dir = {K_LEFT:(-5,0), K_RIGHT:(5,0), K_UP:(0,-5), K_DOWN:(0,5)}

pygame.init()

running = True
while running :
    for event in pygame.event.get() :
        if event.type == QUIT :
            running = False
 
        if event.type == MOUSEBUTTONDOWN :
            if rect1.collidepoint(event.pos) :
                moving = True

        if event.type == MOUSEBUTTONUP :
                moving = False

        if event.type == MOUSEMOTION and moving :
            rect1.move_ip(event.rel)

    screen.fill(pyc.GRAY)
    pygame.draw.rect(screen,pyc.RED, rect1)

    if moving :
        pygame.draw.rect(screen,pyc.BLUE,rect1,5)
    pygame.display.flip()

pygame.quit()