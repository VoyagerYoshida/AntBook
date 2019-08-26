# 01 : 数独

### キーワード

- 探索
- 探索順序を工夫する
- バックトラック

### AtCoder 上の類題

- [UTPC 2013 E 2-SAT](https://atcoder.jp/contests/utpc2013/tasks/utpc2013_05)　(実は素直な探索で解けて、計算量の見積りが本質です) -> a.py
- [JOI 2008 予選 D 薄氷渡り](https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d)　(見積もり大事です、[AOJ 0535](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0535) に同じ) -> b.py
- [JOI 2009 予選 F 方向音痴のトナカイ](https://atcoder.jp/contests/joi2010yo/tasks/joi2010yo_f)　(後ろから解くと速いです、[AOJ 0548](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0548) に同じ) -> c.py
- [AOJ 2026 Divisor is the Conqueror](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2026)　(同じく後ろから解くと速いバックトラックです) -> d.py
- [AOJ 2443 ReverseSort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2443)　(前と後ろの両方から攻める**両側探索**と呼ばれているものです) -> e.py
- [AOJ 0091 Blur](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0091)　(AOJ Volume 0 で最難と有名です、integrality がよくわからないですが**単体法**でも通りました、ということはもしかしたらフロー解があるのかもです) -> f.py

### コメント

基本的には DFS などによる全探索ですが、全探索方法があまり自明でないタイプの問題です。DFS ではしばしば「前の状態に戻す」といことをするので、そこをいかに高速に実現するかが大事になることもあります (そこを強く意識した DFS を**バックトラック**と言います)。