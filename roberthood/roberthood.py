import sys
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return math.hypot(p2.x - self.x, p2.y - self.y)

    def __lt__(self, p2):
        return self.y < p2.y or (self.y == p2.y and self.x < p2.x)

    def __eq__(self, p2):
        return self.y == p2.y and self.x == p2.x

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

# Three points are a counter-clockwise turn if orientation > 0, clockwise if
# orientation < 0, and collinear if orientation = 0 because orientation is a
# determinant that gives twice the signed area of the triangle formed by
# p1, p2 and p3.
def orientation(p1, p2, p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)


class AngleComparator:
    def __init__(self, min_point, this_point):
        self.pm = min_point
        self.p1 = this_point

    def __lt__(self, comp):
        tmp = orientation(self.pm, self.p1, comp.p1)
        return tmp > 0 or (tmp == 0 and self.pm.dist(self.p1) < self.pm.dist(comp.p1))


def convex_hull(points):
    # Make sure points are unique and that there are enough points.
    #points = list(set(points))
    if len(points) <= 2:
        return points

    # Find min point in terms of y coordinate.
    min_point, i = min(zip(points, range(len(points))))
    points.pop(i)

    # Sort by angle relative to min point.
    points.sort(key=lambda x: AngleComparator(min_point, x))

    # Initialize candidate hull to be the first three points that are not
    # collinear, including min_point. Leave the remaining untested points as
    # candidates.
    p1 = points[0]
    for i2 in range(1, len(points)):
        p2 = points[i2]
        if orientation(min_point, p1, p2) == 0:
            p1 = p2
        else:
            break
    else:
        # All points are collinear.
        return [min_point, p1]
    hull = [min_point, p1, p2]
    points = points[i2+1:]

    # Add min point as last candidate to finalize hull correctly.
    points.append(min_point)
    # Add each candidate in order and see which points can be eliminated.
    for point in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    # Pop sentinel min_point, since we don't need a closed circuit.
    hull.pop()

    print(len(hull), file=sys.stderr)
    return hull


def max_pairwise_dist(points):
    max_dist = 0.0
    hull = convex_hull(points)
    for ii, p1 in enumerate(hull):
        for jj, p2 in enumerate(hull):
            if ii != jj:
                dist = math.hypot(p2.x - p1.x, p2.y - p1.y)
                if dist > max_dist:
                    max_dist = dist
    return max_dist


def main():
    n_points = int(sys.stdin.readline())
    points = []
    for line in sys.stdin:
        x, y = (int(c) for c in line.split())
        points.append(Point(x, y))
    assert len(points) == n_points
    print(max_pairwise_dist(points))


if __name__ == '__main__':
    main()
