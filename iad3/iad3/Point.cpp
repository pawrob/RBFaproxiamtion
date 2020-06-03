#include "Point.h"

Point::Point(double ox, double oy)
{
    x = ox;
    y = oy;
}

Point::~Point() {}

void Point::setX(double px)
{
    x = px;
}

void Point::setY(double py)
{
    y = py;
}

double Point::getX()
{
    return x;
}

double Point::getY()
{
    return y;
}
