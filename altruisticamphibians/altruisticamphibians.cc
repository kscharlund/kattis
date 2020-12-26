#include <vector>
#include <iostream>
#include <algorithm>
#include <tuple>

using namespace std;

static int heights[200000001] = {0};

typedef tuple<int, int, int> Frog;

int main()
{
    int n, d;
    cin >> n >> d;
    vector<Frog> frogs;
    frogs.reserve(size_t(n));
    for (int ii = 0; ii < n; ++ii)
    {
        int l, w, h;
        cin >> l >> w >> h;
        frogs.push_back(Frog(w, l, h));
    }
    sort(frogs.begin(), frogs.end(), std::greater<Frog>());
    int n_escaped = 0;
    for (Frog frog : frogs)
    {
        int w, l, h;
        tie(w, l, h) = frog;
        if (l + heights[w] > d)
        {
            ++n_escaped;
        }
        for (int ii = 0; ii < w; ++ii)
        {
            heights[ii] = max(heights[ii], heights[ii + w] + h);
        }
    }
    cout << n_escaped << endl;
    return 0;
}