# 14 : ソートしてからナップサック DP

### キーワード

- DP
- ナップサック DP
- 先にソート

### AtCoder 上の類題

- [JOI 2011 予選 C 最高のピザ](https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_c)　([AOJ 0567](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0567) に同じ) -> a.py
- [JOI 2010 本選 B 古本屋](https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho2)　([AOJ 0561](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0561) に同じ) -> b.py
- [TDPC H ナップザック](https://atcoder.jp/contests/tdpc/tasks/tdpc_knapsack) -> c.py
- [2017 CODE FESTIVAL Final D Zabuton](https://atcoder.jp/contests/cf17-final/tasks/cf17_final_d)　(難しいですが、先にソートするんだろうな...と思えることが重要です。そう思えたらどうソートするかをひたすら考えます) -> d.py
- [SRM 502 DIV1 Medium TheProgrammingContestDivOne](https://qiita.com/drken/items/e77685614f3c6bf86f44)　(SRM の問題ですが、個人的に良問だと思います。) -> e.py

### コメント

DP 部分はごく普通のナップサック DP ですが、一見すると順序も自由に入れ替えられるので困るタイプの DP です。こういったものは順番を先に fix できるケースが多いのでそれをどうしたらいいかをひたすら考察することになります。

DEGwer さんの[数え上げテクニック集](https://drive.google.com/file/d/1WC7Y2Ni-8elttUgorfbix9tO1fvYN3g3/view)の「3.1 大きい順に並べる」にも類似の記載があります。

余談ですが「ソートしてナップサック」をかなり一般的なフレームワークに乗せた論文がアルゴリズム系の国際会議 ISSAC 2016 の Best Paper Award に選ばれています！

- [Yasushi Kawase, Kazuhisa Makino, and Kento Seimi: Optimal Composition Ordering Problems for Piecewise Linear Functions, Proceedings of the 27th International Symposium on Algorithms and Computation (ISAAC2016, LIPICS64)](http://drops.dagstuhl.de/opus/frontdoor.php?source_opus=6812)