from math import sqrt, log
from LinearNeuron import LinearNeuron

class RBF :
    def __init__(self, b ,learningFactor):
        self.radialNeurons = []
        self.linearNeuron = LinearNeuron
        self.bias = b
        self.error = None
        self.learningFactor = learningFactor

    def setSigmas(self):
        #dla każdego neuronu radialnego ustawiamy wartości sigmy
        for i in range ( len ( self.radialNeurons ) - 1 ):
            distance = abs ( self.radialNeurons[i].centre - self.radialNeurons[i+1].centre )
            if distance == 0 :
                distance = 0.01
            self.radialNeurons[i].sigma = sqrt ( - (distance * distance) / ( log(1/2) * 2 ) )

    def setError(self,input,output):
        sum = 0
        sum = sum + pow( ( self.linearNeuron.outputValue - output ) , 2 )
        self.error = sum

    def errorFunction(self,value):
        sum = 0
        sum = self.bias
        for i in range( len ( self.linearNeuron.weights ) ) :
            sum = sum + self.linearNeuron.weights[i] * self.radialNeurons[i].gaussianFunction( value )
        return sum

    def updateWeights(self,outputValue,inputValue):
        for i in range ( len( self.linearNeuron.weights ) ) :
            self.linearNeuron.weights[i] = self.linearNeuron.weights[i] - self.learningFactor * self.radialNeurons[i].gaussianFunction( inputValue ) * ( self.linearNeuron.outputValue - outputValue )

    def derivative(self,weight,inputs,outputs,radialNeurons):
        sum = 0
        for i in range( len ( inputs ) ) :
            radialSum = 0
            for j in range( len(radialNeurons)):
                radialSum = radialSum + radialNeurons[j].gaussianFunction( inputs[i] )
            sum = sum + ( self.errorFunction( inputs[i] ) - outputs[i] ) * radialSum
        return sum / len(inputs)

    def attributeWeights(self):
        for i in range( len ( self.linearNeuron.weights ) ):
            self.linearNeuron.weights[i] = self.linearNeuron.newWeights[i]

