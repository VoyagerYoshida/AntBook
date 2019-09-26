import sys
import numpy as np
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)
INF = float('inf')

N, W_max = MAP()
VW = [MAP() for _ in range(N)]
V, W = zip(*VW)


def case1():
    # (重さ, 価値)
    left = [(0, 0)]
    right = [(0, 0)]
    for i in range(N//2): left += [(x + W[i], y + V[i]) for x, y in left]
    for i in range(N//2, N): right += [(x + W[i], y + V[i]) for x, y in right]
    left.sort()  # 重さ順
    right.sort()

    # 価値が無いものを除く
    def remove_worthless(li):
        temp = []
        current_value = -1
        for x, y in li:
            if x > W_max: break
            if y > current_value:
                current_value = y
                temp.append((x, y))

        return temp

    left = remove_worthless(left)
    right = remove_worthless(right)
    right.append((INF, 0))

    idx = 0
    ans = 0
    for x, y in left[::-1]:
        R_max = W_max - x  # 右で使える重さは左で使った残り
        while right[idx+1][0] <= R_max: idx += 1  # 右の重量が残り以下のもの
        res = y + right[idx][1]
        if ans < res: ans = res

    return ans


def case2():
    L = N*1000 + 1
    dp = np.zeros(L, dtype=np.int64)  # 総重量, 最大価値
    idx = 1
    for v, w in VW:
        dp[w:w+idx] = np.maximum(dp[w:w+idx], dp[:idx] + v)
        idx += w

    return dp[:W_max+1].max()


def case3():
    L = N*1000 + 1
    dp = np.zeros(L, dtype=np.int64)  # 総価値, 最小重量
    dp[1:] = 10 ** 18
    idx = 1
    for v, w in VW:
        dp[v:v+idx] = np.minimum(dp[v:v+idx], dp[:idx] + w)
        idx += v

    possible_value = (dp <= W_max).nonzero()[0]

    return possible_value.max()


def main():
    if N <= 30: print(case1())  # N <= 30
    elif max(W_max) <= 1000: print(case2())  # N <= 200 and 1 <= w_{i} <= 1,000
    else: print(case3())  # N <= 200 and 1 <= v_{i} <= 1,000


if __name__ == '__main__':
    main()
