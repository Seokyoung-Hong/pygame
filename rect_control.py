import pygame
from pygame.locals import *
from pygame.rect import *
import pyc


size = width, height = 800,600
screen = pygame.display.set_mode(size)
rect1 = Rect(50,60,200,80)
rect2= Rect(100,20,200,130)

dir = { K_LEFT : (-5,0), K_RIGHT:(5,0), K_UP : (0,-5), K_DOWN : (0,5)}

pygame.init()

running = True
while running :
    for ev in pygame.event.get() :
        if ev.type == QUIT :
            running = False
        if ev.type == KEYDOWN :
            if ev.key in dir :
                v= dir[ev.key]
                rect2.move_ip(v)
    
    clip = rect1.clip(rect2)
    union = rect1.union(rect2)
    
    
    screen.fill(pyc.GRAY)
    
    pygame.draw.rect(screen,pyc.YELLOW, union,0)
    pygame.draw.rect(screen,pyc.GREEN, clip,0)
    pygame.draw.rect(screen,pyc.BLUE, rect1,2)
    pygame.draw.rect(screen,pyc.RED, rect2,5)
    
    pygame.display.flip()
            
                
pygame.quit()