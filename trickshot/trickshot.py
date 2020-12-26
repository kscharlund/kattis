import sys
import math

EPS = 1e-16

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)


def impact_point(p1, p2, r):
    '''
    Return the point where a ball needs to impact the ball at p1 in order for
    the impacted ball to end up at p2.
    '''
    dx = -(p2.x - p1.x)
    dy = -(p2.y - p1.y)
    dst = 2 * r / (math.hypot(dx, dy) + EPS)
    return Point(p1.x + dx * dst, p1.y + dy * dst)


def reflected_point(p1, p2, pr):
    '''
    Return the reflection of pr across the line from p1 to p2.
    '''
    dx = p2.x - p1.x
    dy = p2.y - p1.y

    # Look for intersection of line (p1.x + dx*t, p1.y + dy*t) with
    # the orthogonal line (pr.x - dy*u, pr.y + dx*u).
    # Solving the system
    # dx * t + dy * u = pr.x - p1.x
    # dy * t - dx * u = pr.y - p1.y
    # gives
    # t = (-dy * (pr.y - p1.y) - dx * (pr.x - p1.x)) / (-dy*dy - dx*dx)
    #   = ( dy * (pr.y - p1.y) + dx * (pr.x - p1.x)) / ( dy*dy + dx*dx)
    # u = ( dx * (pr.y - p1.y) - dy * (pr.x - p1.x)) / (-dy*dy - dx*dx)
    #   = (-dx * (pr.y - p1.y) + dy * (pr.x - p1.x)) / ( dy*dy + dx*dx)
    # See
    # http://www.ahinson.com/algorithms_general/Sections/Geometry/ParametricLineIntersection.pdf
    # for more derivation.
    u = (-dx * (pr.y - p1.y) + dy * (pr.x - p1.x)) / (dx*dx + dy*dy + EPS)

    return Point(pr.x - dy*2*u, pr.y + dx*2*u)


def on_table(pt, w, l, r):
    x_ok = r <= pt.x <= w-r
    y_ok = r <= pt.y <= l-r
    return x_ok and y_ok


def too_close(p1, p2, pr, r):
    '''
    Check if a ball travelling from p1 to p2 would collide with a ball at pr.
    '''
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    t = (dx * (pr.x - p1.x) + dy * (pr.y - p1.y)) / (dx*dx + dy*dy + EPS)
    #u = (-dx * (pr.y - p1.y) + dy * (pr.x - p1.x)) / (dx*dx + dy*dy + EPS)
    #print('t:', t, 'u', u, file=sys.stderr)
    pi = Point(p1.x + t*dx, p1.y + t*dy)
    return 0 < t < 1 and math.hypot(pr.x - pi.x, pr.y - pi.y) < 2 * r


def main():
    w, l = (int(x) for x in sys.stdin.readline().split())
    r, x1, y1, x2, y2, x3, y3, h = (int(x) for x in sys.stdin.readline().split())
    lh = Point(0, l)
    rh = Point(w, l)
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)

    p02 = impact_point(p2, lh, r)
    p13 = impact_point(p3, rh, r)
    p01 = impact_point(p1, p13, r)
    p0s = reflected_point(p01, p13, p02)

    theta = math.atan2(p01.y - p0s.y, p01.x - p0s.x)
    d = (h - p0s.y) / (p01.y - p0s.y + EPS) * (p01.x - p0s.x) + p0s.x
    p0 = Point(d, h)

    ok = (p02.y < p2.y
          and p13.y < p3.y
          and p01.y < p1.y
          and on_table(p0, w, l, r)
          and on_table(p02, w, l, r)
          and on_table(p13, w, l, r)
          and on_table(p01, w, l, r)
          and not too_close(p0, p01, p2, r))
    if not ok:
        print('impossible')
    else:
        print('{:.02f} {:.02f}'.format(d, theta * 180 / math.pi))


if __name__ == '__main__':
    main()
