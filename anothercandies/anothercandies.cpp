#include <iostream>

using namespace std;

int main()
{
    int n_cases;
    cin >> n_cases;
    for (int ii = 0; ii < n_cases; ++ii)
    {
        unsigned long long n_children;
        cin >> n_children;
        unsigned long long sum = 0;
        for (unsigned long long jj = 0; jj < n_children; ++jj)
        {
            unsigned long long candies;
            cin >> candies;
            sum = (sum + candies) % n_children;
        }
        if (sum)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
    }
    return 0;
}