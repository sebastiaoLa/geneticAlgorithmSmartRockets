from math import hypot

from .constants import LIFESPAN, MAXROCKETS, TARGETPOS
from random import choice
from .rocket import Rocket


class Population(object):
    def __init__(self):
        self.gen = 1
        self.count = 0
        self.pop = []
        self.matingpool = []
        for i in range(0,MAXROCKETS):
            self.pop.append(Rocket())

    def checkCollide(self,rects):
        for j in rects:
            for i in self.pop:
                if i.rect.colliderect(j):
                    i.crashed = True

    def all_done(self):
        return False not in [ i.crashed or i.hit for i in self.pop]

    def draw(self,display):
        self.count += 1
        if self.count<LIFESPAN and not self.all_done():
            for i in self.pop:  
                i.update(self.count)
                i.show(display)
        else:
            self.newGen()
            


    def calcFitness(self):
        for i in self.pop:
            i.fitness = hypot(i.rect.center[0]-TARGETPOS[0],i.rect.center[1]-TARGETPOS[1])
        maxFitness = 0
        for i in self.pop:
            if i.fitness>maxFitness:
                maxFitness = i.fitness
        crashed = 0
        hited = 0
        for i in self.pop:
            i.fitness = (i.fitness/maxFitness)*100
            if i.crashed:
                crashed += 1
                i.fitness = i.fitness/20
            if i.hit:
                hited  += 1
                i.fitness = i.fitness*100/(i.hitTime/50)
        print ('generation: ',self.gen)
        print ((crashed/float(MAXROCKETS))*100,'% crashed')
        print ((hited/float(MAXROCKETS))*100,'% hited')

    def fillMatingPool(self):
        self.matingpool = []
        for i in self.pop:
            self.matingpool += [i.dna]*int(i.fitness)


    def newGen(self):
        self.calcFitness()
        self.fillMatingPool()
        self.pop = []
        for i in range(0,MAXROCKETS):
            partnerA = choice(self.matingpool)
            partnerB = choice(self.matingpool)
            self.pop.append(Rocket(partnerA.crossover(partnerB)))
        self.count = 0
        self.gen += 1
