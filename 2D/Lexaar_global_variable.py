import pygame
from pygame.locals import*
from win32api import*
import Lexaar_Console

scr = pygame.display.set_mode((GetSystemMetrics(0),GetSystemMetrics(1)), FULLSCREEN)

scrSize = (GetSystemMetrics(0), GetSystemMetrics(1))

colliders = list()

triggers = list()


#Direction Keyword
UP = 'UP'
DWN = 'DOWN'
RGHT = 'RIGHT'
LFT = 'LEFT'

direction = 'UP'

#Console
console = Lexaar_Console.console()

#AudioTypes
MUSIC = 1
AMBIENT = 2
PLAYED_ONCE = 3

#All musics
AudioMusics = []
AudioSound = []

#Thing to blit() without events
WithoutEvent = []

#Special keys
Space = 32
Up_Arrow = 38
Down_Arrow = 40
Left_Arrow = 37
Right_Arrow = 39