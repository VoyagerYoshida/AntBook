# 09 : Farm Tour

### キーワード

- フロー
- 最大流・最小費用流
- **点素パス・辺素パス**のパッキング

### AtCoder 上の類題

- [AOJ 3047 Shiritori](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=3047)　(辺素パスの考え方になじんでいると簡単です) -> a.py
- [TDPC R グラフ](https://atcoder.jp/contests/tdpc/tasks/tdpc_graph)　(想定解法はもちろん DP ですが、フローでも解けることで有名です。結局 2 本の点素パスを流す問題に落ちます。) -> b.py
- [AOJ 2520 自転車](http://judge.u-aizu.ac.jp/onlinejudge/cdescription.jsp?cid=ACPC2013Day1&pid=F)　(2 本の点素パスが取れるかを問う問題です) -> c.py
- [ARC 039 D 旅行会社高橋君](https://atcoder.jp/contests/arc039/tasks/arc039_d)　(フローで解く問題ではないですが、「**二重辺連結成分分解**して得られる各成分は edge-connectivity が 2 以上である (どの 2 点間も 2 本の辺素パスがとれる)」という性質を思うと解法が自然に思えます) -> d.py

### コメント
グラフ上の 2 点 s, t が与えられて「頂点を共有しないような s-t パスの集合」を点素パスと呼び、最適な点素パスの集合を求めるタイプの問題です (辺を共有しないものは辺素パス)。こういった問題はほとんどの場合、フローを流す問題になります。