import sys
from collections import deque
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    R, C = MAP()
    sy, sx = MAP()
    gy, gx = MAP()
    sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
    c = [list(INPUT()) for _ in range(R)]

    c[sy][sx] = 0
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([[sy, sx]])

    # 幅優先探索
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            if c[y+dy][x+dx] == ".":
                c[y+dy][x+dx] = c[y][x] + 1
                queue.append([y+dy, x+dx])

    print(c[gy][gx])


if __name__ == '__main__':
    main()
