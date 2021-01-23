import pygame
import random
import time

humany = 500
ts = 0.1
human_width = 100

hit = False

display_width = 800
display_height = 600
pygame.font.init()
screen = pygame.display.set_mode((display_width,display_height))
display_width -= human_width
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
img = pygame.image.load("human.png")
running = True
pygame.display.set_caption('Avoid Covid')
pygame.display.update()
humanx = (display_width * 0.45)
humany = (display_height * 0.8)
x_change = 0
corona_speed = 3
corona_starty = display_height+1

hblist = []
hp = 4

def addhealth():
   l = len(hblist)
   if l%2 == 0:
       hblist.append(pygame.draw.rect(screen, (0,255,0), pygame.Rect(775, 100 + 10*l, 10, 10)))
   else:
       hblist.append(pygame.draw.rect(screen, (0,128,0), pygame.Rect(775, 100 + 10*l, 10, 10)))
   pygame.display.update()

#for i in range(hp):
#   addhealth()
#   pygame.display.update()
#   time.sleep(ts)

def deletehealth():
   screen.fill((0,0,0),(775, 100, 10, 300))
   j = len(hblist)
   print(j)
   del hblist[j-1]
#   time.sleep(1)
   
   for m in range(j-1):
        if m%2 == 0:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(775, 100 + 10*m, 10, 10))
        else:
            pygame.draw.rect(screen, (0,128,0), pygame.Rect(775, 100 + 10*m, 10, 10))
   pygame.display.update()


def message_display(text):
    largeText = pygame.font.Font(pygame.font.get_default_font(), 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)

def crash():
    message_display("You caught covid!")
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def corona(coronax, coronay, coronaw, coronah, color):
    pygame.draw.rect(screen, color, [coronax, coronay, coronaw, coronah])

def human(x,y):
    screen.blit(img, (x, y))

for h in range(hp):
#    print("enter addhealth")
    addhealth()

pygame.display.update()
time.sleep(3)


while running == True:
    screen.fill(black,(0,0,750,600))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT  or event.key == pygame.K_a:
                    x_change = -3

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0


    if corona_starty > display_height:
        added = 0
        corona_startx = random.randrange(0, display_width)
        corona_starty = -600
        if corona_speed < 6:
            corona_speed += 0.5
        corona_width = 50
        corona_height = 50
        
    corona(corona_startx, corona_starty, corona_width, corona_height, red)
    corona_starty += corona_speed
    
    if humanx > 0 and x_change == -3:
        humanx -= 3

    if humanx < 648 and x_change == 3:
        humanx += 3

    print("coronax = ",corona_startx)
    print("coronay = ",corona_starty)
    print("humanx = ",humanx)
    print("humany = ",humany)
    
#    time.sleep(5)

    human(humanx, humany)
    if humany < corona_starty+corona_height:
        print("y crossover")
        if (humanx > corona_startx and humanx <corona_startx + corona_width) or (humanx+human_width > corona_startx and humanx + human_width < corona_startx+corona_width):
            print("x crossover")
            hit = True
            corona_starty = 650
            print("y reset = ",corona_starty)

#    time.sleep(2)


    if hit:
        print("in hit")
        print("len ",len(hblist))
        if len(hblist)>2:
            for d in range(2):
               deletehealth()
#            pygame.display.update()
            hit = False
        else:
            screen.fill((0,0,0),(775, 100, 10, 300))
            print("in else")
            running = False
    else:
        print("in not hit")
        if (len(hblist)<6 and added==0):
           print("add hp")
           addhealth()
           added = 1
         

    pygame.display.update()
    clock.tick(120)

print("Sorry you are infected with COVID; please take 14 days rest")
quit()
pygame.quit()
