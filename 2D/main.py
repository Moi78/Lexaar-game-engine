import Lexaar
from Lexaar_2D_Character import*
from Lexaar_Trigger import*
import Lexaar_Audio
import Lexaar_Image
import Lexaar_HUD

import test_mainPerso

test = Lexaar.MainClass("Hello world", "devel")

test.backGroundImage("AssetsTest/Fond.png")

test.setShowMouseCursor(True)

perso = test_mainPerso.MainChara()

audioTest = Lexaar_Audio.Sound("AssetsTest/Test.wav", 0.1)

audioTest2 = Lexaar_Audio.Music("AssetsTest/Test2.wav", True)
audioTest2.play(0.1)

button = Lexaar_HUD.Button(1600,105, "AssetsTest/BNormal.png", "AssetsTest/BHovered.png", "AssetsTest/BPressed.png", lambda:perso.teleport(0,0))
button.resize(50)

txt = Lexaar_HUD.Text("Teleport to 0,0", "AssetsTest/FONT.ttf",1600, 90, 20, (0,0,0))

temoin = True

file = Lexaar.LFile("AssetsTest/Fond.png")
while temoin == True :
    test.eventLaunch()
    button.eventLaunch()
    txt.eventLaunch()
    perso.eventLaunch()