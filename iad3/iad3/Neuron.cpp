#include "Neuron.h"
#include "header.h"

Neuron::Neuron(Point point)
{
    X = point.getX();
    Y = point.getY();
}

Neuron::Neuron(int number)
{
    for (int i = 0; i < number; i++)
    {
        w.push_back(Weights());
        w[i].weight=rand()/double(RAND_MAX);
    }
}

Neuron::~Neuron(){}

void Neuron::setR(double py)
{
    r = py;
}

double Neuron::getR()
{
    return r;
}

double Neuron::getX()
{
    return X;
}

double Neuron::getY()
{
    return Y;
}

void Neuron::setOut(double output)
{
    outputValue = output;
}

double Neuron::getOut()
{
    return outputValue;
}

void Neuron::feedForward(vector <Neuron> neurons)
{
    double sum = 0;
    for (int i = 0; i < neurons.size(); i++)
    {
        sum+=neurons[i].getOut()*this->w[i].weight;
    }
    setOut(sum);
}

void Neuron::updateWeights(vector <Neuron> neurons, Point point)
{
    for (int i = 0; i < neurons.size(); i++)
    {
        double oldDeltaWeight=this->w[i].deltaWeight;
        double newDeltaWeight=neurons[i].getOut()*(getOut() - point.getY())*learningRate;//+momentum*oldDeltaWeight;
        this->w[i].deltaWeight=newDeltaWeight;
        this->w[i].weight -=newDeltaWeight;
    }

}
