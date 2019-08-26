import sys
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
sys.setrecursionlimit(10 ** 9)


def main():
    N = INT()
    T = [INT() for _ in range(N)]
    T.sort()

    S = [0, 0]  # 肉焼き器
    for t in reversed(T): S[S[0] > S[1]] += t  # True なら S[1] に, False なら S[0] に t が大きい順に加えられる.
    print(max(S))


if __name__ == '__main__':
    main()
