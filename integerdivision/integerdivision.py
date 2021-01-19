import sys
from collections import defaultdict

n, d = map(int, sys.stdin.readline().split())
ns = map(int, sys.stdin.readline().split())
hist = defaultdict(int)
for a in ns:
    hist[a // d] += 1
print(sum(c * (c - 1) // 2 for c in hist.values()))
