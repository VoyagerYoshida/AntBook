import sys
from itertools import permutations  # permutations(A, b) : リスト A の要素のうち k 個を取り出した順列を全て出力.
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
sys.setrecursionlimit(10 ** 9)


def main():
    N = INT()
    K = INT()
    cards = [INT() for _ in range(N)]

    # k 個の順列 p の要素をつなげて, セットに重複なく格納しカウントする.
    print(len(set(''.join(map(str, p)) for p in permutations(cards, K))))


if __name__ == '__main__':
    main()
