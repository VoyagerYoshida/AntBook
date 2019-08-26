# 04 : 平均最大化

### キーワード

- 二分探索
- 平均値の最大化
- 「a[0], ..., a[n-1] の**平均**が K 以上」を「a[0]-K, ..., a[n-1]-K の**総和**が 0 以上」にするテク

### AtCoder 上の類題

- [ABC 034 D 食塩水](https://atcoder.jp/contests/abc034/tasks/abc034_d)　(そのもの) -> a.py
- [ARC 026 D 道を直すお仕事](https://atcoder.jp/contests/arc026/tasks/arc026_4)　(少し難しめです) -> b.py
- [ARC 060 C 高橋君とカード](https://atcoder.jp/contests/arc060/tasks/arc060_a)　(二分探索ではないですが**平均を総和にするテク**を使うとオーダーが落ちます) -> c.py
- [ARC 075 E Meaningful Mean](https://atcoder.jp/contests/arc075/tasks/arc075_c)　(やはり平均を総和にするテク、下に出て来る**転倒数**も絡みます) -> d.py

### コメント

「a[0], ..., a[n-1] の平均が K 以上」を
「a[0]-K, ..., a[n-1]-K の総和が 0 以上」にするテクは
二分探索に限らずちょくちょく見る印象です。