# -*- coding: utf-8 -*-

import Lexaar
import Lexaar_2D_Character
import Lexaar_global_variable
import Lexaar
from pygame import*
from pygame.locals import*

class PlayerMapCollision() :
    def __init__(self, x, y, h, w) :
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.collZone = Rect(self.x, self.y, self.w, self.h)

    def isInsideVolume(self, posX, PosY, Width, Height) :
        tempRect = Rect(posX, PosY, Width, Height)
        return self.collZone.colliderect(tempRect)
    def inVolumeValX(self, posX) :
        bx = self.x
        diffX = (bx + self.w) - posX
        return diffX
    
    def inVolumeValXMinus(self, posX) :
        bx = self.x
        diffX = bx - posX
        return diffX

    def collideAndGetBack(self, fromW, chara) :
        if(self.isInsideVolume( chara.BX, chara.BY, chara.posPerso.w, chara.posPerso.h)) :
            if(fromW == '-X') :
                chara.posPerso.x -= self.inVolumeValXMinus(chara.LRP)
            if(fromW == 'X') :
                chara.posPerso.x -= self.inVolumeValX(chara.BX)