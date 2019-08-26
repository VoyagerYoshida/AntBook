import sys
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    N, M = MAP()
    # d[i][j][k] : i, j, k の能力を持つ人間が応募できる最も年収の高い会社の年収を格納
    dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

    for _ in range(N):
        a, b, c, w = MAP()
        dp[a][b][c] = max(dp[a][b][c], w)

    for i in range(101):
        for j in range(101):
            for k in range(101):
                dp[i][j][k] = max(dp[i][j][k], dp[max(0, i-1)][j][k], dp[i][max(0, j-1)][k], dp[i][j][max(0, k-1)])

    for _ in range(M):
        x, y, z = MAP()
        print(dp[x][y][z])


if __name__ == '__main__':
    main()
