import sys
import heapq

removed = set()
patients = []

n, k = map(int, sys.stdin.readline().split())
for _ in range(n):
    q, *args = sys.stdin.readline().split()
    if q == '1':
        t, m, s = args
        t, s = int(t), int(s)
        # Note reversed sign for s. This is because we use a min heap.
        # t has positive sign, since a larger t corresponds to shorter wait
        # time. Note that the min heap also gives us automatic name sorting.
        w = t * k - s
        heapq.heappush(patients, (w, m))
    elif q == '2':
        while patients and patients[0][1] in removed:
            heapq.heappop(patients)
        if patients:
            _, m = heapq.heappop(patients)
            print(m)
        else:
            print('doctor takes a break')
    elif q == '3':
        _, m = args
        removed.add(m)
