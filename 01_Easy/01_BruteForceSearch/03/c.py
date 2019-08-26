import sys
from collections import deque
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    H, W = MAP()
    dungeon = []  # 地図を表す 2 次元リスト. 元の白マスは 0, 元の黒マスは 1, 変更(白->黒)マスは 2 で状態を保持する.
    walls = 0  # 元の黒マスの数
    for _ in range(H):
        line = [0 if i == "." else 1 for i in INPUT()]
        walls += line.count(1)
        dungeon.extend([line])

    # 幅優先探索
    queue = deque([(0, 0, 1)])
    while queue:
        y, x, cnt = queue.popleft()
        if y == H-1 and x == W-1:
            print(H*W - walls - cnt)  # マスの総数 - 元の黒マスの数 - 最短経路のマス数
            exit()
        for row, col in [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]:
            if 0 <= row < H and 0 <= col < W and not dungeon[row][col]:  # 移動先が白マス(0)の場合
                dungeon[row][col] = 2
                queue.append((row, col, cnt+1))

    print(-1)


if __name__ == '__main__':
    main()
