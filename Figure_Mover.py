from pygame import *
from pygame.locals import *
import pyc


C1_GREEN = (204, 255, 204)
C1_BLUE = (153, 204, 255)


size = width,height = 1280,720
screen = display.set_mode(size)
bgColor = C1_BLUE
screen.fill(bgColor)

pos1 = [0,0,100,70]
draw.rect(screen,pyc.BLUE,pos1)
display.update()

clock = time.Clock()

init()
distance = 10

running = True
while running:
    clock.tick(60)
    for Event in event.get():
        if Event.type == QUIT : 
            running = False
        if Event.type == KEYDOWN :
            if Event.key == K_ESCAPE :
                running = False
    event.pump()
    keys = key.get_pressed()
    
    if keys[ord('s')]:
        if pos1[1] >= height - pos1[3]:
            pos1[1] = height - pos1[3]
        else :
            pos1[1] += distance
            
    elif keys[ord('w')]:
        if pos1[1] <=0:
            pos1[1] = 0
        else :
            pos1[1] -= distance
        
    elif keys[ord('a')]:
        if pos1[0] <= 0:
            pos1[0] = 0
        else :
            pos1[0] -= distance
    
    elif keys[ord('d')]:
        if pos1[0] >= width - pos1[2]:
            pos1[0] = width - pos1[2]
        else :
            pos1[0] += distance
    
    print(pos1)
    
    screen.fill(bgColor)
    draw.rect(screen,pyc.BLUE,pos1)
    display.update()

quit()
    
    
