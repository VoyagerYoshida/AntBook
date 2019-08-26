# 01 : ランダムウォーク

### キーワード

- 期待値
- 連立一次方程式

### AtCoder 上の類題

- [AOJ 2171 Strange Couple](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2171)　(AOJ の問題ですが例題のランダムウォークに極めて近いです) -> a.py
- [Indeedなう 2015 E Page Rank](https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_e)　(特殊な連立一次方程式を解きます) -> b.py
- [codeflyer 2018 本選 D 数列 XOR](https://atcoder.jp/contests/bitflyer2018-final-open/tasks/bitflyer2018_final_d)　(掃き出し法に関する理解を問います) -> c.py
- [AOJ 2530 Reverse Game](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2530)　(例題 3-2-4 の類題でも簡単に触れた F2 体上の連立一次方程式です、しかしサイズが大きいので **bitset 高速化**を用います) -> d.py

### コメント

連立一次方程式を解いたりする問題です。双六のような確率的挙動が出て来ると連立一次方程式を解くことになるケースが多いイメージがあります。

参考記事:

- [競技プログラミングのための線形代数](http://topcoder.g.hatena.ne.jp/pepsin-amylase/20131203) (amylase さん)
- [競技プログラミングにおける確率・期待値問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2016/11/14/223727) (はまやんさん)
- [競技プログラミングにおける連立方程式問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/03/15/221719) (はまやんさん)