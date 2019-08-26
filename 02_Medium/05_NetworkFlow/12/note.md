# 12 : Intervals

### キーワード

- フロー
- DP
- (重みつき) 区間スケジューリング問題
- DP を DAG 上の最短路問題とみなす
- それを容量 K に拡張する

### AtCoder 上の類題

- [AOJ 2266 Cache Strategy](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2266)　(比較的似ています、少し難しいです) -> a.py
- [KUPC 2016 H 壁壁壁壁壁壁壁](https://atcoder.jp/contests/kupc2016/tasks/kupc2016_h)　(類題と言っていいのか微妙かもですが... Starry Sky Tree を用いる高速化もするなど難しいです) -> b.py

### コメント
非常に中身の濃い問題です。蟻本にて、K = 1 の場合を先に考えていますが、これは (重みつきの) 区間スケジューリング問題で簡単な DP で解けます。

aizuzia さんの [DP を DAG 上の最短経路と思う話](http://d.hatena.ne.jp/Tayama/20111210/1323502092)を思い出すと、K = 1 の場合の DP を DAG 上の最短経路問題だと思えます。ここから頑張って一般の K に拡張することになります。