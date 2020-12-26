#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <map>

using namespace std;

typedef vector<vector<int> > vvi;

struct Graph {
    int n_nodes;
    vvi i_edges;
    vvi o_edges;
    vector<char> visited;
    vector<int> visited_nodes;
    map<int, vector<int> > components;
    vector<int> component_assignments;

    Graph(int n_nodes)
    {
        this->n_nodes = n_nodes;
        i_edges.resize(n_nodes);
        o_edges.resize(n_nodes);
        visited.resize(n_nodes);
        visited_nodes.reserve(n_nodes);
        component_assignments.resize(n_nodes, -1);
    }

    void add_edge(int src, int dst)
    {
        o_edges[src].push_back(dst);
        i_edges[dst].push_back(src);
    }

    void visit(int node)
    {
        if (!visited[node])
        {
            visited[node] = 1;
            for (int v: o_edges[node])
                visit(v);
            visited_nodes.push_back(node);
        }
    }

    void assign(int node, int root)
    {
        if (component_assignments[node] < 0)
        {
            component_assignments[node] = root;
            components[root].push_back(node);
            for (int v: i_edges[node])
                assign(v, root);
        }
    }

    void find_scc()
    {
        for (int u = 0; u < n_nodes; ++u)
            visit(u);
        for (auto uit = visited_nodes.rbegin(); uit != visited_nodes.rend(); ++uit)
            assign(*uit, *uit);
    }
};

int main()
{
    int n_cases;
    cin >> n_cases;
    for (int ii = 0; ii < n_cases; ++ii)
    {
        int n_nodes, n_edges;
        cin >> n_nodes >> n_edges;
        Graph graph(n_nodes);
        for (int jj = 0; jj < n_edges; ++jj)
        {
            int src, dst;
            cin >> src >> dst;
            graph.add_edge(src-1, dst-1);
        }
        graph.find_scc();
        if (graph.components.size() == 1)
        {
            cout << 0 << endl;
        }
        else
        {
            int n_zero_o = 0;
            int n_zero_i = 0;
            for (auto it = graph.components.begin(); it != graph.components.end(); ++it)
            {
                int i_degree = 0;
                int o_degree = 0;
                for (int node: it->second)
                {
                    for (int src: graph.i_edges[node])
                        if (graph.component_assignments[src] != it->first)
                            i_degree++;
                    for (int dst: graph.o_edges[node])
                        if (graph.component_assignments[dst] != it->first)
                            o_degree++;
                }
                if (i_degree == 0)
                    n_zero_i += 1;
                if (o_degree == 0)
                    n_zero_o += 1;
            }
            cout << (max(n_zero_i, n_zero_o)) << endl;
        }
    }
    return 0;
}
