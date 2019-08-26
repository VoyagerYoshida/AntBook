# 04 : K-th Number

### キーワード

- 平方分割

### AtCoder 上の類題

- [ARC 033 C データ構造](https://atcoder.jp/contests/arc033/tasks/arc033_3)　(例題 3-3-2 のところでも挙げましたが平方分割でも解けます) -> a.py
- [ARC 042 D あまり](https://atcoder.jp/contests/arc042/tasks/arc042_d)　(離散対数を求める **Baby-Step Giant-Step** を用いますが、これも平方分割の一種と言えます) -> b.py
- [KUPC 2014 K 乱数調整](https://atcoder.jp/contests/utpc2014/tasks/utpc2014_k)　(同じく BSGS です) -> c.py
- [JOI 春合宿 2016 day3-2 回転寿司](https://atcoder.jp/contests/joisc2016/tasks/joisc2016_h)　(難しいです、問題は[ここ](https://www.ioi-jp.org/camp/2016/2016-sp-tasks/2016-sp-d3.pdf)) -> d.py
- [第3回 ドワンゴからの挑戦状 本選 B ニワンゴくんの約数](https://atcoder.jp/contests/dwacon2017-honsen/tasks/dwango2017final_b)　(最近話題の **Mo のアルゴリズム**で解けますが、Mo のアルゴリズムも平方分割の一種と言えます) -> e.py

### コメント

平方分割は極めて汎用性の高いテクニックですね。平方分割以外が想定解法でも平方分割で解ける問題は非常に多いです。例題 3-3-1〜3 の類題で挙げた問題たちも、平方分割でも解けるものは多いです。

参考記事:

- [セグメント木をあきらめた人のための平方分割](http://kujira16.hateblo.jp/entry/2016/12/15/000000) (しょラーさん)
- [競技プログラミングにおける平方分割問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/04/12/180257) (はまやんさん)
- [競技プログラミングにおけるMo's Algorithm問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/04/18/012937) (はまやんさん)