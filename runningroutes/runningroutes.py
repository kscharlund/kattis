import sys


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


n = int(sys.stdin.readline().strip())
adj = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

@memoize
def solve(args):
    l, r = args
    if l >= r:
        return 0
    if r - l == 1:
        return adj[l][r]
    res = 0
    for k in range(l, r + 1):
        res = max(res, solve((l + 1, k - 1)) + solve((k + 1, r)) + adj[l][k])
    return res

print(solve((0, n - 1)))
