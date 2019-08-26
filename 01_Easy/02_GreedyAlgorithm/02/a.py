import sys, re  # 正規表現 re.findall("w", s) : 文字列 s の中のパターン w とマッチする部分をすべてリストとして返す.
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
sys.setrecursionlimit(10 ** 9)


def main():
    T = INT()
    ans = []

    for _ in range(T):
        S = INPUT()
        ans.append(len(re.findall("(tokyo|kyoto)", S)))  # パターン同士の重複部が無いように取り出される.

    for a in ans: print(a)


if __name__ == '__main__':
    main()
