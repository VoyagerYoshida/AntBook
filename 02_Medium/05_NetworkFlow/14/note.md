# 14 : 線形計画問題

### キーワード

- 線形計画問題
- 単体法

### AtCoder 上の類題

- [SRM 231 DIV1 Hard Mixture](https://community.topcoder.com/stat?c=problem_statement&pm=3942&rd=6520)　(単体法の verify その 1) -> a.py
- [UVa 10498 Happiness](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1439)　(単体法の verify その 2) -> b.py
- GCJ 2008 Round2 C Simplex -> c.py

### コメント

P.223〜224 のコラムに関連する話です。
ネットワークフロー問題はだいたい **IP** (整数計画問題) に定式化できます。
それを **LP 緩和** (整数制約のついた変数の整数制約を取り除くこと) します。そうすると最適値は変わってしまうことが多いですが、ネットワークフロー系の問題の多くは**完全単網性**を満たすので、LP 緩和しても最適値が元の問題と変わらないことが言えます。従って、元の問題を LP 緩和した問題に対して単体法なりで解くことにより、元の問題の最適解が求められることが言えます。

少しわかりづらいかもですが、この辺の話は以下がとても参考になります:

- [LPとグラフと定式化](http://tokoharu.github.io/tokoharupage/docs/formularization.pdf) (とこはるさん)
- [LPっぽいのと最小カット](http://d.hatena.ne.jp/komiyam/20121208/1354895372) (komiyam さん)
- [競技プログラミングにおける線形計画問題・整数計画問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/05/31/131424) (はまやんさん)

類題としては、フローかどうかにかかわらず**単体法**が使える問題を挙げました。