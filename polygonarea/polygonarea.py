#!/usr/local/bin/python3

import sys


def calculate_orientation(points):
    # Find point on convex hull.
    ci = 0
    cx, cy = points[0]
    for i in range(1, len(points)):
        x, y = points[i]
        if x < cx or (x == cx and y < cy):
            ci, cx, cy = i, x, y
    px, py = points[ci - 1]
    nx, ny = points[(ci + 1) % len(points)]
    det = (cx - px)*(ny - py) - (nx - px)*(cy - py)
    return 'CW' if det < 0 else 'CCW'


def calculate_area(points):
    area_sum = 0
    for i in range(len(points)):
        cx, cy = points[i]
        px, py = points[i-1]
        area_sum += px*cy - cx*py
    return abs(area_sum / 2.0)


def main():
    while True:
        points = []
        n_points = int(sys.stdin.readline())
        if not n_points:
            break
        for case in range(n_points):
            x, y = sys.stdin.readline().split()
            points.append((int(x), int(y)))
        print('{} {:.1f}'.format(calculate_orientation(points),
                                 calculate_area(points)))


if __name__ == '__main__':
    main()
