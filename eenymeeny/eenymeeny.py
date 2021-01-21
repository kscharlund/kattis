import sys

rhyme = sys.stdin.readline().split()
n = int(sys.stdin.readline().strip())
kids = [sys.stdin.readline().strip() for _ in range(n)]

teams = [[], []]
step = len(rhyme) - 1
idx = 0
for i in range(n):
    idx = (idx + step) % (n - i)
    teams[i & 1].append(kids.pop(idx))
for team in teams:
    print(len(team))
    for k in team:
        print(k)
