# 02 : 仕事の割り当て

### キーワード

- フロー
- 二部グラフ
- 二部グラフの最大マッチング
- 割り当て問題

### AtCoder 上の類題

- [AOJ Course Bipartite Matching](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_7_A&lang=jp)　(二部マッチングの verify に、問題のサイズは小さめ) -> a.py
- [ABC 091 C 2D Plane 2N Points](https://atcoder.jp/contests/abc091/tasks/arc092_a)　(実は Greedy に解けるのですが、フローで殴れます) -> b.py
- [AOJ 1163 カードゲーム](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1163&lang=jp)　(とても典型的な二部マッチングです) -> c.py
- [AOJ 2480 Blame Game](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2480)　(難しめです、二部マッチングの**最適性条件**についての深い理解を問う良問です) -> d.py
- [Indeed なう F 就職活動](https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_f)　(難しいです、結局フローを流すわけではないですが、**Hall の定理**を適用します) -> e.py
- [ARC 076 F Exhausted?](https://atcoder.jp/contests/arc076/tasks/arc076_d)　(難しいです、セグメントツリーの類題としても挙げました。やはり Hall の定理を適用します) -> f.py

### コメント

最大流問題の最もよくある応用として、二部グラフの最大マッチングがあります。二部グラフの最大マッチングに関連する話題として **Hall の定理**があります。これは二部グラフに対する最大流最小カット定理や、**Dilworth の定理** (下に出て来ます) との等価性も知られており、ネットワークフロー理論の強力な定理群の 1 つの側面と考えることができます。