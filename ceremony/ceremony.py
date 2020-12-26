import sys


def main():
    n = int(sys.stdin.readline())
    heights = list(int(x) for x in sys.stdin.readline().split())
    print(min((min(i + h for i, h in enumerate(reversed(sorted(heights)))), n)))


main()
