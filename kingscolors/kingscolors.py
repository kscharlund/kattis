import sys
import math
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    #denom = reduce(op.mul, range(1, r+1), 1)
    denom = math.factorial(r)
    return numer // denom

def tree_chromatic_polynomial(n, k):
    return k * ((k - 1) ** (n - 1))

def tree_almost_stirling_number(n, k):
    '''
    The graphical Stirling number is 1 / k! times this result, but we want to
    include all permutations of labels as well.

    Note that the real sum is from 0 to k, not 0 to k-2. However, the chromatic
    polynomial of a tree is 0 for k = 0 and k = 1.

    Reference: https://www3.nd.edu/~dgalvin1/pdf/forests_and_cycles.pdf
    '''
    return sum(((-1) ** i) * ncr(k, i) * tree_chromatic_polynomial(n, k-i) for i in range(k - 1))

def main():
    n, k = (int(x) for x in sys.stdin.readline().strip().split())
    m = 1000000007
    print(tree_almost_stirling_number(n, k) % m)

if __name__ == '__main__':
    main()
