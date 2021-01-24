import random
import time
import pygame

print('Hello! Welcome to Avoid COVID by the HGamers!')
#time.sleep(5)
print('In this game, you must avoid COVID by using the Arrow keys.\n' 'If covid hits you, lose 2 health. Every single wave you survive, you get 1 extra health.\n', 'If you survive 7(by default) waves, you will survive COVID, and you win the game.')
#time.sleep(10)
print('On a more serious note, here are some quick facts about COVID.')
fact1 = ('COVID-19 is a type of coronavirus, a deadly lung disease')
fact2 = ('The most simple and most effective way to avoid COVID-19 in real life is wearing masks and using safety gloves in unsanitary areas')
fact3 = ('Hand sanitizers are very helpful during this time, giving a quick way to make sure your hands are clean.\n' 'Alternativley, washing your hands for 20 seconds is effective.')
fact4 = ('Symptoms of COVID-19 are as follows- chills, coughing, sneezing, breathing issues, fatigue and headaches.')
#time.sleep(5)
print(fact1)
#time.sleep(5)
print(fact2)
#time.sleep(10)
print(fact3)
#time.sleep(10)
print(fact4)
time.sleep(5)

pygame.init()
screen = pygame.display.set_mode((800,600))
img = pygame.image.load("testimg.png")
cimg1 = pygame.image.load("cvd.png")
scr = pygame.image.load("scr_final.png")

humany = 500
humanx = random.randint(100, 600)

target = 5
sleeptime = 0.2



#for health bars
hblist = []
light_green = (0,255,0) 
dark_green = (0,128,0)

#Function to add health bar

def addhealth():
    i = len(hblist)
    if i % 2 == 0:
        hblist.append(pygame.draw.rect(screen, light_green, pygame.Rect(775, 100+10*i, 10, 10)))
    else:
        hblist.append(pygame.draw.rect(screen, dark_green, pygame.Rect(775, 100+10*i, 10, 10)))

#Function to delete health bar

def deletehealth():
# fill the region where current rectangle is drawn with BG colour; not entire screen
    screen.fill((0,0,0),(775,100,10,300))
    j = len(hblist)

    del hblist[j-1]

    for m in range(0,j-1):
        if m % 2 == 0:
            pygame.draw.rect(screen, light_green, pygame.Rect(775, 100+10*m, 10, 10))
        else:
            pygame.draw.rect(screen, dark_green, pygame.Rect(775, 100+10*m, 10, 10))



def imginsert(x_human,y_human):
        screen.blit(img, (x_human,y_human))

def cimginsert(x_human,y_human):
    screen.blit(cimg1, (x_human,y_human))


def covid(x_human,y_human):
    imginsert(x_human,y_human)
    running = True
    no_loop = 0
    move_right = False
    move_left = False
    hit = False
    no_hit = 0
    countsuccess = 0
    win = False

    for h in range(4):
        addhealth()

    while running == True:
        cy = 0
        cy1 = 300
        cy2 = 400
        cx = x_human
        cx1 = x_human
        cx2 = x_human
        cimginsert(x_human, cy)
        pygame.display.update()

        img1 = False
        img2 = False
       
        for i in range(121):
            
            for event in pygame.event.get():               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move_left = True
                    elif event.key == pygame.K_RIGHT:
                        move_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        move_left = False
                    elif event.key == pygame.K_RIGHT:
                        move_right = False
                    
            if move_left:
                if x_human >= 25:
                    x_human = x_human -15*(no_loop+1)/4
                    screen.fill((0,0,0),(x_human+15*(no_loop+1)/4,y_human,100,100))
            if move_right:
                if x_human <= 600:
                    x_human = x_human + 15*(no_loop+1)/4
                    screen.fill((0,0,0),(x_human-15*(no_loop+1)/4,y_human,100,100))
                    
            imginsert(x_human, y_human)
            pygame.display.update()

            screen.fill((0,0,0), (cx,cy,25,20))
            screen.fill((0,0,0), (cx1,cy1,25,20))
            screen.fill((0,0,0), (cx2,cy2,25,20))
            
            cy = cy + 5
            cimginsert(cx, cy)
            
            if img1 == True:
                cy1 = cy1 + 5
                cimginsert(cx1, cy1)

            if img2 == True:
                cy2 = cy2 + 5
                cimginsert(cx2, cy2)
            
            pygame.display.update()
            time.sleep(sleeptime/(no_loop+1))

            if i == 40:
                cx1 = x_human
                cimginsert(cx1,cy1)
                img1 = True
                

            if i == 80:
                cx2 = x_human
                cimginsert(cx2,cy2)
                img2 = True

# Human: Width = 100; Height = 72;     COVID: Width = 25; Height = 16; Social Distance gap = 5 in width         
            if ((cx-x_human < 105 and cx-x_human > -30)and (cy-y_human <= 72 and cy-y_human >= -16)) or ((cx1-x_human < 105 and cx1-x_human > -30) and (cy1-y_human <= 72 and cy1-y_human >= -16)) or ((cx2-x_human < 105 and cx2-x_human > -30) and (cy2-y_human <= 72 and cy2-y_human >= -16)):
                hit = True

            else:
                screen.fill((0,0,0),(cx,600,25,20))

# End Outer For Loop for downward movement of Virus

        no_loop = no_loop+1
        
        if hit:
            if len(hblist)>2:
                for d in range(2):
                    deletehealth()
                    hit=False
            else:
                running = False
        else:
            addhealth()
            countsuccess = countsuccess+1
            print("Success Achieved = ",countsuccess)
            if countsuccess > target:
                win = True
                running = False

    if win == False:
        print("Sorry you are infected with COVID; please take 14 days rest & get well soon")
    elif win == True:
        print("Well Done! You have taken necessary safety precautions against COVID and beaten the virus.\n","You can now take the vaccine.")
        screen.fill((0,0,0))
        screen.blit(scr, (50,75))
        pygame.display.update()
        time.sleep(5)

    pygame.quit()
    quit()

covid(humanx,humany)

             
