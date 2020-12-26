import sys


def main():
    heights = [0 for _ in range(10**8 + 1)]
    frogs = []
    n, d = (int(x) for x in sys.stdin.readline().strip().split())
    for _ in range(n):
        l, w, h = (int(x) for x in sys.stdin.readline().strip().split())
        frogs.append((w, h, l))
    frogs.sort(reverse=True)
    n_escaped = 0
    for w, h, l in frogs:
        if l + heights[w] > d:
            n_escaped += 1
        for i in range(w):
            heights[i] = max(heights[i], heights[i + w] + h)
    print(n_escaped)

if __name__ == '__main__':
    main()
