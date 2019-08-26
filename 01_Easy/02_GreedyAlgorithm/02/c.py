import sys
from bisect import bisect_left as bl  # bl(A, x) : ソート済みリスト A に対して順序を崩さずに x を挿入できるインデックスを返す.
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    N = INT()
    # 2 次元リストを x[0] で昇順にソート, x[0] が同じ場合は x[1] で降順にソート.
    WH = sorted([list(MAP()) for _ in range(N)], key=(lambda x: (x[0], -x[1])))

    present = [WH[0][1]]  # プレゼントの短辺の長さを昇順に格納
    for _, h in WH[1:]:
        if h > present[-1]: present.append(h)
        else: present[bl(present, h)] = h  # w の長さが一つ前と同じなら, h が短いほうに置き換える.

    print(len(present))


if __name__ == '__main__':
    main()
