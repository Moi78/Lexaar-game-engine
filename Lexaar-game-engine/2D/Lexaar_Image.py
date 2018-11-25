import Lexaar
import Lexaar_global_variable
import pygame
from pygame.locals import*
import time

class image(Lexaar.MainClass) :
    def __init__(self, file, x, y) :
        """Image display"""
        self.imagePath = Lexaar.LFile(file)
        self.imageX = x
        self.imageY = y
        self.image = pygame.image.load(self.imagePath.getFile()).convert_alpha()

    def setImage(self, new_image) :
        self.image = pygame.image.load(new_image)

    def eventLaunch(self) :
        Lexaar_global_variable.scr.blit(self.image, (self.imageX,self.imageY))

    def getImage(self) :
        return self.image

class Image_Animation(Lexaar.MainClass) :
    def __init__(self, files = tuple(), framerate = 30, x = 0, y = 0) :
        self.files = files

        if type(self.files) is not tuple :
            raise TypeError("\"files\" argument must be a tuple containing all images path.")

        self.framerate = framerate
        self.index = 1
        self.maxIndex = len(self.files)
        
        self.x = x
        self.y = y

        self.currentImage = image(self.files[0], self.x, self.y)
        
        self.timeStart = int(time.time()*1000)
        self.isPaused = False

    def nextFrame(self) :
        if self.index < self.maxIndex :
            self.currentImage.setImage(self.files[self.index])
            self.index += 1
        else :
            self.index = 0

    def pause(self) :
        self.isPaused = True

    def unpause(self) :
        self.isPaused = False

    def eventLaunch(self) :
        stoptime = int(time.time()*1000)
        frameTime = int((1/self.framerate)*1000)
        if stoptime >= self.timeStart + frameTime :
            if not self.isPaused :
                self.nextFrame()
            self.timeStart = int(time.time()*1000)
        else :
            pass

        Lexaar_global_variable.scr.blit(self.currentImage.getImage(), (self.x, self.y))