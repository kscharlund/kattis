import sys

def makes_sense(bites):
    for i, bite in enumerate(bites):
        if bite != 'mumble' and i + 1 != int(bite):
            return False
    return True

if __name__ == '__main__':
    sys.stdin.readline()
    bites = sys.stdin.readline().strip().split()
    print('makes sense' if makes_sense(bites) else 'something is fishy')
