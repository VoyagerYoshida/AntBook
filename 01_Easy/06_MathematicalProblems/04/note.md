# 04 : 素数の個数

### キーワード

- 素数
- Eratosthenes の篩

### AtCoder 上の類題

- [天下一プログラマーコンテスト2012 予選C A 与えられた数より小さい素数の個数について](https://atcoder.jp/contests/tenka1-2012-qualc/tasks/tenka1_2012_9) -> a.py
- [ABC 084 D 2017-like Number](https://atcoder.jp/contests/abc084/tasks/abc084_d)　(累積和テクも使います) -> b.py
- [AOJ 0009 素数](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009&lang=jp)　(素数関連のライブラリの verify にはこの問題が一番よいかもです) -> c.py
- [AOJ 2286 Farey Sequence](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2286)　(一見違う問題ですが、エラトスネテスの篩っぽい方法で解けます) -> d.py

### コメント

そすーそすー
Eratosthenes の篩です。
Eratosthenes の篩的な前処理をしたあとに「素因数分解」を高速に実行する osa_k 法も。