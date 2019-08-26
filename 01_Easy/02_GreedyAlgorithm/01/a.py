import sys
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
sys.setrecursionlimit(10 ** 9)


def main():
    change = 1000 - INT()
    ans = 0

    for coin in [500, 100, 50, 10, 5, 1]:
        ans += change // coin
        change -= (change//coin) * coin

    print(ans)


if __name__ == '__main__':
    main()
