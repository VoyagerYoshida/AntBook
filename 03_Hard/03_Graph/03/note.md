# 03 : Housewife Wind

### キーワード

- ツリー上のクエリ
- LCA
- Euler Tour
- ダブリング

### AtCoder 上の類題

- [ABC 014 D 閉路](https://atcoder.jp/contests/abc014/tasks/abc014_4)　(LCA を試すよい例題です) -> a.py
- [KUPC 2015 J MODクエリ](https://atcoder.jp/contests/kupc2015/tasks/kupc2015_j)　(LCA 関連のダブリングをするか、HL 分解をします) -> b.py
- [JOI 2011 本選 E JOI 国のお祭り事情](https://atcoder.jp/contests/joi2012ho/tasks/joi2012ho5)　(色んな解法が考えられます, [AOJ 0575](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0575) に同じ) -> c.py
- [天下一プログラマーコンテスト2015 本戦 F 根付き木のみさわさん](https://atcoder.jp/contests/tenka1-2015-final/tasks/tenka1_2015_final_f)　(Euler Tour) -> d.py
- [NJPC 2017 H 白黒ツリー](https://atcoder.jp/contests/njpc2017/tasks/njpc2017_h)　(Euler Tour) -> e.py
- [UTPC 2013 I 支配と友好](https://atcoder.jp/contests/utpc2013/tasks/utpc2013_09)　(Euler Tour) -> f.py
- [square869120Contest #5 H Percepts of Atcoder](https://atcoder.jp/contests/s8pc-5/tasks/s8pc_5_h)　(ダブリングをします、HL分解的な発想に基づいているようです) -> g.py
- [JOI 2015 春合宿 day2-3 道路整備](https://atcoder.jp/contests/joisc2015/tasks/joisc2015_g)　(色んなアルゴリズムを総動員します、二重辺連結成分分解も、問題は[ここ](https://www.ioi-jp.org/camp/2015/2015-sp-tasks/2015-sp-d2.pdf)) -> h.py
- [JOI 2017 春合宿 day2-3 鉄道旅行](https://atcoder.jp/contests/joisc2017/tasks/joisc2017_f)　(最後に LCA のようなものを求めるダブリングに近いことをします、問題は[ここ](https://www.ioi-jp.org/camp/2017/2017-sp-tasks/2017-sp-d2-railway_trip-review.pdf)) -> i.py

### コメント

ツリー上のクエリに関する問題です。典型的にはダブリング、オイラーツアーから、少しよく見るものに **HL 分解**などがあります。

参考記事:

- [完全制覇・ツリー上でのクエリ処理技法](https://topcoder.g.hatena.ne.jp/iwiwi/20111205/1323099376) (iwi さん)
- [Heavy-Light Decomposition](http://beet-aizu.hatenablog.com/entry/2017/12/12/235950) (beet さん)
- [競技プログラミングにおけるLCA問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/05/03/131624) (はまやんさん)
- [競技プログラミングにおけるオイラーツアー問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/04/10/163548) (はまやんさん)
- [競技プログラミングにおけるHL分解まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/04/10/172636) (はまやんさん)