#ifndef NEURON_H
#define NEURON_H

#include "Point.h"

#define learningRate 0.3
#define momentum 0.4

typedef struct Weights{
    double weight;
    double deltaWeight;
};

class Neuron
{
private:
    double X;
    double Y;
    double r;
    vector <Weights> w;
    double outputValue;
public:
    Neuron(Point point);
    Neuron(int numberOfWeights);
    ~Neuron();
    void setR(double py);
    double getR();
    double getX();
    double getY();
    void setOut(double output);
    double getOut();
    void feedForward(vector <Neuron> neurons);
    void updateWeights(vector <Neuron> neurons, Point point);
};

#endif // NEURON_H
