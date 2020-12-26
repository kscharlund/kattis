import sys


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """
    class Memodict(dict):
        """Memoization dictionary."""
        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret
    return Memodict().__getitem__


@memoize
def num_ways(blockage):
    # print(blockage, file=sys.stderr)
    curr_l, curr_c, curr_r = blockage[-1]
    n_ways = 0
    if curr_l:
        if curr_c:
            if curr_r:
                # All blocked.
                if len(blockage) > 1:
                    n_ways = num_ways(blockage[:-1])
                else:
                    n_ways = 1
            else:
                # curr_l and curr_c.
                if len(blockage) > 1:
                    next_l, next_c, next_r = blockage[-2]
                    n_ways = num_ways(blockage[:-1])
                    if not next_r:
                        n_ways += num_ways(blockage[:-2] + ((next_l, next_c, True),))
                else:
                    n_ways = 1
        else:
            if curr_r:
                # curr_l and curr_r.
                if len(blockage) > 1:
                    next_l, next_c, next_r = blockage[-2]
                    n_ways = num_ways(blockage[:-1])
                    if not next_c:
                        n_ways += num_ways(blockage[:-2] + ((next_l, True, next_r),))
                else:
                    n_ways = 1
            else:
                # Only curr_l.
                if len(blockage) > 1:
                    next_l, next_c, next_r = blockage[-2]
                    n_ways = 2 * num_ways(blockage[:-1])
                    if not next_c:
                        n_ways += num_ways(blockage[:-2] + ((next_l, True, next_r),))
                    if not next_r:
                        n_ways += num_ways(blockage[:-2] + ((next_l, next_c, True),))
                    if not next_c and not next_r:
                        n_ways += num_ways(blockage[:-2] + ((next_l, True, True),))
                else:
                    n_ways = 2
    else:
        if curr_c:
            if curr_r:
                # curr_c and curr_r.
                if len(blockage) > 1:
                    next_l, next_c, next_r = blockage[-2]
                    n_ways = num_ways(blockage[:-1])
                    if not next_l:
                        n_ways += num_ways(blockage[:-2] + ((True, next_c, next_r),))
                else:
                    n_ways = 1
            else:
                # Only curr_c.
                if len(blockage) > 1:
                    next_l, next_c, next_r = blockage[-2]
                    n_ways = num_ways(blockage[:-1])
                    if not next_l:
                        n_ways += num_ways(blockage[:-2] + ((True, next_c, next_r),))
                    if not next_r:
                        n_ways += num_ways(blockage[:-2] + ((next_l, next_c, True),))
                    if not next_l and not next_r:
                        n_ways += num_ways(blockage[:-2] + ((True, next_c, True),))
                else:
                    n_ways = 1
        else:
            if curr_r:
                # Only curr_r.
                if len(blockage) > 1:
                    next_l, next_c, next_r = blockage[-2]
                    n_ways = 2 * num_ways(blockage[:-1])
                    if not next_c:
                        n_ways += num_ways(blockage[:-2] + ((next_l, True, next_r),))
                    if not next_l:
                        n_ways += num_ways(blockage[:-2] + ((True, next_c, next_r),))
                    if not next_l and not next_c:
                        n_ways += num_ways(blockage[:-2] + ((True, True, next_r),))
                else:
                    n_ways = 2
            else:
                # No blockage.
                if len(blockage) > 1:
                    next_l, next_c, next_r = blockage[-2]
                    # print('Next: ', next_l, next_c, next_r, file=sys.stderr)
                    n_ways = 3 * num_ways(blockage[:-1])
                    if not next_l:
                        n_ways += 2 * num_ways(blockage[:-2] + ((True, next_c, next_r),))
                    if not next_c:
                        n_ways += num_ways(blockage[:-2] + ((next_l, True, next_r),))
                    if not next_r:
                        n_ways += 2 * num_ways(blockage[:-2] + ((next_l, next_c, True),))
                    if not next_l and not next_c:
                        n_ways += num_ways(blockage[:-2] + ((True, True, next_r),))
                    if not next_l and not next_r:
                        n_ways += num_ways(blockage[:-2] + ((True, next_c, True),))
                    if not next_c and not next_r:
                        n_ways += num_ways(blockage[:-2] + ((next_l, True, True),))
                    if not next_l and not next_c and not next_r:
                        n_ways += num_ways(blockage[:-2] + ((True, True, True),))
                else:
                    n_ways = 3
    # print('<=', n_ways, file=sys.stderr)
    return n_ways


def main():
    mm, nn = (int(x) for x in sys.stdin.readline().strip().split())
    if nn:
        blockage_coords = [float(x) for x in sys.stdin.readline().strip().split()]
    blockage = [[False for x in range(3)] for y in range(mm)]
    for ii in range(nn):
        b_x, b_y = int(blockage_coords[ii*2]), int(blockage_coords[ii*2 + 1])
        blockage[b_x][b_y] = True
    blockage = tuple(tuple(x) for x in blockage)
    print(num_ways(blockage))


if __name__ == '__main__':
    main()
