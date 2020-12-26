import sys

sys.stdin.readline()
pushes = list(int(x) for x in reversed(sys.stdin.readline().strip().split()))
dirtiness = 0
cleanups = 0
num_dirty = 0
for day in range(1, 366):
    dirtiness += num_dirty
    if dirtiness >= 20:
        cleanups += 1
        num_dirty = 0
        dirtiness = 0
    if pushes and pushes[-1] == day:
        num_dirty += 1
        pushes.pop()
if num_dirty:
    cleanups += 1
print(cleanups)
