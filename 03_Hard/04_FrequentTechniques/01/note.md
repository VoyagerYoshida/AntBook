# 01 : Largest Rectangle in a Histogram

### キーワード

- ヒストグラム長方形面積最大化
- stack

### AtCoder 上の類題

- [KUPC 2013 D カーペット](https://atcoder.jp/contests/kupc2013/tasks/kupc2013_d)　(ほぼそのものな問題です) -> a.py
- [ARC 081 F Flip and Rectangles](https://atcoder.jp/contests/arc081/tasks/arc081_d)　(ヒストグラム長方形面積最大化に帰着されます) -> b.py
- [ABC 064 D Insertion](https://atcoder.jp/contests/abc064/tasks/abc064_d)　(**括弧列**に関する例題です) -> c.py
- [ARC 076 E Connected?](https://atcoder.jp/contests/arc076/tasks/arc076_c)　(見た目違いますが結局、括弧列の問題になります) -> d.py

### コメント

ナイーブにやると O(n^2) かかる処理を stack を用いて O(n) で済ませるテクニックです。類似の話題として[最大正方形の面積 - 正方形探索](http://algorithms.blog55.fc2.com/blog-entry-131.html)もあります。他に stack を用いて実施できる典型的な問題として**括弧列**に関する問題があります。