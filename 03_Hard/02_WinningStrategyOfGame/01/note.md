# 01 : コインのゲーム１

### キーワード

- DP
- ゲーム
- ゲーム DP

### AtCoder 上の類題

- [TDPC B ゲーム](https://atcoder.jp/contests/tdpc/tasks/tdpc_game)　(初級編でも挙げました) -> a.py
- [ABC 025 C 双子と○×ゲーム](https://atcoder.jp/contests/abc025/tasks/abc025_c)　(ゲーム DP) -> b.py
- [ARC 038 B マス目と駒](https://atcoder.jp/contests/arc038/tasks/arc038_b)　(ゲーム DP) -> c.py
- [ARC 085 D ABS](https://atcoder.jp/contests/arc085/tasks/arc085_b)　(実は O(1) で解けますが、条件反射でゲーム DP を書けるとすぐに解けます) -> d.py
- [AOJ 2376 DisconnectedGame](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2376&lang=jp)　(面白いです) -> e.py
- [ARC 038 D 有向グラフと数](https://atcoder.jp/contests/arc038/tasks/arc038_d)　(状態がループするので**後退解析**します) -> f.py
- [AOJ 1377 Black and White Boxes](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1377)　(去年の ICPC Asia で出題されて話題になった **Hackenbush** です) -> g.py
- [AGC 010 F Tree Game](https://atcoder.jp/contests/agc010/tasks/agc010_f)　(E 問題に比べれば多少考えやすい気がします) -> h.py

### コメント

ゲームに関する DP です。難しい問題でなければ**ゲーム木探索**を理解していれば簡単です。

参考資料

- [状態がループするゲームの解析（後退解析）](http://pekempey.hatenablog.com/entry/2018/02/01/182034) (pekempey さん)
- [ACM-ICPC 2016 Asia Tsukuba Regional, K 解法](http://natsugiri.hatenablog.com/entry/2016/10/23/234716) (natsugiri さん)