import sys

n, m, s, d = map(int, sys.stdin.readline().split())
slots = list(enumerate(map(int, sys.stdin.readline().split())))
slots.sort(key=lambda x: -x[1])
refill = {}
while n > 0:
    i, c = slots.pop()
    refill[i] = min(d - c, n)
    n -= refill[i]
remaining = sum(c for i, c in slots)
if remaining < m:
    print('impossible')
else:
    print(' '.join(str(refill.get(i, 0)) for i in range(s)))
