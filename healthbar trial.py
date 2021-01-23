import pygame
import time
ts = 0.1
pygame.init()

screen = pygame.display.set_mode((800,600))
hblist = []
hp = 6
def addhealth():
    l = len(hblist)
    if l%2 == 0:
        hblist.append(pygame.draw.rect(screen, (0,255,0), pygame.Rect(700, 30 + 10*l, 10, 10)))
    else:
        hblist.append(pygame.draw.rect(screen, (0,128,0), pygame.Rect(700, 30 + 10*l, 10, 10)))



for i in range(hp):
    addhealth()
    pygame.display.update()
    time.sleep(ts)

def deletehealth():
    screen.fill((0,0,0),(700, 30, 10, 100))
    j = len(hblist)
    print(j)
    del hblist[j-1]

    for m in range(j-1):
        if m%2 == 0:
            hblist.append(pygame.draw.rect(screen, (0,255,0), pygame.Rect(700, 30 + 10*m, 10, 10)))
        else:
            hblist.append(pygame.draw.rect(screen, (0,128,0), pygame.Rect(700, 30 + 10*m, 10, 10)))

deletehealth()
pygame.display.update()
        
