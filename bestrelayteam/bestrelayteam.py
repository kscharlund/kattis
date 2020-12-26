import sys

def main():
    n = int(sys.stdin.readline().strip())
    runners = []
    for _ in range(n):
        nm, a, b = sys.stdin.readline().strip().split()
        runners.append((float(b), float(a), nm))
    runners.sort()

    best_team = None
    best_time = 1000.0
    for i in range(n):
        if i < 3:
            rest = runners[0:i] + runners[(i+1):4]
        else:
            rest = runners[0:3]
        time = runners[i][1] + sum(b for b, a, nm in rest)
        if time < best_time:
            best_team = [runners[i]] + rest
            best_time = time
    print(best_time)
    print('\n'.join(nm for b, a, nm in best_team))

if __name__ == '__main__':
    main()
