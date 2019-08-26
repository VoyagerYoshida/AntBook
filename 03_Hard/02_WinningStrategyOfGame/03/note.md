# 03 : Euclid's Game

### キーワード

- ゲーム
- 自由度の観点から選べる手が実質的に高々 2 通りしかない

### AtCoder 上の類題

- [ARC 085 D ABS](https://atcoder.jp/contests/arc085/tasks/arc085_b)　(ゲーム DP でも挙げた問題ですが、O(1) で解けます、問題の構造は Euclid's Game によく似ています) -> a.py
- [AGC 010 D Decrementing](https://atcoder.jp/contests/agc010/tasks/agc010_d)　(難しめですが、結局選べる手が高々 2 通りしかないゲームです) -> b.py

### コメント

一見探索領域が広くてメモ化もできなくて難しそうですが、実質的に選べる手が高々 2 通りしかないタイプのゲームです。