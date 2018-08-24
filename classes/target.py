from pygame import image

from PIL import Image
from .constants import HEIGHT

class Target(object):
    def __init__(self):
        origImg = Image.open('props/target.png').resize((int(HEIGHT*0.05),int(HEIGHT*0.05)),Image.LANCZOS)
        print (origImg,(int(HEIGHT*0.05),int(HEIGHT*0.05)))
        origImg.save('props/temp.png','PNG')
        self.img = image.load('props/temp.png')
        print (self.img)
        self.rect = self.img.get_rect()
    
    def set_center(self,pos):
        self.rect.center = pos

    def draw(self,display):
        display.blit(self.img,self.rect)