#include <vector>
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> hs;
    hs.reserve(n);
    for (int i = 0; i < n; ++i)
    {
        int h;
        cin >> h;
        hs.push_back(h);
    }

    vector<vector<int> > halfs(n);
    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            if (2 * hs[j] <= hs[i])
            {
                halfs[i].push_back(j);
            }
        }
    }

    long long int count = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < halfs[i].size(); ++j)
        {
            int k = halfs[i][j];
            count += halfs[k].size();
        }
    }

    cout << count << endl;

    return 0;
}