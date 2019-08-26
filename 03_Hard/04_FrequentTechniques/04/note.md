# 04 : K-Anonymous Sequence

### キーワード

- DP
- Convex Hull Trick を用いた DP 高速化

### AtCoder 上の類題

- [COLOCON -Colopl programming contest 2018 Final C スペースエクスプローラー高橋君](https://atcoder.jp/contests/colopl2018-final/tasks/colopl2018_final_c)　(DP 高速化ではないですが CHT のシンプルな例題です) -> a.py
- [yukicoder No.409 ダイエット](https://yukicoder.me/problems/no/409) -> b.py
- [Japan Alumni Group Summer Camp 2015 Day 4 I Live Programming](https://atcoder.jp/contests/jag2015summer-day4/tasks/icpc2015summer_day4_i)　(実はダイエットとほぼ同じです) -> c.py
- [JOI 2017 春合宿 day3-1 長距離バス](https://atcoder.jp/contests/joisc2017/tasks/joisc2017_g)　(問題は[ここ](https://www.ioi-jp.org/camp/2017/2017-sp-tasks/2017-sp-d3-coach-review.pdf)) -> d.py
- [ARC 066 F Contest with Drinks Hard](https://atcoder.jp/contests/arc066/tasks/arc066_d)　(分割統治法も絡みます) -> e.py

### コメント

DP 高速化技法としてよく見られる手法の 1 つ、Convex Hull Trick です。
DP 高速化関連記事:

- [DP高速化](http://ferin-tech.hatenablog.com/entry/2018/02/23/071343) (フェリンさん)
- [Convex-Hull Trick](http://satanic0258.hatenablog.com/entry/2016/08/16/181331) (satanic さん)
- [難しい典型テクとか](https://www.slideshare.net/ikumihide/ss-50881829) (とざんさん)
- [数え上げテクニック集](https://drive.google.com/file/d/1WC7Y2Ni-8elttUgorfbix9tO1fvYN3g3/view)の「11. 高速化のテクニック」 (DEGwer さん)
- [動的計画法高速化テクニック（オフライン・オンライン変換）](https://qiita.com/tmaehara/items/0687af2cfb807cde7860) (前原さん)
- [競技プログラミングにおける動的計画法更新最適化まとめ（CHT, MongeDP, AlianDP, インラインDP, きたまさ法）](http://hamayanhamayan.hatenablog.jp/entry/2017/03/20/234711) (はまやんさん)