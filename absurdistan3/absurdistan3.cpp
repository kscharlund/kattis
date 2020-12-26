#include <cstdio>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int n;
vector<int> degree;
vector<vector<int> > edges;

void print_edges()
{
    for (int i = 0; i < n; ++i)
    {
        fprintf(stderr, "%d: ", i + 1);
        for (auto e = edges[i].begin(); e != edges[i].end(); ++e)
            fprintf(stderr, "%d ", *e + 1);
        fprintf(stderr, "\n");
    }
    fprintf(stderr, "\n");
}

int main()
{
    scanf("%d", &n);
    degree.resize(n);
    edges.resize(n);
    vector<int> dst(n, -1);
    int found = 0;

    for (int i = 0; i < n; ++i)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        --a;
        --b;
        ++degree[a];
        ++degree[b];
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    //print_edges();

    queue<int> q;
    for (int i = 0; i < n; ++i)
    {
        if (degree[i] == 1)
        {
            q.push(i);
        }
    }
    if (q.empty())
    {
        // Just start anywhere.
        q.push(0);
    }

    while (!q.empty())
    {
        int s = q.front();
        q.pop();
        if (degree[s] >= 1)
        {
            int d = edges[s].back();
            edges[s].pop_back();
            for (auto it = edges[d].begin(); it != edges[d].end(); ++it)
            {
                if (*it == s)
                {
                    edges[d].erase(it);
                    break;
                }
            }
            dst[s] = d;
            --degree[s];
            --degree[d];
            if (degree[d] == 1)
            {
                q.push(d);
            }
            ++found;
        }

        if (q.empty() && found < n)
        {
            for (int i = 0; i < n; ++i)
            {
                if (dst[i] == -1)
                {
                    q.push(i);
                    break;
                }
            }
        }
        //print_edges();
    }

    for (int i = 0; i < n; ++i)
    {
        printf("%d %d\n", i+1, dst[i]+1);
    }

    return 0;
}
