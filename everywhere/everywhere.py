import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    trips = set()
    for _ in range(n):
        trips.add(sys.stdin.readline().strip())
    print(len(trips))
