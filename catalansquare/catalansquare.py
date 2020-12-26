import sys
import math
# import timeit


# def binom_1(n, k):
#     ntok = 1
#     ktok = 1
#     for i in range(1, k+1):
#         ntok *= n
#         ktok *= i
#         n -= 1
#     return ntok // ktok
# 
# 
# def binom_2(n, k):
#     binom = 1
#     for (num, den) in zip(range(n, n-k, -1), range(1, k+1, 1)):
#         binom = (binom * num) // den
#     return binom


def binom(n, k):
    fn = math.factorial(n)
    fk = math.factorial(k)
    fn_k = math.factorial(n-k)
    return fn // fk // fn_k


def binom_2n_n(n):
    f2n = math.factorial(2*n)
    fn = math.factorial(n)
    return f2n // fn // fn


def catalan(n):
    return binom_2n_n(n) // (n + 1)


def catalan_squared(n):
    return catalan(n + 1)


if __name__ == '__main__':
    print(catalan_squared(int(sys.stdin.read())))
    # print(timeit.timeit("binom(10000, 5000)", number=100, globals=globals()))
    # print(timeit.timeit("binom_1(10000, 5000)", number=100, globals=globals()))
    # print(timeit.timeit("binom_2(10000, 5000)", number=100, globals=globals()))
