import Lexaar
from Lexaar_2D_Character import*
from Lexaar_global_variable import*

class MainChara(Character_2D) :
    def __init__(self) :
        Character_2D.__init__(self, "AssetsTest/DOWN.png", 652, 56, Up_Arrow, Down_Arrow, Right_Arrow, Left_Arrow, 5, "AssetsTest/UP.png", "AssetsTest/LEFT.png", "AssetsTest/RIGHT.png")

    def eventLaunch(self) :
        Character_2D.eventLaunch(self)