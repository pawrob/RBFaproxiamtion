from NeuralNetwork import NeuralNetwork
import matplotlib.pyplot as mpl

def showValues(values) :
    string = ''
    for i in range ( len(values) ) :
        string = string + str(values[i]) + " "
    print(string)

n = 2                        #Liczba neuronów w warstwie ukrytej
topology = [4,n,4]             #określenie topologii, czyli liczby neuronow w danej warstwie
bias = False                   #Zakladamy, ze biasu nie ma
network = NeuralNetwork(topology, bias) #stworzenie naszej sieci
#inicjalizacje:
error = 0.0
iteration = 0
tab = []
inputValues = []
expectedValues = []
resultValues = []
XAxis = []
YAxis = []
inputFile = []
outputFile = []
#otwieranie plików
input = open("transformation.txt", mode = "r")
errors = open("errors.txt",'w')

#przepisywanie plików input i output do tablicy, aby potem na podstawie tej tablicy przeprowadzać naukę

for line in input.readlines() :
    for char in line :
        if char != ' ' and char != '\n' :
            inputFile.append( int(char) )
print(inputFile)                 #sprawdzenie poprawnosci, organoleptycznie
outputFile = inputFile
print(outputFile)

#główna pętla
while iteration < 10000 :

    error = 0                                            #deklarujemy błąd jako 0
    placement = 0                                        #placement, czyli miejsce w naszym pliku, w ktorym jestesmy. Na początku to 0, po pierwszej iteracji to 4 itd aż do 16,
                                                         #czyli długości naszego pliku ( 4 kolumny po 4 wiersze )
    while placement < len(inputFile):                    #tutaj sprawdzenie dlugosci pliku, zamiennik EOF()
        for i in range (0,topology[0]) :
            inputValues.append( inputFile[placement + i ] ) #wartosci wejsciowe (jeden rządek, np 0 0 1 0 )
        for i in range(0, topology[len(topology) - 1 ]):
            expectedValues.append( outputFile[placement + i] ) #oczekiwane wartosci

        placement = placement + topology[0] #tutaj właśnie zmiana placement, czyli jakby miejsca w naszym pliku

        network.fill( inputValues ) #wypelniamy sieć wartościami
        network.getResults(resultValues) #pobieramy wartości finalne pochodzące z ostatnich neuronów (3 warstwa)
        network.reversePropagation(expectedValues,bias) #algorytm propagacji wstecznej, do którego potrzebujemy info o biasie oraz wartości oczekiwane

        #wyswietlanie rezultatów
        if iteration%100 ==0 or iteration == 1 or iteration == 99 :
            print("------------------")
            showValues( inputValues )
            print("vs")
            showValues( resultValues )
            print("------------------")

        error = error + network.networkError #błąd nam się zwiększa o błąd

        inputValues.clear() #czyścimy wejściowe wartości (czyli cztery bajty, no cztery cyfry)
        expectedValues.clear() #oczekiwane wartości też czyścimy

        #tworzeie wektorów wykresów
    if iteration % 10 == 0 : #ten warunek to jedynie zapisywanie błędu oraz wrzucanie błędów do naszych wektorów, ktore nam potem stworzą osie X i Y
        errors.write(str(error/4) + '\n')
        XAxis.append(iteration/10)
        YAxis.append(error/4)
    iteration = iteration + 1

#Wykresik
mpl.plot(XAxis,YAxis)
mpl.xlabel("iteracja")
mpl.ylabel("blad")
mpl.ylim(bottom=0)
mpl.show()
