import sys


E_ORBIT = 365
M_ORBIT = 687

def case(e, m):
    d = 0
    if e:
        d_e = E_ORBIT - e
        e = 0
        m = (m + d_e) % M_ORBIT
        d += d_e
    while m:
        d_m = E_ORBIT
        m = (m + d_m) % M_ORBIT
        d += d_m
    return d


def case2(e, m):
    for d in range(E_ORBIT * M_ORBIT):
        if (((e + d) % E_ORBIT) == 0) and (((m + d) % M_ORBIT) == 0):
            return d


def main():
    for i, line in enumerate(sys.stdin):
        e, m = tuple(int(x) for x in line.split())
        print('Case {}: {}'.format(i+1, case2(e, m)))


if __name__ == '__main__':
    main()
