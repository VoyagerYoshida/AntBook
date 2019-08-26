# 03 : A Simple Problem with Integers

### キーワード

- 区間加算
- 遅延評価つきセグメントツリー
- 区間加算対応 BIT

### AtCoder 上の類題

- [AOJ Course RSQ and RAQ](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G&lang=jp)　(まったく同じです) -> a.py
- [AOJ Course RMQ and RAQ](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H&lang=jp)　(「区間加算」と「最小値」、いわゆる有名な **Starry Sky Tree** です！) -> b.py
- [JOI 2016 春合宿 day3-2 雇用計画](https://atcoder.jp/contests/joisc2016/tasks/joisc2016_d)　(座標圧縮もします、問題は[ここ](https://www.ioi-jp.org/camp/2016/2016-sp-tasks/2016-sp-d2.pdf)) -> c.py
- [CODE FESTIVAL 2015 決勝 D 足ゲームII](https://atcoder.jp/contests/code-festival-2015-final-open/tasks/codefestival_2015_final_d)　(いもす法で解けますが、Starry Sky Tree があれば貼るだけです) -> d.py
- [square869120Contest #2 H Counting 1's](https://atcoder.jp/contests/s8pc-2/tasks/s8pc_2_h)　(Starry Sky 以外のを) -> e.py
- [JOI 2012 春合宿 day3-2 かくれんぼ](https://atcoder.jp/contests/joisc2010/tasks/joisc2010_hideseek)　(問題は[ここ](https://www.ioi-jp.org/camp/2010/2010-sp-tasks/2010-sp-day3_22.pdf)) -> f.py
- [ARC 076 F Exhausted?](https://atcoder.jp/contests/arc076/tasks/arc076_d)　(面白いです) -> g.py

### コメント

いわゆる遅延評価つきセグメントツリーです。遅延評価セグメントツリーについてはよい資料と問題集がたくさんあるので以下に貼ります:

- [僕のセグメントツリーの使い方](http://kyuridenamida.hatenablog.com/entry/2012/11/14/043421) (きゅうりさん)
- [遅延評価セグメント木をソラで書きたいあなたに](http://tsutaj.hatenablog.com/entry/2017/03/30/224339) (つたじろうさん)
- [データ構造と代数(後編)](https://tomcatowl.github.io/post/ds-and-alg-2/) (tomcatowlさん)
- [初心者の初心者による初心者のための典型segment tree](http://d.hatena.ne.jp/DEGwer/20131211/1386757368) (DEGwerさん)
- [競技プログラミングにおけるセグメントツリー問題まとめ セグメントツリー, BIT, 遅延評価セグメントツリー](http://hamayanhamayan.hatenablog.jp/entry/2017/07/08/173120) (はまやんさん)