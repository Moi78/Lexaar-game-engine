import Lexaar
import test_mainPerso

MainGame = Lexaar.MainClass("Hello World", "devel")
MainGame.open_level("AssetsTest/Level1.LEXLVL")

while True :
    MainGame.eventLaunch()