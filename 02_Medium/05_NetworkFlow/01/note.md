# 01 : 最大通信量

### キーワード

- フロー
- 最大流
- 最大流最小カット定理

### AtCoder 上の類題

- [AOJ Course Maximum Flow](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp)　(最大流問題の verify に) -> a.py
- [yukicoder No.654 Air E869120](https://yukicoder.me/problems/no/654)　([アルゴリズムデザイン](https://www.amazon.co.jp/アルゴリズムデザイン-Jon-Kleinberg/dp/4320122178)にも載っている典型的な最大流の適用例です) -> b.py
- [ABC 010 D 浮気予防](https://atcoder.jp/contests/abc010/tasks/abc010_4)　(**最小カット**問題を解きたくなるので、最大流に帰着します) -> c.py
- [ARC 074 F Lotus Leaves](https://atcoder.jp/contests/arc074/tasks/arc074_d)　(最小カットが自然に出て来るので、最大流に帰着します) -> d.py
- [KUPC 2016 E 柵](https://atcoder.jp/contests/kupc2016/tasks/kupc2016_e)　(同じく) -> e.py
- [JAG Practice Contest for ACM-ICPC Asia Regional 2014 F Reverse a Road II](https://atcoder.jp/contests/jag2014autumn/tasks/icpc2014autumn_f)　(少し難しいですが、最大流最小カット定理の構造をきちんと理解しているかを問う良問です) -> f.py

### コメント

最大流問題です。問題設定からは最小カットの方が自然に思い浮かぶような問題 (最大流最小カット定理から最大流問題を解くことに帰着します) も含めました。