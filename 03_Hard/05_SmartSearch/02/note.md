# 02 : Sequence Destroyer

### キーワード

- 探索
- 枝刈り探索
- 解が悪くなったら打ち切る
- 分枝限定法やα-β法的な枝刈り探索

### AtCoder 上の類題

- [KUPC 2016 F 早解き](https://atcoder.jp/contests/kupc2016/tasks/kupc2016_f)　(α-β 的なことをします) -> a.py
- [Japan Alumni Group Summer Camp 2013 Day 4 E Optimal alpha beta pruning ](https://atcoder.jp/contests/jag2013summer-day4/tasks/icpc2013summer_day4_e)　(α-β します) -> b.py
- [ABC 032 D ナップサック問題](https://atcoder.jp/contests/abc032/tasks/abc032_d)　(DP や半分全列挙で解きますが[分枝限定法でまとめて解く](https://qiita.com/hamko/items/cceb1a92da14e2755527)こともできます) -> c.py
- [AOJ 1131 Unit Fraction Partition](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1131&lang=jp)　(枝刈りをすると通る系です) -> d.py
- [JAG Practice Contest for ACM-ICPC Asia Regional 2013 J Magical Switches](https://atcoder.jp/contests/jag2013autumn/tasks/icpc2013autumn_j)　(枝刈り探索しますが計算時間の指数の底を評価できたりして面白いです) -> e.py

### コメント

分枝限定法やα-β法に代表されるような、「解が悪くなったら打ち切る」系の枝刈り探索をする問題です。計算量オーダーが不明になることが多く出題側も苦心しそうなタイプの問題です。ここではもっと広く枝刈り探索に関する問題を載せました。
参考記事:

- [競技プログラミングにおける枝刈り問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/12/23/155922) (はまやんさん)