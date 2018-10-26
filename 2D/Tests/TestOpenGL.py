import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

pygame.display.init()
pygame.display.set_mode((800,600))

while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            quit()

    