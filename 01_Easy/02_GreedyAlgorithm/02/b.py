import sys
from operator import itemgetter
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    N, M = MAP()
    AB = sorted([list(MAP()) for _ in range(M)], key=itemgetter(1))  # 2 次元リストを x[1] で昇順にソート.

    # 区間 (a, b) が重複していないものをカウントする.
    point = cnt = 0
    for (a, b) in AB:
        if a > point:
            point = b - 1
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
