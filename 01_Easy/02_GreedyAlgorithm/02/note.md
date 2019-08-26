# 02 : 区間スケジューリング問題

### キーワード

- Greedy
- 区間の終端でソート (DEGwer さんの[数え上げテクニック集](https://drive.google.com/file/d/1WC7Y2Ni-8elttUgorfbix9tO1fvYN3g3/view) にも記載あり)

### AtCoder 上の類題

- [KUPC 2015 A 東京都](https://atcoder.jp/contests/kupc2015/tasks/kupc2015_a)　(見た目文字列な問題ですが、区間スケジューリングです) -> a.py
- [ABC 103 D - Islands War](https://atcoder.jp/contests/abc103/tasks/abc103_d)　(実は区間スケジューリングです) -> b.py
- [Codeforces 296 DIV1 B Clique Problem](http://codeforces.com/contest/528/problem/B)　(少し難しめ、区間スケジューリング問題に帰着できます)
- [ABC 038 D プレゼント](https://atcoder.jp/contests/abc038/tasks/abc038_d)　(難しめです、区間ソートして LIS に帰着) -> c.py

### コメント
**区間の終端 (または始端) でソートする**のは極めてよくみるテクニックで、今後難しい問題に挑むときにも常に念頭に置いておきたいです。