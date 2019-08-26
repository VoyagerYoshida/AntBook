import sys
import numpy as np
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    W = INT()
    N, K = MAP()

    dp = np.zeros((K+1, W+1), np.int)  # dp[i][j] : 容量制限 i, 個数制限 j の場合の 最大重要度を要素に持つ 2 次元配列.
    for _ in range(N):
        A, B = MAP()
        # 2 つの 2 次元配列の各要素について比較し, それぞれ大きいほうを取る.
        if A <= W: dp[1:, A:] = np.maximum(dp[1:, A:], dp[:K, :W+1-A] + B)

    print(dp[K, W])


if __name__ == '__main__':
    main()
