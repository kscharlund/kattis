import sys
import math

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, l, d, g = map(int, sys.stdin.readline().split())
    print(
        0.25 * l * l * n / math.tan(math.pi / n)  # Original n-gon.
        + n * d * g * l                           # Rectangular land grab.
        + math.pi * (d * g) ** 2                  # Circular land grab.
    )
