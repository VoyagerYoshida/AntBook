import sys
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
LIST = lambda: list(map(int, INPUT().split()))
sys.setrecursionlimit(10 ** 9)


def main():
    N = INT()
    AB = sorted([LIST() for _ in range(N)], key=(lambda x: -x[1]))  # y 座標が高い順にソート
    CD = sorted([LIST() for _ in range(N)])  # x 軸が低い順にソート

    cnt = 0
    # 赤と青の点をソートされた順に比較していくと, 青の点を中心に反時計回りに枝が回転するような探索になる.
    for c, d in CD:
        for a, b in AB:
            if a < c and b < d:
                AB.remove([a, b])
                cnt += 1
                break

    print(cnt)


if __name__ == '__main__':
    main()
