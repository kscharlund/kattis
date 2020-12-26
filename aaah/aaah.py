import sys
if __name__ == '__main__':
    a1 = sys.stdin.readline().strip()
    a2 = sys.stdin.readline().strip()
    if len(a1) < len(a2):
        print('no')
    else:
        print('go')
