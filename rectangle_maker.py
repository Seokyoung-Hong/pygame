from pygame import *
from pygame.locals import * 
import sys
import pyc

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

C1_BLUE = (204,204,255)
C1_GREEN = (204, 255, 204)
bgcolor = C1_GREEN


key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN,K_b:BLUE,K_y:YELLOW,K_w:WHITE}
print(key_dict)

size = width, height = 800,600
screen = display.set_mode(size)
# bgcolor = WHITE
# caption = f'BG Color {bgcolor}'
# display.set_caption(caption)
screen.fill(bgcolor)
display.update()
init()

start = (0,0)
end = (0,0)
dSize = (0,0)
drawing = False
rectList = []



run =True
while run :
    for Event in event.get():
        print(Event)
        
        # if Event.type == KEYDOWN :
        #     if Event.key in key_dict:
        #         bgcolor = key_dict[Event.key]
        #         # caption = f'BG Color {bgcolor}'
        #         # display.set_caption(caption)
        #     else :
        #         bgcolor = C1_BLUE
              
        
        if Event.type == MOUSEBUTTONDOWN :
            start = Event.pos
            dSize = 0,0
            drawing = True
            print(Event)
            
        elif Event.type == MOUSEBUTTONUP :
            end = Event.pos
            dSize = end[0] - start[0] , end[1] - start[1]
            drawing = False
            rect = Rect(start,dSize)
            rectList.append(rect)
            print(Event)
            
        elif Event.type == MOUSEMOTION and drawing == True :
            end = Event.pos
            dSize = end[0] - start[0], end[1] - start[1]
            screen.fill(bgcolor)
            for r in rectList :
                draw.rect(screen,BLACK,r,4)
            draw.rect(screen,RED,(start,dSize),2)
            display.update()

                            
        elif Event.type == QUIT:
            run = False
        # screen.fill(bgcolor)
        # display.update()
quit()
sys.exit()