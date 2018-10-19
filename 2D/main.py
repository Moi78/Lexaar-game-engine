import Lexaar
import test_mainPerso
import Lexaar_global_variable

MainGame = Lexaar.MainClass("Hello World", "devel")
MainGame.open_level("AssetsTest/Level2.LEXLVL")

print(Lexaar_global_variable.WithoutEvent)

MainGame.open_level("AssetsTest/Level1.LEXLVL")

print(Lexaar_global_variable.WithoutEvent)

while True :
    MainGame.eventLaunch()
    MainGame.levelEvent()    