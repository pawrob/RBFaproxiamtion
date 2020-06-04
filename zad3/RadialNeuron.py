from math import sqrt

class RadialNeuron :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = None
        self.distances = []

        #Ta funkcja ustala promien naszego neurona jako srednia dystansu do najblizszych n neuronow
        #n jest ustalane na poczatku algorytmu
    def setRadius(self,neurons,neighbourhoodCoefficient):
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
