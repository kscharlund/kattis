import sys
import math


def n_days(statues):
    return math.ceil(math.log2(statues)) + 1


if __name__ == '__main__':
    print(n_days(int(sys.stdin.read())))
