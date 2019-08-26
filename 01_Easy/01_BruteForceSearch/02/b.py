import sys
from copy import deepcopy
INPUT = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 9)


def main():
    A = [list(INPUT()) for _ in range(10)]
    B = [['x'] * 10 for _ in range(10)]

    # 深さ優先探索
    def dfs(x, y):
        # 停止条件
        if not (0 <= x < 10):
            return
        elif not (0 <= y < 10):
            return
        elif Ac[x][y] == "x":
            return

        Ac[x][y] = "x"

        dfs(x + 1, y)  # 分岐処理 1: 下
        dfs(x - 1, y)  # 分岐処理 2: 上
        dfs(x, y + 1)  # 分岐処理 3: 右
        dfs(x, y - 1)  # 分岐処理 4: 左

    for i in range(10):
        for j in range(10):
            # 方針 : 一か所を埋め立てて, その場所とつながった場所を海にしたとき全て海になるかを確認する.
            Ac = deepcopy(A)
            Ac[i][j] = "o"
            dfs(i, j)

            if Ac == B:
                print("YES")
                exit()

    print("NO")


if __name__ == '__main__':
    main()
