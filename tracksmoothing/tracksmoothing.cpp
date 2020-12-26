#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
    int nCases = 0;
    scanf("%d", &nCases);
    for (int ii = 0; ii < nCases; ++ii)
    {
        int r;
        int n;
        scanf("%d %d", &r, &n);
        int x0, y0;
        scanf("%d %d", &x0, &y0);
        int xp = x0;
        int yp = y0;
        double distSum = 0.0;
        for (int jj = 1; jj < n; ++jj)
        {
            int x, y;
            scanf("%d %d", &x, &y);
            int dx = x - xp;
            int dy = y - yp;
            double dist = sqrt(dx*dx + dy*dy);
            distSum += dist;
            //fprintf(stderr, "Dist: %f\n", dist);
            xp = x;
            yp = y;
        }
        int dx = x0 - xp;
        int dy = y0 - yp;
        double dist = sqrt(dx*dx + dy*dy);
        distSum += dist;
        double circ = M_PI * 2.0 * r;
        //fprintf(stderr, "Dist: %f\n", dist);
        //fprintf(stderr, "DistSum: %f\n", distSum);
        //fprintf(stderr, "Circ: %f\n", circ);
        if (distSum < circ)
        {
            printf("Not possible\n");
        }
        else
        {
            double scale = (distSum - circ) / distSum;
            printf("%0.6f\n", scale);
        }
    }
    return 0;
}