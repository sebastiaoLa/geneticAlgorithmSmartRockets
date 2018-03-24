import pygame

class Rocket(object):
    def __init__(self,img_path):
        self.img = pygame.image.load(img_path)
        self.rect = img.get_rect()