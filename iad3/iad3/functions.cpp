#include "header.h"
#include <iostream>
#include "gnuplot_i.hpp"

using namespace std;

void getData(string name, vector <Point> &points, int lines)
{
    ifstream data;
    data.open(name, ios::in);
    if (data.good())
    {
        for (int i = 0; i < lines; i++)
        {
            double a, b;
            data >> a >> b;
            points.push_back(Point(a, b));
        }
    }
    else {
        cout << "Nie udalo sie otworzyc pliku." << endl;
    }
}

void showVectorValues(vector<double> &v)
{
    for(int i=0; i<v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

double distance(Neuron neuron1, Neuron neuron2)
{
    return sqrt(pow((neuron1.getX() - neuron2.getX()), 2) + pow((neuron1.getY() - neuron2.getY()), 2));
}

double distance(Point point, Neuron neuron)
{
    return sqrt(pow((point.getX() - neuron.getX()), 2) + pow((point.getY() - neuron.getY()), 2));
}

double Gauss(double dist, Neuron neuron)
{
    return exp((-pow(dist, 2))/(2*pow(neuron.getR(), 2)));
}

void replot(vector <Point> &points, vector <Neuron> &neurons)
{
    vector <double> px, py, nx, ny;
    for (int i = 0; i < points.size(); i++)
    {
        px.push_back(points[i].getX());
        py.push_back(points[i].getY());
    }
    for (int i = 0; i < neurons.size(); i++)
    {
        nx.push_back(neurons[i].getX());
        ny.push_back(neurons[i].getY());
    }
    plot(px, py, nx, ny);
}

void replot(vector <Point> &points, vector <Point> &points1, vector <Neuron> &neurons)
{
    vector <double> px, py, nx, ny, rx, ry;
    for (int i = 0; i < points.size(); i++)
    {
        px.push_back(points[i].getX());
        py.push_back(points[i].getY());
    }
    for (int i = 0; i < points1.size(); i++)
    {
        nx.push_back(points1[i].getX());
        ny.push_back(points1[i].getY());
    }
    for (int i = 0; i < neurons.size(); i++)
    {
        rx.push_back(neurons[i].getX());
        ry.push_back(neurons[i].getY());
    }
    plot(px, py, nx, ny, rx, ry);
}

void plot(vector<double> oX, vector<double> oY, vector<double> centX, vector<double> centY, vector<double> rX, vector<double> rY)
{
    //system("pause");

    Gnuplot::set_GNUPlotPath(GNUPLOT_PATH);
    Gnuplot main_plot;

    main_plot.set_title( "wykres" );
    main_plot.set_xlabel( "Os x" );
    main_plot.set_ylabel( "Os y" );

    main_plot.set_xrange( -10, 10 );
    main_plot.set_yrange( -14, 10 );

    main_plot.set_grid();

    main_plot.set_style( "points" );

    main_plot.plot_xy(centX, centY, "punkty z pliku" );
    main_plot.plot_xy(oX, oY, "aproksymacja" );
    main_plot.plot_xy(rX, rY, "neurony" );

    _sleep(5000);
    main_plot.remove_tmpfiles();

}

void plot(vector<double> oX, vector<double> oY, vector<double> centX, vector<double> centY)
{
    //system("pause");

    Gnuplot::set_GNUPlotPath(GNUPLOT_PATH);
    Gnuplot main_plot;

    main_plot.set_title( "wykres" );
    main_plot.set_xlabel( "Os x" );
    main_plot.set_ylabel( "Os y" );

    main_plot.set_xrange( -10, 10 );
    main_plot.set_yrange( -14, 10 );

    main_plot.set_grid();

    main_plot.set_style( "points" );

    main_plot.plot_xy(oX, oY, "punkty" );
    main_plot.plot_xy(centX, centY, "neurony" );

    _sleep(3000);
    main_plot.remove_tmpfiles();

}
