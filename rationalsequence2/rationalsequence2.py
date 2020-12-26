import sys


def F(n):
    if n == 1:
        return (1, 1)
    #print(n, file=sys.stderr)
    p, q = F(n//2)
    #print(n//2, p, q, file=sys.stderr)
    if n & 1:
        return (p+q, q)
    else:
        return (p, p+q)


def F_inv(p, q):
    n = 0
    level = 1
    while p != q:
        if p > q:
            n += level
            p -= q
        else:
            q -= p
        level *= 2
    n += level
    return n


def main():
    sys.stdin.readline()
    for line in sys.stdin:
        k, pq = line.split()
        p, q = (int(x) for x in pq.split('/'))
        print(k, F_inv(p, q))


main()
