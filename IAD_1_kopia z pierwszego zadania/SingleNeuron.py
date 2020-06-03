import random, math
from Weight import Weight
learningRate = 0.5 # wpolczynnik nauki
momentum = 0.2  #momentum


class SingleNeuron:
    def __init__(self,now,bias):
        self.outputValue = None
        self.numberOfWeights = now
        self.bias = bias
        self.weights = []
        self.bias = Weight()
        self.changeFactor = None
        for weight in range(self.numberOfWeights) :
            self.weights.append(Weight())
        if not bias:
            self.bias.weight = 0.0


    def fillWith(self,previous):# otrzymujemy poprzednią warstwę, która informuje nas ile dla każdego neuronu w obecnej warstwie musi być wejść
                                #oraz która przechowuje informacje o wyjściowych wartościach neuronów w niej samej (poprzedniej)
        sum = 0.0
        #poniżej wyjście neuronu jest uzupełniane o sumę poprzednich wyjść wymnożonych przez wagi w naszym neuronie
        for neuron in range( len(previous.neurons) ):
            sum = sum + ( previous.neurons[neuron].outputValue ) * self.weights[neuron].weight
        sum = sum + self.bias.weight
        self.outputValue = self.activationFunction(sum)

    def sum(self, whichLayer, whichNeuron):
        sum = 0.0
        for neuron in range ( len(whichLayer.neurons) ) :
            sum = sum + whichLayer.neurons[neuron].changeFactor * whichLayer.neurons[neuron].weights[whichNeuron].weight
        return sum


    def activationFunction(self,x): #funkcja aktywacji
        return 1 / (1 + math.exp(-x))

    def DerivativeOfActivationFunction(self,x): #pochodna funkcji aktywacji
        return x * (1-x)

    def outputLayerWeights(self, expectedValues):
        #błąd, inaczej współczynnik zmienności, który jest obliczany jako (Wartość wyjściowa - wartość oczekiwana) pomnożona razy pochodna
        self.changeFactor = (self.outputValue - expectedValues) * self.DerivativeOfActivationFunction(self.outputValue)

    def hiddenLayerWeights(self, layer, neuron):
        self.changeFactor = self.sum(layer,neuron) * self.DerivativeOfActivationFunction( self.outputValue )

    def updateWeights(self,previous, b): #aktualzacja wag
        for i in range ( len(previous.neurons) ) :
            previousNeuron = previous.neurons[i]
            oldDeltaWeight = self.weights[i].deltaWeight
            newDeltaWeight = learningRate * previousNeuron.outputValue * self.changeFactor + momentum * oldDeltaWeight #wzor na nową wagę
            self.weights[i].deltaWeight = newDeltaWeight
            self.weights[i].weight = self.weights[i].weight - newDeltaWeight

        if b : #jeśli jest bias to trzeba zrobić dodatkowo:
            oldDeltaWeight = self.bias.deltaWeight
            newDeltaWeight = learningRate * self.changeFactor + momentum * oldDeltaWeight
            self.bias.deltaWeight = newDeltaWeight
            self.bias.weight = self.bias.weight - newDeltaWeight

