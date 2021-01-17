import sys

for i, line in enumerate(sys.stdin):
    if line.strip() == 'END':
        break
    print(
        i + 1,
        'EVEN' if len({x for x in line.split('*')[1:-1]}) < 2 else 'NOT EVEN'
    )
