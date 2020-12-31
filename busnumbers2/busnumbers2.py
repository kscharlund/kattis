import sys
from collections import defaultdict
from math import ceil
from pprint import pprint


def gen_cubes(m):
    max_n = ceil(m ** (1/3))
    return [n ** 3 for n in range(1, max_n)]


def get_largest_bus_number(cubes, m):
    n = len(cubes)
    num_sums = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n):
            s = cubes[i] + cubes[j]
            if s <= m:
                num_sums[s] += 1
    bus_numbers = [k for k, c in num_sums.items() if c > 1]
    return max(bus_numbers) if bus_numbers else 'none'


m = int(sys.stdin.readline().strip())
print(get_largest_bus_number(gen_cubes(m), m))
