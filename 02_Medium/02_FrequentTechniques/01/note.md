# 01 : Subsequence

### キーワード

- しゃくとり法

### AtCoder 上の類題

- [AOJ Course The Number of Windows](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=jp)　(しゃくとり法の練習に) -> a.py
- [ABC 032 C 列](https://atcoder.jp/contests/abc032/tasks/abc032_c)　(ほぼそのまんまです) -> b.py
- [ABC 038 C 単調増加](https://atcoder.jp/contests/abc038/tasks/abc038_c)　(しゃくとり法は最大区間・最小区間を求めるだけでなく数え上げにも有効です) -. c.py
- [ARC 098 D Xor Sum 2](https://atcoder.jp/contests/arc098/tasks/arc098_b)　(同じく数え上げにも有効です) -> d.py

### コメント

高難易度問題において部分的に登場するイメージが強いテクです。
求めるものが「最小の区間」か「最大の区間」かはあまり影響がないです。POJ の例題は最小区間ですが、ABC 032 C は最大区間です。そればかりか、しゃくとり法は条件を満たすものを**列挙する**タイプのアルゴリズムなので数え上げもできます。