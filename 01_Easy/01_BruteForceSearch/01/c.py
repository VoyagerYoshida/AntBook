import sys
from math import ceil  # 小数点以下切り上げ
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
LIST = lambda: list(map(int, INPUT().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')

D, G = MAP()
PC = [LIST() for _ in range(D)]


# 深さ優先探索
def dfs(g, i):
    if i <= 0: return INF  # 停止条件
    n = min(ceil(g/(100*i)), PC[i-1][0])  # 点数の高い問題から, 選べるだけ選ぶ. min(x, MAX) で上限設定.
    s = 100 * i * n
    if n == PC[i-1][0]: s += PC[i-1][1]
    if g > s: n += dfs(g-s, i-1)  # 分岐処理 1

    # 100*i 点問題を考慮する選択肢(1)と, 考慮しない選択肢(2)を比較し小さい方を選ぶ
    return min(n, dfs(g, i-1))  # 分岐処理 2


def main():
    print(dfs(G, D))


if __name__ == '__main__':
    main()
