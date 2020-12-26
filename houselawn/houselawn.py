import sys

def parse_mower(i, line):
    n, p, c, t, r = line.split(',')
    return (int(p), i, int(c), int(t), int(r), n)

def main():
    lawn_size, num_mowers = tuple(int(x)
                                  for x in sys.stdin.readline().strip().split())
    mowers = [parse_mower(i, sys.stdin.readline().strip())
              for i in range(num_mowers)]
    acceptable = [(p, i, n)
                  for (p, i, c, t, r, n) in mowers
                  if 10080 * c * t / (t + r) >= lawn_size]
    last_price = -1
    for p, i, n in sorted(acceptable):
        if last_price == -1:
            last_price = p
        if p > last_price:
            break
        print(n)
    if not acceptable:
        print('no such mower')

if __name__ == '__main__':
    main()
