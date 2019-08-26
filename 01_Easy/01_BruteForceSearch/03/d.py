import sys
import numpy as np
from scipy.ndimage.morphology import distance_transform_cdt
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    H, W = MAP()
    A = [INPUT() for _ in range(H)]

    # A : 2 次元 numpy 配列. 白マス -> True, 黒マス -> False
    A = np.array([[(Ai[j] != "#") for j in range(W)] for Ai in A])
    # distance_transform_cdt(X) : 2 次元 numpy 配列 X の要素 0 からの距離を要素に持つ 2 次元 numpy 配列を返す.
    # [metric] taxicab : マンハッタン距離 (4 近傍), chessboard : チェビシェフ距離 (8 近傍)
    print(distance_transform_cdt(A, metric="taxicab").max())


if __name__ == '__main__':
    main()
