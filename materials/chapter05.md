# Pythonと関数型プログラミング

教科書の補助教材です。

---

### はじめに

インタープリタの出力例をコピペして書いている場合は、最初に ` >>> ` マークがついています。手元で試したい場合は、 `>>>` マークは無視してコードを書いて下さい
```python
>>> 5 * 3
15
```

また、ただの例を書いている場合もあります。これはプレビューした時に見やすいのでこういう表記になっています。例：
```python
# 全部文字列 とは
"shinseitaro"
```

---

## 関数型プログラミングとはなにか？

+ (教科書にはいろいろ書いてありますが、よくわかんないと思います。)
+ (なので、ここはご批判覚悟で、ざっくりまとめてみました。だいたいあってると思うし細かいことは気にしないことにします。)

### 命令型プログラミング
+ 与えられたデータに命令を下していくだけ
+ 書いてあるとおりに上から順に命令を下していくだけ
+ 命令とデータはきっちり分ける
### 関数型プログラミング
+ 「引数を受け取り、値を返す」という手続きを守った書き方
+ 返ってきた値を使って次の処理を行う
    + 返ってきた値を捨てる、というのも「捨てる」という「次の処理」を行っているので同じ事
+ 命令とデータはきっちり分ける
### オブジェクト指向
+ データがメソッドを持つ
+ データとメソッドを一体化している

### 例

```python
# 命令型
>>> 1 + 1
2
>>> 100 > 0
True
```
+ 言われた通りの命令を淡々とこなしているだけ

```python
# 関数型
>>> len([1,2,3])
3
>>> print("Hello")
Hello
>>> x = print("Hello")
Hello
>>> type(x)
<class 'NoneType'>
```
+ 関数に引数を渡して、値を返すという一連の流れに沿った処理
+ `print()` 関数は、引数を出力した後、`None` を返している。

```python
# オブジェクト指向
>>> name_list = ["taro", "jiro", "hanako"]
>>> name_list.append("tanaka")
>>> name_list
['taro', 'jiro', 'hanako', 'tanaka']
```
+ データ型自身が、自分にたいして行うことが出来る処理（メソッド）を最初から持っている
+ データにメソッドがブラブラぶら下がっている

## オブジェクト指向と関数型プログラミング

+ 二つの最大の違いは、**データに対して破壊的かどうか**
+ オブジェクト指向の発想は破壊的な事が多い
+ 関数型プログラミングは、非破壊的。

```python
# オブジェクト指向
>>> name_list = ["taro", "jiro", "hanako"]
>>> name_list.sort()
>>> name_list
['hanako', 'jiro', 'taro']
```

```python
# 関数型
>>> name_list = ["taro", "jiro", "hanako"]
>>> sorted(name_list)
['hanako', 'jiro', 'taro']
>>> name_list
['taro', 'jiro', 'hanako']
```

## 副作用（side effect）

+ 副作用！ (しんせいたろうが最も嫌う問題)
+ **データの状態が変わってしまうこと**
+ つまりは、破壊的にデータを変えてしまうこと
+ オブジェクト指向だと副作用が起きてしまう
+ しかし、この**副作用を上手に使って行くこともオブジェクト指向的アイデア**

```python
# オブジェクト指向
>>> name_list = ["taro", "jiro", "hanako"]
>>> name_list.sort()
>>> name_list
['hanako', 'jiro', 'taro'] # 副作用！
```

```python
# 関数型
>>> name_list = ["taro", "jiro", "hanako"]
>>> sorted(name_list)
['hanako', 'jiro', 'taro']
>>> name_list
['taro', 'jiro', 'hanako'] # 元のデータは変化していない＝副作用が起きていない
```

## Python の文と式
+ 説明しているのでパス

## lambda 式
+ 無名関数
+ 名前のない関数
+ あんがいよく使う
+ 初心者の間は作らなくてもいいですが、解読出来るようになって下さい :-)

### 作り方

```python
lambda 引数: 引数を使った式
```

### 関数と lambda 式
+ 以下は同じものを return します
    ```python 
    >>> def add_100(x):
    ...     return x + 100
    ... 
    >>> lambda x: x + 100
    ```


+ 例：「大文字小文字関係なくソートしてほしい！」など並び替える方法をカスタマイズ（materials/chapter04.md）の「自作の関数でもOK」のところ
    ```python
    # 辞書の１要素で並べ直す。例えば、辞書の "score" というキーワードの値順に並べ替えたい場合
    def get_score(d):
        return d["score"]
    
    dict_scores = [ 
        {"name": "taro", "score":80}, 
        {"name": "jiro", "score":90}, 
        {"name": "goro", "score":50}, 
        ]

    # keyに関数名を渡す
    >>> dict_scores.sort(key=get_score)
    >>> dict_scores
    [{'name': 'goro', 'score': 50}, {'name': 'taro', 'score': 80}, {'name': 'jiro', 'score': 90}]
    ```
    + `get_score()` 関数はたった一行なので関数をわざわざ作るのがメンドイ。無名関数で済ませたい。

    ```python
    dict_scores = [ 
        {"name": "taro", "score":80}, 
        {"name": "jiro", "score":90}, 
        {"name": "goro", "score":50}, 
        ]

    # keyにlambda で作った無名関数を渡す
    >>> dict_scores.sort(key=lambda x: x["score"])
    >>> dict_scores
    [{'name': 'goro', 'score': 50}, {'name': 'taro', 'score': 80}, {'name': 'jiro', 'score': 90}]    
    ```

## 内包表記（comprehension) 
+ リスト内包表記
+ マジでよく使う
+ しんせいたろうも（好んで）よく使う
+ ただ、この表記方法を嫌う人もおおい

### 使いかた

+ 以下の二つは同じものをReturnします

```python
names = [
        {"first_name": "Iona","last_name": "Batting"}, 
        {"first_name": "Abner", "last_name": "Baynom"}, 
        {"first_name": "Cale","last_name": "Brighouse"}, 
        {"first_name": "Janice", "last_name": "Golby"},
    ]

# ① いつもの方法
a_list = [] # 空のリストを用意する
>>> for name in names:
...     a_list.append(name["first_name"])
>>> a_list
['Iona', 'Abner', 'Cale', 'Janice']

# ② リスト内包表記
>>> b_list = [name["first_name"] for name in names]
>>> b_list
['Iona', 'Abner', 'Cale', 'Janice']
```
+ リスト内包表記では、 ループ変数を使ってをするかを、 for の前に書いて値を取得し、その結果をそのままリストで返す、という処理を行います。
+ 上の例でもわかりますが、同じ結果を得るにいつもの方法だと3行、リスト内包表記だと１行で終ります。
+ しかし、可読性という意味では明らかに読みづらいです。（だから嫌われる）
+ よってこれも、初心者の間は作らなくてもいいですが、解読出来るようになって下さい :-)

### リスト内包表記で利用する if 

+ リスト内包表記の中に if を書くことができます
+ 例：もし last_name が B で始まるならリストに追加したい場合

```python
names = [
        {"first_name": "Iona","last_name": "Batting"}, 
        {"first_name": "Abner", "last_name": "Baynom"}, 
        {"first_name": "Cale","last_name": "Brighouse"}, 
        {"first_name": "Janice", "last_name": "Golby"},
    ]

# for 文の場合：
>>> l = list()
>>> for name in names:
...     if name["last_name"].startswith("B"):
...             l.append(name)
... 
>>> l
[{'first_name': 'Iona', 'last_name': 'Batting'}, {'first_name': 'Abner', 'last_name': 'Baynom'}, {'first_name': 'Cale', 'last_name': 'Brighouse'}]

# リスト内包表記の場合

>>> [name for name in names if name["last_name"].startswith("B")]
[{'first_name': 'Iona', 'last_name': 'Batting'}, {'first_name': 'Abner', 'last_name': 'Baynom'}, {'first_name': 'Cale', 'last_name': 'Brighouse'}]
```
+ if 文を後ろにつけるスタイル
+ 慣れればわかるけど、なれるまで結構？？？となると思います

### ディクショナリ内包表記

+ 辞書でもできます。

```python 
ids = range(3)
names = ["taro", "jiro", "hanako"]

# for 文
d = dict()
for i, n in zip(ids, names): #zip関数はP200を参照
    d[i] = n 
print(d)
# {0: 'taro', 1: 'jiro', 2: 'hanako'}

# ディクショナリ内包表記
print( {i:n for i, n in zip(ids, names)} )
# {0: 'taro', 1: 'jiro', 2: 'hanako'}
   
```

### set内包表記

+ setでもできます。
```python 
names = ["taro", "jiro", "hanako", "taro", "jiro", "hanako", "taro", "jiro", "hanako"]
print({n.upper() for n in names})
# {'HANAKO', 'JIRO', 'TARO'}
```

## イテレータを使う

for 文を使ってシーケンスを処理する時、シーケンスの要素がすべて終わったら処理を終わるという流れでした。これは、「処理を始める前にシーケンスの中身が何で何個入っているか」を先に知っておく必要があります。

つまり、for 文でループする前にシーケンスを一度評価（読み込み）しています。

しかし、もしデータが100億個とかあった場合、先に読みこむという作業だけで結構な時間がかかります。

こういう時にイテレータという発想が便利です。

イテレータは、「データを一つ取って処理し、処理が終わったら次があるかどうか問い合わせをする。あれば処理して、なければ終了」という流れを取ります。これを**遅延評価**といいます。

つまり処理すべきデータがこのあと何個あるかなんて最初から知る必要はない、という発想です。ま、そうですね。

ここまで説明しといてなんですが、Python の for 文は内部的には イテレータが使われています。そのほうが処理が早いからです。しかし、私達はそれを気にせず for 文を使っています。

細かいことは覚えなくてもよいです。ただ、イテレータという仕組みがあることと、遅延評価という言葉だけ覚えておいてください。















