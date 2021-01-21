import sys

n = int(sys.stdin.readline().strip())
ts = list(map(int, sys.stdin.readline().split()))
maxs = [max(t1, t2) for t1, t2 in zip(ts[:-2], ts[2:])]
min_max = maxs[0]
min_i = 0
for i, m in enumerate(maxs[1:]):
    if m < min_max:
        min_i, min_max = i + 1, m
print(min_i + 1, min_max)
