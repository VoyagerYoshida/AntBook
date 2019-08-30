# 01 : 01 ナップサック問題

### キーワード

- DP
- ナップサック DP

### AtCoder 上の類題

- [AOJ Course 0-1ナップザック問題](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp)　(例題そのものです)
- [TDPC A コンテスト](https://atcoder.jp/contests/tdpc/tasks/tdpc_contest)　(部分和問題です) -> a.py
- [TDPC D サイコロ](https://atcoder.jp/contests/tdpc/tasks/tdpc_dice)　(添字増やす系のナップサックです) -> b.py
- [ABC 015 D 高橋くんの苦悩](https://atcoder.jp/contests/abc015/tasks/abc015_4)　(全体の個数制約が加わります、くちもちとくらさん提供) -> c.py
- [JOI 2012 予選 D 暑い日々](https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d)　([AOJ 0579](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0579) に同じ) -> d.py
- [TDPC E 数](https://atcoder.jp/contests/tdpc/tasks/tdpc_number)　(いわゆる**桁 DP** です。桁 DP もナップサックの一種で、bit DP とは別物です) -> e.py

### コメント

ナップサックな DP については[記事](https://qiita.com/drken/items/a5e6fe22863b7992efdb)を書いてみました。DP を漸化式だととらえる立場からの入門記事です。DP を全探索の効率化から入る立場の入門資料として「[プログラミングコンテストにおける動的計画法](https://www.slideshare.net/iwiwi/ss-3578511)」がとてもよいです。漸化式派と全探索メモ化派は、強い人たちの間でも二分されているので肌の合う考え方で入門していくのがいいと思います。

桁 DP について参考記事:

- [桁DP入門](http://pekempey.hatenablog.com/entry/2015/12/09/000603) (pekempey さん)
- [競技プログラミングにおける桁DP問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/04/23/212728) (はまやんさん)
