#!/usr/bin/env python
"""
Solution to Limited Correspondence Kattis problem.
"""

import sys


def match(str1, str2):
    """
    Check if str1 and str2 have a common prefix, and if so also return the
    remainder of each string (at least one will be empty).
    """
    if len(str1) < len(str2):
        return (str2.startswith(str1), '', str2[len(str1):])
    return (str1.startswith(str2), str1[len(str2):], '')


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
def correspond(args):
    """
    Recursively find pairs of strings that concatenate to the same result.
    """
    # One tuple argument for fast memoization, unpack here.
    ab_pairs, a_prefix, b_prefix, res = args
    # Look for all valid continuations, depth first.
    all_res = []
    for (i, (a_i, b_i)) in enumerate(ab_pairs):
        # First, verify that required prefixes match.
        a_ok, a_next, a_prefix_rem = match(a_i, a_prefix)
        b_ok, b_next, b_prefix_rem = match(b_i, b_prefix)
        # Then, check if A and B match. In that case, B should have remainder of
        # A as prefix or vice versa.
        ab_ok, b_prefix_next, a_prefix_next = match(a_next, b_next)
        if a_ok and b_ok and ab_ok:
            new_a_prefix = a_prefix_rem + a_prefix_next
            new_b_prefix = b_prefix_rem + b_prefix_next
            new_res = res + (a_next if new_b_prefix else b_next)
            if not new_a_prefix and not new_b_prefix:
                all_res.append(new_res)
            else:
                new_ab_pairs = ab_pairs[:i] + ab_pairs[i+1:]
                all_res.append(
                    correspond((new_ab_pairs,
                                new_a_prefix,
                                new_b_prefix,
                                new_res)))
    # Out of the valid sequences, only return the best one.
    sorted_res = [s for l, s in sorted(zip((len(x) for x in all_res), all_res)) if s]
    return sorted_res[0] if sorted_res else ''


def main():
    """Entry point."""
    lines = [x.strip() for x in sys.stdin.readlines()]
    i = 0
    case_num = 1
    while i < len(lines):
        n_pairs = int(lines[i])
        ab_pairs = tuple(tuple(x.split()) for x in lines[i+1:i+1+n_pairs])
        res = correspond((ab_pairs, '', '', ''))
        if res:
            print('Case {}: {}'.format(case_num, res))
        else:
            print('Case {}: IMPOSSIBLE'.format(case_num))
        i = i+1+n_pairs
        case_num += 1


if __name__ == '__main__':
    main()
