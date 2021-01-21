import sys


def solve(s1, s2, r, c1, c2):
    sx = s1[c1] + s2[c2]
    if s1[1-c1] < s2[1-c2]:
        sy = s2[1-c2]
        rx = s1[c1]
        ry = s1[1-c1]
    else:
        sy = s1[1-c1]
        rx = s2[c2]
        ry = s2[1-c2]
    cases = []
    if r[0] <= rx:
        # print(sy, ry, r[1], sx)
        y = max(ry + r[1], sy)
        cases.append(sx * y)
    if r[1] <= rx:
        # print(sy, ry, r[0], sx)
        y = max(ry + r[0], sy)
        cases.append(sx * y)
    cases.append(max(sx, r[0]) * (sy + r[1]))
    cases.append(max(sx, r[1]) * (sy + r[0]))
    cases.append((sx + r[0]) * max(sy, r[1]))
    cases.append((sx + r[1]) * max(sy, r[0]))
    # print(cases)
    return min(cases)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    a1, b1, a2, b2, a3, b3 = map(int, sys.stdin.readline().split())
    hs = ((a1, b1), (a2, b2), (a3, b3))
    print(min([
        solve(hs[0], hs[1], hs[2], 0, 0),
        solve(hs[0], hs[1], hs[2], 0, 1),
        solve(hs[0], hs[1], hs[2], 1, 0),
        solve(hs[0], hs[1], hs[2], 1, 1),
        solve(hs[1], hs[2], hs[0], 0, 0),
        solve(hs[1], hs[2], hs[0], 0, 1),
        solve(hs[1], hs[2], hs[0], 1, 0),
        solve(hs[1], hs[2], hs[0], 1, 1),
        solve(hs[2], hs[0], hs[1], 0, 0),
        solve(hs[2], hs[0], hs[1], 0, 1),
        solve(hs[2], hs[0], hs[1], 1, 0),
        solve(hs[2], hs[0], hs[1], 1, 1),
    ]))
