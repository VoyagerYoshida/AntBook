import sys
from collections import defaultdict
from math import gcd
# from fractions import gcd
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    N, D = MAP()
    # dp : dp[i] (1<=i<=N) が 6 の約数を key に持つ辞書のリスト.
    # dp[i][k] は, 次 (i+1 回目) サイコロを振って出た目が k の場合に, 出た目の積が N になる i 回目までの試行の数.
    dp = [defaultdict(int) for i in range(N+1)]
    dp[0][D] = 1

    for i in range(N):
        for d in dp[i]:
            for j in range(1, 7): dp[i+1][d//gcd(d, j)] += dp[i][d]

    print(dp[N][1] / 6**N)


if __name__ == '__main__':
    main()
