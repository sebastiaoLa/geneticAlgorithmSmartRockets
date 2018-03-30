from classes.constants import WIDTH,HEIGHT,MAXROCKETS,LIFESPAN,TARGETPOS,MAXOBSTACLES,FULLSCREEN
import pygame,sys
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, MOUSEMOTION, QUIT, K_f
from classes.target import Target
from classes.text import Text
from classes.popControl import Population
from classes.obstacle import Obstacle
from time import time

class Game(object):
    def __init__(self):
        pygame.init()
        size = (WIDTH,HEIGHT)
        if FULLSCREEN:
            self.displaySurf = pygame.display.set_mode(size,pygame.HWSURFACE|pygame.FULLSCREEN)
        else:
            self.displaySurf = pygame.display.set_mode(size,pygame.HWSURFACE)
        self.population = Population()
        self.clock = pygame.time.Clock()

        self.target = Target()
        self.target.set_center(TARGETPOS)

        self.text = Text()

        self.obstacles = [Obstacle()]

        # for i in range(0,MAXOBSTACLES):
        #     print 'new obstacle',len(self.obstacles)
        #     obs = Obstacle(self.obstacles)
        #     self.obstacles.append(obs)

    def draw(self):
        self.displaySurf.fill((0,0,0))
        self.target.draw(self.displaySurf)
        self.text.set_text("Lifetime: "+str(self.population.count),"Generation: "+str(self.population.gen))
        self.text.draw(self.displaySurf)
        if self.population.gen > len(self.obstacles) and len(self.obstacles)<MAXOBSTACLES:
            self.obstacles.append(Obstacle(self.obstacles))
            print 'novo obstaculo'
        for i in self.obstacles:
            i.draw(self.displaySurf)
        self.population.checkCollide(self.obstacles)
        self.population.draw(self.displaySurf)
    
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_f:
                        pygame.display.toggle_fullscreen()
                    if event.key == K_ESCAPE:
                        sys.exit()
                        pygame.quit()
                        exit()  
                if event.type == pygame.QUIT:
                    sys.exit()
            self.draw()
            pygame.display.flip()
            

game = Game()
game.main_loop()