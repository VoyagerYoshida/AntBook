# 02 : バブルソートの交換回数

### キーワード

- BIT
- 転倒数

### AtCoder 上の類題

- [AOJ Course The Number of Inversions](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D&lang=jp)　(バブルソートの交換回数そのものです) -> a.py
- [Indeedなう 2015 E Line up!](https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_e)　(重みつき転倒数という感じです) -> b.py
- [Tenka1 2017 E CARtesian Coodinate](https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_e)　(転倒数) -> c.py
- [ARC 088 E Papple Sort](https://atcoder.jp/contests/arc088/tasks/arc088_c)　(転倒数) -> d.py
- [ARC 033 C データ構造](https://atcoder.jp/contests/arc033/tasks/arc033_3)　(BIT + 二分探索が自然ですが、平方分割などの解法も考えられます) -> e.py
- [第2回早稲田大学プログラミングコンテスト G だるま落とし](https://atcoder.jp/contests/wupc2nd/tasks/wupc_07)　(BIT + 二分探索) -> f.py
- [JOI 2010 本選 E 微生物実験](https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho5)　([AOJ 0564](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0564) に同じ) -> g.py

### コメント

ここんとこ AtCoder 上でも頻出の転倒数 (BIT や分割統治法で求めます) です。
**BIT 上二分探索**を用いるタイプの問題もここに載せました。BIT については hos さんの神資料があります:

- [Binary Indexed Tree のはなし](http://hos.ac/slides/20140319_bit.pdf)