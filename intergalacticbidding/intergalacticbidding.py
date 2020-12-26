#!/usr/local/bin/python3

import sys

def winners(candidates, target_sum):
    curr_sum = 0
    result = set()

    while candidates:
        bid, name = candidates.pop()
        new_sum = bid + curr_sum
        if new_sum <= target_sum:
            curr_sum = new_sum
            result.add(name)
            if new_sum == target_sum:
                return result

    return set()

def main():
    n_bids, target = (int(x) for x in sys.stdin.readline().strip().split())
    candidates = []
    for _ in range(n_bids):
        n, b = sys.stdin.readline().strip().split()
        b = int(b)
        if b <= target:
            candidates.append((b, n))
    res = winners(sorted(candidates), target)
    print(len(res))
    for r in res:
        print(r)

if __name__ == '__main__':
    main()
