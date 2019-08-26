# 02 : Lake Counting

### キーワード

- DFS
- (弱) 連結成分分解
- グリッドグラフ上の探索

### AtCoder 上の類題

- [ATC 001 A 深さ優先探索](https://atcoder.jp/contests/atc001/tasks/dfs_a)　(かなり似ています) -> a.py
- [ARC 031 B 埋め立て](https://atcoder.jp/contests/arc031/tasks/arc031_2)　(比較的似ています) -> b.py
- [ARC 037 B バウムテスト](https://atcoder.jp/contests/arc037/tasks/arc037_b)　(見た目は違いますが実装するアルゴリズムは似ています) -> c.py
- [AOJ 1160 島はいくつある？](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp)　(ほぼまったくそのままな問題です)

### コメント

初めて Lake Counting を見たときはとても難しそうに思えましたが、今となってはパターン化した DFS の実装で簡単に記述できます。このタイプの DFS をスラスラと書けるようになることが、競技プログラミングの重要なステップになると思います。

また、ARC 037 B バウムテストは Lake Counting とは見た目は違いますがやることはすごく似ています。こういうのを同じ問題だと思えるようになることもまた、重要なステップかと思います。

- [DFS (深さ優先探索) 超入門！ 〜 グラフ・アルゴリズムの世界への入口 〜【前編】](https://qiita.com/drken/items/4a7869c5e304883f539b)
- [DFS (深さ優先探索) 超入門！ 〜 グラフ・アルゴリズムの世界への入口 〜【後編】](https://qiita.com/drken/items/a803d4fc4a727e02f7ba)