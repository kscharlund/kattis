import sys

rows, cols = map(int, sys.stdin.readline().split())
cw_rows = [sys.stdin.readline().strip() for _ in range(rows)]
cw_cols = [''.join(l[c] for l in cw_rows) for c in range(cols)]
words = [w for line in cw_rows + cw_cols for w in line.split('#') if len(w) > 1]
words.sort()
print(words[0])
