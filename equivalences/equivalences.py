import sys
from pprint import pprint
sys.setrecursionlimit(200000)

class SCCGraph:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.i_edges = [[] for _ in range(n_nodes)]
        self.o_edges = [[] for _ in range(n_nodes)]
        self.visited = [False for _ in range(n_nodes)]
        self.visited_nodes = []
        self.components = {}
        self.component_assignments = [-1 for _ in range(n_nodes)]

    def add_edge(self, src, dst):
        self.o_edges[src].append(dst)
        self.i_edges[dst].append(src)

    def _visit(self, node):
        if not self.visited[node]:
            self.visited[node] = True
            for v in self.o_edges[node]:
                self._visit(v)
            self.visited_nodes.append(node)

    def _assign(self, node, root):
        if self.component_assignments[node] < 0:
            self.component_assignments[node] = root
            self.components.setdefault(root, []).append(node)
            for v in self.i_edges[node]:
                self._assign(v, root)

    def find_scc(self):
        for u in range(self.n_nodes):
            self._visit(u)
        # pprint(self.visited)
        # pprint(list(reversed(self.visited_nodes)))
        for u in reversed(self.visited_nodes):
            self._assign(u, u)


def main():
    n_cases = int(sys.stdin.readline().strip())
    for _ in range(n_cases):
        n_statements, n_proofs = (int(x) for x in sys.stdin.readline().split() if x)
        graph = SCCGraph(n_statements)
        for _ in range(n_proofs):
            src, dst = (int(x) - 1 for x in sys.stdin.readline().split() if x)
            graph.add_edge(src, dst)
        graph.find_scc()
        # pprint(graph.component_assignments)
        # pprint(graph.components)
        if len(graph.components) == 1:
            print(0)
        else:
            n_zero_i = 0
            n_zero_o = 0
            for root, nodes in graph.components.items():
                i_degree = sum(len([e for e in graph.i_edges[node] if graph.component_assignments[e] != root]) for node in nodes)
                o_degree = sum(len([e for e in graph.o_edges[node] if graph.component_assignments[e] != root]) for node in nodes)
                if i_degree == 0:
                    n_zero_i += 1
                if o_degree == 0:
                    n_zero_o += 1
            print(max(n_zero_i, n_zero_o))

main()
