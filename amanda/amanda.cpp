#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

static const int UNKNOWN = -1;
static const int RED = 0;
static const int BLUE = 1;

int n;
int m;
int b = 0;
vector<int> res;
vector<set<int>> edges;

bool resolve(int i, int t)
{
    //fprintf(stderr, "Resolving %d as %d\n", i, t);
    if (res[i] == UNKNOWN)
    {
        res[i] = t;
        b += t;
        return true;
    }
    else
    {
        return res[i] == t;
    }
}

bool twocolor(int s, int *nr, int *nb)
{
    queue<int> q;
    q.push(s);
    res[s] = RED;
    //fprintf(stderr, "%d = %d\n", s, RED);
    ++(*nr);

    while (!q.empty())
    {
        int i = q.front();
        int c = res[i];
        q.pop();
        //fprintf(stderr, "Popping %d = %d\n", i, c);

        for (auto it = edges[i].begin(); it != edges[i].end(); ++it)
        {
            //fprintf(stderr, "Edge %d = %d -> %d = %d\n", i, c, *it, res[*it]);
            if (res[*it] == UNKNOWN)
            {
                q.push(*it);
                res[*it] = (c == RED) ? BLUE : RED;
                //fprintf(stderr, "%d = %d\n", *it, (c == RED) ? BLUE : RED);
                if (c == RED)
                {
                    ++(*nb);
                }
                else
                {
                    ++(*nr);
                }
            }
            else if (res[*it] == c)
            {
                // Failed two-coloring
                //fprintf(stderr, "%d = %d but %d = %d\n", i, c, *it, res[*it]);
                return false;
            }
        }
    }

    //fprintf(stderr, "OK twocolor, nr = %d, nb = %d\n", *nr, *nb);

    return true;
}

int main()
{
    scanf("%d %d", &n, &m);
    res.resize(n+1, UNKNOWN);
    edges.resize(n+1);
    set<int> q;

    // Apply 0- and 2-edges. Save 1-edges.
    for (int i = 0; i < m; ++i)
    {
        int src, dst, t;
        scanf("%d %d %d", &src, &dst, &t);
        if (t == 1)
        {
            edges[src].insert(dst);
            edges[dst].insert(src);
            //fprintf(stderr, "Saving %d -> %d\n", src, dst);
        }
        else
        {
            if (resolve(src, t ? 1 : 0) && resolve(dst, t ? 1 : 0))
            {
                q.insert(src);
                q.insert(dst);
            }
            else
            {
                printf("impossible\n");
                return 0;
            }
        }
    }

    // Resolve 1-edges from known nodes, pushing new known nodes when created.
    while (!q.empty())
    {
        auto srcit = q.begin();
        for (auto it = edges[*srcit].begin(); it != edges[*srcit].end(); ++it)
        {
            if (res[*it] == UNKNOWN)
            {
                (void)resolve(*it, res[*srcit] ? 0 : 1);
                q.insert(*it);
            }
            else if (res[*it] == res[*srcit])
            {
                printf("impossible\n");
                return 0;
            }
        }
        q.erase(srcit);
    }

    // Two-color 1-connected components.
    for (int i = 0; i < n; ++i)
    {
        if (res[i] == -1 && !edges[i].empty())
        {
            int nr = 0, nb = 0;
            if (twocolor(i, &nr, &nb))
            {
                b += min(nr, nb);
            }
            else
            {
                printf("impossible\n");
                return 0;
            }
        }
    }

    printf("%d\n", b);
    return 0;
}