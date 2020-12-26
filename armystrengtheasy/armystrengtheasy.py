import sys

def main():
    n_cases = int(sys.stdin.readline())
    for case in range(n_cases):
        sys.stdin.readline()
        n_g, n_m = (int(x) for x in sys.stdin.readline().split())
        m_g = max(int(x) for x in sys.stdin.readline().split())
        m_m = max(int(x) for x in sys.stdin.readline().split())
        print('MechaGodzilla' if m_m > m_g else 'Godzilla')

if __name__ == '__main__':
    main()
