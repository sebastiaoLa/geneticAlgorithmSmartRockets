from constants import WIDTH,HEIGHT,MAXROCKETS
import pygame,sys

from rocket import Rocket

class Game(object):
    def __init__(self):
        pygame.init()
        size = (WIDTH,HEIGHT)
        
        self.displaySurf = pygame.display.set_mode(size)
        self.rockets = [Rocket()]*MAXROCKETS
        self.clock = pygame.time.Clock()

    def draw(self):
        self.displaySurf.fill((0,0,0))
        for i in self.rockets:
            i.update()
            i.show(self.displaySurf)
        for i in range(len(self.rockets)-1,-1,-1):
            if self.rockets[i].destroyed():
                # print i.destroyed()
                self.rockets.pop(i)
    
    def main_loop(self):
        while True:
            if len(self.rockets) == 0:
                print 'all crashed'
                sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)
            

game = Game()
game.main_loop()