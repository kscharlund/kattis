#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;

vi cache;
int greedy(vi const &coins, int x)
{
    if (cache[x] >= 0)
    {
        return cache[x];
    }
    if (x == 0)
        return 0;
    int i = 1;
    while (i < (int)coins.size() && coins[i] <= x)
    {
        ++i;
    }
    int ret = greedy(coins, x - coins[i-1]) + 1;
    cache[x] = ret;
    return ret;
}

/*
 * Reference: Optimal Bounds for the Change-Making Problem, Kozen and Zaks.
 * https://www.cs.cornell.edu/~kozen/Papers/change.pdf
 */

int main()
{
    cin.sync_with_stdio(false);

    int m;
    cin >> m;
    vi coins(m);
    for (int i = 0; i < m; ++i)
    {
        cin >> coins[i];
    }
    if (m < 3)
    {
        cout << "canonical" << endl;
    }
    else
    {
        bool canonical = true;
        int lb = coins[2] + 1, ub = coins[m-1] + coins[m-2];
        cache.resize(ub, -1);
        for (int x = lb + 1; canonical && x < ub; ++x)
        {
            int g = greedy(coins, x);
            for (int c: coins) {
                if (c > x)
                {
                    break;
                }
                int g_c = greedy(coins, x - c);
                if (g - g_c > 1)
                {
                    canonical = false;
                    break;
                }
            }
        }
        cout << (canonical ? "canonical" : "non-canonical") << endl;
    }

    return 0;
}