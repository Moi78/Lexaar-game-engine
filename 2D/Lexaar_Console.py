# -*- coding: utf-8 -*-

import Lexaar_global_variable
from pygame import*

class console() :
    def __init__(self) :
        font.init()

        self.text_color = (255,255,255)
        self.console_font = font.SysFont("Consolas", 15)
        self.console_message = self.console_font.render("Console succefully initalized !!! YAY", 1, self.text_color)

        self.messages = list()

        self.messagesY = [5]
        self.actualY = 15
        self.index = 0
    
    def blitMessage(self) :
        self.actualY = 10
        self.index = 0
        for i in self.messages :
            Lexaar_global_variable.scr.blit(i, (10, self.messagesY[self.index]))
            self.messagesY.append(self.actualY)
            self.actualY += 15
            self.index += 1

    def sysPrint(self, message, color = (255,255,255)) :
        """Print message to the screen"""
        self.text_color = color
        self.console_message = self.console_font.render(str(message), 1, self.text_color)

        self.messages.append(self.console_message)