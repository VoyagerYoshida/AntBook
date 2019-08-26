# 16 : 挿入 DP

### キーワード

- DP
- 挿入 DP

### AtCoder 上の類題

- [TDPC O 文字列](https://atcoder.jp/contests/tdpc/tasks/tdpc_string) -> a.py
- [天下一プログラマーコンテスト 2015 本戦 E 天下一コップ](https://atcoder.jp/contests/tenka1-2015-final-open/tasks/tenka1_2015_final_e) -> b.py
- [JOI 2018/2019 予選 F - 座席 (Seats)](https://atcoder.jp/contests/joi2019yo/tasks/joi2019_yo_f) -> c.py
- [JOI 2016 春合宿 day1-3 ソリティア](https://atcoder.jp/contests/joisc2016/tasks/joisc2016_c)　(かなり難しいです、問題は[ここ](https://www.ioi-jp.org/camp/2016/2016-sp-tasks/2016-sp-d1.pdf)) -> d.py

### コメント

発想はナップサックに近いのですが、今ある並びの中に新しいものを挿入していく DP です。高難易度でお馴染みです。「bit DP でやりたくなるけど制約上とても無理で、部分点として bit DP が設定されている」というのがよくあるパターンです。

DEGwer さんの[数え上げテクニック集](https://drive.google.com/file/d/1WC7Y2Ni-8elttUgorfbix9tO1fvYN3g3/view)の「3.2 順列は挿入 DP」に挿入 DP がどういうときに有効かの説明が書いてあります。

参考記事:
[競技プログラミングにおける挿入DP問題まとめ](http://hamayanhamayan.hatenablog.jp/entry/2017/10/04/112825) (はまやんさん)