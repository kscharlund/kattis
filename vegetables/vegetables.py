import heapq
import sys


def min_cuts(min_ratio, pieces):
    pieces = [-x for x in pieces]
    min_weight = max(pieces)

    pq = list(zip(pieces, range(len(pieces))))
    heapq.heapify(pq)
    n_cuts = 0
    pieces_per_piece = [1 for _ in pieces]
    while n_cuts < 500:
        max_weight, index = heapq.heappop(pq)
        if min_weight/max_weight > min_ratio:
            break
        n_cuts += 1
        pieces_per_piece[index] += 1
        new_weight = pieces[index] / pieces_per_piece[index]
        if new_weight > min_weight:
            min_weight = new_weight
        heapq.heappush(pq, (new_weight, index))

    assert n_cuts < 500
    return n_cuts


def main():
    ln = sys.stdin.readline().split()
    min_ratio, _ = float(ln[0]), int(ln[1])
    pieces = [float(x) for x in sys.stdin.read().split()]
    print(min_cuts(min_ratio, pieces))


main()
