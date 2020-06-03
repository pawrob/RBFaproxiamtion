
#ifndef HEADER_H
#define HEADER_H

#include <string>
#include <chrono>
#include <random>
#include <fstream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <random>
#include <math.h>
#include "Point.h"
#include "Neuron.h"

#define GNUPLOT_PATH "C:\\gnuplot\\bin"

using namespace std;

void showVectorValues(vector<double> &v);
void getData(string name, vector <Point> &points, int lines);
double distance(Neuron neuron1, Neuron neuron2);
double distance(Point point, Neuron neuron);
double Gauss(double dist, Neuron neuron);
void replot(vector <Point> &points, vector <Neuron> &neurons);
void replot(vector <Point> &points, vector <Point> &points1, vector <Neuron> &neurons);
void plot(vector<double> oX, vector<double> oY, vector<double> centX, vector<double> centY, vector<double> rX, vector<double> rY);
void plot(vector<double> oX, vector<double> oY, vector<double> centX, vector<double> centY);

#endif // HEADER_H
