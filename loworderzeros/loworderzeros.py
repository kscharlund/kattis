import sys
import math


def low_order_digit(n):
    prod = 1
    a_2 = 0
    a_5 = 0
    for i in range(2, n+1):
        while i % 2 == 0:
            i //= 2
            a_2 += 1
        while i % 5 == 0:
            i //= 5
            a_5 += 1
        prod = ((i % 10) * prod) % 10
    for i in range(a_2 - a_5):
        prod = (prod * 2) % 10
    return prod


N = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def low_order_digit_rec(n):
    if n < 10:
        return N[n]
    a = 4 if n // 10  % 2 else 6
    return (a * low_order_digit_rec(n // 5) * N[n % 10]) % 10

def main():
    for line in sys.stdin:
        n = int(line)
        if not n:
            break
        print(low_order_digit_rec(n))


if __name__ == '__main__':
    main()
