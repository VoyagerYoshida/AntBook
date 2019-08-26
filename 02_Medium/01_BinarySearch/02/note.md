# 02 : Cable Master

### キーワード

- 二分探索
- 解を仮定し可能か判定 (判定問題にするテク)
- 連続値に対する二分探索
- 方程式を解く二分探索

### AtCoder 上の類題

- [ABC 023 D 射撃王](https://atcoder.jp/contests/abc023/tasks/abc023_d)　(よい例題です) -> a.py
- [ARC 050 B 花束](https://atcoder.jp/contests/arc050/tasks/arc050_b)　(よい例題です) -> b.py
- [ABC 026 D 高橋君ボール1号](https://atcoder.jp/contests/abc026/tasks/abc026_d)　(連続量に対する二分探索... どちらかと言うと二分法です) -> c.py
- [AOJ 2220 The Number of the Real Roots of a Cubic Equation](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2220)　(方程式を解きます) -> d.py

### コメント

「～を満たす最大 (最小) の値を求めよ」という問題に対して、

- 解 x を仮定して可能かを判定する問題に置き換えて
- 解 x が可能となるような最大 (最小) の x を求める

というのはあまりにも頻繁に出て来るテクニックです！
x という解がとりあえず存在すると仮定することによって、Greedy に判定問題を解くことができるようになるケースが多いです。
また Cable Master は連続値に関する二分探索でもあるので、その筋の問題も加えました。