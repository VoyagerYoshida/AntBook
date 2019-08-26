# 08 : Minimizing Maximizer

### キーワード

- セグメントツリーによる DP 高速化
- セグメントツリー上の DP
- インライン DP (実家 DP)

### AtCoder 上の類題

- [第4回 ドワンゴからの挑戦状 本戦 B だんだん強く](https://beta.atcoder.jp/contests/dwacon2018-final-open/tasks/dwacon2018_final_b) -> a.py
- [JOI 2019 予選 E - イルミネーション (Illumination)](https://atcoder.jp/contests/joi2019yo/tasks/joi2019_yo_e) -> b.py
- [ARC 073 F Many Moves](https://atcoder.jp/contests/arc073/tasks/arc073_d)　(sky さんの記事で解説されています) -> c.py
- [ARC 085 F NRE](https://atcoder.jp/contests/arc085/tasks/arc085_d)　(区間を扱う系はインライン DP であることが多いようです) -. d.py
- [JOI 2015 春合宿 day1-3 たのしいたのしい家庭菜園](https://atcoder.jp/contests/joisc2015/tasks/joisc2015_c)　(問題は[ここ](https://www.ioi-jp.org/camp/2015/2015-sp-tasks/2015-sp-d1.pdf)) -> e.py

### コメント

最近 AtCoder 上でも流行っている[インライン DP](http://topcoder.g.hatena.ne.jp/skyaozora/20171212/1513084670) (sky さん) です。