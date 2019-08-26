# 05 : 個数制限付き部分和問題

### キーワード

- DP
- ナップサック DP
- DP の値に bool 値より多くの情報を持たせる
- DP の値に復元のための情報を持たせる
- (少し発展すると) 戻す DP

###  AtCoder 上の類題

- [Maximum-Cup 2018 D Many Go Round](https://atcoder.jp/contests/maximum-cup-2018/tasks/maximum_cup_2018_d)　(DP に bool 値より多くの情報を持たせることで解けます、bitset 高速化で殴ることもできます) -> a.py
- [JOI 2013 本選 D フクロモモンガ](https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho4)　(少し難しめです、DP 値を利用して状態を復元します、[AOJ 0601](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0601)に同じ) -> b.py
- [ARC 083 E Bichrome Tree](https://atcoder.jp/contests/arc083/tasks/arc083_c)　(難しめです) -> c.py
- [ARC 028 D 注文の多い高橋商店](https://atcoder.jp/contests/arc028/tasks/arc028_4)　(かなり難しいです、戻す DP とのセット) -> d.py

### コメント

DP の値を単に bool 型にするのではなく、より多くの情報を持たせることで問題を解いたり、さらに DP 値も利用して状態を復元したりする系の問題です。その辺りのことは[前記事](https://qiita.com/drken/items/a5e6fe22863b7992efdb)に詳しく書いてみました。元々高度なテクニックなので問題例も難しめです。

戻す DP について参考記事:

- [戻すDP](http://sigma425.hatenablog.com/entry/2015/07/31/121439) (sigma さん)
- [競技プログラミングにおける戻すDP問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/03/19/154334) (はまやんさん)