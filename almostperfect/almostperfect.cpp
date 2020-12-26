#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int nn;
    while (cin >> nn)
    {
        long long sum = 1;
        for (int dd = 2; dd <= (int)sqrt(nn); ++dd)
        {
            if ((nn % dd) == 0)
            {
                //cerr << nn << " = " << dd << " * " << (nn / dd) << endl;
                sum += dd;
                if (nn / dd != dd)
                {
                    sum += nn / dd;
                }
            }
        }
        //cerr << sum << endl;
        cout << nn;
        if (sum == nn)
        {
            cout << " perfect" << endl;
        }
        else if (abs(sum - nn) < 3)
        {
            cout << " almost perfect" << endl;
        }
        else
        {
            cout << " not perfect" << endl;
        }
    }
    return 0;
}
