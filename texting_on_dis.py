from pygame import *
from pygame.locals import *
from pygame.rect import *
import pyc

init()

def draw_point(text, pos):
    img = font.render(text, True, (255,0,100))
    draw.circle(screen, pyc.RED, pos, 5)
    screen.blit(img, pos)
    
size = 800,600
C1_GREEN = (204,255,204)
C1_BLUE = (153,204,255)


screen = display.set_mode(size)

rect = Rect(50,70,300,200)

print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}, top left = {rect.topleft}')
print(f'centre={rect.center}')


pts = ('topleft', 'topright', 'bottomleft', 'bottomright', 'midtop', 'midright', 'midbottom', 'midleft', 'center')

font = font.Font("NANUMSQUAREROUNDB.TTF", 10)

running = True
while running :
    
    for ev in event.get() :
        if ev.type == QUIT :
            running = False
            
    screen.fill(C1_GREEN)
    draw.rect(screen, pyc.GREEN, rect)
    
    for pt in pts :
        pass
        draw_point(pt, eval(f'rect.{pt}'))
    display.flip()
    
quit()
