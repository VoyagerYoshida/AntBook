# 03 : 二人組

### キーワード

- 一般グラフの最大マッチング (not フロー)

### AtCoder 上の類題

- [AOJ 2347 Sunny Graph](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2347)　(Tutte 行列を少し変えて行列補完します、難しいです) -> a.py
- [TOC 2006 Round1 Medium Separate Connections](https://community.topcoder.com/stat?c=problem_statement&pm=6095&rd=9917)　(一般マッチングを verify する問題として長年君臨しています) -> b.py
- [UOJ No.79 一般图最大匹配](http://uoj.ac/problem/79)　(中国語ですが一般マッチングのようです) -> c.py
- [ARC 080 F Prime Flip](https://atcoder.jp/contests/arc080/tasks/arc080_d)　(結局二部グラフの最大マッチングで解けるのですが、一瞬、一般マッチングが必要そうな気分になります) -> d.py
- [RUPC 2018 day2 G Combine Two Elements](https://onlinejudge.u-aizu.ac.jp/beta/room.html#RitsCamp18Day2/problems/G)　(結局二部グラフになるのですが、一般グラフの最大マッチングで殴れます) -> e.py

### コメント

一般グラフの最大マッチングです。大きく以下の 2 通りの方法が知られていますが、プログラミングコンテストでの出題歴は非常に少なく、もし「一般グラフの最大マッチング」に帰着されたと感じたときは違う解法があるケースが多そうです。

- Edmonds の花アルゴリズム
- 行列補完 (Tutte 行列)