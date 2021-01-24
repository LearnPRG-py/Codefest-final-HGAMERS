import pygame
import random
import time

print('Hello! Welcome to Avoid COVID by the Hgamers!')
time.sleep(5)
print('In this game, you must avoid COVID by using the WASD keys. If covid hits you, lose 2 health. Every single wave you survive, you get 1 extra health. If you survive x waves, you will survive COVID, and you win the game.')
time.sleep(10)
print('On a more serious note, here are some quick facts about COVID.')
fact1 = ('COVID-19 is a type of coronavirus, a deadly lung disease')
fact2 = ('The most simple and most effective way to avoid COVID-19 in real life is wearing masks and using safety gloves in unsanitary areas')
fact3 = ('Hand sanitizers are very helpful during this time, giving a quick way to make sure your hands are clean. Alternativley, washing your hands for 20 seconds is effective.')
fact4 = ('Symptoms of COVID-19 are as follows- Chills, coughing, sneezing, breathing issues, faigue and headaches.')
time.sleep(5)
print(fact1)
time.sleep(5)
print(fact2)
time.sleep(10)
print(fact3)
time.sleep(10)
print(fact4)
time.sleep(10)

humany = 500
ts = 0.1
human_width = 100

hit = False
target = 15
win = False

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

def deletehealth():
   screen.fill((0,0,0),(775, 100, 10, 300))
   j = len(hblist)
   del hblist[j-1]

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
        to_add = 0
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

    human(humanx, humany)
    if humany < corona_starty+corona_height:
        if (humanx > corona_startx and humanx <corona_startx + corona_width) or (humanx+human_width > corona_startx and humanx < corona_startx+corona_width):
            hit = True
            corona_starty = 650

    if hit:
        if len(hblist)>2:
            for d in range(3):
               deletehealth()
            hit = False
        else:
            screen.fill((0,0,0),(775, 100, 10, 300))
            running = False
    else:
        if (len(hblist)<target and to_add==0):
           addhealth()
           to_add = 1

    if len(hblist) == 15:
       running = False
       win = True
         
    pygame.display.update()
    clock.tick(120)

if win == True:
   print("Well Done! You have taken necessary safety precautions against COVID and beaten the virus.\n","You can now take the vaccine.")
else:
   print("Sorry you are infected with COVID; please take 14 days rest & get well soon")

quit()
pygame.quit()
