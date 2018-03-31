from pyglet import image
from pyglet.sprite import Sprite

from os.path import isfile

from PIL import Image
from constants import HEIGHT,TARGETPOS

class Target(object):
    def __init__(self,batch = None):
        if isfile('props/temp.png'):
            self.img = Sprite(image.load('props/temp.png'),TARGETPOS[0],TARGETPOS[1],batch=batch)
        else:
            origImg = Image.open('props/target.png').resize((int(HEIGHT*0.05),int(HEIGHT*0.05)),Image.LANCZOS)
            origImg.save('props/temp.png','PNG')
            self.img = Sprite(image.load('props/temp.png'),TARGETPOS[0],TARGETPOS[1],batch=batch)
    
    def set_center(self,pos):
        self.img.x = pos[0]
        self.img.y = pos[1]

    def draw(self):
        self.img.draw()