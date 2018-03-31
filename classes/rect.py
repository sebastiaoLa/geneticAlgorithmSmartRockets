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
    
    def draw(self):
        pyglet.graphics.draw(4,pyglet.gl.GL_QUADS, ('v2f',[self.right(),self.top(),self.left(),self.top(),self.left(),self.bottom(),self.right(),self.bottom()]))