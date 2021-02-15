from math import sqrt,exp, log
from random import randrange
class RadialNeuron :
    def __init__(self,data):
        #centrum, czyli losowa wartosc z puli poczatkowej

        self.centre = data[randrange(0,len(data))]
        #losowa sigma
        self.sigma = 1
        self.distances = []

    #Ta funkcja ustala promien naszego neurona jako srednia dystansu do najblizszych n neuronow
    #n jest ustalane na poczatku algorytmu
    def setCentre(self,neurons,neighbourhoodCoefficient):
        for neuron in neurons :
            self.distances.append ( self.neuronsEuclideanDistance(self,neuron) )
        self.distances = sorted(self.distances)
        sum = 0
        for i in range ( neighbourhoodCoefficient ) :
            sum = sum +  self.distances[i]
        self.radius = sum/neighbourhoodCoefficient

        #dystans euklidesowy miedzy dwoma neuronami
    def neuronsEuclideanDistance(self,a,b):
        return sqrt(  pow( (a.x - b.x ),2 ) + pow( (a.y - b.y ),2 )  )

    def gaussianFunction(self, x):
        distance = abs( self.centre - x )
        return exp( - (distance * distance) / ( 2 * self.sigma * self.sigma ) )




