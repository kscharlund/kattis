import sys


def solve(p, q):
    if p == q:
        # Root, special case.
        np, nq = 1, 2
    elif p < q:
        # F(n) is a left child. Then F(n+1) has the same parent, and the
        # calculation is straightforward.
        np, nq = q, q - p
    else:
        # p > q, F(n) is a right child.
        # First, find the first parent node that is a left child.
        lv = p // q
        pp, pq = p - q * lv, q
        # Then go to next in level order. If q == 1, then pn will be the root.
        pnp, pnq = pq, pq - pp
        # Finally go down through the left subtree again.
        np, nq = pnp, pnq + pnp * lv
    return np, nq

def main():
    sys.stdin.readline()
    for line in sys.stdin:
        k, pq = line.split()
        p, q = (int(x) for x in pq.split('/'))
        np, nq = solve(p, q)
        print(k, '{}/{}'.format(np, nq))


main()
