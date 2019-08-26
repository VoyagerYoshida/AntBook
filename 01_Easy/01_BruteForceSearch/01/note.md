# 01 : 部分和問題

### キーワード

- 再帰関数を用いた全探索
- $ 2^{N} $ 通りを調べる全探索 (bit 全探索)

### AtCoder 上の類題

- [ABC 045 C - たくさんの数式](https://atcoder.jp/contests/arc061/tasks/arc061_a)　(同じく $ 2^{N} $ 通りを調べる全探索です) -> a.py
- [ABC 079 C - Train Ticket](https://atcoder.jp/contests/abc079/tasks/abc079_c) -> b.py
- [ABC 104 C - All Green](https://atcoder.jp/contests/abc104/tasks/abc104_c) -> c.py
- [ARC 029 A - 高橋君とお肉](https://atcoder.jp/contests/arc029/tasks/arc029_1) -> d.py
- [ABC 002 D - 派閥](https://atcoder.jp/contests/abc002/tasks/abc002_4)　(全探索部分の考え方は共通です) -> e.py

### コメント

通称 **bit 全探索**と呼ばれているタイプの全探索です。蟻本のように再帰関数の形で書くこともできますし、ビットで集合を管理する手法で全探索することもできます。

- [再帰関数を学ぶと、どんな世界が広がるか](https://qiita.com/drken/items/23a4f604fa3f505dd5ad)
- [ビット演算 (bit 演算) の使い方を総特集！ 〜 マスクビットから bit DP まで 〜](https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361)

