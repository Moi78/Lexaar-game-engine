import Lexaar
import pygame
from pygame.locals import*
from Lexaar_global_variable import*
import Lexaar_PlayerMapCollisions
import win32api
import win32con
from threading import Thread

class Character_2D(Lexaar_PlayerMapCollisions.PlayerMapCollision, Lexaar.MainClass) :
    def __init__(self, charaImagePath, spawnx, spawny, key_moveUP = "W", key_moveDOWN = "S", key_moveRIGHT = "D", key_moveLEFT = "A", speed = 5, charaImagePathUP = "", charaImagePathLeft = "", charaImagePathRight = "") :       
        """Class to create a character with inputs some others methods"""
        
        self.key_moveUP = key_moveUP
        self.key_moveDOWN = key_moveDOWN
        self.key_moveLEFT = key_moveLEFT
        self.key_moveRIGHT = key_moveRIGHT

        self.walking = False

        self.charaImage = pygame.image.load(charaImagePath).convert_alpha()

        self.ImgUP = charaImagePathUP
        self.ImgLeft = charaImagePathLeft
        self.ImgRight = charaImagePathRight
        self.ImgDown = charaImagePath

        self.imgChangeOrientationUP = False
        self.imgChangeOrientationLFT = False
        self.imgChangeOrientationRGHT = False

        if(charaImagePathUP != "") :
            self.imgChangeOrientationUP = True
        if(charaImagePathLeft != "") :
            self.imgChangeOrientationLFT = True
        if(charaImagePathRight != "") :
            self.imgChangeOrientationRGHT = True


        self.speed = speed
        
        self.posPerso = self.charaImage.get_rect()

        self.posPerso.x = spawnx
        self.posPerso.y = spawny

        self.BX = self.posPerso.x
        self.BY = self.posPerso.y
        self.HP = self.posPerso.topright
        self.LLP = self.posPerso.bottomleft
        self.LRP = self.posPerso.bottomright

        self.testingX = self.posPerso.x
        self.testingY = self.posPerso.y

        scr.blit(self.charaImage, self.posPerso)
        self.rect = 0

        self.hurtingedge = False

    def eventLaunch(self) :
        """Event system"""
        if(win32api.GetAsyncKeyState(self.key_moveUP) != 0) :
            self.moveUD(-1)
            self.recomputeXandY()

            if(self.imgChangeOrientationUP == True) :
                self.charaImage = pygame.image.load(self.ImgUP).convert_alpha()
            
        if(win32api.GetAsyncKeyState(self.key_moveDOWN) != 0) :
            self.moveUD(1)
            self.recomputeXandY()

            self.charaImage = pygame.image.load(self.ImgDown).convert_alpha()

        if(win32api.GetAsyncKeyState(self.key_moveLEFT) != 0) :
            self.moveRL(-1)
            self.recomputeXandY()
            
            if(self.imgChangeOrientationLFT == True) :
                self.charaImage = pygame.image.load(self.ImgLeft).convert_alpha()

        if(win32api.GetAsyncKeyState(self.key_moveRIGHT) != 0) :
            self.moveRL(1)
            self.recomputeXandY()
            
            if(self.imgChangeOrientationRGHT) :
                self.charaImage = pygame.image.load(self.ImgRight).convert_alpha()

        scr.blit(self.charaImage, self.posPerso)

    def setSpeed(self, speed) :
        """Set the speed of your character"""
        self.speed = speed

    def teleport(self, posX, posY) :
        """Teleport your character"""
        self.posPerso.x = posX
        self.posPerso.y = posY
        scr.blit(self.charaImage, self.posPerso)

    def getPosX(self) :
        """Get X position of the character"""
        return self.posPerso.x

    def getPosY(self) :
        """Get Y position of the character"""
        return self.posPerso.y

    def isColliding(self, collider) :
        """Get your character is colliding (In dev)"""
        return self.posPerso.colliderect(collider)

    def recomputeXandY(self) :
        """Reload hitbox's position of the character"""
        self.BX = self.posPerso.x
        self.BY = self.posPerso.y
        self.HP = self.posPerso.topright
        self.LLP = self.posPerso.bottomleft
        self.LRP = self.posPerso.bottomright

    def moveRL(self, multi) :
        """Move Right-Left (mutlti arg must be between -1 and 1)"""
        if(Lexaar.MainClass.isBetween(self, -1, multi, -1)) :
            raise ValueError("\"multi\" parameter must be between 1 and -1")

        if(self.BX + self.speed > 0) :

            if(self.LRP[0] + self.speed < scrSize[0]) :

                self.posPerso.x += self.speed * multi
                if(self.LRP[0] + self.speed < scrSize[0] + 15) :
                    self.hurtingedge = False
            else :
                self.teleport(scrSize[0] - (self.posPerso.w + 10), self.BY)
                self.hurtingedge = True
        else :

            self.teleport(0, self.BY)
            self.hurtingedge = True

    def moveUD(self, multi) :
        """Move Up-Down (multi arg must be between -1 and 1)"""
        if(Lexaar.MainClass.isBetween(self, -1, multi, -1)) :
            raise ValueError("\"multi\" parameter must be between 1 and -1")

        if(self.BY + self.speed > 0) :

            if(self.LLP[1] + self.speed < scrSize[1]) :
                self.posPerso.y += self.speed * multi
                if(self.LLP[1] + self.speed < scrSize[1] - 15) :
                    self.hurtingedge = False

                if(self.BY + self.speed < 15) :
                    self.hurtingedge = True
                    console.sysPrint(self.hurtingedge, (255,0,255))
            else :
                self.teleport(self.LLP[0], scrSize[1] - (self.posPerso.h + 10))
                self.hurtingedge = True
        else :

            self.teleport(self.BX, 0)
            self.hurtingedge = True

    def getPosition(self) :
        """Get X and Y position of the character"""
        position = (self.BX, self.BY)
        return position

    def hurtingEdge(self) :
        """If the character touch the edge of the screen it return True else it return False"""
        return self.hurtingedge