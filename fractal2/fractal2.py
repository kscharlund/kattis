import sys
import math
from collections import namedtuple
from bisect import bisect_left
from pprint import pprint

#Point = namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        if isinstance(p, Point):
            return Point(
                self.x * p.x - self.y * p.y,
                self.x * p.y + self.y * p.x
            )
        return self.scale(p)

    def __rmul__(self, p):
        return self.__mul__(p)

    def __truediv__(self, p):
        if isinstance(p, Point):
            den = p.x * p.x + p.y * p.y
            return Point(
                (self.x * p.x + self.y * p.y) / den,
                (self.y * p.x - self.x * p.y) / den
            )
        return self.scale(1 / p)

    def abs(self):
        return math.hypot(self.x, self.y)

    def scale(self, a):
        return Point(self.x * a, self.y * a)

    def dot(self, p):
        return self.x * p.x + self.y * p.y

    def cross(self, p):
        return self.x * p.y - self.y * p.x

def transform(p, q, r, fp, fq):
    pr = r - p
    pq = q - p
    fpq = fq - fp
    return fp + pr * fpq / pq

n_cases = int(sys.stdin.readline().strip())
for _ in range(n_cases):
    n_points = int(sys.stdin.readline().strip())
    points = [
        Point(*map(int, sys.stdin.readline().split())) for _ in range(n_points)
    ]
    depth = int(sys.stdin.readline().strip())
    fraction = float(sys.stdin.readline().strip())

    lengths = [(p2 - p1).abs() for p1, p2 in zip(points[:-1], points[1:])]
    total_length = sum(lengths)

    dist_left = fraction * total_length
    res = points[0]
    p0, q0 = points[0], points[-1]
    p, q = p0, q0
    scale = 1
    for level in range(1, depth + 1):
        for i in range(len(lengths)):
            if dist_left < scale * lengths[i]:
                break
            dist_left -= scale * lengths[i]
            res += transform(p0, q0, points[i+1], p, q) - transform(p0, q0, points[i], p, q)

        p, q = transform(p0, q0, points[i], p, q), transform(p0, q0, points[i+1], p, q)
        if level == depth:
            res += (dist_left / (scale * lengths[i])) * (q - p)
        scale = scale * lengths[i] / total_length

    print(res.x, res.y)
