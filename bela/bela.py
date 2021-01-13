import sys

dominant = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 20,
    'T': 10,
    '9': 14,
    '8': 0,
    '7': 0,
}
nondominant = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 2,
    'T': 10,
    '9': 0,
    '8': 0,
    '7': 0,
}
def points(d, c):
    v, s = c
    if s == d:
        return dominant[v]
    return nondominant[v]

n, d = sys.stdin.readline().split()
print(sum(points(d, l.strip()) for l in sys.stdin))
