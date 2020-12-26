import sys


def solve_case(prices, stickers):
    sum = 0
    for required, reward in prices:
        sum += min(stickers[idx] for idx in required) * reward
    return sum


def main():
    n_test_cases = int(sys.stdin.readline())
    for ti in range(n_test_cases):
        n_prices, n_stickers = (int(x) for x in sys.stdin.readline().split())

        prices = []
        for pi in range(n_prices):
            data = sys.stdin.readline().split()
            required = set(int(x) - 1 for x in data[1:-1])
            reward = int(data[-1])
            for req, _ in prices:
                if not req.isdisjoint(required):
                    raise ValueError("Non-disjoint price requirements")
            prices.append((required, reward))

        stickers = list(int(x) for x in sys.stdin.readline().split())

        print(solve_case(prices, stickers))


if __name__ == '__main__':
    main()
