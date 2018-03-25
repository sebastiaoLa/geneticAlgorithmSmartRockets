from pygame import image,math,transform
from constants import WIDTH,HEIGHT,GRAVITY
import random

class Rocket(object):
    def __init__(self):
        self.img = image.load('props/rocket.png')
        self.rect = self.img.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.rect.bottom = HEIGHT-50
        self.vel = math.Vector2(0,-1)
        self.acc = math.Vector2()
        self.angle = 90

    def destroyed(self):
        return self.rect.center[0]<0 or self.rect.center[0]>WIDTH or self.rect.center[1]<0 or self.rect.center[1]>HEIGHT

    def applyForce(self,force):
        self.acc += force

    def update(self):
        self.acc = math.Vector2()
        self.applyForce(GRAVITY)
        self.applyForce(math.Vector2(random.randint(-2,2),random.randint(-2,2)))
        self.vel += self.acc
        # self.vel = math.Vector2(random.randint(-2,2),random.randint(-2,2))
        self.rect = self.rect.move(self.vel.x,self.vel.y)
        transform.rotate(self.img,self.vel.as_polar()[1]-self.angle)
        # if random.random()<0.1:
        #     print self.rect.move(self.vel.x,self.vel.y), self.vel

    def show(self,disp):
        disp.blit(self.img,self.rect)
