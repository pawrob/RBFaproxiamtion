import pandas as pd
from matplotlib import pyplot as plt
from RadialNeuron import RadialNeuron
from LinearNeuron import LinearNeuron
from RadialBasisFunctionNetwork import RBF
learningFactor = 0.3
bias = 0

inputValues = None
outputValues = None

errorPlotDataX = []
errorPlotDataY = []

RBF = RBF(bias, learningFactor)

c = input("Na ktorych danych chcesz trenowac siec, na 1 czy 2? : ")
if c == '1' :
    data1 = pd.read_csv("data_set/approximation_train_1.txt", header=None, sep=' ')
    inputValues = data1[0]
    outputValues = data1[1]
elif c == '2' :
    data1 = pd.read_csv("data_set/approximation_train_2.txt", header=None, sep=' ')
    inputValues = data1[0]
    outputValues = data1[1]

n = input("Podaj liczbe neuronow radialnych : ")
it = input("Podaj liczbe iteracji: ")

for i in range ( int ( n ) ) :
    RBF.radialNeurons.append ( RadialNeuron( inputValues ) )
RBF.setSigmas()

RBF.linearNeuron = LinearNeuron( int ( n ) )

#Trenowanie offline
for j in range ( int ( it ) ) :
    for i in range ( len ( inputValues ) ) :
        RBF.error = 0

        outputValue = outputValues[i]
        inputValue = inputValues[i]

        RBF.linearNeuron.setOutput(RBF.radialNeurons,inputValue)
        RBF.updateWeights(outputValue,inputValue)

        RBF.setError(inputValue, outputValue)
        #print( RBF.linearNeuron.weights )
    errorPlotDataX.append( j )
    errorPlotDataY.append( RBF.error )
    print("Iteracja: ", j, " blad: " , RBF.error)


print("Trwa rysowanie wykresu")
#rysowanie wykresu neuronow oraz ich polaczenia
plotX = []
plotY = []
for i in range ( -400, 400) :
    plotX.append(i/100)
    plotY.append( RBF.linearNeuron.getOutput(RBF.radialNeurons,i/100) )
x = []
y = []
for j in range ( len ( RBF.radialNeurons) ):
    for i in range (-400,400) :
        x.append( i/100 )
        y.append(RBF.radialNeurons[j].gaussianFunction(i/100) * RBF.linearNeuron.weights[j])
    plt.plot(x,y,lw=0.2)
plt.plot(plotX,plotY, lw=2)
plt.show()

#Pokazywanie wkyresu bledu
plt.plot( errorPlotDataX, errorPlotDataY, lw = 1 )
plt.show()

print("Czas na test")
#Test na danych testowych
data = pd.read_csv("data_set/approximation_test.txt", header = None, sep =' ')
testXValues = data[0]
testYValues = data[1]
testYOutputValues = []
for value in testXValues :
    testYOutputValues.append( RBF.linearNeuron.getOutput(RBF.radialNeurons , value) )
plt.plot(testXValues, testYOutputValues, 'o' , markersize = 1 )
plt.show()

