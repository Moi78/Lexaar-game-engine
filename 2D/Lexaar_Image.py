import Lexaar
import Lexaar_global_variable
import pygame
from pygame.locals import*

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

    def eventLaunch(self) :
        pygame.time.delay(int((1/self.framerate)*1000))

        if self.index < self.maxIndex :
            self.currentImage.setImage(self.files[self.index])
            self.index += 1
        else :
            self.index = 0