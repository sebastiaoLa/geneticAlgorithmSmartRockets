from pyglet import image
from pyglet.sprite import Sprite
from constants import WIDTH,HEIGHT,GRAVITY,TARGETPOS
from dna import Dna
import random
from math import hypot
from euclid import Vector2

class Rocket(object):
    def __init__(self,dna = None,batch = None):
        if batch:
            self.img = Sprite(image.load('props/rocket.png'),WIDTH/2,int(HEIGHT*0.1),batch=batch)
        else:
            self.img = Sprite(image.load('props/rocket.png'),WIDTH/2,int(HEIGHT*0.1))
        self.vel = Vector2(0,-1)
        self.acc = Vector2()
        self.fitness = 0
        self.hit = False
        self.hitTime = 0
        self.crashed = False
        if dna:
            self.dna = dna
        else:
            self.dna = Dna()

    def destroyed(self):
        return self.img.x<0 or self.img.x>WIDTH or self.img.y<0 or self.img.y>HEIGHT

    def applyForce(self,force):
        self.acc += force
        self.acc = self.acc.normalize()

    def update(self,count):
        if not self.crashed and not self.hit:
            self.acc = Vector2()
            # self.applyForce(GRAVITY)
            self.applyForce(self.dna.genes[count])
            self.vel += self.acc
            self.img.x,self.img.y = self.img.x+self.vel.x,self.img.y+self.vel.y
            if self.destroyed():
                self.crashed = True
            elif hypot(self.img.x-TARGETPOS[0],self.img.y-TARGETPOS[1])<20:
                self.hit = True
                self.hitTime = count

    def draw(self):
        self.img.draw()
