import sys
import math

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
        return Point(self.x * p, self.y * p)

    def __rmul__(self, p):
        return self.__mul__(p)

    def __truediv__(self, p):
        if isinstance(p, Point):
            den = p.x * p.x + p.y * p.y
            return Point(
                (self.x * p.x + self.y * p.y) / den,
                (self.y * p.x - self.x * p.y) / den
            )
        return Point(self.x / p, self.y / p)

    def abs(self):
        return math.hypot(self.x, self.y)

    def dot(self, p):
        return self.x * p.x + self.y * p.y

    def cross(self, p):
        return self.x * p.y - self.y * p.x

def transform(p, q, r, fp, fq):
    # Given p, q, f(p) and f(q) where f is a linear transformation,
    # return f(r)
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

    vectors = [p2 - p1 for p1, p2 in zip(points[:-1], points[1:])]
    lengths = [v.abs() for v in vectors]
    total_length = sum(lengths)
    total_vector = points[-1] - points[0]

    d = fraction * total_length
    r = points[0]
    trans = Point(1, 0)
    scale = 1
    for level in range(1, depth + 1):
        for i in range(n_points - 1):
            if d < scale * lengths[i] + 1e-10:
                break
            d -= scale * lengths[i]
            r += trans * vectors[i]
        else:
            raise ValueError('Fraction > 1?')

        if level == depth:
            r += d * (trans * vectors[i]) / (scale * lengths[i])

        trans *= vectors[i] / total_vector
        scale *= lengths[i] / total_length

    print(r.x, r.y)
