#include <cstdio>
#include <stack>

using namespace std;

#define V(g, y, x) (g[y * 1000 + x])
static int graph[1000 * 1000] = {0};
static int component[1000 * 1000] = {0};
static char buf[1001];
static int nRows;
static int nCols;
static int nComponents = 0;

typedef pair<int, int> rc;

bool check(int r, int c, int t)
{
    return r >= 0 && r < nRows && c >= 0 && c < nCols && V(graph, r, c) == t && V(component, r, c) == 0;
}

void find_component(int r, int c, int l)
{
    V(component, r, c) = l;
    // fprintf(stderr, "Labelling %d, %d = %d\n", r, c, l);
    int t = V(graph, r, c);
    if (check(r - 1, c, t))
    {
        find_component(r - 1, c, l);
    }
    if (check(r + 1, c, t))
    {
        find_component(r + 1, c, l);
    }
    if (check(r, c - 1, t))
    {
        find_component(r, c - 1, l);
    }
    if (check(r, c + 1, t))
    {
        find_component(r, c + 1, l);
    }
}

int main()
{
    scanf("%d %d", &nRows, &nCols);
    for (int r = 0; r < nRows; ++r)
    {
        scanf("%s", buf);
        for (int c = 0; c < nCols; ++c)
        {
            V(graph, r, c) = buf[c] - '0';
            // fprintf(stderr, "%d", V(graph, r, c));
        }
        // fprintf(stderr, "\n");
    }

    for (int r = 0; r < nRows; ++r)
    {
        for (int c = 0; c < nCols; ++c)
        {
            if (V(component, r, c) == 0)
            {
                // fprintf(stderr, "label %d %d\n", r, c);
                find_component(r, c, ++nComponents);
            }
        }
    }

    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
    {
        int sr, sc, er, ec;
        scanf("%d %d %d %d", &sr, &sc, &er, &ec);
        --sr;
        --sc;
        --er;
        --ec;
        if (V(component, sr, sc) == V(component, er, ec))
        {
            printf("%s\n", V(graph, sr, sc) ? "decimal" : "binary");
        }
        else
        {
            printf("neither\n");
        }
    }

    return 0;
}
