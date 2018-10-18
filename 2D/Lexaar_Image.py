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

        Lexaar_global_variable.WithoutEvent.append((self.image, self.imageX, self.imageY))