#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

double radial_distance(double radius, double n_rings, double a_y, double b_y)
{
    return abs(a_y - b_y) * (radius / n_rings);
}

double circular_distance(double radius, double n_rings, double n_slices, double a_x, double b_x, double yy)
{
    return abs(a_x - b_x) * (M_PI * radial_distance(radius, n_rings, yy, 0.0)) / n_slices;
}

int main()
{
    double n_slices, n_rings, radius;
    cin >> n_slices >> n_rings >> radius;
    double a_x, a_y, b_x, b_y;
    cin >> a_x >> a_y >> b_x >> b_y;

    double min_dist = 10000000000.0;
    for (int ii = static_cast<int>(min(a_y, b_y)); ii >= 0; --ii)
    {
        double a_r = radial_distance(radius, n_rings, a_y, (double)ii);
        double b_r = radial_distance(radius, n_rings, b_y, (double)ii);
        double ab_c = circular_distance(radius, n_rings, n_slices, a_x, b_x, (double)ii);
        double dist = a_r + b_r + ab_c;
        min_dist = min(dist, min_dist);
        //cerr << "Radial: " << a_r << " + " << b_r << endl;
        //cerr << "Circular: " << ab_c << endl;
        //cerr << "Dist: " << dist << " (min: " << min_dist << ")" << endl;
    }
    printf("%.8lf\n", min_dist);
    return 0;
}