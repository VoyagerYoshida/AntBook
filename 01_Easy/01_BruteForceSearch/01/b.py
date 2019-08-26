import sys
INPUT = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 9)


def main():
    S = INPUT()
    l = len(S)

    # bit 全探索
    for i in range(2 ** (l - 1)):
        tmp = S[0]
        for j in range(l - 1):
            if (i >> j) & 1: tmp += "+"
            else: tmp += "-"
            tmp += S[j + 1]

        if eval(tmp) == 7:
            print(tmp + "=7")
            break


if __name__ == '__main__':
    main()
