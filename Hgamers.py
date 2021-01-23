import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
img = pygame.image.open("human.png")
human_width = 100
<<<<<<< HEAD
gameDisplay = pygame.display.set_mode((display))
=======
running = True
def human(x,y):
    game.Display.blit(img, (x, y))
while running == True:
    if event.type == pygame.quit():
        running = False
<<<<<<< HEAD
=======
while running == true:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False
>>>>>>> 8917182ff47b0ed33802f6bf3df1162f1e5050cc
quit()
pygame.quit()
>>>>>>> bbac26c65e0e97ba77d76d1c19b7af5bcf7dc172
