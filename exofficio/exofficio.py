import sys
from pprint import pprint

def adj(u, r, c, visited):
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        v = (u[0] + dr, u[1] + dc)
        if 0 <= v[0] < r and 0 <= v[1] < c and v not in visited:
            yield v

r, c = map(int, sys.stdin.readline().split())

# Find the minimum diameter spanning tree.
# Because of the particular structure of the problem, this is easier than
# normal. Since the problem is symmetrical and all edge weights are 1, the
# center of the graph is either in the middle node (if R and C are odd),
# the middle edge (if R or C is odd) or an arbitrary edge as close to the middle
# as possible (if R and C are even).
# Notes on the general MDST problem in the description of problem C in
# https://web.archive.org/web/20160309101249/https://adn.botao.hu/adn-backup/blog/attachments/month_0705/32007531153238.pdf.
# Also, since the edge weigths are 1, a Shortest Path Tree is actually just a
# BFS tree.

edges = set()
visited = set()
queue = []

m = ((r - 1) // 2, (c - 1) // 2)
visited.add(m)
queue.append(m)
if not c % 2:
    m2 = ((r - 1) // 2, c // 2)
    edges.add((m, m2))
    visited.add(m2)
    queue.append(m2)

while queue:
    u = queue.pop(0)
    for v in adj(u, r, c, visited):
        visited.add(v)
        edges.add((min(u, v), max(u, v)))
        queue.append(v)

print(' _' * c)
for y in range(r):
    sys.stdout.write('|')
    for x in range(c):
        sys.stdout.write(' ' if ((y, x), (y + 1, x)) in edges else '_')
        sys.stdout.write(' ' if ((y, x), (y, x + 1)) in edges else '|')
    sys.stdout.write('\n')
