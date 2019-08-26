import sys
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
sys.setrecursionlimit(10**9)
mod = 10**9 + 7


def main():
    D = INT()
    N = [int(n) for n in INPUT()]

    point = 0
    V = [0] * D  # V[i] に, 1 から N までの数のうち, D で割ったあまりが i+1 になるようなものの数を格納
    W = [0] * (D+10)
    for n in N:
        for i in range(D+10): W[i] = 0  # W を 0 で初期化
        for i, v in enumerate(V):
            if v - 0:
                W[i+1] += v
                W[i+10] -= v

        W[point] += 1
        W[point+n] -= 1

        tmp = 0
        for i, w in enumerate(W):
            tmp = (tmp+w) % mod
            V[i % D] += tmp

        point += n
        point %= D

    V[point] += 1
    print((V[0]-1) % mod)


if __name__ == '__main__':
    main()
