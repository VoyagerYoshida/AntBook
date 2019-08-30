# 04 : 特殊な状態の列挙

### キーワード

- n! 通りの全探索
- next_permutation

### AtCoder 上の類題

- [ABC 054 C One-stroke Path](https://atcoder.jp/contests/abc054/tasks/abc054_c) -> a.py
- [JOI 2009 予選 D カード並べ](https://atcoder.jp/contests/joi2010yo/tasks/joi2010yo_d)　([AOJ 0546](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0546) に同じ) -> b.py
- [yukicoder No.133 カードゲーム](https://yukicoder.me/problems/199)　(yumechi さん提供)

### コメント
小さな n でしか適用できないので難しい問題になると逆に見かけないですが、n! 通りの全探索ができることも重要なステップになります。n が少し大きくなると **bit DP** が想定解法であるケースが多いです。
