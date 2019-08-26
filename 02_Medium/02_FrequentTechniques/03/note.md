# 03 : Face The Right Way

### キーワード

- 反転 (ライツアウト)
- XOR 操作
- 2 回やったら元に戻る
- 操作の順序を入れ替えても結果は変わらない
- 端から順に決まる Greedy
- 差分更新

### AtCoder 上の類題

- [ABC 048 C Boxes and Candies](https://atcoder.jp/contests/arc064/tasks/arc064_a)　(反転ではないですが、端から決まっていく感じは似ています) -> a.py
- [ABC 083 D Wide Flip](https://atcoder.jp/contests/arc088/tasks/arc088_b)　(一見似ていますが全然違う問題です) -> b.py
- [JOI 2012 本選 A 電飾](https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1)　(それほど似ていないですが面白いです, [AOJ 0603](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0603) に同じ) -> c.py
- [JOI 2008 本選 C あみだくじ](https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_c)　(差分更新系の問題も挙げます、[AOJ 0540](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0540) に同じ。) -> d.py
- [RUPC 2018 day1-C 一致](https://onlinejudge.u-aizu.ac.jp/beta/room.html#RitsCamp18Day1/problems/C)　(差分更新していく感じはよく似ています) -> e.py
- [KUPC 2012 H 植林](https://atcoder.jp/contests/kupc2012/tasks/kupc2012_8)　(少し難しめです。2 回やったら元に戻る性質をフルに考察します) -> f.py

### コメント

**ライツアウト**系の問題 (決まった領域の反転を繰り返して全部白にしたりする系) です。
例題 POJ No.3276 の難易度は高めですが非常に学ぶ要素の多い問題です。
XOR 操作においてしばしば以下のような考察が重要になります。

- 2 回やったら元に戻る (逆元が自分自身)
- 操作の順序を入れ替えても結果は変わらない

この問題の場合、さらに「**端から考える**」ことによって次々と Greedy に決まっていきます。さらに毎ステップごとの操作を実施するのが計算量的に厳しくても「**差分を更新すればいい**」という発想も頻出です。