from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
#glutInit()

glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800,600)
glutInitWindowPosition(200,200)
win = glutCreateWindow("Opengl Test")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()