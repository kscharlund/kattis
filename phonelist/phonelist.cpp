#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int nCases;
    cin >> nCases;
    for (int ii = 0; ii < nCases; ++ii)
    {
        int nLines;
        cin >> nLines;
        vector<string> numbers;
        for (int jj = 0; jj < nLines; ++jj)
        {
            string number;
            cin >> number;
            numbers.push_back(number);
        }
        sort(numbers.begin(), numbers.end());
        bool ok = true;
        for (int jj = 0; jj < nLines - 1; ++jj)
        {
            if (!numbers[jj+1].compare(0, numbers[jj].length(), numbers[jj]))
            {
                ok = false;
                break;
            }
        }
        cout << (ok ? "YES" : "NO") << endl;
    }
    return 0;
}