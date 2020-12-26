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
def prob(args):
    d, m_s, m_o = args
    if not m_o:
        return 1
    if d >= sum(m_s) + sum(m_o):
        return 1
    if d < sum(m_o):
        return 0

    res = 0
    i_n = 1 / (len(m_o) + len(m_s))

    subres = -1
    prev = -1
    for i, m in enumerate(m_o):
        if m == prev:
            res += subres
            continue
        prev = m
        if m == 1:
            new_m_o = m_o[:i] + m_o[i+1:]
        else:
            new_m_o = tuple(sorted(m_o[:i] + (m - 1,) + m_o[i+1:]))
        subres = i_n * prob((d - 1, m_s, new_m_o))
        res += subres
    subres = -1
    prev = -1
    for i, m in enumerate(m_s):
        if m == prev:
            res += subres
            continue
        prev = m
        if m == 1:
            new_m_s = m_s[:i] + m_s[i+1:]
        else:
            new_m_s = tuple(sorted(m_s[:i] + (m - 1,) + m_s[i+1:]))
        subres = i_n * prob((d - 1, new_m_s, m_o))
        res += subres
    return res

def main():
    _, _, d = (int(x) for x in sys.stdin.readline().strip().split())
    m_s = tuple(int(x) for x in sys.stdin.readline().strip().split())
    m_o = tuple(int(x) for x in sys.stdin.readline().strip().split())
    print(prob((d, m_s, m_o)))

def profmain():
    d = 59
    m_s = (6, 6, 6, 6, 6)
    m_o = (6, 6, 6, 6, 6)
    print(prob((d, m_s, m_o)))

if __name__ == '__main__':
    main()
    #import cProfile
    #cProfile.run('profmain()')
