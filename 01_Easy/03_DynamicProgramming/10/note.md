# 10 : 区間 DP

### キーワード

- DP
- 区間 DP

### AtCoder 上の類題

- [TDPC I イゥイ](https://atcoder.jp/contests/tdpc/tasks/tdpc_iwi) -> a.py
- [AOJ 2415 刺身](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2415)　(Monge です) -> b.py
- [ATC 002 C 最適二分探索木](https://atcoder.jp/contests/atc002/tasks/atc002_c)　(刺身と一緒ですが Monge してもなお足りず、Hu-Tucker が必要です) -> c.py

### コメント

区間に対する DP です。Monge 性は蟻本にない話題なのでどこかで学ぶ必要があります。通常の区間 DP は *O*($ n^{3} $) かかり、Monge 性を満たすと *O*($ n^{2} $) にすることができます。

最適二分探索木問題に限ってはさらに *O*(*n* log*n*) で解ける Hu-Tucker のアルゴリズムが知られています。

参考記事:
[競技プログラミングにおける区間DP問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/02/27/152226) (はまやんさん)