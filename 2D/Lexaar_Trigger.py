import Lexaar
from pygame import*
from pygame.locals import*
from Lexaar_global_variable import*

class Trigger_2D(Lexaar.MainClass) :
    def __init__(self, posX, posY, width, height, debugDraw) :
        """Trigger detect movables objects in a defined zone"""
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height

        self.trigger = dict()

        self.trigger["topLeft"] = (self.posX,self.posY)
        self.trigger["topRight"] = (self.posX + self.width, self.posY)
        self.trigger["bottomRight"] = (self.posX + self.width, self.posY + self.height)
        self.trigger["bottomLeft"] = (self.posX, self.posY + self.height)

        triggers.append(self.trigger)

        self.debugDraw = debugDraw

    def isCollidingWith(self, collider) :
        selfRect = pygame.Rect((self.posX, self.posY),(self.width, self.height))

        if selfRect.colliderect(collider) :
            return True
        else :
            return False

    def eventLaunch(self) :
        pygame.draw.rect(scr, (255,0,255), ((self.posX, self.posY),(self.width, self.height)), 5)