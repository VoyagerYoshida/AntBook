import sys
INPUT = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 9)


def main():
    S = INPUT()
    l = len(S)
    ans = 0

    # bit 全探索
    for i in range(2**(l-1)):
        tmp = S[0]
        for j in range(l-1):
            # a >> b は, 2 進数 a の 右ビットシフト.
            # a = 4 (100), b = 1 のとき, a >> b = 2 (10) となる.
            # a & c は, 2 進数 a と 2 進数 c のビットマスク(論理積 AND).
            # a = 2 (10), c = 1 (01) のとき, a & c = 0 (00) となる.
            if (i >> j) & 1: tmp += "+"  # i を 2 進数にした際の右から j 番目の数字(0 or 1)を返す.
            tmp += S[j+1]

        ans += eval(tmp)  # eval(s) は, 文字列 s で与えられた式の計算結果を返す.

    print(ans)


if __name__ == '__main__':
    main()
