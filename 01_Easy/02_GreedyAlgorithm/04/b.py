import sys
from bisect import bisect_left as bl
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
sys.setrecursionlimit(10 ** 9)


def main():
    N = INT()
    li = []

    for i in range(N):
        w = INT()
        w_index = bl(li, w)
        if w_index == len(li): li.append(w)  # w の挿入箇所が丁度 li の後ろの時, li にアペンド
        else: li[w_index] = w  # 要素の 1 つを w で置き換え (li の要素の総和が小さくなるように)

    print(len(li))


if __name__ == '__main__':
    main()
