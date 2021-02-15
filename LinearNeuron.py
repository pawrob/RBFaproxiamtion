import random
class LinearNeuron:
    def __init__(self,numberOfRadialNeurons):
        self.weights = self.setInitialWeights(numberOfRadialNeurons)
        self.newWeights = self.setInitialWeights(numberOfRadialNeurons)
        self.outputValue = None

    #Ta funkcja ustawia poczatkowe wagi dla naszego linearnego neuronu z przedzialu 0-1
    def setInitialWeights(self,n):
        weights = []
        for i in range(n) :
            weights.append( random.randrange( -100,100 ) / 100 )
        return weights

    #Ta funkcja zwraca wartość wyjściową naszego neuronu
    def setOutput(self, radialNeurons, value):
        output = 0
        for i in range ( len ( radialNeurons ) ) :
            output = output + radialNeurons[i].gaussianFunction( value ) * self.weights[i]
        self.outputValue = output

    def getOutput(self, radialNeurons, value):
        output = 0
        for i in range ( len ( radialNeurons ) ) :
            output = output + radialNeurons[i].gaussianFunction( value ) * self.weights[i]
        return output




