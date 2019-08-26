# 07 : 巨大ナップサック

### キーワード

- 半分全列挙

### AtCoder 上の類題

- [AOJ Course Huge Knapsack Problem](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_H&lang=jp)　(手法の verify に) -> a.py
- [ABC 032 D ナップサック問題](https://atcoder.jp/contests/abc032/tasks/abc032_d)　(例題 2-3-4 のテクも使います) -> b.py
- [AGC 026 C - String Coloring](https://atcoder.jp/contests/agc026/tasks/agc026_c)　(半分全列挙と見抜けさえすればという感じです) -> c.py
- [ARC 017 C 無駄なものが嫌いな人](https://atcoder.jp/contests/arc017/tasks/arc017_3) -> d.py
- [CODE THANKS FESTIVAL 2017 G Mixture Drug](https://atcoder.jp/contests/code-thanks-festival-2017/tasks/code_thanks_festival_2017_g)　(いわゆる**最大安定集合問題**です) -> e.py

### コメント
例題 3-2-6 は O(n^4) を O(n^2 logn) にする系の半分全列挙でしたが、今度は O(2^n) を O(n 2^(n/2)) にする系の半分全列挙です。
最後の問題は「一般グラフの最大安定集合問題」そのものですが、n <= 40 程度なら半分全列挙で解けます。さらに計算時間を落とした O(1.381^n) のシンプルなアルゴリズムもあります:

参考記事:

- [指数時間アルゴリズム入門](https://www.slideshare.net/wata_orz/ss-12131479) (wata さん)
- [JOI 2015 予選6：財宝の、想定解法よりも効率的な解法の解説](https://drive.google.com/file/d/1mMknATB6sWxVIUSJkhpSMGIUvJOVYsYR/view) (square さん)
- [競技プログラミングにおける半分全列挙問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2018/01/06/112704) (はまやんさん)