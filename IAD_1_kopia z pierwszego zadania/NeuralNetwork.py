from SingleNeuron import SingleNeuron

class Layer:
    def __init__(self):
        self.neurons = []

class NeuralNetwork :
    def __init__(self,topology, bias):
        self.layers = []
        self.numberOfLayers = len(topology)
        self.networkError = 0
        for layer in range (0, self.numberOfLayers) :
            if layer == 0 :
                numberOfWeights = 0
            else  :
                numberOfWeights = topology[layer-1]
            self.layers.append( Layer() )
            for neuron in range (topology[layer]) :
                self.layers[layer].neurons.append( SingleNeuron(numberOfWeights,bias) )


    def fill(self, inputValues):
        #Ta pętla wypełnia warstwę zerową wartościami wejściowymi
        for neuron in range(len(inputValues)):
            self.layers[0].neurons[neuron].outputValue = inputValues[neuron]
        #Dla pozostałych warstw wypełniamy neurony zgodnie z algorytmem w funkcji fillWith()
        for layer in range (1, len(self.layers) ) :
            current = self.layers[layer]
            previous = self.layers[layer-1]
            for neuron in range ( len(current.neurons) ) :
                current.neurons[neuron].fillWith(previous)

    def getResults(self,values):
        values.clear()
        for i in range ( len(self.layers[-1].neurons) ):
            values.append( self.layers[-1].neurons[i].outputValue )


    def reversePropagation(self, expectedValues, bias):
        #Ostatnia warstwa to output, środkowa to ukryta
        output = self.layers[-1]
        hidden = self.layers[1]
        self.networkError = 0.0
        for i in range( len(output.neurons) ) :
            delta = expectedValues[i] - output.neurons[i].outputValue #dla każdego neuronu liczymy deltę, która będzie wynosić (wartość oczekiwana - wartość otrzymana)
            self.networkError = self.networkError + (delta * delta) / 2.0 #zgodnie ze wzorem tak liczymy network error
        for i in range( len(output.neurons) ) :
            output.neurons[i].outputLayerWeights(expectedValues[i]) #dla każdego neuronu warstwy koncowej ustawiamy wartosc błędu (changeFactor)
        for i in range( len(hidden.neurons) ) :
            hidden.neurons[i].hiddenLayerWeights(output, i ) #dla kazdego neuronu warstwy ukrytej ustawiamy również wartość błędu (changeFactor)

        for num in reversed ( ( range(1 , len ( self.layers ) ) ) )   : # Dla każdej warstwy od tyłu ( czyli dla drugiej i pierwszej)
            current = self.layers[num] #druga albo pierwsza
            previous = self.layers[num-1] #pierwsza albo zerowa
            for neuron in range ( len(current.neurons) )  : #dla każdego neuronu w obecnej warstwie (current)
                current.neurons[neuron].updateWeights ( previous, bias ) #aktualizujemy wagi, które są na wejściu do neurona w naszej obecnej warstwie

