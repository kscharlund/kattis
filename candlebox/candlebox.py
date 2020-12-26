import sys

def main():
    d = int(input())
    r = int(input())
    t = int(input())
    for a_r in range(max(4, 3 + d), 45):
        a_t = a_r - d
        c_r = a_r * (a_r + 1) // 2 - 6
        c_t = a_t * (a_t + 1) // 2 - 3
        #print(a_t, c_r, c_t, c_r + c_t, file=sys.stderr)
        if (c_r + c_t) == (r + t):
            print(r - c_r)
            break
    else:
        print(0)

if __name__ == '__main__':
    main()
