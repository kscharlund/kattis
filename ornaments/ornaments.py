import sys
import math


def tangent_point(rr, hh):
    """
    Find the point (xx, yy) where the line between (xx, yy) and (0, hh) is a
    tangent to the circle with radius rr around (0, 0).
    """
    x0, y0 = 0, hh
    def ff(x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        dr = math.hypot(dx, dy)
        det = x0 * y1 - x1 * y0
        disc = rr ** 2 * dr ** 2 - det ** 2
        return disc
    # A point guaranteed to be outside the circle:
    xo, yo = rr, hh
    lb, ub = 1, 0
    while True:
        alpha = (lb + ub) / 2
        xx, yy = alpha * xo, alpha * yo
        da = ff(xx, yy)
        # print(lb, ub, alpha, da, xx, yy)
        if abs(da) < 1e-7:
            break
        if da < 0:
            lb = alpha
        else:
            ub = alpha
    det = x0 * yy - xx * y0
    dr = math.hypot(yy - y0, xx - x0)
    return (det * (yy - y0) / dr ** 2, -det * (xx - x0) / dr ** 2)


def line_part(xx, yy, hh):
    """
    Length of two lines from (0, hh) to (xx, yy).
    """
    ll = math.hypot(xx, yy - hh)
    # print(f'Line length: {ll}', file=sys.stderr)
    return 2 * ll


def circle_part(yy, rr):
    """
    Length of half circle plus two circle segments from y = 0 to yy.
    """
    half_circle = math.pi * rr
    circle_segment = math.asin(yy/rr) * rr
    # print(f'Half circle: {half_circle}, segment: {circle_segment}', file=sys.stderr)
    return half_circle + 2 * circle_segment

def slow_method():
    """
    This was my first attempt, which unfortunately got TLE. :)
    For some reason, the trigonometric properties used below didn't occur to me.
    Maybe I was tired?

    Keeping the code for future reference anyway.
    """
    for line in sys.stdin:
        rr, hh, ss = (int(x) for x in line.split())
        if not any((rr, hh, ss)):
            break
        # print(f'Radius: {rr}, Height: {hh}', file=sys.stderr)
        if hh != rr:
            xx, yy = tangent_point(rr, hh)
        else:
            xx, yy = 0, hh
        # print(f'Tangent point: ({xx}, {yy}), calculated radius {math.hypot(xx, yy)}', file=sys.stderr)
        dd = circle_part(yy, rr) + line_part(xx, yy, hh)
        dd += (ss / 100) * dd
        print(f'{dd:.2f}')

def fast_method():
    for line in sys.stdin:
        rr, hh, ss = (int(x) for x in line.split())
        if not any((rr, hh, ss)):
            break
        # Line part: 2 * leg of right triangle with hypotenuse hh and other leg rr.
        dd = 2 * (hh ** 2 - rr ** 2) ** 0.5
        # Circle part: whole circle excluding the segments inside the triangle above.
        dd += 2 * (math.pi - math.acos(rr / hh)) * rr
        # Slack part: add ss percent.
        dd += (ss / 100) * dd
        print(f'{dd:.2f}')

fast_method()
