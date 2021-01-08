#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main()
{
    while (true)
    {
        int n;
        scanf("%d", &n);
        if (n < 0)
            break;
        vector<vi> adj(n);
        vi weights(n);
        for (int i = 0; i < n; ++i)
        {
            int w, c, e;
            scanf("%d %d", &w, &c);
            for (int j = 0; j < c; ++j)
            {
                scanf("%d", &e);
                adj[i].push_back(e - 1);
            }
            weights[i] = -w;
        }

        const int inf_distance = 1000000;
        vi distance(n, inf_distance);
        distance[0] = -100;
        for (int i = 0; i < n - 1; ++i)
        {
            for (int u = 0; u < n; ++u)
            {
                if (distance[u] < inf_distance)
                {
                    for (int v: adj[u])
                    {
                        int dist = distance[u] + weights[v];
                        if (dist < distance[v] && dist < 0)
                        {
                            // dist < 0 check ensures we only propagate valid
                            // paths.
                            distance[v] = dist;
                        }
                    }
                }
            }
        }

#if 0
        for (int i = 0; i < n; ++i)
            fprintf(stderr, "distance[%d] = %d\n", i, distance[i]);
        fprintf(stderr, "Negative cycle detection:\n");
#endif

        bool stable = false;
        while (!stable)
        {
            stable = true;
            // Detect and propagate negative weight cycles forward, setting
            // distance to -inf.
            for (int u = 0; u < n; ++u)
            {
                if (distance[u] < inf_distance)
                {
                    for (int v: adj[u])
                    {
                        int dist = distance[u] + weights[v];
                        if (dist < distance[v]
                            && dist < 0
                            && distance[v] != -inf_distance)
                        {
                            distance[v] = -inf_distance;
                            stable = false;
                        }
                    }
                }
            }
        }

#if 0
        for (int i = 0; i < n; ++i)
            fprintf(stderr, "distance[%d] = %d\n", i, distance[i]);
#endif

        if (distance[n - 1] < 0)
        {
            printf("winnable\n");
        }
        else
        {
            printf("hopeless\n");
        }
    }

    return 0;
}
