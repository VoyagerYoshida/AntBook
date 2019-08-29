# AtCoder 版蟻本
## 説明
これはプログラミングコンテストチャレンジブックの勉強用個人レポジトリです.

## コンテンツ
### 初級編 ( 01_Easy )
[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)
1. すべての基本 "全探索" ( 01_BruteForceSearch )
1. 猪突猛進! "貪欲法" ( 02_GreedyAlgorithm )
1. 値を覚えて再利用 "動的計画法" ( 03_DynamicProgramming )
1. データを工夫して記憶する "データ構造" ( 04_DataStructure )
1. あれもこれも実は "グラフ" ( 05_Graph )
1. 数学的な問題を解くコツ ( 06_MathematicalProblems )

### 中級編 ( 02_Medium )
[AtCoder 版！蟻本 (中級編)](https://qiita.com/drken/items/2f56925972c1d34e05d8)
1. 値の検索だけじゃない! "二分探索" ( 01_BinarySearch )
1. 厳選!頻出テクニック(1) ( 02_FrequentTechniques )
1. さまざまなデータ構造を操ろう ( 03_DataStructure )
1. 動的計画法を極める! ( 04_DynamicProgramming )
1. 水を流して解く "ネットワークフロー" ( 05_NetworkFlow )
1. 平面・空間を扱う "計算幾何" ( 06_ComputationalGeometry )

### 上級編 ( 03_Hard )
[AtCoder 版！蟻本 (上級編)](https://qiita.com/drken/items/9b311d553aa434bb26e4)
1. より複雑な数学的問題 ( 01_MathematicalProblems )
1. ゲームの必勝法を編み出せ! ( 02_WinningStrategyOfGame )
1. グラフマスターへの道 ( 03_Graph )
1. 厳選! 頻出テクニック(2) ( 04_FrequentTechniques )
1. 工夫を凝らして賢く探索 ( 05_SmartSearch )
1. 分けて解いてまとめる! "分割統治法"　( 06_DivideAndConquerMethod ) 
1. 文字列を華麗に扱う ( 07_CharacterString )

## コードテンプレート
```python
import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
# from fractions import gcd
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
from bisect import bisect_left

INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
S_MAP = lambda: map(str, INPUT().split())
LIST = lambda: list(map(int, INPUT().split()))
S_LIST = lambda: list(map(str, INPUT().split()))

sys.setrecursionlimit(10**9)
INF = float('inf')
mod = 10**9 + 7


def main():
    a = 0


if __name__ == '__main__':
    main()
　　
```

### ライブラリ
#### *sys*, *re*, *os*
- *sys* : インタプリタで使用・管理している変数や, インタプリタの動作に深く関連する関数を定義しています.
- *re* : Perl に見られる正規表現マッチング操作と同様のものを提供します.
- *os* : OS 依存の機能を利用するポータブルな方法を提供します.
#### *collections*
- **deque**(\[iterable\[, maxlen\]\]) : iterable で与えられるデータから, 新しい deque オブジェクトを (append() をつかって) 左から右に初期化して返します. iterable が指定されない場合, 新しい deque オブジェクトは空になります.
- **defaultdict**(\[default_factory\[, ...\]\]) : 新しいディクショナリ様のオブジェクトを返します.  defaultdict は組み込みの dict のサブクラスです.メソッドをオーバーライドし, 書き込み可能なインスタンス変数を 1 つ追加している以外は dict クラスと同じです. 同じ部分については以下では省略されています. 
- **Counter**(\[iterable-or-mapping\]) : Counter はハッシュ可能なオブジェクトをカウントする dict のサブクラスです. これは, 要素を辞書のキーとして保存し, そのカウントを辞書の値として保存するコレクションです. カウントは、0 や負のカウントを含む整数値をとれます. Counter クラスは, 他の言語のバッグや多重集合のようなものです. 
#### *math*
- **ceil**(x) : x の「天井」(x 以上の最小の整数)を返します.
- **sqrt**(x) : x の平方根を返します.  
- **hypot**(x, y) : ユークリッドノルム (sqrt(x*x + y*y)) を返します. これは原点から点 (x, y) のベクトルの長さです.
- **factorial**(x) : x の階乗を整数で返します.
- **pi** : 利用可能なだけの精度の数学定数 π = 3.141592... (円周率).
- **sin**(x), **cos**(x) : x ラジアンの正弦, 余弦を返します.
- **radians**(x) : 角 x を度からラジアンに変換します.
- (注 : from fractions import ) **gcd**(a, b) : 整数 a と b の最大公約数を返します. a と b のいずれかがゼロでない場合, gcd(a, b) の値は a と b の両方を割り切ることのできる, 最も大きな正の整数です. gcd(0, 0) は 0 を返します.
#### *itertools*
- **permutations**(iterable, r=None): iterable の要素からなる長さ r の順列 (permutation) を連続的に返します。
- **combinations**(iterable, r) : 入力 iterable の要素からなる長さ r の部分列を返します. 
- **product**(\*iterables, repeat=1) : 入力イテラブルのデカルト積です. 
- **accumulate**(iterable\[, func\]) : 累計や加算ではない (func オプション引数で指定される) 2変数関数による累積結果を返すイテレータを作成します。 func が与えられた場合、2つの引数を取る関数でなければなりません。 入力 iterable の要素は、 func が引数として取れる型を持ちます。 
#### *operator*
- **itemgetter**(item or \*item) : 演算対象からその __getitem__() メソッドを使って item を取得する呼び出し可能なオブジェクトを返します. 二つ以上のアイテムを要求された場合には, アイテムのタプルを返します.  
- **mul**(a, b) : 数値 a および b について a * b を返します。
#### *copy*
- **deepcopy**(x\[,memo\]) : x の深い(deep)コピーを返します.
#### *string*
- **ascii_lowercase** : 小文字 'abcdefghijklmnopqrstuvwxyz'. この値はロケールに依存せず, 固定です.
- **ascii_uppercase** : 大文字 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. この値はロケールに依存せず, 固定です.
- **digits** : 文字列 '0123456789' です.
#### *functools*
- **reduce**(function, iterable\[, initializer\]) : 2 引数の function を iterable の要素に対して左から右に累積的に適用し, イテラブルを単一の値に縮約します. 
#### *bisect*
- **bisect_left**(a, x, lo=0, hi=len(a)) : ソートされた順序を保ったまま x を a に挿入できる点を探し当てます. リストの中から検索する部分集合を指定するには, パラメータの lo と hi を使います. 
