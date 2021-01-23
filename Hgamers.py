import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
img = pygame.image.load("human.png")
running = True
def human(x,y):
    game.Display.blit(img, (x, y))
while running == True:
    for Event in pygame.event.get():
      if Event.type == pygame.QUIT:
         running = False
quit()
pygame.quit()
