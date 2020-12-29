import sys
from collections import defaultdict
from pprint import pprint


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """
    class Memodict(dict):
        """Memoization dictionary."""
        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret
    return Memodict().__getitem__


def overlaps(r1, r2):
    w1, h1, x1, y1 = r1
    w2, h2, x2, y2 = r2
    r1, b1 = x1 + w1, y1 + h1
    r2, b2 = x2 + w2, y2 + h2
    return not (x1 >= r2 or x2 >= r1 or y1 >= b2 or y2 >= b1)


def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if not n:
            break

        articles = []
        areas = []
        overlapping = defaultdict(set)
        for ii in range(n):
            w, h, x, y = (int(p) for p in sys.stdin.readline().split())
            articles.append((w, h, x, y))
            for jj in range(ii):
                if overlaps(articles[ii], articles[jj]):
                    overlapping[ii].add(jj)
                    overlapping[jj].add(ii)
            areas.append(w*h)

        def solve(i, selected, area):
            if i == n:
                return area
            if selected & overlapping[i]:
                return solve(i + 1, selected, area)
            else:
                return max(
                    solve(i + 1, selected | {i}, area + areas[i]),
                    solve(i + 1, selected, area)
                )

        print(solve(0, set(), 0))


main()
