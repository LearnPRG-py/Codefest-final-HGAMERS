import pygame
import random
import time
import textwrap

humany = 500
ts = 0.1
score = -3
img = pygame.image.load("testimg.png")
human_width = 100
display_width = 800
display_height = 600
pygame.font.init()
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
cvd = pygame.image.load("cvd.png")
corona_width = cvd.get_width()
corona_height = cvd.get_height()

running = True
pygame.display.set_caption('Avoid Covid')
msgtime = 2

def wrap_text(message, wraplimit):
    return textwrap.fill(message, wraplimit)

def show_score():
    largeText = pygame.font.Font(pygame.font.get_default_font(), 10)
    TextSurf, TextRect = text_objects("Score: " + str(score), largeText)
    TextRect.center = (740, 40)
    screen.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def covidinfo_display(text):
    screen.fill(white)
    largeText = pygame.font.Font(pygame.font.get_default_font(), 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def message_display(text):
    largeText = pygame.font.Font(pygame.font.get_default_font(), 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)

covidinfo_display('Hello! Welcome to Avoid COVID by the Hgamers!')
time.sleep(2*msgtime)

covidinfo_display('In this game, you must avoid COVID by using the AD or arrow keys.')
time.sleep(msgtime)

covidinfo_display('If covid hits you, lose 1 health. Every covid you survive, you get 1 point.')
time.sleep(msgtime)

covidinfo_display('On a more serious note, here are some quick facts about COVID.')
fact1 = ('COVID-19 is a type of coronavirus, a deadly lung disease')
fact2 = ('The most simple and most effective way to avoid COVID-19 in real life is...')
fact3 = ('Wearing masks and using safety gloves in unsanitary areas')
fact4 = ('Hand sanitizers are helpful, a quick way to make sure your hands are clean')
fact5 = ('Alternativley, washing your hands for 20 seconds is effective.')
fact6 = ('Symptoms of COVID are...')
fact7 = ('Chills, coughing, sneezing, breathing issues, fatigue and headaches')
time.sleep(msgtime)

covidinfo_display(fact1)
time.sleep(msgtime)

covidinfo_display(fact2)
time.sleep(msgtime)

covidinfo_display(fact3)
time.sleep(msgtime)

covidinfo_display(fact4)
time.sleep(msgtime)

covidinfo_display(fact5)
time.sleep(msgtime)

covidinfo_display(fact6)
time.sleep(msgtime)

covidinfo_display(fact7)
time.sleep(msgtime)

covidinfo_display('GET READY!!!')
time.sleep(2*msgtime)

pygame.display.update()
display_width -= human_width
humanx = (display_width * 0.45)
humany = (display_height * 0.8)
x_change = 0
corona_speed = 3
corona_starty1 = display_height+1
corona_starty2 = display_height+1
corona_starty3 = display_height+1

hblist = []
hp = 5
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
   print("Health is now:" + str(j))
   del hblist[j-1]

def showhealth():
    l = len(hblist)
    
    for i in range(l):
        if i%2 == 0:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(700, 30 + 10*i, 10, 10))
        else:
            pygame.draw.rect(screen, (0,128,0), pygame.Rect(700, 30 + 10*i, 10, 10))


def crash():
    message_display("You caught covid!")
    pygame.display.update()

def corona(coronax, coronay, coronaw, coronah, color):
    screen.blit(cvd, (coronax, coronay))
    #pygame.draw.rect(screen, color, [coronax, coronay, coronaw, coronah])

def human(x,y):
    screen.blit(img, (x, y))

while running == True:

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


    if corona_starty1 > display_height:
        score += 1
        corona_startx1 = random.randrange(0, display_width)
        corona_starty1 = -600 + random.randrange(0, 200)
        if corona_speed < 5:
            corona_speed += 0.5

    if corona_starty2 > display_height:
        score += 1
        corona_startx2 = random.randrange(0, display_width)
        corona_starty2 = -600 + random.randrange(0, 200)

    if corona_starty3 > display_height:
        score += 1
        corona_startx3 = random.randrange(0, display_width)
        corona_starty3 = -600 + random.randrange(0, 200)

    screen.fill(white)
    showhealth()
    show_score()
    corona(corona_startx1, corona_starty1, corona_width, corona_height, black)
    corona(corona_startx2, corona_starty2, corona_width, corona_height, black)
    corona(corona_startx3, corona_starty3, corona_width, corona_height, black)

    corona_starty1 += corona_speed
    corona_starty2 += corona_speed
    corona_starty3 += corona_speed
    
    if humanx > 0 and x_change == -3:
        humanx -= 3
    if humanx < display_width and x_change == 3:
        humanx += 3

    #if humanx <= display_width - human_width and humanx >= 0:
    #    humanx += x_change

    human(humanx, humany)
    if humany <= corona_starty1:
        if corona_startx1 >= humanx and corona_startx1 <= humanx + human_width or corona_startx1+corona_width >= humanx and corona_startx1+corona_width <= humanx+human_width:
            corona_starty1 = display_height+1
            print("xy crossover")
            score -= 1
            deletehealth()
            showhealth()
            j = len(hblist)
            if 0 == j:
                crash()
                running = False
                time.sleep(3)
    if humany <= corona_starty2:
        if corona_startx2 >= humanx and corona_startx2 <= humanx + human_width or corona_startx2+corona_width >= humanx and corona_startx2+corona_width <= humanx+human_width:
            corona_starty2 = display_height+1
            print("xy crossover")
            score -= 1
            deletehealth()
            showhealth()
            j = len(hblist)
            if 0 == j:
                crash()
                running = False
                time.sleep(3)
    if humany <= corona_starty3:
        if corona_startx3 >= humanx and corona_startx3 <= humanx + human_width or corona_startx3+corona_width >= humanx and corona_startx3+corona_width <= humanx+human_width:
            corona_starty3 = display_height+1
            print("xy crossover")
            score -= 1
            deletehealth()
            showhealth()
            j = len(hblist)
            if 0 == j:
                crash()
                running = False
                time.sleep(3)
    pygame.display.update()
    clock.tick(120)

quit()
pygame.quit()
