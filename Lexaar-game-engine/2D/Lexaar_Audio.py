import Lexaar
import Lexaar_global_variable
import Lexaar_Except
import pygame
from pygame.locals import*


class Music(Lexaar.MainClass) :
    def __init__(self, AudioWAVFile, isLooping) :
        """Class to play music, /!\\ it takes only .wav files"""
        pygame.mixer.init()

        self.AudioWAVFile = Lexaar.LFile(AudioWAVFile)
        self.isLooping = isLooping

        if self.AudioWAVFile.checkExtension(".wav") :
            pass
        else :
            raise Lexaar_Except.FileExtensionError("File must be an \"WAV\" audio file.")

        self.wav = pygame.mixer.Sound(self.AudioWAVFile.getFile())
        Lexaar_global_variable.AudioMusics.append(self.wav)

    def play(self, volume = 1.0) :
        """Play music with specified volume"""
        self.wav.set_volume(volume)

        if self.isLooping :
            #pygame.mixer.Sound.play(loops = -1)
            self.wav.play(loops = -1)
        else :
            self.wav.play()

    def stop(self) :
        """Stop Music"""
        self.wav.stop()

    def set_volume(self, new_volume) :
        """Set music volume"""
        self.wav.set_volume(new_volume)

class Sound(Lexaar.MainClass) :
    def __init__(self, AudioWAVFile, volume) :
        """Class to play a sound with specified volume, /!\\ it takes only .wav files and you cannot make sound looping"""
        pygame.mixer.init()

        self.AudioWAVFile = Lexaar.LFile(AudioWAVFile)

        if self.AudioWAVFile.checkExtension(".wav") :
            pass
        else :
            raise Lexaar_Except.FileExtensionError("File must be an \"WAV\" audio file.")

        self.wav = pygame.mixer.Sound(self.AudioWAVFile.getFile())
        self.wav.set_volume(volume)
        Lexaar_global_variable.AudioSound.append(self.wav)

    def play(self) :
        """Play sound"""
        self.wav.play()

    def stop(self) :
        """Stop Sound"""
        self.wav.stop()

    def set_volume(self, new_volume) :
        """Set sound volume"""
        self.wav.set_volume(new_volume)