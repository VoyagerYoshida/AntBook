# 03 : 個数制約付きナップサック

### キーワード

- DP
- deque
- スライド最小値を用いた DP 高速化

### AtCoder 上の類題

- [CODE FESTIVAL 2016 Tournament Round 3 A ストラックアウト](https://atcoder.jp/contests/cf16-tournament-round3-open/tasks/asaporo_d) -> a.py
- [JOI 2014 予選 F 財宝](https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_f)　([AOJ 0613](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0613) に同じ) -> b.py
- [COLOCON Colopl programming contest 2018 D すぬけそだて――トレーニング――](https://atcoder.jp/contests/colopl2018-qual/tasks/colopl2018_qual_d)　(より単純な解法も) -> c.py
- [JOI 2009 本選 E ダンジョン](https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_e)　(deque を使う O(n) 解法があるようです、[AOJ 0553](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0553) に同じ) -> d.py
- [treeone カット問題](https://twitter.com/ei1333/status/952921366570844161): おまけに -> e.py

### コメント

DP 高速化技法としてよく見られる手法の 1 つ、スライド最小値 (他に累積和, インライン DP, Convex Hull Trick など) です。多くの場合、segtree を用いた高速化もできますが、スライド最小値が決まると segtree 高速化よりも計算量オーダーを落とせます。