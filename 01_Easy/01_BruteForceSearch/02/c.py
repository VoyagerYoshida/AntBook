import sys
INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())
sys.setrecursionlimit(10 ** 9)

N, M = MAP()
edges = [set() for _ in range(N)]
visited = [0] * N


# 深さ優先探索
def dfs(node, parent=-1):
    visited[node] = 1
    for n in edges[node]:
        # 停止条件(n != parent and visited[n] == 1)かつ分岐処理(dfs(n, node))
        # 来たノード(parent)以外で到達済みノードが見つかれば, 閉回路ありとして 0 を返す.
        if n != parent and (visited[n] == 1 or dfs(n, node) == 0): return 0

    return 1


def main():
    ans = 0

    # 各ノードから伸びた辺を保持するセットのリスト edges を作成する.
    for _ in range(M):
        u, v = MAP()
        u, v = u - 1, v - 1
        edges[u].add(v)
        edges[v].add(u)

    for i, vis in enumerate(visited):
        if vis == 0: ans += dfs(i)  # 1 つの連結成分について見る

    print(ans)


if __name__ == '__main__':
    main()
