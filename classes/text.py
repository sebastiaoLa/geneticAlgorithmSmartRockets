from pyglet.text import HTMLLabel

from constants import FONTSIZE,RED,HEIGHT,WIDTH

class Text(object):
    def __init__(self,batch=None):
        self.text = []
        self.batch = batch
    
    def set_text(self,*text):
        self.text = text

    def draw(self):
        html = ''
        for i in self.text:
            html += i+' <br> '
        htmllbl = HTMLLabel(html,x=0,y=HEIGHT,anchor_x='left',anchor_y='top',multiline=True,width=int(WIDTH*0.3))
        htmllbl.color = (255,0,0,255)
        htmllbl.draw()
        