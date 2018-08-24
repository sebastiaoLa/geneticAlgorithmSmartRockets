import random
from math import hypot

from pygame import image, math, transform

from .constants import GRAVITY, HEIGHT, TARGETPOS, WIDTH
from .dna import Dna


class Rocket(object):
    def __init__(self,dna = None):
        self.img = image.load('props/rocket.png')
        self.rect = self.img.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.rect.bottom = HEIGHT-50
        self.vel = math.Vector2(0,-1)
        self.acc = math.Vector2()
        self.fitness = 0
        self.hit = False
        self.hitTime = 0
        self.crashed = False
        if dna:
            self.dna = dna
        else:
            self.dna = Dna()

    def destroyed(self):
        return self.rect.centerx<0 or self.rect.centerx>WIDTH or self.rect.centery<0 or self.rect.centery>HEIGHT

    def applyForce(self,force):
        if self.acc.length() != 0:
            self.acc = self.acc.normalize()
        self.acc += force

    def update(self,count):
        if not self.crashed and not self.hit:
            self.acc = math.Vector2()
            # self.applyForce(GRAVITY)
            self.applyForce(self.dna.genes[count])
            self.vel += self.acc
            self.rect = self.rect.move(int(self.vel.x),int(self.vel.y))
            if self.destroyed():
                self.crashed = True
            elif hypot(self.rect.centerx-TARGETPOS[0],self.rect.centery-TARGETPOS[1])<20:
                self.hit = True
                self.hitTime = count

    def show(self,disp):
        disp.blit(self.img,self.rect)        
