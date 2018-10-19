from os.path import splitext
import pygame
from pygame.locals import*
import Lexaar_global_variable
from win32api import GetSystemMetrics
import win32api
import win32con
import time
import os.path
import os
import importlib

class MainClass :

    def __init__(self, gameName, gamestate, colliderList = list()):
        """A little game engine, you are using the 2D version of that engine"""

        self.colliderList = colliderList

        self.gameName = gameName

        self.gamestate = gamestate

        pygame.display.init()
        pygame.display.set_caption(gameName)

        self.maintenir_process = True
        self.bckg = 0
        self.lib = None
        self.level_event_func_name = None

    def setName(self, newName) :
        """Set game's name"""
        pygame.display.set_caption(newName)

    def eventLaunch(self) :
        """Main events, YOU MUST CALL THAT FUNCTION IN YOUR MAINLOOP"""
        pygame.display.flip()

        if(self.bckg != 0) :
            Lexaar_global_variable.scr.blit(self.bckg, (0,0))
            
        if(self.gamestate == "devel"):
            Lexaar_global_variable.console.blitMessage()
        for event in pygame.event.get():
            if event.type == QUIT :
                self.maintenir_process = False

            if event.type == KEYDOWN and event.key == K_ESCAPE :
                self.maintenir_process = False
                pygame.quit()
        if len(Lexaar_global_variable.WithoutEvent) != 0 :
            for i in Lexaar_global_variable.WithoutEvent :
                Lexaar_global_variable.scr.blit(i[0], (i[1], i[2]))

    def backGroundImage(self, pathToImage) :
        """Set background image"""
        self.bckg = pygame.image.load(pathToImage).convert_alpha()
        self.bckg = pygame.transform.scale(self.bckg, (GetSystemMetrics(0),GetSystemMetrics(1)))
        Lexaar_global_variable.scr.blit(self.bckg, (0,0))

    def isKeyPressed(self, key) :
        """Return True if chosen key is pressed"""
        if(win32api.GetAsyncKeyState(key) != 0) :
            return True
        
        else :
            return False

    def delay(self, milli_sec) :
        """Wait..."""
        milli_start = int(round(time.time() * 1000))

        while int(round(time.time() * 1000)) - milli_start != milli_sec :
            #NOTHING
            print(milli_start - int(round(time.time() * 1000)))

        return milli_sec

    def isBetween(self, valMin, valToCheck, valMax) :
        """Check if a number is between two other numbers"""
        if(valToCheck > valMin) :
            if(valToCheck < valMax) :
                return True
            else :
                return False
        else :
            return False

    def setShowMouseCursor(self, value) :
        """Show or not mouse cursor"""
        pygame.mouse.set_visible(value)

    def open_level(self, path) :
        """Open level defined by a .LEXLVL level"""

        self.level_event_func_name = None
        self.lib = None

        Lexaar_global_variable.AudioMusics = []
        Lexaar_global_variable.AudioSound = []
        Lexaar_global_variable.WithoutEvent = []

        #print(self.level_event_func_name, " ", self.lib)

        lvl = open(path, 'r')
        lines = lvl.readlines()

        cutted_lines = list()

        for i in range(len(lines)) :
            lines[i] = lines[i].replace("\n", "")

        for i in lines :
            cutted_lines.append(i.split(":"))
        
        for commands in cutted_lines :
            if commands[0] == "background" :
                self.backGroundImage(commands[1])

            if commands[0] == "linked-file" :
                arg = commands[1]
                self.lib = importlib.import_module(arg)

            if commands[0] == "event-func" :
                self.level_event_func_name = commands[1]

        #print(self.level_event_func_name, " ", self.lib)

        lvl.close()

    def levelEvent(self) :
        """Maintain level event"""
        try :
            exec("self.lib." + self.level_event_func_name)
        except NameError:
            print("Invalid event function name")
            pass
                


class LFile(MainClass) :
            
    def __init__(self, filePath) :
        """Engine's file gestion system"""
        self.filePath = filePath

        if os.path.exists(self.filePath) != True :
            raise FileExistsError("File \"" + self.filePath + "\" does no exist.")

        self.extension = splitext(self.filePath)
        self.extension[1].lower()

        Lexaar_global_variable.console.sysPrint(self.extension[1], (255,0,0))

    def checkExtension(self, extension) :
        """Check file extension"""
        if extension == self.extension[1] :
            return True
        else :
            return False

    def getFile(self) :
        """Get file path, it return a string"""
        return self.filePath