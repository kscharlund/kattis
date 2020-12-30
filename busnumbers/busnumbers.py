import sys

sys.stdin.readline()
numbers = [int(x) for x in sys.stdin.readline().split()]
numbers.sort()
output = []
first = last = numbers[0]
for num in numbers[1:]:
    if num == last + 1:
        last = num
    else:
        if last - first > 1:
            output.append(f'{first}-{last}')
        elif last == first:
            output.append(str(first))
        else:
            output.append(f'{first} {last}')
        first = last = num
if last - first > 1:
    output.append(f'{first}-{last}')
elif last == first:
    output.append(str(first))
else:
    output.append(f'{first} {last}')
print(' '.join(output))
