import sys
from itertools import permutations  # permutations(range(N)) : 長さ N の順列(0,1, ..., N-1)を全て出力.
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    N, M = MAP()
    edges = set()  # 方向付きで枝を保持

    for _ in range(M):
        u, v = MAP()
        edges |= {(u-1, v-1), (v-1, u-1)}

    # 0 から始まる順列 p のうち, (p[i], p[i+1]) が枝集合 edges にすべて含まれるかを確認し, カウントする.
    print(sum(all((u, v) in edges for u, v in zip(p, p[1:])) for p in permutations(range(N)) if p[0] == 0))


if __name__ == '__main__':
    main()
