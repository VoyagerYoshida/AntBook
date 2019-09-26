# 03 : 個数制限なしナップサック問題

### キーワード

- DP
- ナップサック DP
- 個数制限なしナップサック DP

### AtCoder 上の類題

- [AOJ Course ナップザック問題](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=jp)　(例題そのものです)
- [AOJ 2502 VOCAL ANDROID](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2502)

### コメント

各品物を何個でも選んでよいバージョンのナップサックです。愚直にやると計算量が *O*($ nW^{2} $) かかってしまうところをうまくやって *O*(*nW*) に落とすテクニックです。**配列再利用**と呼ばれる DP 時のメモリ消費を抑えるテクニックとも相性がいいです。忘れた頃に見かけるイメージです。