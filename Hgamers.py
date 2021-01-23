import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((800,600))
img = pygame.image.load("human.png")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pygame.display.set_caption('avoid covid')
human_width = 100
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
