import sys


def cheese_percentage(r, c):
    cheese_ratio = (r - c) * (r - c) / (r * r)
    return 100.0 * cheese_ratio


def main():
    r, c = (int(x) for x in sys.stdin.read().split())
    print(cheese_percentage(r, c))


if __name__ == '__main__':
    main()
