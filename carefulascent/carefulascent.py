import sys

gx, gy = (int(x) for x in sys.stdin.readline().split())
n = int(sys.stdin.readline().strip())
shields = []
for _ in range(n):
    l, u, f = sys.stdin.readline().split()
    shields.append((int(l), int(u), float(f)))
shields.sort()
y = 0
ratio = 0
while shields:
    l, u, f = shields.pop()
    ratio += l - y
    ratio += (u - l) * f
    y = u
ratio += gy - y
print(gx / ratio)
