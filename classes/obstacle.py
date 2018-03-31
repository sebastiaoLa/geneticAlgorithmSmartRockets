from constants import WIDTH,HEIGHT,WHITE,OBSTACLETESTLIMIT

from random import randint

from pyglet.gl import *

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def __str__(self):
        return str([self.x, self.y, self.width, self.height])
    
    def as_list(self):
        return [self.x, self.y, self.width, self.height]
    
    def left(self):
        return self.x
    
    def right(self):
        return self.x + self.width
    
    def bottom(self):
        return self.y
    
    def top(self):
        return self.y + self.height
    
    def collides(self, rect2):
        if self.right() <= rect2.left():
            return False
        elif self.left() >= rect2.right():
            return False
        elif self.top() <= rect2.bottom():
            return False
        elif self.bottom() >= rect2.top():
            return False
        else:
            return True
    
    def collides_point(self, x, y):
        if x >= self.left() and x <= self.right() and y >= self.bottom() and y <= self.top():
            return True
        return False


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
        else:
            self.rect = Rect(randint(int(WIDTH*0.1),int(WIDTH*0.8)),randint(int(HEIGHT*0.3),int(HEIGHT*0.6)),self.width,self.height)
            self.checkAgain = True
            while self.checkAgain:
                self.checkCollide(rects)
                self.tests += 1
            

    def newCenter(self):
        if self.tests<OBSTACLETESTLIMIT:
            self.rect.x,self.rect.y = randint(int(WIDTH*0.1),int(WIDTH*0.8)),randint(int(HEIGHT*0.3),int(HEIGHT*0.6))
            print 'new pos',
        else:
            self.width = randint(int(WIDTH*0.01),int(WIDTH*0.2))
            self.height = randint(int(HEIGHT*0.01),int(HEIGHT*0.2))
            self.rect = Rect(randint(int(WIDTH*0.1),int(WIDTH*0.8))+self.width/2,randint(int(HEIGHT*0.3),int(HEIGHT*0.6))+self.height/2,self.width,self.height)
            print 'new rect'
            self.tests = 0

    def checkCollide(self,rects):
        self.checkAgain = False
        for i in rects:
            if self.rect.collides(i):
                self.newCenter()
                self.checkAgain = True
                break

    def draw(self):
        pyglet.graphics.draw(4,pyglet.gl.GL_QUADS, ('v2f',[self.rect.right(),self.rect.top(),self.rect.left(),self.rect.top(),self.rect.left(),self.rect.bottom(),self.rect.right(),self.rect.bottom()]))
