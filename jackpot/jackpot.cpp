#include <iostream>
#include <vector>

using namespace std;

typedef vector<long long int> vi;

template <typename T>
T gcd(T a, T b) {
    while (b) {
        T t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int w;
        cin >> w;
        vi wheels(w);
        for (int j = 0; j < w; ++j) {
            cin >> wheels[j];
        }
        if (w < 2) {
            cout << wheels[0] << "\n";
            continue;
        }
        long long int gcf = wheels[0] * wheels[1] / gcd(wheels[0], wheels[1]);
        for (int k = 1; gcf < 1000000000 && k < w; ++k) {
            gcf = gcf * wheels[k] / gcd(gcf, wheels[k]);
        }

        if (gcf > 1000000000) {
            cout << "More than a billion.\n";
        } else {
            cout << gcf << "\n";
        }
    }
    return 0;
}