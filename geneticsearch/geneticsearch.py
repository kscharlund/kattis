import sys

def count_occurrences(s, p):
    '''
    Count occurrences of p in s.
    '''
    start = 0
    count = 0
    while True:
        match = s.find(p, start)
        if match < 0:
            break
        start = match + 1
        count += 1
    return count


def generate_sub_patterns(p):
    return {p[:i] + p[i+1:] for i in range(len(p))}


def generate_add_patterns(p):
    return {p[:pos] + char + p[pos:] for char in ('A', 'G', 'C', 'T') for pos in range(len(p) + 1)}


def main():
    for line in sys.stdin:
        if line.strip() == '0':
            break
        s, l = line.split()
        t1 = count_occurrences(l, s)
        t2 = 0
        for p in generate_sub_patterns(s):
            t2 += count_occurrences(l, p)
        t3 = 0
        if len(s) < len(l):
            for p in generate_add_patterns(s):
                t3 += count_occurrences(l, p)
        print(t1, t2, t3)


if __name__ == '__main__':
    main()
