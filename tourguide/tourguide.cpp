#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

// For senior i, distance as a function of time is:
// sqrt((cos(a_i)*v_i*t + x_i - x_d)^2 + (sin(a_i)*v_i*t + y_i - y_d)^2)
// For the driver, distance as a function of time is v_d*t.
// Squaring both sides and rearranging gives the quadratic equation:
// (v_i^2 - v_d^2) * t^2 +
// + 2*v_i*(cos(a_i)*(x_i-x_d) + sin(a_i)*(y_i-y_d)) * t +
// + (x_i-x_d)^2 + (y_i-y_d)^2 = 0

int main()
{
   while (true)
   {
      int nn = 0;
      scanf("%d", &nn);
      if (nn == 0)
      {
         break;
      }

      double v_0 = 0.0;
      scanf("%lf", &v_0);
      double v_0_sq = v_0 * v_0;

      vector<double> xs(nn);
      vector<double> ys(nn);
      vector<double> vs(nn);
      vector<double> as(nn);
      vector<double> vxs(nn);
      vector<double> vys(nn);
      vector<double> vs_sq(nn);
      vector<int> idx(nn);
      for (int ii = 0; ii < nn; ++ii)
      {
         scanf("%lf %lf %lf %lf", &xs[ii], &ys[ii], &vs[ii], &as[ii]);
         vxs[ii] = cos(as[ii]) * vs[ii];
         vys[ii] = sin(as[ii]) * vs[ii];
         vs_sq[ii] = vs[ii] * vs[ii];
         idx[ii] = ii;
      }

      double t_min = 10000000.0;
      do
      {
         double x_0 = 0.0;
         double y_0 = 0.0;
         double t_max = 0.0;
         double tt = 0.0;
         for (int ii: idx)
         {
            // Solve quadratic equation.
            double dx = tt*vxs[ii] + xs[ii] - x_0;
            double dy = tt*vys[ii] + ys[ii] - y_0;

            double aa = vs_sq[ii] - v_0_sq;
            double bb = vxs[ii] * dx + vys[ii] * dy;
            double cc = dx*dx + dy*dy;
            double qq = bb*bb - aa*cc;

            if (abs(cc) <= 1e-9)
            {
               tt += 0.0;
            }
            else
            {
               tt += (-sqrt(qq) - bb) / aa;
            }

            // Start next iteration where we ended this one.
            x_0 = vxs[ii] * tt + xs[ii];
            y_0 = vys[ii] * tt + ys[ii];

            // Update t_max using the time for this senior to get back.
            t_max = max(tt + hypot(x_0, y_0) / vs[ii], t_max);
         }

         t_min = min(t_max, t_min);
      } while (next_permutation(idx.begin(), idx.end()));

      printf("%ld\n", lround(t_min));

   }
   return 0;
}
