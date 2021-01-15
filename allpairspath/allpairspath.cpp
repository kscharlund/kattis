#include <iostream>
#include <vector>

using namespace std;

static const int INF = 10000000;

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    while (true)
    {
        int n, m, q;
        cin >> n >> m >> q;
        if (!(n || m || q)) {
            break;
        }

        // Read graph.
        vector<int> dist(n*n, INF);
        for (int i = 0; i < n; ++i) {
            dist[i*n + i] = 0;
        }
        for (int i = 0; i < m; ++i) {
            int u, v, w;
            cin >> u >> v >> w;
            // min because there may be several edges between u and v.
            dist[u*n + v] = min(dist[u*n + v], w);
        }

        // Floyd-Warshall all pairs shortest path.
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (dist[i*n + k] < INF && dist[k*n + j] < INF) {
                        dist[i*n + j] = min(dist[i*n + j], dist[i*n + k] + dist[k*n + j]);
                    }
                }
            }
        }

        // Propagate negative cycles.
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; dist[i*n + j] != -INF && k < n; ++k) {
                    if (dist[i*n + k] < INF && dist[k*n + j] < INF && dist[k*n + k] < 0) {
                        dist[i*n + j] = -INF;
                    }
                }
            }
        }

        // Process queries.
        for (int i = 0; i < q; ++i) {
            int u, v;
            cin >> u >> v;
            if (dist[u*n + v] == -INF) {
                cout << "-Infinity\n";
            } else if (dist[u*n + v] == INF) {
                cout << "Impossible\n";
            } else {
                cout << dist[u*n + v] << "\n";
            }
        }
        cout << "\n";
    }
    return 0;
}
