import sys

def up(pos, v, w=None, l=None):
    if w and l:
        return (pos[0], max(0, min(pos[1] + v, l - 1)))
    return (pos[0], pos[1] + v)

def down(pos, v, w=None, l=None):
    if w and l:
        return (pos[0], max(0, min(pos[1] - v, l - 1)))
    return (pos[0], pos[1] - v)

def left(pos, v, w=None, l=None):
    if w and l:
        return (max(0, min(pos[0] - v, w - 1)), pos[1])
    return (pos[0] - v, pos[1])

def right(pos, v, w=None, l=None):
    if w and l:
        return (max(0, min(pos[0] + v, w - 1)), pos[1])
    return (pos[0] + v, pos[1])

ops = {
    'u': up,
    'd': down,
    'l': left,
    'r': right,
}

while True:
    w, l = map(int, sys.stdin.readline().split())
    if not (w or l):
        break
    apos = rpos = (0, 0)
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        o, v = sys.stdin.readline().split()
        rpos = ops[o](rpos, int(v))
        apos = ops[o](apos, int(v), w, l)
    print(f'Robot thinks {rpos[0]} {rpos[1]}')
    print(f'Actually at {apos[0]} {apos[1]}')
    print()
