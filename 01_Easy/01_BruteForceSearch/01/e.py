import sys
from itertools import combinations as comb  # 組み合わせ. comb(p, r) でタプル p から長さ r の全てのタプル列のリストを返す.
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    N, M = MAP()
    XY = [tuple(map(int, INPUT().split())) for _ in range(M)]

    for i in range(N, 0, -1):  # N 人から, できるだけ人数が多くなるように i 人とる.
        for j in comb(range(1, N+1), i):  # i 人の部分集合(タプル)のリストを作成する.
            if all((x, y) in XY for x, y in comb(j, 2)):  # 部分修吾の任意の組み合わせが全て XY に存在するかを調べる.
                print(i)
                exit()


if __name__ == '__main__':
    main()
