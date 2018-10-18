import Lexaar
from Lexaar_global_variable import*
import pygame
from pygame.locals import*
import win32gui

class Button(Lexaar.MainClass) :
    def __init__(self, posX, posY, normal, hovered, pressed, command) :
        """Just a normal button"""
        self.posX = posX
        self.posY = posY

        self.imgNormal = pygame.image.load(normal).convert_alpha()
        self.posButton = self.imgNormal.get_rect()
        self.imgPressed = pygame.image.load(pressed).convert_alpha()
        self.imgHovered = pygame.image.load(hovered).convert_alpha()

        self.images = (self.imgNormal, self.imgPressed, self.imgHovered)

        self.posButton.x = self.posX
        self.posButton.y = self.posY

        self.blitImage = self.imgNormal

        self.command = command

        self.buttonSize = self.imgNormal.get_size()

    def resize(self, scale = None, sizeX = None, sizeY = None) :
        buttonNowSize = self.buttonSize
        scale = scale
        sizeX = sizeX
        sizeY = sizeY

        if scale != None :
            scale = (int(buttonNowSize[0]*scale/100), int(buttonNowSize[1]*scale/100))

            self.imgHovered = pygame.transform.scale(self.imgHovered, (scale[0], scale[1]))
            self.imgNormal = pygame.transform.scale(self.imgNormal, (scale[0], scale[1]))
            self.imgPressed = pygame.transform.scale(self.imgPressed, (scale[0], scale[1]))

            self.posButton = self.imgNormal.get_rect()
            self.posButton.x = self.posX
            self.posButton.y = self.posY

    def eventLaunch(self) :
        point = win32gui.GetCursorPos()
        if self.posButton.collidepoint(point) :
            if Lexaar.MainClass.isKeyPressed(self, 0x01) :
                self.blitImage = self.imgPressed
                self.command()
            else :
                self.blitImage = self.imgHovered
        else :
            self.blitImage = self.imgNormal

        scr.blit(self.blitImage, self.posButton)


#Entry class will be developped later
class Entry(Lexaar.MainClass) :
    """Text Entry"""
    def __init__(self, posX, posY, bckg, sizeX = None, sizeY = None) :
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.bckg = pygame.image.load(bckg).convert_alpha()

        if self.sizeX != None and self.sizeY != None:
            self.bckg = pygame.transform.scale(self.bckg, (self.sizeX, self.sizeY))

        self.selfPos = self.bckg.get_rect()
        self.selfPos.x = self.posX
        self.selfPos.y = self.posY

    def eventLaunch(self) :
        if self.selfPos.collidepoint(win32gui.GetCursorPos()) :
            pass

        scr.blit(self.bckg, self.selfPos)

class Text(Lexaar.MainClass) :
    def __init__(self, text, posX, posY, font, size, textColor = (255,255,255),**kwars) :
        pygame.font.init()

        self.text = str(text)
        self.pos = (posX, posY)
        self.size = size

        self.f = open(font, 'r')
        self.font = pygame.font.Font(font, self.size)
        self.color = textColor

        self.renderText = self.font.render(self.text, 1, self.color)

    def eventLaunch(self) :
        scr.blit(self.renderText, (self.pos[0],self.pos[1]))