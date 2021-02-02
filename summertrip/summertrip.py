import sys
from collections import defaultdict
from pprint import pprint


events = sys.stdin.readline().strip()
letters = set(events)
since_last = defaultdict(set)
count = 0
for event in events:
    for letter in letters:
        if letter != event:
            since_last[letter].add(event)
        else:
            count += len(since_last[letter])
            since_last[letter].clear()
    # pprint(since_last, stream=sys.stderr)
    # print(count, file=sys.stderr)
print(count)
