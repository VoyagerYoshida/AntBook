# 02 : Tree 

### キーワード

- 分割統治法
- ツリーの重心
- ツリーの重心分解

### AtCoder 上の類題

- [ARC 087 F Squirrel Migration](https://atcoder.jp/contests/arc087/tasks/arc087_d)　(ツリーの重心に関する数学的問題、包除原理も使います) -> a.py
- [2018 第4回ドワンゴからの挑戦状 予選 E ニワンゴくんの家探し](https://atcoder.jp/contests/dwacon2018-prelims/tasks/dwacon2018_prelims_e)　(ツリーの重心分解) -> b.py
- [DISCO presents ディスカバリーチャンネル コードコンテスト2016 予選 D 道路網](https://atcoder.jp/contests/ddcc2016-qual/tasks/ddcc_2016_qual_d)　(重心分解) -> c.py
- [AOJ 2559 Minimum Spanning Tree](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2559)　(マージテクや重心分解の典型的良問です) -> d.py
- [AOJ 1330 Never Wait for Weights](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1330)　(データ構造をマージする一般的なテク) -> e.py
- [AGC E Blue and Red Tree](https://atcoder.jp/contests/agc014/tasks/agc014_e)　(マージテク) -> f.py
- [UTPC 2014 I 盆栽](https://atcoder.jp/contests/utpc2014/tasks/utpc2014_i)　(マージテク) -> g.py
- [JOI 2012 春合宿 day1-1 ビルの飾り付け 2](https://atcoder.jp/contests/joisc2012/tasks/joisc2012_building2)　(マージテク発祥の問題です、問題は[ここ](https://www.ioi-jp.org/camp/2012/2012-sp-tasks/2012-sp-day1-building2-slides.pdf)) -> h.py

### コメント

ツリーの重心分解を用いたツリー上の分割統治法です。**データ構造をマージする一般的なテク**で解けるケースも多いイメージがあります。また、ツリーの重心の数学的性質を活用するタイプの問題も挙げました。
参考記事:

- [ツリーの重心分解 (木の重心分解) の図解](https://qiita.com/drken/items/4b4c3f1824339b090202)
- ["データ構造をマージする一般的なテク" とは？](https://topcoder.g.hatena.ne.jp/iwiwi/20131226/1388062106) (iwi さん)
- [やぶについて書きます](https://camypaper.bitbucket.io/2016/12/18/adc2016/) (紙ペーパーさん)
- [競技プログラミングにおける重心分解問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/12/19/152143) (はまやんさん)
- [競技プログラミングにおけるマージテク問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/02/10/132728) (はまやんさん)