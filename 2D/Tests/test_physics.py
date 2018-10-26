import pygame
import pymunk
from pygame.locals import *
import pymunk.pygame_util
from pymunk import Vec2d

pygame.display.init()
fen = pygame.display.set_mode((1250,700))
draw_options = pymunk.pygame_util.DrawOptions(fen)
space = pymunk.Space()
space.gravity = 0,-900

segment = pymunk.Segment(space.static_body, (10, 50), (1240,50), 1.0)
segment.elasticity = 5
segment.color = pygame.color.THECOLORS["white"]
space.add(segment)

inertie = pymunk.moment_for_circle(100, 0, 50)
corpBalle = pymunk.Body(100, inertie)
corpBalle.position = 350, 500
balle = pymunk.Circle(corpBalle, 50)
balle.elasticity = 0.2
balle.color = pygame.color.THECOLORS["blue"]
space.add(balle, corpBalle)

while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            quit()

    dt = 1.0 / 60.0 / 5.0
    for i in range(5) :
        space.step(dt)

    fen.fill(0)
    space.debug_draw(draw_options)

    pygame.display.flip()
    pygame.time.Clock().tick(60)