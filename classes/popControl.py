from pyglet.graphics import Batch
from rect import Rect
from rocket import Rocket
from constants import MAXROCKETS,LIFESPAN,TARGETPOS
from math import hypot
from random import choice

class Population(object):
    def __init__(self,batch = None):
        self.gen = 1
        self.count = 0
        self.pop = []
        self.matingpool = []
        if batch:
            self.batch = batch
        else:
            self.batch = Batch()
        for i in range(0,MAXROCKETS):
            self.pop.append(Rocket(batch=self.batch))

    def checkCollide(self,rects):
        for j in rects:
            for i in self.pop:
                if i.rect.collides(j):
                    i.crashed = True

    def all_done(self):
        return False not in [ i.crashed or i.hit for i in self.pop]

    def update(self):
        self.count += 1
        if self.count<LIFESPAN and not self.all_done():
            for i in self.pop:  
                i.update(self.count)
        else:
            self.newGen()

    def draw(self):
        self.batch.draw()

    def calcFitness(self):
        for i in self.pop:
            i.fitness = hypot(i.img.x-TARGETPOS[0],i.img.y-TARGETPOS[1])
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
        print 'generation: ',self.gen
        print (crashed/float(MAXROCKETS))*100,'% crashed'
        print (hited/float(MAXROCKETS))*100,'% hited'

    def fillMatingPool(self):
        self.matingpool = []
        for i in self.pop:
            self.matingpool += [i.dna]*int(i.fitness)

    def cleanPop(self):
        for i in range(len(self.pop)-1,0,-1):
            del self.pop[i]
        self.pop = []

    def newGen(self):
        self.calcFitness()
        self.fillMatingPool()
        self.cleanPop()
        for i in range(0,MAXROCKETS):
            partnerA = choice(self.matingpool)
            partnerB = choice(self.matingpool)
            self.pop.append(Rocket(dna=partnerA.crossover(partnerB),batch=self.batch))
        self.count = 0
        self.gen += 1