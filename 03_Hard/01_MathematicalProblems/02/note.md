# 02 : mod 演算あれこれ, Fermat の小定理, 中国剰余定理

### キーワード

- nCr
- mod_inverse
- Fermat の小定理、Euler の定理
- 中国剰余定理、連立線形合同方程式

### AtCoder 上の類題

- [ABC 024 D 動的計画法](https://atcoder.jp/contests/abc024/tasks/abc024_d)　(nCr に関する式変形をします) -> a.py
- [AGC 001 E BBQ Hard](https://atcoder.jp/contests/agc001/tasks/agc001_e)　(難しめの二項係数計算をします) -> b.py
- [yukicoder 0186 中華風 (Easy)](http://yukicoder.me/problems/447)　(**中国剰余定理**ライブラリの verify に) -> c.py
- [AOJ 2659 箸](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2659)　(中国剰余定理を繰り返します) -> d.py
- [SRM 449 DIV1 Hard StairsColoring](https://qiita.com/drken/items/apps.topcoder.com/stat?c=problem_statement&pm=10551&rd=13903)　(**カタラン数**のよい例ではありますが、最後が少し面倒です) -> e.py
- [Japan Alumni Group Summer Camp 2013 Day 3 D Fast Division](https://atcoder.jp/contests/jag2013summer-day3/tasks/icpc2013summer_day3_d)　(Fermat の小定理です) -> f.py
- [Japan Alumni Group Summer Camp 2015 Day 4 D Identity Function](https://atcoder.jp/contests/jag2015summer-day4/tasks/icpc2015summer_day4_d)　(Fermat の小定理も、Euler の定理も使います、Euler の定理の部分は離散対数を用いてもよいです) -> g.py
- [2017 Tenka1 F ModularPowerEquation!!](https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_f)　(Euler の定理を用いた考察をします、問題の再帰的な構造を見出します) -> h.py

### コメント

nCr に関わる問題や、中国剰余定理・連立線形合同方程式を用いる問題などです。この辺りの話題についてもよい記事が豊富にあるので紹介します:

- [数え上げテクニック集](https://drive.google.com/file/d/1WC7Y2Ni-8elttUgorfbix9tO1fvYN3g3/view)の「14. 二項係数のテクニック」 (DEGwer さん)
- [nCr mod mの求め方](https://www37.atwiki.jp/uwicoder/pages/2118.html) (uwi さん)
- [整数テクニック集](https://github.com/kirika-comp/articles/blob/pre-releases/pre-seisuuron.pdf) (kirika さん)
- [競技プログラミングにおける数学的問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/10/14/125941) (はまやんさん)
- [競技プログラミングにおける中国剰余定理問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/10/14/125941) (はまやんさん)