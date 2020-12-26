import sys


def main():
    n_cases = int(sys.stdin.readline())
    for _ in range(n_cases):
        n_people = int(sys.stdin.readline())
        people = []
        for _ in range(n_people):
            name, level, _ = sys.stdin.readline().split()
            name = name[:-1]
            key = 1.0
            fac = 0.1
            for des in reversed(level.split('-')):
                if des == 'lower':
                    key += fac
                elif des == 'upper':
                    key -= fac
                fac *= 0.1
            people.append((key, name))
        people.sort()
        print('\n'.join(p[1] for p in people))
        print('=' * 30)


if __name__ == '__main__':
    main()
