import pandas as pd
from matplotlib import pyplot as plt
from RadialNeuron import RadialNeuron

data1 = pd.read_csv("approximation_train_1.txt",header = None, sep = ' ')
data2 = pd.read_csv("approximation_train_2.txt",header = None, sep = ' ')

plt.plot(data1[0],data1[1],'o')
plt.plot(data2[0],data2[1],'x')
plt.show()

radialNeurons = []
linearNeurons = []

#gowno w dupie
n = input("Podaj liczbe neuronow radialnych : ")
m = input("Podaj liczbe neuronow liniowych : ")
for i in range ( n ) :
    radialNeurons.append ( RadialNeuron() )
for i in range ( m ) :
    linearNeurons.append ( LinearNeuron() )