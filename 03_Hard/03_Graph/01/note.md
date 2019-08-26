# 01 : Popular Cows

### キーワード

- 強連結成分分解

### AtCoder 上の類題

- [JOI 2006 本選 D 最悪の記者](https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_d)　(DAG の**トポロジカルソート**です、[AOJ 0519](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0519) に同じ) -> a.py
- [AOJ Course Strongly Connected Components](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C&lang=jp)　(強連結成分分解の verify に) -> b.py
- [TDPC R グラフ](https://atcoder.jp/contests/tdpc/tasks/tdpc_graph)　(強連結成分分解して DP します。フローでも解けるので例題 3-5-9 でも挙げました) -> c.py
- [SRM 608 DIV1 Medium BigO](https://qiita.com/drken/items/SRM 608 DIV1 Medium BigO)　(SRM の問題ですがとても面白いです) -> d.py

### コメント

有向グラフに強連結成分分解を行い、強連結成分を 1 点につぶすと DAG になります。DAG 上で DP したりなど、色んな問題が出題されます。