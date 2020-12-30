import sys
from collections import defaultdict
from pprint import pprint

n = int(sys.stdin.readline())
hs = [int(x) for x in sys.stdin.readline().split()]

halfs = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        if 2 * hs[j] <= hs[i]:
            halfs[i].append(j)

count = 0
for i in halfs:
    for j in halfs[i]:
        count += len(halfs.get(j, []))
print(count)
