#!/usr/local/bin/python3

import sys
import math

def inv_nchoose2(m):
    '''
    m = n choose 2, calculate m.
    '''
    return (1 + math.sqrt(1 + 8 * m)) / 2

def solve(n_00, n_01, n_10, n_11):
    if n_00 + n_01 + n_10 + n_11 == 0:
        # No combinations, answer can be '0' or '1'.
        return '0'

    f_n_z = inv_nchoose2(n_00)
    f_n_o = inv_nchoose2(n_11)
    f_n_t = inv_nchoose2(n_00 + n_01 + n_10 + n_11)
    n_z = int(f_n_z)
    n_o = int(f_n_o)
    n_t = int(f_n_t)

    if n_z != f_n_z or n_o != f_n_o or n_t != f_n_t:
        return 'impossible'

    # Special cases for all zeros or all ones.
    if n_z == 1 and n_o == n_t:
        return n_o * '1'
    if n_o == 1 and n_z == n_t:
        return n_z * '0'

    # Number of ones plus number of zeros must equal number of digits.
    if n_z + n_o != n_t:
        return 'impossible'

    # Number of ones times number of zeros equals number of 01 and 10.
    if n_z * n_o != n_01 + n_10:
        return 'impossible'

    zs = 0
    os = 0
    s = []
    for _ in range(n_t):
        if n_01 >= (n_o - os):
            s.append('0')
            zs += 1
            n_01 -= n_o - os
        else:
            s.append('1')
            os += 1
            n_10 -= n_z - zs

    #print(n_z, zs, n_o, os, n_t, file=sys.stderr)
    return ''.join(s)

def main():
    n_00, n_01, n_10, n_11 = (int(x) for x in sys.stdin.readline().strip().split())
    print(solve(n_00, n_01, n_10, n_11))

if __name__ == '__main__':
    main()