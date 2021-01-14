#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int main()
{
    int n;
    cin >> n;

    vvi adj(n);
    vvi dp(n);
    for (int i = 0; i < n; ++i) {
        adj[i].resize(n);
        dp[i].resize(n);
        for (int j = 0; j < n; ++j) {
            cin >> adj[i][j];
        }
    }

    // Max number of runners from i to i + 1 is 1 if there is an edge.
    for (int i = 0; i < n - 1; ++i)
        dp[i][i + 1] = adj[i][i + 1];

    for (int d = 2; d < n; ++d) {
        // For increasing intervals, move along the polygon and find the best
        // ways starting in each node.
        for (int l = 0; l + d < n; ++l) {
            int r = l + d;
            for (int k = l; k <= r; ++k) {
                // Use the best edge starting in l and going at most to r,
                // counting edges that are under it as well as to the right
                // of it.
                int under = k > l ? dp[l+1][k-1] : 0;
                int right = k < r ? dp[k+1][r] : 0;
                dp[l][r] = max(dp[l][r], under + right + adj[l][k]);
            }
        }
    }

    cout << dp[0][n-1] << endl;
}
