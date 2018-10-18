# -*- coding: utf-8 -*-

import Lexaar
from pygame import*
from pygame.locals import*
from Lexaar_global_variable import*

class Trigger_2D(Lexaar.MainClass) :
    def __init__(self, posX, posY, width, height) :
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

    def isCollidingWith(self, collider) :
        topLeft = self.trigger["topLeft"]
        topRight = self.trigger["topRight"]
        bottomLeft = self.trigger["bottomLeft"]

        rangeX = (topLeft[0], topRight[0])
        rangeY = (topLeft[1], bottomLeft[1])

        if(Lexaar.MainClass.isBetween(self, rangeX[0], collider.BX, rangeX[1])) :
            if(Lexaar.MainClass.isBetween(self, rangeY[0], collider.BY, rangeY[1])) :
                return True
            
        if(Lexaar.MainClass.isBetween(self, rangeX[0], collider.HP[0], rangeX[1])) :
            if(Lexaar.MainClass.isBetween(self, rangeY[0], collider.HP[1], rangeY[1])) :
                return True
        if(Lexaar.MainClass.isBetween(self, rangeX[0], collider.LLP[0], rangeX[1])) :
            if(Lexaar.MainClass.isBetween(self, rangeY[0], collider.LLP[1], rangeY[1])) :
                return True
        if(Lexaar.MainClass.isBetween(self, rangeX[0], collider.LRP[0], rangeX[1])) :
            if(Lexaar.MainClass.isBetween(self, rangeY[0], collider.LRP[1], rangeY[1])) :
                return True
        return False