# 10 : Evacuation Plan

### キーワード

- フロー
- 最小費用流
- **重みつき**二部マッチング
- 割り当て問題

### AtCoder 上の類題

- [Maximum-Cup 2013 F 3人の騎士と1匹の犬](https://atcoder.jp/contests/maximum-cup-2013/tasks/maximum_2013_f)　(2 カテゴリ間の重みつきマッチングを考える点ではよく似ています) -> a.py
- [Code festival 2014 上海 H Dungeon](http://kmjp.hatenablog.jp/entry/2015/01/04/0930)　(これも似た感じです) -> b.py
- [ABC 004 D マーブル](https://atcoder.jp/contests/abc004/tasks/abc004_4)　(想定解法ではないですが最小費用流でも解けます) -> c.py
- [AOJ 2581 完全順列](http://judge.u-aizu.ac.jp/onlinejudge/cdescription.jsp?cid=RitsCamp14Day3&pid=G)　(面白いです) -> d.py
- [AOJ 2293 Dangerous Tower](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2293)　(**任意流量**の最小費用流になります) -> e.py

### コメント

例題 3-5-6 と同じく 2 つのカテゴリ間でマッチングを作るタイプの問題 (**割当問題**とも呼びます) ですが、今度は重みのあるバージョンです。