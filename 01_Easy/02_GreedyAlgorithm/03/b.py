import sys
INPUT = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 9)


def main():
    A = INPUT()
    print(-1 if A == "a" else "a")


if __name__ == '__main__':
    main()
