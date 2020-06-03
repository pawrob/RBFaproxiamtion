#include <iostream>
#include "header.h"
#pragma warning(disable:4996)

using namespace std;

int main()
{
    vector <Point> testPoints, trainingPoints, index, results;
    vector <Neuron> neurons;
    int neuronNo;
    getData("approximation_test.txt", testPoints, 1000);
    getData("approximation_train_1.txt", trainingPoints, 81);
    getData("approximation_train_1.txt", index, 81);
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    shuffle(index.begin(), index.end(), std::default_random_engine(seed));

    cout << "Wpisz ile neuronow: ";
    cin >> neuronNo;

    //tworzenie neuronow radialnych
    for (int i = 0; i < neuronNo; i++)
    {
        neurons.push_back(Neuron(index[i]));
    }

    //tworzenie neuronu liniowego
    Neuron linearNeuron(neuronNo);

    //ustawianie R dla neuronow radialnych
    /*for (int i = 0; i < neurons.size(); i++)
    {
        double maximum = 0;
        for (int j = 0; j < neurons.size(); j++)
        {
            if ((distance(neurons[i], neurons[j]) > maximum))
            {
                maximum = distance(neurons[i], neurons[j]);
            }
        }
        neurons[i].setR(maximum/sqrt(2*neurons.size()));
    }*/
    for (int i = 0; i < neurons.size(); i++)
        neurons[i].setR(1);

    replot(trainingPoints, neurons);
    int counter = 0;
    //petla
    do
    {
        for (int i = 0; i < trainingPoints.size(); i++)
        {
            for (int j = 0; j < neurons.size(); j++)
            {
                //if (counter == 20)
                    //cout << distance(trainingPoints[i], neurons[j]) << "  " << Gauss(distance(trainingPoints[i], neurons[j]), neurons[j]) << endl;
                neurons[j].setOut(Gauss(distance(trainingPoints[i], neurons[j]), neurons[j]));
            }
            linearNeuron.feedForward(neurons);
            results.push_back(Point(trainingPoints[i].getX(), linearNeuron.getOut()));
            linearNeuron.updateWeights(neurons, trainingPoints[i]);
        }
        if (counter % 10 == 0)
            replot(results, trainingPoints, neurons);
        results.clear();
        counter++;
    } while (counter <= 20);

    cout << "NR = " << neurons.size() << endl;

    results.clear();
    for (int i = 0; i < testPoints.size(); i++)
    {
        for (int j = 0; j < neurons.size(); j++)
        {
            neurons[j].setOut(Gauss(distance(testPoints[i], neurons[j]), neurons[j]));
        }
        linearNeuron.feedForward(neurons);
        results.push_back(Point(testPoints[i].getX(), linearNeuron.getOut()));
    }
    replot(results, testPoints, neurons);

    return 0;
}
