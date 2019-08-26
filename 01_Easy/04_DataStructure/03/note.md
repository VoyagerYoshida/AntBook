# 03 : 食物連鎖

### キーワード

- Union-Find 木
- ノードコピーして考える

### AtCoder 上の類題

- [ATC 001 B Union Find](https://atcoder.jp/contests/atc001/tasks/unionfind_a)　(とりあえず Union-Find 木を verify する問題です) -> a.py
- [ABC 049 D 連結](https://atcoder.jp/contests/abc049/tasks/arc065_b)　(Union-Find 木のよい例題です) -> b.py
- [ARC 097 D Equals](https://atcoder.jp/contests/arc097/tasks/arc097_b)　(やはりよい例題です) -> c.py
- [ARC 036 D 偶数メートル](https://atcoder.jp/contests/arc036/tasks/arc036_d)　(難しめですが、蟻本の例題に非常に近い問題です) -> d.py
- [ABC 087 D People on a Line](https://atcoder.jp/contests/arc090/tasks/arc090_b)　(色んな解法がありますが、**重み付き Union-Find 木**が楽です) -> e.py
- [2017 CODE FESTIVAL THANKS H Union Sets](https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_h)　(非常に色んな解法のある問題です、**永続 Union-Find 木**や**並列二分探索**で通せます) -> f.py
- [JOI 2011 本選 E JOI 国のお祭り事情 (Festivals in JOI Kingdom)](https://atcoder.jp/contests/joi2012ho/tasks/joi2012ho5)　(大分難しいです, [AOJ 0575](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0575) に同じ) -> g.py

### コメント

Union-Find 木はちょくちょく出てくるデータ構造です。蟻本の例題はとてもよい問題ではあるのですが、中国語の問題というのが大分辛いですね...。発展的話題として、重み付き Union-Find 木や、永続 Union-Find 木があります。

参考記事:
[競技プログラミングにおけるUnionFind問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/10/04/101826) (はまやんさん)