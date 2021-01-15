#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
static const int INF = 10000;

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    for (int x = 0; x < n; ++x) {
        int m;
        cin >> m;
        vi ds(m);
        vvi dp(m);
        vvi ud(m);
        for (int i = 0; i < m; ++i) {
            cin >> ds[i];
            dp[i].resize(1000, INF);
            ud[i].resize(1000);
        }
        int max_h = accumulate(ds.begin(), ds.end(), 0);
        dp[0][ds[0]] = ds[0];
        ud[0][ds[0]] = 1;
        for (int i = 1; i < m; ++i) {
            for (int h = 0; h < max_h; ++h) {
                if (dp[i-1][h] != INF) {
                    if (h >= ds[i] && dp[i-1][h] < dp[i][h - ds[i]]) {
                        dp[i][h - ds[i]] = dp[i-1][h];
                        ud[i][h - ds[i]] = -1;
                    }
                    dp[i][h + ds[i]] = max(dp[i-1][h], h + ds[i]);
                    ud[i][h + ds[i]] = 1;
                }
            }
        }
        if (dp[m-1][0] == INF) {
            cout << "IMPOSSIBLE\n";
        } else {
            int h = 0;
            string ans;
            for (int i = m - 1; i >= 0; --i) {
                ans = (ud[i][h] < 0 ? "D" : "U") + ans;
                h -= ud[i][h] * ds[i];
            }
            cout << ans << "\n";
        }
    }
}