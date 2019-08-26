# 04 : Sequence

### キーワード

- Suffix Array

### AtCoder 上の類題

- [SPOJ SARRAY Suffix Array](http://www.spoj.com/problems/SARRAY/)　(高速な SA ライブラリの verify に。昔は SA-IS でないと通らなかったようですが現在はもう少し遅い解法でも通るようです。) -> a.py
- [DISCO presents ディスカバリーチャンネル プログラミングコンテスト2016 予選 C アメージングな文字列は、きみが作る！](https://atcoder.jp/contests/discovery2016-qual/tasks/discovery_2016_qual_c)　(SA 以外のところがむしろメインかもですが、辞書順最小な接尾辞を選ぶ考え方は似通っています) -> b.py
- [Japan Alumni Group Summer Camp 2014 Day 4 F Longest Match](https://atcoder.jp/contests/jag2014summer-day4/tasks/icpc2014summer_day4_f)　(SA + segtree です) -> c.py
- [CODE FESTIVAL 2016 Elimination Tournament Round 1 B 数字列をカンマで分ける問題](https://atcoder.jp/contests/cf16-tournament-round1-open/tasks/asaporo_f)　(SA + 二分探索です) -> d.py
- [RUPC 2018 day H Hth Number](https://onlinejudge.u-aizu.ac.jp/beta/room.html#RitsCamp18Day2/problems/H)　(非常に教育的かつ典型的な SA + 二分探索です) ->e.py

### コメント

Suffix Array です。Suffix Array を求めるアルゴリズムは様々なものが提案されており、特に O(n)O(n) で求められる **SA-IS** は理論上も実際上も高速です。