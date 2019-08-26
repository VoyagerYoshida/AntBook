# 13 : グリッド DP

### キーワード

- DP
- グリッド DP

### AtCoder 上の類題

- [JOI 2006 予選 F 通学経路](https://atcoder.jp/contests/joi2007yo/tasks/joi2007yo_f)　([AOJ 0515](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0515) に同じ) -> a.py
- [JOI 2007 本選 D ぴょんぴょん川渡り](https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_d)　([AOJ 0530](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0530) に同じ) -> b.py
- [JOI 2008 本選 D 散歩](https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_d)　([AOJ 0541](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0541) に同じ) -> c.py
- [JOI 2009 予選 E 通勤経路](https://atcoder.jp/contests/joi2010yo/tasks/joi2010yo_e)　([AOJ 0547](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0547) に同じ) -> d.py

### コメント

DAG DP の一種ですが、特にグリッド上の DP です。JOI ではよく見るイメージです。
一般の DAG DP と異なり、メモ化再帰じゃなくても for 文でループを回す実装ができます。