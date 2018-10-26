import Lexaar_global_variable
import test_mainPerso
import Lexaar_HUD
import Lexaar_Physic_Engine
import Lexaar
import Lexaar_Image

perso = test_mainPerso.MainChara()
button = Lexaar_HUD.Button(0,0,"AssetsTest/BNormal.png", "AssetsTest/BHovered.png", "AssetsTest/BPressed.png", lambda : perso.teleport(500,900))
button.resize(50)

block1 = Lexaar_Physic_Engine.Body_Rectangle(23, 56, 254, 236, True)

txtTest = Lexaar_HUD.Text("Test", 900,500,"font.ttf", 50,(76,255,224))

testAnimation = Lexaar_Image.Image_Animation(("AssetsTest/UP.png", "AssetsTest/RIGHT.png", "AssetsTest/LEFT.png", "AssetsTest/DOWN.png"), 60, 30,1200)

def eventLaunch() :
    if Lexaar.MainClass.isKeyPressed(1, ord('H')) :
        txtTest.setText("Coucou")
    perso.eventLaunch()
    button.eventLaunch()
    block1.eventLaunch()
    txtTest.eventLaunch()

def eventLaunch_core2() :
    testAnimation.eventLaunch()