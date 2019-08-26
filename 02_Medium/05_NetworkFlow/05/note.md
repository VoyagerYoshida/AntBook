# 05 : Asteroids

### キーワード

- フロー
- 二部グラフ
- 二部グラフの最小点被覆・最大安定集合
- グリッド問題を二部グラフにする 2 つの方法

### AtCoder 上の類題

- [SoundHound Inc. Programming Contest 2018 (春) C 広告](https://beta.atcoder.jp/contests/soundhound2018/tasks/soundhound2018_c)　(パターン 2 の典型問題で**最大安定集合問題**です) -> a.py
- [2015 天下一 予選A C 天下一美術館](https://atcoder.jp/contests/tenka1-2015-quala/tasks/tenka1_2015_qualA_c)　(パターン 2) -> b.py
- [yukicoder No.421 しろくろチョコレート](https://yukicoder.me/problems/no/421)　(パターン 2) -> c.py
- [AOJ 2429 まるかいて](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2429)　(パターン 1 で二部グラフにします、最小費用流になります) -> d.py
- [Japan Alumni Group Spring Contest 2014 C Decoding Ancient Messages](https://atcoder.jp/contests/JAG2014Spring/tasks/icpc2014spring_c)　(難しめですがパターン 1 の面白い問題です) -> e.py

### コメント

グリッドに関する問題はしばしば二部グラフにして考えることが有効ですが、2 つのパターンをよく見る気がします:

1. 左ノードが x 座標、右ノードが y 座標に対応して、各マス (x, y) は左右を結ぶ辺に対応する (Asteroids はこっち)
2. グリッドグラフは市松模様に塗ると二部グラフである

参考記事:

- [競技プログラミングにおける最大クリーク問題、最大独立集合問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/08/13/182948) (はまやんさん)