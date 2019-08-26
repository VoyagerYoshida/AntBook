# 04 : Fliptile 

### キーワード

- 反転 (ライツアウト)
- XOR 操作
- 操作の順序を入れ替えても結果は変わらない
- なにかを決めると Greedy

### AtCoder 上の類題

- [JOI 2007 予選 E おせんべい](https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e)　(比較的近い感じです、[AOJ 0525](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0525) に同じ) -> a.py
- [ABC 018 D バレンタインデー](https://atcoder.jp/contests/abc018/tasks/abc018_4)　(見た目は違いますが、なにかを決めると残りが Greedy に決まる感じは似ています) -> b.py
- [yukicoder No.226 0-1パズル](https://yukicoder.me/problems/no/226)　(例題にかなり近いと思います) -> c.py
- [AOJ 1308 Awkward Lights](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1308)　(ライツアウトです、**連立一次方程式**を解きます) -> d.py

### コメント

ライツアウト第二弾です！
今度は端から考えようとしてもいきなり一意には決まりません。
しかし最初の一列を全部決めると、それより下は全部 Greedy に決まっていきます。
このように「なにかを決めると残りは Greedy に決まる」というのも頻出の印象です。

また、Greedy 系の解法ではいかんともしがたいライツアウト系に対しては、
**連立一次方程式**を解く解法も検討するとよさそうです。