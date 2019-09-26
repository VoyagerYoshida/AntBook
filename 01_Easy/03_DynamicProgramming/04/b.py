import sys
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)
INF = float('inf')


def main():
    N, K = MAP()
    A = [INT() for _ in range(N)]

    # 全勝の場合, 1 日目しか満足しない
    if sum(A) == K:
        print(1)
        exit(0)

    dp = [INF] * (N+1)  # sum(A[0]~A[i]) 試合あった時, i+1 日間で通算 dp[j] 回以上勝っていれば, 最大で計 j 日は機嫌が良い.
    dp[0] = 0
    denom = 0  # 前日までのゲームした回数の和
    for i in range(N):
        a = A[i]
        for j in reversed(range(N)):
            if dp[j] == INF: continue
            # (前日の勝率を上回るのに必要な勝利数)/a > dp[i]/denom を式変形
            w = a*dp[j]//denom + 1 if denom else 1  # 1 日目だけ w = 1 (始めは勝率 1/2 からスタート)
            if w <= a: dp[j+1] = min(dp[j+1], dp[j] + w)
        denom += a

    print(sum(x <= K for x in dp) - 1)  # dp[1] ~ dp[N] の中で勝利数 K より小さい数をカウントする.


if __name__ == '__main__':
    main()
