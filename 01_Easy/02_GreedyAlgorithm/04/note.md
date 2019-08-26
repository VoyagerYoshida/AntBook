# 04 : Saruman's Army

### キーワード

- Greedy
- より厳しいところをとっていく Greedy (より一般に「**交換しても悪化しない**」)

### AtCoder 上の類題

- [ABC 083 C Multiple Gift](https://atcoder.jp/contests/abc083/tasks/arc088_a)　(例題はなるべく遠い方を選ぶ Greedy でしたが、これは近い方を選ぶ Greedy です) -> a.py
- [ARC 006 C 積み重ね](https://atcoder.jp/contests/arc006/tasks/arc006_3)　(典型問題です) -> b.py
- [ABC 005 C おいしいたこ焼きの売り方](https://atcoder.jp/contests/abc005/tasks/abc005_3)　(少し難しくなった Greedy です、Greedy に解けるマッチングの例です) -> c.py
- [SRM 560 DIV1 Easy TomekPhone](https://community.topcoder.com/stat?c=problem_statement&pm=12296)　(一次元量同士を比較する最大二部マッチング、Greedy に解けるマッチング例です)
- [ABC 091 C 2D Plane 2N Points](https://atcoder.jp/contests/abc091/tasks/arc092_a)　(二次元量同士を比較する最大二部マッチング、Greedy に解けるマッチング例です) -> d.py

### コメント
Greedy アルゴリズムを考えるときに、より厳しいところをとっていく考え方は頻出のイメージです。その最も典型的な例として、一次元的 (二次元量もOK) な数量の大小関係だけでマッチング条件が決まるような問題における最大二部マッチング問題があります。