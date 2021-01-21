import sys
from collections import defaultdict

start = sys.stdin.readline().strip()[-1]
n = int(sys.stdin.readline().strip())
words = defaultdict(list)
for _ in range(n):
    w = sys.stdin.readline().strip()
    words[w[0]].append(w)
if start in words:
    for w in words[start]:
        if w[-1] not in words or (w[-1] == start and len(words[start]) == 1):
            print(f'{w}!')
            break
    else:
        print(words[start][0])
else:
    print('?')
