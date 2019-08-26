# 03 : Aggressive Cows

### キーワード

- 二分探索
- 最小値の最大化 (最大値の最小化)

### AtCoder 上の類題

- [CODE FESTIVAL 2015 予選A D 壊れた電車](https://beta.atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_d)　(いい感じの例題です、くぬーさん提供) -> a.py
- [JOI 2013 本選 C バームクーヘン](https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho3)　(しゃくとり法の要素もあって少し難しいです、[AOJ 0600](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0600) に同じ) -> b.py
- [JOI 2016 本選 C JOIOI 王国](https://atcoder.jp/contests/joi2017ho/tasks/joi2017ho_c)　(判定問題に落としてからの Greedy パートが難しめです。実は二分探索しなくても解けます。) -> c.py

### コメント

最小値の最大化を見たら条件反射で二分探索したくなります。なぜなら
　　min(f(i))>=K⇔すべてのiに対してf(i)>=Kmin(f(i))>=K⇔すべてのiに対してf(i)>=K
という関係が成り立つからです。いかにも二分探索のフレームワークがはまりそうですね。

判定問題に落とした後は Greedy であることが多いです。
Greedy パートの難易度は問題によって大きく変わって来ます。