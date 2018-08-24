from random import randint

from pygame import Rect

from .constants import HEIGHT, OBSTACLETESTLIMIT, WHITE, WIDTH


class Obstacle(object):
    def __init__(self, rects = None):
        self.width = randint(int(WIDTH*0.01),int(WIDTH*0.2))
        self.height = randint(int(HEIGHT*0.01),int(HEIGHT*0.2))
        # self.width = int(HEIGHT*0.1)
        # self.height = self.width
        self.color = WHITE

        self.tests = 0
        if not rects:
            self.rect = Rect(WIDTH/2-self.width/2,HEIGHT/2-self.height/2,self.width,self.height)

        if rects:
            self.rect = Rect((randint(int(WIDTH*0.1),int(WIDTH*0.8)),randint(int(HEIGHT*0.3),int(HEIGHT*0.6)),self.width,self.height))
            self.checkAgain = True
            while self.checkAgain:
                self.checkCollide(rects)
                self.tests += 1
            

    def newCenter(self):
        if self.tests<OBSTACLETESTLIMIT:
            self.rect.center = (randint(int(WIDTH*0.1),int(WIDTH*0.8)),randint(int(HEIGHT*0.3),int(HEIGHT*0.6)))
            print ('new pos'),
        else:
            self.width = randint(int(WIDTH*0.01),int(WIDTH*0.2))
            self.height = randint(int(HEIGHT*0.01),int(HEIGHT*0.2))
            self.rect = Rect(randint(int(WIDTH*0.1),int(WIDTH*0.8))+self.width/2,randint(int(HEIGHT*0.3),int(HEIGHT*0.6))+self.height/2,self.width,self.height)
            print ('new rect')
            self.tests = 0

    def checkCollide(self,rects):
        self.checkAgain = False
        for i in rects:
            if self.rect.colliderect(i):
                self.newCenter()
                self.checkAgain = True
                break

    def draw(self,disp):
        disp.fill(self.color,self.rect)
