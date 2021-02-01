import sys

def words():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    i = 0
    while True:
        letters = []
        j = i
        while j or not letters:
            letters.append(chars[j & 7])
            j >>= 3
        yield ''.join(letters)
        i += 1

a, b = map(int, sys.stdin.readline().split())
gen = words()
print(' '.join(next(gen) for _ in range(b)))
