import sys
sys.setrecursionlimit(7500)


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


BEFORE, INVERT, AFTER = range(3)


def is_left(s, i, t):
    return s[i] == (')' if t == INVERT else '(')


@memoize
def possible_rec(args):
    s, i, l, t = args
    if i == len(s):
        # Base case, end of string.
        return l == i - l
    if l < i - l:
        # Too many right brackets in prefix.
        return False
    rec_s = possible_rec((s, i+1, l+is_left(s, i, t), t))
    if t == BEFORE:
        return rec_s or possible_rec((s, i, l, INVERT))
    if t == INVERT:
        return rec_s or possible_rec((s, i, l, AFTER))
    return rec_s


def is_possible(s):
    n = len(s)

    # Impossible to balance odd number of brackets.
    if n % 2:
        return False

    n_half = n // 2

    # Memory for dynamic programming. Only needs two lines for i and i+1.
    poss_b_prev = [False for _ in range(n+1)]
    poss_b_curr = poss_b_prev[:]
    poss_i_prev = poss_b_prev[:]
    poss_i_curr = poss_b_prev[:]
    poss_a_prev = poss_b_prev[:]
    poss_a_curr = poss_b_prev[:]

    # Base condition: half of the string need to be left brackets.
    poss_a_curr[n_half] = True
    poss_i_curr[n_half] = True
    poss_b_curr[n_half] = True

    # Fill table backwards. i is current read position in string, and thus also
    # length of prefix.
    for i in range(n - 1, -1, -1):
        # Swap line buffers.
        poss_a_prev, poss_a_curr = poss_a_curr, poss_a_prev
        poss_i_prev, poss_i_curr = poss_i_curr, poss_i_prev
        poss_b_prev, poss_b_curr = poss_b_curr, poss_b_prev

        # Check current character.
        is_l = s[i] == '('
        is_r = not is_l

        # l is current number of left brackets in prefix (also counting right
        # brackets during inversion).
        # If l < (i + 1) / 2, not enough left brackets in prefix.
        # If l > n_half, too many left brackets in prefix.
        # If l > i, more left brackets than characters in prefix.
        for l in range((i + 1) // 2, min(i, n_half) + 1):
            poss_a_curr[l] = poss_a_prev[l + is_l]
            poss_i_curr[l] = poss_i_prev[l + is_r] or poss_a_curr[l]
            poss_b_curr[l] = poss_b_prev[l + is_l] or poss_i_curr[l]

    # Get result.
    return poss_b_curr[0]


def main():
    s = sys.stdin.readline().strip()
    print('possible' if is_possible(s) else 'impossible')


if __name__ == '__main__':
    main()
