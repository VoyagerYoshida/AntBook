import sys
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
LIST = lambda: list(map(int, INPUT().split()))
sys.setrecursionlimit(10 ** 9)


def main():
    N = INT()
    P = LIST()

    # S = [2, 3, 5] のとき, sum = [0, 2, 3, 5, 7 , 8, 10] となる.
    # bit = 10110101101 となり, sum の集合内にある桁が 1 になる.
    bit = 1
    for p in P: bit = (bit << p) | bit
    print(bin(bit).count("1"))


if __name__ == '__main__':
    main()
