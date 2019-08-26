import sys
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
LIST = lambda: list(map(int, INPUT().split()))
sys.setrecursionlimit(10 ** 9)


def main():
    D, N = MAP()
    T = [INT() for _ in range(D)]
    ABC = [LIST() for _ in range(N)]

    max_min = []  # d 日目に着れる服のうち, 派手さが最大のものと最小のものを格納する 2 次元リスト.
    for t in T:
        tmp = [c for a, b, c in ABC if a <= t <= b]
        max_min.append([max(tmp), min(tmp)])

    dp = [[0, 0]]  # i 日目に派手さがそれぞれ最大, 最小のものを選んだときの i 日目までの派手さの差の総和.
    for d in range(1, D):
        dp.append([max(dp[-1][j] + abs(max_min[d-1][j]-max_min[d][i]) for j in range(2)) for i in range(2)])

    print(max(dp[D-1]))


if __name__ == '__main__':
    main()
