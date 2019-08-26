# 01 : 巡回セールスマン問題

### キーワード

- bit DP
- TSP

### AtCoder 上の類題

- [JOI 2016 予選 D ぬいぐるみの整理](https://atcoder.jp/contests/joi2017yo/tasks/joi2017yo_d)　(とてもよい bit DP の例題です) -> a.py
- [AOJ Course Traveling Salesman Problem](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=jp)　(巡回セールスマン問題です) -> b.py
- [ABC 041 D 徒競走](https://atcoder.jp/contests/abc041/tasks/abc041_d)　(**トポロジカルソートの数え上げ**です。bit DP の例題としてはとてもよいです。トポソ数え上げは一般グラフでは #P-complete ですが、ツリー上ではツリー DP で効率よく解けます) -> c.py
- [JAG Practice Contest for ACM-ICPC Asia Regional 2013 C SIRO Challenge](https://atcoder.jp/contests/jag2013autumn/tasks/icpc2013autumn_c)　(重ための TSP です) -> d.py

### コメント

ついに bit DP まで来ました。ナイーブに考えると n! 通り探索する必要のありそうな問題に対して、2^n 通り程度の状態考えればいいようにする使い方が最もよく見られます。