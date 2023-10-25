from pygame.math import Vector2
from pygame import display

FULLSCREEN = False

if FULLSCREEN:
    display.init()
    screen = display.Info()
    WIDTH = int(screen.current_w)
    HEIGHT = int(screen.current_h)
else:
    WIDTH = 800
    HEIGHT = 600


MAXROCKETS = 500
GRAVITY = Vector2(0,0.01)
LIFESPAN = 600
MUTATIONFACTOR = 5

TARGETPOS = (WIDTH/2,int(HEIGHT*0.1))
FONTSIZE = 14

RED = (255,0,0)
WHITE = (255,255,255)

MAXOBSTACLES = 20

OBSTACLETESTLIMIT = 30