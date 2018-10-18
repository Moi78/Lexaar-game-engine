import Lexaar
import Lexaar_global_variable
import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

class Camera(Lexaar.MainClass) :
    def __init__(self, fov, near, far, pos = tuple()) :
        glClearColor(0,0,0,0)

        # sets the projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(fov, (Lexaar_global_variable.scrSize[0] / Lexaar_global_variable.scrSize[1]), near, far)
        glTranslatef(0.0,0.0,-5)

        # sets the model view
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

class Cube(Lexaar.MainClass) :
    def __init__(self, X = 1, Y = 1, Z = 1, Rot = 0) :
        self.vertices= (
        (1*X, -1*Y, -1*Z),
        (1*X, 1*Y, -1*Z),
        (-1*X, 1*Y, -1*Z),
        (-1*X, -1*Y, -1*Z),
        (1*X, -1*Y, 1*Z),
        (1*X, 1*Y, 1*Z),
        (-1*X, -1*Y, 1*Z),
        (-1*X, 1*Y, 1*Z)
        )

        self.edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7)
        )

    def eventLaunch(self) :
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINES)
        for edge in self.edges :
            for vertex in edge :
                glVertex3fv(self.vertices[vertex])
        glEnd()
        glRotatef(20, 1,1,0)
        pygame.time.wait(20)
        image = pygame.image.load("AssetsTest/Fond.png").convert_alpha()
        Lexaar_global_variable.scr.blit(image, (0,0))