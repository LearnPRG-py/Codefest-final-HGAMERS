import pygame
import random
pygame.init()
humanx = 400
humany = 500
human_width = 100
screen = pygame.display.set_mode((800,600))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
img = pygame.image.load("human.png")
running = True
def human(x,y):
    screen.blit(img, (x, y))
while running == True:
    human(humanx, humany)
    for Event in pygame.event.get():
      if Event.type == pygame.QUIT:
         running = False

quit()
pygame.quit()
