import sys
from collections import deque
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)

H, W, N = MAP()
dungeon_map = tuple(["X"*(W+1)] + ["X"+INPUT() for _ in range(H)])  # インデックス 0 の部分をずらすため


# 幅優先探索
def bfs(start, factory):
    y, x = start
    queue = deque()
    queue.append((0, y, x))
    # 各行について, bit 列で状態を保持. 地点 (y, x) について, bin_map[y] の 1+x 桁目が 0 なら未到達, 1 なら到達済を表す.
    bin_map = [0] * (H+1)
    bin_map[y] |= (1 << x)  # |= : 論理和

    while queue:
        cnt, y, x = queue.popleft()
        print(cnt, y, x)
        print(bin_map)
        for h, w in [[y-1, x], [y, x+1], [y+1, x], [y, x-1]]:
            if 0 <= h <= H and 0 <= w <= W:
                # 移動先が工場の場合
                if (h, w) == factory: return cnt + 1  # 終了条件
                # 移動先に障害物が無く, 未到達の場合
                elif dungeon_map[h][w] != "X" and not (bin_map[h] >> w) & 1:
                    queue.append((cnt+1, h, w))
                    bin_map[h] |= 1 << w  # 地点 (h, w) を到達済に変更


def main():
    # 巣と工場の位置を 2 次元タプルの辞書で持つ(スタート地点のキーは 0)
    point = {}
    for y, row in zip(range(1, H+1), dungeon_map[1:]):
        for d in list(row):
            if d.isdigit(): point[int(d)] = (y, row.index(d))  # isdigit(s) : 文字列 s が 0 以上の整数なら True
            elif d == "S": point[0] = (y, row.index(d))

    ans = 0
    for i in range(N): ans += bfs(point[i], point[i+1])

    print(ans)


if __name__ == '__main__':
    main()
