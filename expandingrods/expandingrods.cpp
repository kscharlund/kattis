#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;

static const int N_LUT_STEPS = 10000;

/*
 * Generate lookup table of x/s for different values of alpha.
 *
 * Derivation:
 *  s = r * alpha
 *  x = 2 * r * sin(alpha/2)
 *  x / s = 2 * r * sin(alpha/2) / (r * alpha) = sin(alpha / 2) / (alpha / 2)
 *
 * Using x / s and this LUT, we find an approximate value of alpha / 2.
 */
vd generate_x_s_lut()
{
    vd res;
    res.reserve(N_LUT_STEPS);
    for (int i = 1; i <= N_LUT_STEPS; ++i) {
        double alpha_2 = i * M_PI / (2 * N_LUT_STEPS);
        res.push_back(sin(alpha_2) / alpha_2);
    }
    return res;
}

/*
 * Refine (alpha/2) using Newton-Raphson.
 * f(alpha/2) = sin(alpha/2) - (x/s) * (alpha/2)
 * f'(alpha/2) = cos(alpha/2) - (x/s)
 */
double refine_alpha_2(double x_s, double guess)
{
    double res = 0.0;
    // int it = 0;
    while (true) {
        double f = sin(guess) - x_s * guess;
        double fp = cos(guess) - x_s;
        res = guess - f / fp;
        // cerr << "it " << (++it) << ": " << guess << " -> " << res << endl;
        if (fabs(guess - res) < 1e-8)
            break;
        guess = res;
    }
    return res;
}

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);

    while (true) {
        double x, n, C;
        cin >> x >> n >> C;
        if (x < 0)
            break;

        double s = x * (1.0 + n * C);
        double x_s = x / s;
        if (fabs(x_s - 1.0) < 1e-7) {
            cout << fixed << setprecision(9) << 0.0 << "\n";
            continue;
        }

        vd lut = generate_x_s_lut();
        auto pos = lower_bound(lut.begin(), lut.end(), x_s, greater<double>());
        double alpha_2 = distance(lut.begin(), pos) * M_PI / (2 * N_LUT_STEPS);
        alpha_2 = refine_alpha_2(x_s, alpha_2);
        double r = s / (2.0 * alpha_2);
        double h = r * (1 - cos(alpha_2));
        cout << fixed << setprecision(9) << h << "\n";
    }

    return 0;
}
