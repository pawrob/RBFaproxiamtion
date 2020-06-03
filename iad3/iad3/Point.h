#ifndef POINT_H
#define POINT_H

#include <chrono>
#include <random>

using namespace std;

class Point
{
    private:
        double x;
        double y;
    public:
        Point(double ox, double oy);
        virtual ~Point();
        void setX(double px);
        void setY(double py);
        double getX();
        double getY();
};

#endif // POINT_H
