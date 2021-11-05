#import
import pygame, sys
from pygame.locals import *

#init pygame module
pygame.init()

#assign fps
FPS = 30
clock = pygame.time.Clock()

#colors
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

#surface 300x300 pixel display
Width= 300
Height = 300
Displaysurf = pygame.display.set_mode((Width,Height))
Displaysurf.fill(white)
pygame.display.set_caption("my drawing")

#create lines and shapes
pygame.draw.line(Displaysurf,blue, (0,0),(300,300),13)
pygame.draw.line(Displaysurf,red, (300,0),(0,300),13)
pygame.draw.line(Displaysurf,green, (150,0),(150,300),10)
pygame.draw.line(Displaysurf,black, (0,150),(300, 150),10)
pygame.draw.circle(Displaysurf,white,(150,150),60)
pygame.draw.rect(Displaysurf, red,(88,88,125,125))
pygame.draw.circle(Displaysurf,white,(150,150),60)


#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #refresh

    pygame.display.update()
    clock.tick(FPS)