# 06 : 最長増加部分列問題

### キーワード

- DP
- LIS
- インライン DP (実家 DP)

### AtCoder 上の類題

- [ABC 006 D トランプ挿入ソート](https://atcoder.jp/contests/abc006/tasks/abc006_4) -> a.py
- [ABC 038 D プレゼント](https://atcoder.jp/contests/abc038/tasks/abc038_d)　(区間スケジューリング問題のところでも挙げました) -> b.py
- [TDPC K ターゲット](https://atcoder.jp/contests/tdpc/tasks/tdpc_target) -> c.py
- [JOI 2016 春合宿 day1-1 マトリョーシカ人形](https://atcoder.jp/contests/joisc2016/tasks/joisc2016_a)　(難しいです。LIS ではないですが LIS の理解があると解きやすいです。問題文は[ここ](https://www.ioi-jp.org/camp/2016/2016-sp-tasks/2016-sp-d1.pdf)) -> d.py

### コメント

sky さんの提唱する[インライン DP](http://topcoder.g.hatena.ne.jp/skyaozora/20171212/1513084670) (通称、実家DP) の最も簡単な例で、なおかつ超頻出の **LIS** です。LIS に帰着できる問題は数多いのでライブラリとして持っておくだけでも強いですが、LIS の仕組みにより精通しているとより応用の効く問題もあります。

参考記事:
[競技プログラミングにおける最長部分増加列問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/04/26/151849) (はまやんさん)