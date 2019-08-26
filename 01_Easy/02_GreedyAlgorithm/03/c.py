import sys
from collections import Counter  # 文字列やリストの要素の出現回数をカウントし辞書で返す.
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    N, K = MAP()
    S = INPUT()

    T = sorted(S)
    mismatch = 0  # 入力文字列 S と 解答文字列 ans の異なる文字の数を先頭から順にカウントする.
    ans = ''
    for i in range(N):
        # cnt : 入力文字列 S と 解答文字列 ans の i 番目までの要素の差集合 (S にしかないもの) の辞書.
        cnt = Counter(S[:i+1]) - Counter(list(ans))
        num = sum(cnt.values())

        for t in T:
            miss = mismatch + (t != S[i])  # miss : 今までの mismatch に対して, t が S[i] と違う場合に 1 を加える.
            diff = num - (cnt[t] > 0)  # diff : 辞書 cnt 中に文字 t があれば, diff = num - 1
            if miss + diff <= K:
                ans += t
                T.remove(t)
                mismatch = miss
                break

    print(ans)


if __name__ == '__main__':
    main()
