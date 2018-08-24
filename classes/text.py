from pygame import font

from .constants import FONTSIZE,RED,HEIGHT

class Text(object):
    def __init__(self):
        self.font = font.Font(font.get_default_font(),FONTSIZE)
        self.text = []
    
    def set_text(self,*text):
        self.text = []
        for i in text:
            self.text.append(self.font.render(str(i),True,RED))

    def draw(self,display):
        height = 0
        for i in self.text:
            height += i.get_rect().height

        for i in self.text:
            rect = i.get_rect()
            rect.left = 10
            rect.top = HEIGHT-height
            height -= rect.height
            display.blit(i,rect)
        