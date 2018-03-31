from constants import LIFESPAN,MUTATIONFACTOR
from euclid import Vector2
from random import random,randint

class Dna(object):
    def __init__(self,genes = None):
        if genes:
            self.genes = genes
        else:
            self.genes = []
            for i in range(0,LIFESPAN):
                self.genes.append(Vector2(random()*randint(-1,1),random()*randint(-1,1)))

    def crossover(self,partner):
        mid = randint(int(len(self.genes)*0.4),int(len(self.genes)*0.6))
        newGenes = []
        for i in range(0,len(self.genes)):
            if randint(0,100)<MUTATIONFACTOR:
                newGenes.append(Vector2(random()*randint(-1,1),random()*randint(-1,1)))
            else:
                if i < mid:
                    newGenes.append(self.genes[i])
                else:
                    newGenes.append(partner.genes[i])
        return Dna(newGenes)

