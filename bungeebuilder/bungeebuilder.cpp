#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vi hs(n);
    for (int i = 0; i < n; ++i) {
        cin >> hs[i];
    }
    vi mhl(n);
    vi mhr(n);
    mhl[0] = hs[0];
    mhr[n-1] = hs[n-1];
    for (int i = 1; i < n; ++i) {
        mhl[i] = max(mhl[i-1], hs[i]);
        mhr[n - i - 1] = max(mhr[n - i], hs[n - i - 1]);
    }
    int h = 0;
    for (int i = 0; i < n; ++i) {
        h = max(h, min(mhl[i], mhr[i]) - hs[i]);
    }
    cout << h << endl;
    return 0;
}