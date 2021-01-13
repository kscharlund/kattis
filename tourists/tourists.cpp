#include <vector>
#include <queue>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef map<pair<int, int>, int> miii;

struct lca_data
{
    int _n;
    vi parent;
    vi rank;
    vi black;
    vi ancestor;

    explicit lca_data(int n) : _n(n), parent(n+1), rank(n+1), black(n+1), ancestor(n+1)
    {
    }

    void dsf_make_set(int x)
    {
        parent[x] = x;
        rank[x] = 1;
    }

    void dsf_union(int x, int y)
    {
        auto xr = dsf_find(x);
        auto yr = dsf_find(y);
        if (rank[xr] > rank[yr])
        {
            parent[yr] = xr;
        }
        else if (rank[yr] > rank[xr])
        {
            parent[xr] = yr;
        }
        else
        {
            parent[yr] = xr;
            rank[xr] += 1;
        }
    }
 
    int dsf_find(int x)
    {
        if (parent[x] != x)
            parent[x] = dsf_find(parent[x]);
        return parent[x];
    }

    void find_ancestors(int r, vvi const &children, vvi &pairs, miii &lca)
    {
        dsf_make_set(r);
        ancestor[r] = r;
        for (int c: children[r])
        {
            find_ancestors(c, children, pairs, lca);
            dsf_union(r, c);
            ancestor[dsf_find(r)] = r;
        }
        black[r] = 1;
        for (int p: pairs[r])
        {
            if (black[p])
            {
                lca[make_pair(min(r, p), max(r, p))] = ancestor[dsf_find(p)];
            }
        }
    }
};


void calc_dists(int r, vvi &children, vi &dists)
{
    queue<int> q;
    q.push(r);
    dists[r] = 0;
    
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        for (int v: children[u])
        {
            q.push(v);
            dists[v] = dists[u] + 1;
            auto it = find(children[v].begin(), children[v].end(), u);
            swap(*it, children[v].back());
            children[v].pop_back();
        }
    }
}

int main()
{
    cin.sync_with_stdio(false);
    int n;
    cin >> n;

    vvi children(n + 1);
    for (int i = 0; i < n - 1; ++i)
    {
        int u, v;
        cin >> u >> v;
        children[u].push_back(v);
        children[v].push_back(u);
    }

    vi dists(n + 1);
    calc_dists(1, children, dists);
    // for (int i = 2; i <= n; ++i)
    // {
    //     cerr << "Dist from 1 to " << i << ": " << dists[i] << endl;
    // }

    lca_data lca(n);
    miii ancestors;
    vvi pairs(n + 1);
    for (int i = 2; i <= n/2; ++i)
    {
        for (int j = 2; j * i <= n; ++j)
        {
            int p = i * j;
            pairs[i].push_back(p);
            pairs[p].push_back(i);
        }
    }
    lca.find_ancestors(1, children, pairs, ancestors);

    long long int sum = 0;
    for (int i = 2; i <= n; ++i)
    {
        sum += dists[i] + 1;
    }
    for (auto &it: ancestors)
    {
        int u = it.first.first, v = it.first.second, a = it.second;
        int d = dists[u] + dists[v] - 2 * dists[a];
        // cerr << "LCA of " << u << " and " << v << " is " << a << endl;
        // cerr << "Dist is " << d << endl;
        sum += d + 1;
    }
    cout << sum << endl;

    return 0;
}
