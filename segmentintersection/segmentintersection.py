import sys
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])


def area_sign(p1, p2, p3):
    area_2 = (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y)
    # print(p1, p2, p3, area_2, file=sys.stderr)
    if area_2 > 0.5:
        return 1
    elif area_2 < -0.5:
        return -1
    else:
        return 0


def collinear(p1, p2, p3):
    return area_sign(p1, p2, p3) == 0


def between(p1, p2, p3):
    if p1.x != p2.x:
        return p1.x <= p3.x <= p2.x or p2.x <= p3.x <= p1.x
    else:
        return p1.y <= p3.y <= p2.y or p2.y <= p3.y <= p1.y


def parallel(p1, p2, p3, p4):
    if p1 == p2:
        if p3 == p4:
            if p1 == p3:
                # All points are identical.
                return p1
            else:
                # Two different points.
                return None
        else:
            # p1 and p2 are the same, but not p3 and p4.
            # Swap the pairs to avoid problems in `collinear`.
            p1, p2, p3, p4 = p3, p4, p1, p2

    if not collinear(p1, p2, p3):
        return None

    if between(p1, p2, p3):
        if between(p1, p2, p4):
            return (p3, p4)
        if between(p3, p4, p1):
            return (p3, p1)
        if between(p3, p4, p2):
            return (p3, p2)
        raise ValueError('Unexpected configuration')
    if between(p1, p2, p4):
        if between(p3, p4, p1):
            return (p4, p1)
        if between(p3, p4, p2):
            return (p4, p2)
        raise ValueError('Unexpected configuration')
    if between(p3, p4, p1) and between(p3, p4, p2):
        return (p1, p2)

    return None


def intersection(p1, p2, p3, p4):
    """
    Calculate intersection between the line segments p1-p2 and p3-p4.

    If they intersect in a line (i e they are collinear and overlap), return
    a tuple of start and end points for the intersection.

    If there is no intersection, return None.

    See e g https://en.wikipedia.org/wiki/Line–line_intersection for
    derivations of these expressions.
    Also, O'Rourke (1997): Computational Geometry in C, 2 ed.
    """
    denom = (
        p1.x * (p4.y - p3.y) +
        p2.x * (p3.y - p4.y) +
        p4.x * (p2.y - p1.y) +
        p3.x * (p1.y - p2.y)
    )
    if not denom:
        return parallel(p1, p2, p3, p4)

    num_t = (
        p1.x * (p4.y - p3.y) +
        p3.x * (p1.y - p4.y) +
        p4.x * (p3.y - p1.y)
    )
    t = num_t / denom

    num_u = -(
        p1.x * (p3.y - p2.y) +
        p2.x * (p1.y - p3.y) +
        p3.x * (p2.y - p1.y)
    )
    u = num_u / denom

    if t < 0 or t > 1 or u < 0 or u > 1:
        return None

    return Point(p1.x + t * (p2.x - p1.x), p1.y + t * (p2.y - p1.y))


def main():
    n_cases = int(sys.stdin.readline().strip())
    for _ in range(n_cases):
        x1, y1, x2, y2, x3, y3, x4, y4 = (int(x) for x in sys.stdin.readline().split())
        res = intersection(
            Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)
        )
        if res is None:
            print('none')
        elif isinstance(res, Point):
            print(f'{res.x:.2f} {res.y:.2f}')
        else:
            p1, p2 = res
            if abs(p1.x - p2.x) < 1e-4 and abs(p1.y - p2.y) < 1e-4:
                # Note: could use p1 == p2 here as long as all input coordinates
                # are integers (which they are in this problem).
                print(f'{p1.x:.2f} {p1.y:.2f}')
            else:
                if p1.x < p2.x:
                    print(f'{p1.x:.2f} {p1.y:.2f} {p2.x:.2f} {p2.y:.2f}')
                elif p2.x < p1.x:
                    print(f'{p2.x:.2f} {p2.y:.2f} {p1.x:.2f} {p1.y:.2f}')
                elif p1.y < p2.y:
                    print(f'{p1.x:.2f} {p1.y:.2f} {p2.x:.2f} {p2.y:.2f}')
                else:
                    print(f'{p2.x:.2f} {p2.y:.2f} {p1.x:.2f} {p1.y:.2f}')


main()
