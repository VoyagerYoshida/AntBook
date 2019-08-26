# 07 : Matrix Power Series

### キーワード

- 行列累乗
- 行列級数和

### AtCoder 上の類題

- [SRM 446 DIV1 Medium AntOnGraph](https://community.topcoder.com/stat?c=problem_statement&pm=10516&rd=13900)　(SRM の問題ですが面白いので載せます、単に行列累乗を繰り返すのでもできますが、行列級数和で一発で決めることもできます) -> a.py

### コメント

A^n を求めるのが行列累乗なら、E + A + A^2 + ... + A^(n-1) を求めるのが行列級数和です。等比級数の和の公式のようなものを使いたくなるのですが、E - A が逆行列をもつとは限らないのでダメです。AtCoder 上の問題を**募集中**です。