import Lexaar_global_variable
import test_mainPerso
import Lexaar_HUD

perso = test_mainPerso.MainChara()
button = Lexaar_HUD.Button(0,0,"AssetsTest/BNormal.png", "AssetsTest/BHovered.png", "AssetsTest/BPressed.png", lambda : perso.teleport(500,900))
button.resize(50)

def eventLaunch() :
    perso.eventLaunch()
    button.eventLaunch()