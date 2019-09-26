import sys
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)


def main():
    H, W = MAP()
    field = [INPUT() for _ in [0] * H]
    HR = list(range(H))
    WR = list(range(W))
    WR2 = list(range(W-2, -1, -1))

    # horizontal dp, vertical dp
    hor = [[[-1] * H for _ in WR] for _ in HR]  # hor[top][left][bottom] = right
    ver = [[[-1] * W for _ in WR] for _ in HR]  # ver[top][left][right]  = bottom

    for i in HR:
        hi = hor[i]
        fi = field[i]
        curr = hi[-1][i] = W - 1
        curc = fi[-1]
        for j in WR2:
            if fi[j] != curc:
                curr = hi[j][i] = j
                curc = fi[j]
            else:
                hi[j][i] = curr

    for i in HR:
        hi = hor[i]
        vi = ver[i]
        fi = field[i]
        for j in WR:
            hij = hi[j]
            vij = vi[j]
            fij = fi[j]
            curr = hij[i]
            for k in HR[i + 1:]:
                if field[k][j] != fij: break
                curr = hij[k] = min(curr, hor[k][j][k])

            curr = j
            for k in range(H-1, i-1, -1):
                h_ijk = hij[k]
                if h_ijk == -1: continue
                while curr <= h_ijk:
                    vij[curr] = k
                    curr += 1

    ans = 0
    while True:
        if hor[0][0][-1] == W-1: break
        for i in HR:
            hi = hor[i]
            vi = ver[i]
            for j in WR:
                hij = hi[j]
                vij = vi[j]

                # print(ans+1, i, j, 'first')
                # print(hor[i][j])
                # print(ver[i][j])

                # Update hor using hor, ver using ver
                for k in HR[i:]:
                    h_ijk = hij[k]
                    if h_ijk == -1: break
                    if h_ijk == W-1: continue
                    hij[k] = max(h_ijk, hi[h_ijk+1][k])

                for k in WR[j:]:
                    v_ijk = vij[k]
                    if v_ijk == -1: break
                    if v_ijk == H - 1: continue
                    vij[k] = max(v_ijk, ver[v_ijk+1][j][k])

                # print(ans + 1, i, j, 'before')
                # print(hor[i][j])
                # print(ver[i][j])

                # Update hor using ver, ver using hor
                curr = j
                for k in range(H-1, i-1, -1):
                    h_ijk = hij[k]
                    if h_ijk == -1: continue
                    while curr <= h_ijk:
                        vij[curr] = max(vij[curr], k)
                        curr += 1

                curb = i
                for k in range(W-1, j-1, -1):
                    v_ijk = vij[k]
                    if v_ijk == -1: continue
                    while curb <= v_ijk:
                        hij[curb] = max(hij[curb], k)
                        curb += 1

                # print(ans+1, i, j, 'after')
                # print(hor[i][j])
                # print(ver[i][j])
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
