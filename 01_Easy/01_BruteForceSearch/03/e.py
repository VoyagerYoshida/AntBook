import sys
from collections import deque
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    H, W = MAP()
    C = []

    for i in range(H):
        line = list(INPUT())
        for j in range(W):
            if line[j] == "s":
                queue = deque([(i, j)])
                line[j] = 0
            if line[j] == "g": gy, gx = i, j
        C.append(line)

    while queue:
        y, x = queue.popleft()
        for row, col in [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]:
            if 0 <= row < H and 0 <= col < W and type(C[row][col]) is not int:
                if C[row][col] == "#":
                    C[row][col] = C[y][x] + 1
                    queue.append((row, col))
                else:
                    C[row][col] = C[y][x]
                    queue.appendleft((row, col))

    print('YES' if C[gy][gx] < 3 else 'NO')


if __name__ == '__main__':
    main()
