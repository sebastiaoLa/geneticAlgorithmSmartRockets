import pygame

class Game(object):
    def __init__(self):
        pygame.init()
        size = width,heigth = (800,600)
        
        self.displaySurf = pygame.display.set_mode(size)
        self.rocket = pygame.image.load('props/rocket.png')