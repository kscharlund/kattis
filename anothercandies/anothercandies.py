import sys


def main():
    data = [int(x.strip()) for x in sys.stdin.readlines() if x.strip()]
    nn, data = data[0], data[1:]
    for ii in range(nn):
        n_children, data = data[0], data[1:]
        candies, data = data[:n_children], data[n_children:]
        print('YES' if sum(candies) % n_children == 0 else 'NO')


if __name__ == '__main__':
    main()
