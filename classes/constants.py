# from pygame.math import Vector2
# from pygame import display

from euclid import Vector2
from pyglet.canvas import Display

FULLSCREEN = False

if FULLSCREEN:
    screen = Display().get_default_screen()
    WIDTH = int(screen.width)
    HEIGHT = int(screen.height)
else:
    WIDTH = 800
    HEIGHT = 600


MAXROCKETS = 500
GRAVITY = Vector2(0,0.01)
LIFESPAN = 600
MUTATIONFACTOR = 1
TARGETPOS = (WIDTH/2,HEIGHT-int(HEIGHT*0.1))
FONTSIZE = 14

RED = (255,0,0)
WHITE = (255,255,255)

MAXOBSTACLES = 20

OBSTACLETESTLIMIT = 30