# 03 : ドミノ敷き詰め

### キーワード

- bit DP
- bit をスライドさせる感じの bit DP

### AtCoder 上の類題

- [JOI 2010 予選 F JOI旗](https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_f)　(比較的似た問題です、[AOJ 0559](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0559) に同じ) -> a.py
- [CODE FESTIVAL 2014 予選A D 壊れた電卓](https://atcoder.jp/contests/code-festival-2014-quala/tasks/code_festival_qualA_d)　(桁 DP との組み合わせです) -> b.py
- [TDPC Q 連結](https://atcoder.jp/contests/tdpc/tasks/tdpc_concatenation)　(ナップサック DP を進めていくにつれて bit 状態がスライドしていくタイプの DP です、個人的に **sliding bit DP** と呼んでいます) -> c.py
- [ARC 058 E 和風いろはちゃん](https://atcoder.jp/contests/arc058/tasks/arc058_c)　(同じく sliding bit DP です) -> d.py
- [JOI 2012 予選 F お土産購入計画](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0581)　(遷移を詰めるのがちょっと大変です) -> e.py

### コメント

ナップサック DP と組み合わさった感じの bit DP を集めました。

参考記事:

- [競技プログラミングにおけるbitDP問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/07/16/130151)