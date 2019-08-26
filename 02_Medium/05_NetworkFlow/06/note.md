# 06 : Evacuation

### キーワード

- フロー
- 最大流
- 二部マッチング (「人」と「(時刻, ドア)」との間の最大マッチング)
- 割当問題

### AtCoder 上の類題

- [Maximum-Cup 2018 H Maxmin Tour](https://atcoder.jp/contests/maximum-cup-2018/tasks/maximum_cup_2018_h)　(二分探索して、「スタンプ間の移動」と「魔法の石」との間の最大マッチングです) -> a.py
- [ARC 013 D 切り分けできるかな？](https://atcoder.jp/contests/arc013/tasks/arc013_4)　(条件設定が少し複雑です) -> b.py
- [SRM 477 DIV1 Medium PythTriplets](https://qiita.com/drken/items/apps.topcoder.com/stat?c=problem_statement&pm=10766&rd=14157)　(SRM ですが程よい感じの二部マッチングです) -> c.py
- [SRM 594 DIV1 Medium FoxAndGo3](https://qiita.com/drken/items/SRM 594 DIV1 Medium FoxAndGo3)　(マッチングというよりは最大安定集合です、「燃やす埋める」から考えることもできます) -> d.py

### コメント

いわゆる 2 つのカテゴリ間でマッチングを作るタイプの問題 (**割当問題**とも呼びます) です。類題は結構あると思ったのですが、多くの場合は重みもついていて (例題 3-5-10 で挙げます)、重みのないものは意外と見つからなかったです。