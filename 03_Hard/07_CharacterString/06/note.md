# 06 : 最長回文

### キーワード

- Suffix Array
- LCP
- 回文

### AtCoder 上の類題

- [ARC 060 F 最良表現](https://atcoder.jp/contests/arc060/tasks/arc060_d)　(様々な解法があります) -> a.py
- [Japan Alumni Group Summer Camp 2013 Day 3 H Almost Same Substring](https://atcoder.jp/contests/jag2013summer-day3/tasks/icpc2013summer_day3_h)　(様々な解法があります) -> b.py
- [Japan Alumni Group Summer Camp 2015 Day 2 F ほぼ周期文字列](https://atcoder.jp/contests/jag2015summer-day2/tasks/icpc2015summer_day2_f)　(ロリハでも、SA+LCP でもできます) -> c.py
- [ARC 050 D Suffix Concat](https://atcoder.jp/contests/arc050/tasks/arc050_d)　(SA+LCP) -> d.py

### コメント

LCP にさらに RMQ を用いると文字列の場所 i, j の接尾辞の先頭何文字が共通しているかを求めることができます。最長回文はそのような LCP 処理を用いる典型的な例です。