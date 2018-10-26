import Lexaar
import pygame
from pygame.locals import *
import Lexaar_global_variable
import Lexaar_Trigger

class Body_Rectangle(Lexaar_Trigger.Trigger_2D) :
    def __init__(self, bx, by, height, width, debugDraw = False) :
        self.topl = (bx, by)
        self.topr = (bx + width, by)
        self.bottoml = (bx, by + height)
        self.bottomr = (bx + width, by + height)

        self.width = width
        self.height = height

        self.DrawHitbox = debugDraw

    def eventLaunch(self) :
        if self.DrawHitbox :
            pygame.draw.rect(Lexaar_global_variable.scr, (255,0,255), (self.topl, (self.width, self.height)), 5)