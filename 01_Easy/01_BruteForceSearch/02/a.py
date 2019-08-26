import sys
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)

H, W = MAP()
C = [list(INPUT()) for _ in range(H)]


# 深さ優先探索
def dfs(y, x):
    # 停止条件
    if not (0 <= y < H and 0 <= x < W) or C[y][x] == "#": return
    if C[y][x] == "g":
        print("Yes")
        exit()

    C[y][x] = "#"

    dfs(y+1, x)  # 分岐処理 1: 下
    dfs(y-1, x)  # 分岐処理 2: 上
    dfs(y, x+1)  # 分岐処理 3: 右
    dfs(y, x-1)  # 分岐処理 4: 左


def main():
    for i, c in enumerate(C):
        if "s" in c:
            dfs(i, c.index("s"))
            break

    print("No")


if __name__ == '__main__':
    main()
