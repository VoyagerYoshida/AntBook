import sys
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    X, Y = MAP()
    # Y を商が X 以下になる直前まで 2 で割る行為を繰返し, 割った回数 i が解答になる.
    # 最後の商を n とすると, 解答に該当する数列は, [n, n**2, n**4, n**8, ..., n**i] となる.
    print(len(bin(Y//X)) - 2)  # 0b... なので, 先頭の 2 文字分引く. 解答となる数列は


if __name__ == '__main__':
    main()
