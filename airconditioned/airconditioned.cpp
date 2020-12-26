#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> minion;

int main()
{
    int n_minions;
    cin >> n_minions;
    vector<minion> minions;
    minions.reserve(n_minions);
    for (int ii = 0; ii < n_minions; ++ii)
    {
        int lb, ub;
        cin >> lb >> ub;
        // Note upper bound first, to sort by.
        minions.push_back(minion(ub, lb));
    }
    sort(minions.begin(), minions.end());
    int max_covered = 0;
    int n_rooms = 0;
    for (int ii = 0; ii < n_minions; ++ii)
    {
        if (minions[ii].second <= max_covered)
        {
            continue;
        }
        ++n_rooms;
        max_covered = minions[ii].first;
    }
    cout << n_rooms << endl;
    return 0;
}