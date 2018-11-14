import Lexaar
import pygame
from pygame.locals import *
import Lexaar_global_variable
import Lexaar_Trigger

class Body_Rectangle(Lexaar_Trigger.Trigger_2D) :
    def __init__(self, bx, by, height, width, debugDraw = False) :
        Lexaar_Trigger.Trigger_2D.__init__(self, bx, by, height, width, debugDraw)
        self.topl = (bx, by)
        self.topr = (bx + width, by)

        self.width = width
        self.height = height

        self.DrawHitbox = debugDraw

        Lexaar_global_variable.colliders_Passive.append((self.topl, self.width, self.height))

    def eventLaunch(self) :
        Lexaar_Trigger.Trigger_2D.eventLaunch(self)
        #print(Lexaar_global_variable.colliders_Active[0].getPosition())
        if Lexaar_Trigger.Trigger_2D.isCollidingWith(self, Lexaar_global_variable.colliders_Active[0].getCollision()) :
            if Lexaar.MainClass.isBetween(self, self.topl[0], Lexaar_global_variable.colliders_Active[0].getPosition()[0], self.topl[0] + self.width) and Lexaar.MainClass.isBetween(self, self.topl[1], Lexaar_global_variable.colliders_Active[0].getPosition()[1], self.topl[1] + self.height) :
                print("Collide droite")

class class_rectangle() :
    def __init__(self,bx, by, height, width, baseClass, debugDraw = False) :
        self.baseClass = baseClass

        self.collision = (baseClass.BX, baseClass.BY, width, height)

        self.wh = (width, height)

        self.pos = (bx, by)

        self.debugDraw = debugDraw

        Lexaar_global_variable.colliders_Active.append(self)
        self.index = len(Lexaar_global_variable.colliders_Active) - 1

    def getCollision(self) :
        return pygame.Rect(self.collision[0], self.collision[1], self.collision[2], self.collision[3])

    def getPosition(self) :
        return self.pos

    def eventLaunch(self) :
        if self.debugDraw :
            pygame.draw.rect(Lexaar_global_variable.scr, (255,0,255), ((self.collision[0], self.collision[1]), (self.collision[2], self.collision[3])), 5)
        self.collision = (self.baseClass.BX, self.baseClass.BY, self.wh[0], self.wh[1])
        self.pos = (self.baseClass.BX, self.baseClass.BY)