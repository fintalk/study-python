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

```python
# 命令型
# 言われた通りの命令を淡々とこなしているだけ
>>> 1 + 1
2
>>> 100 > 0
True
```

### 関数型プログラミング
+ 「引数を受け取り、値を返す」という手続きを守った書き方
    + 下記の `print()` 関数は、引数を出力した後、`None` を返している。
+ 返ってきた値を使って次の処理を行う
+ 命令とデータはきっちり分ける

```python
# 関数型
# 関数に引数を渡して、値を返すという一連の流れに沿った処理

>>> print("Hello")
Hello
>>> x = print("Hello")
Hello
>>> type(x)
<class 'NoneType'>

>>> x = len([1,2,3])
>>> x * 100
300
```

### オブジェクト指向
+ データがメソッドを持つ
+ データとメソッドを一体化している


```python
# オブジェクト指向
# データ型自身が、自分に対して行うことが出来る処理（メソッド）を最初から持っている
>>> name_list = ["taro", "jiro", "hanako"]
>>> name_list.append("tanaka")
>>> name_list
['taro', 'jiro', 'hanako', 'tanaka']

# オブジェクトにメソッドがブラブラぶら下がっている。ぶら下がっているメソッドを確認するには dir 関数を使う
>>> dir(name_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## オブジェクト指向と関数型プログラミング

+ 二つの最大の違いは、**データに対して破壊的かどうか**
+ オブジェクト指向の発想は破壊的な事が多い
+ 関数型プログラミングは、非破壊的。

```python
# オブジェクト指向
>>> name_list = ["taro", "jiro", "hanako"]
>>> name_list.sort()
>>> name_list
['hanako', 'jiro', 'taro'] # name_list は元の順番から破壊的に変更された
```

```python
# 関数型プログラミング
>>> name_list = ["taro", "jiro", "hanako"]
>>> sorted(name_list)
['hanako', 'jiro', 'taro']
>>> name_list
['taro', 'jiro', 'hanako']# name_list は元の順番を保っている
```

+ このように、オブジェクトが持つデータを変更することで起きる問題を副作用（side effect）と呼ぶ
+ 関数型プログラミングでは、こういうことは起きづらい。
+ オブジェクト指向では、この**副作用を上手に使って行くこと**を前提にコードを書く。
+ ただし、経験的にいうとバグも出やすいので注意すること。
+ 例
    ```python 
    >>> new_list = []
    >>> for name in name_list:
    ...     new_list.append(name.upper()) # 空のリストに要素を追加していく
                                        # （= 破壊的変更を行っていく）
    ... 
    >>> new_list 
    ['TARO', 'JIRO', 'HANAKO']
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
    # 関数定義
    >>> def add_100(x):
    ...     return x + 100
    ... 
    # 無名関数 labmda を使って関数式を作り、ｆに代入
    >>> f = lambda x: x + 100

    # 実行
    >>> add_100(1)
    101
    >>> f(1)
    101
    ```

+ 「大文字小文字関係なくソートしてほしい！」など並び替える方法をカスタマイズ（`materials/chapter04.md`）の「自作の関数でもOK」のところを lambda で書き換えて見る
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
    + `get_score()` **関数はたった一行なので関数をわざわざ作るのがメンドイ**。無名関数で済ませたい。こういう時に使う。

    ```python
    dict_scores = [ 
        {"name": "taro", "score":80}, 
        {"name": "jiro", "score":90}, 
        {"name": "goro", "score":50}, 
        ]

    # keyにlambda で作った無名関数を渡す
    >>> dict_scores.sort(key=lambda x: x["score"]) # return d["score"] と同じ
    >>> dict_scores
    [{'name': 'goro', 'score': 50}, {'name': 'taro', 'score': 80}, {'name': 'jiro', 'score': 90}]    
    ```

## 内包表記（comprehension) 
+ リスト内包表記
+ マジでよく使う
+ しんせいたろうも（好んで）よく使う
+ ただ、この表記方法を嫌う人もおおい(可読性が下がるという理由から)

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
+ 記法
    ```python 
    [変数を使った演算 for 変数 in シーケンス]
    ```
+ 可読性という意味では明らかに読みづらい。（だから嫌われる）
+ よってこれも、初心者の間は書けなくてもいいので、解読出来るようになって下さい :-)

#### 練習問題
+ 以下の for 文をリスト内包表記で書き換えてください。
    ```python 
    # 問題1
    a_list = list()
    for x in range(10):
        a_list.append(x + 100)
    return a_list

    # 問題2 
    b_list = list()
    for k,v in {"first_name": "Samaria", "last_name": "Haseldine", "email": "shaseldine0@un.org"}.items():
        b_list.append(v)
    return b_list
    ```

### リスト内包表記で利用する if 

+ リスト内包表記の中に if 条件文を書く
    ```python
    # 例：もし last_name が B で始まるならリストに追加したい場合
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
    >>> ids = range(3)
    >>> names = ["taro", "jiro", "hanako"]

    # for 文
    >>> d = dict()
    >>> for i, n in zip(ids, names): #zip関数はP200を参照
    >>>     d[i] = n 
    >>> d
    # {0: 'taro', 1: 'jiro', 2: 'hanako'}

    # ディクショナリ内包表記
    >>> {i:n for i, n in zip(ids, names)} 
    # {0: 'taro', 1: 'jiro', 2: 'hanako'}
    ```

### set内包表記

+ setでもできます。
    ```python 
    >>> names = ["taro", "jiro", "hanako", "taro", "jiro", "hanako", "taro", "jiro", "hanako"]
    >>> {n.upper() for n in names}
    # {'HANAKO', 'JIRO', 'TARO'}
    ```

## イテレータを使う

ループ処理は、シーケンスの要素の処理がすべて終わったらループが終わるという流れでした。このため内部的に、処理を始める前にシーケンスの中身を先に読み込むという作業が発生します。もしデータが100億個とかあった場合、先に読みこむという作業だけで結構な時間がかかります。

こういう時に**イテレータ**という発想が便利です。

イテレータは、「データを一つ取って処理し、処理が終わったら次があるかどうか問い合わせをする。あれば処理して、なければ終了」という流れを取ります。これを**遅延評価**といいます。つまり処理すべきデータがこのあと何個あるかなんて最初から知る必要はない、という発想です。

実は、Python の for 文は内部的には イテレータが使われています。そのほうが処理が早いからです。しかし、私達はそれを気にせず for 文を使っています。細かいことは覚えなくてもよいです。ただ、イテレータという仕組みがあることと、遅延評価という言葉だけ覚えておいてください。

### どれだけ違うの？
python 2 系の range() 関数はイテレータ仕様ではありませんでした。
よって、２系では、range()の中身をいったん読み込むのに時間がかかります。

実験 (study-python/materials/chapter05_iter.py)：以下のテストでは、range()関数が返すシーケンスは[0, 1, .... 10**8] という一千万個要素を持つシーケンスです。i が０の時、つまり最初の要素で break しています。

```python 
from time import time
def test():
    for i in range(0, 10**8):
        if i == 0:
            break
start_time = time()
test()
end_time = time()

print(start_time - endtime) # python2の時はプリント文にしてね
```

## ジェネレータを使う

+ 自分でイテレータを実装したい場合、
    1. 関数定義の中に yield 文を書く
+ ジェネレータ関数を呼び出す場合
    1. 関数を呼び出し、変数に入れる
    2. 変数を next() 関数に入れて実行する
+ 例：
    ```python 
    # yield 文を使って値をイールドする
    >>> def func():
    ...     yield 1
    ...     yield 2
    ...     yield 3
    ... 
    # 関数を呼び出して変数に代入する
    >>> f = func()

    # next関数にこの変数を引数として渡す
    >>> next(f)
    1
    >>> next(f)
    2
    >>> next(f)
    3

    # これ以上イールドするものがなくなったら StopIteration エラーを出す
    >>> next(f)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
    >>> 
    ```
+ P246の「素数を返すジェネレータ関数の定義」を解説
    ```python
    # 素数を作るジェネレータ
    # 素数＝1とその数自身と以外には割り切れない正の整数
    # 例：１から50までの素数リスト
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

    def get_prime(x=2):
        # 1は絶対割り切れるので２以降xまでのrangeで
        while True:
            for i in range(2,x):
                # もし割り切れる数字があればBreak
                if x % i == 0:
                    break
            else:
                yield x # ここで一旦この関数を抜けてる。

            # 次に next で呼ばれる時は、ココから始まる。
            print(f"restart {x}")
            x = x + 1 # x に次のデータを入れる

    i = get_prime()
    for c in range(10):
        print(next(i))
        
    ```
    + ポイント：
        + `i = get_prime()` の段階では何もしていない
        + next(i) で呼び出されて初めて、関数の `yield x ` まで実行する
        + 次に呼ばれるまで、そこで待ってる
        + `while True:` は無限ループを作る為に記述。もしこれがなかったら、下記のようなコードになり、`x = x + 1` した後、普通に終了してしまう。
        ```python 
        def get_prime(x=2):
            # 1は絶対割り切れるので２以降xまでのrangeで
            for i in range(2,x):
                # もし割り切れる数字があればBreak
                if x % i == 0:
                    break
            else:
                yield x # ここで一旦この関数を抜けてる。
            # 次に next で呼ばれる時は、ココから始まる。
            # print(f"restart {x}")
            x = x + 1 # x に次のデータを入れる
        ```




## 高階関数

+ 高階関数とは、関数の引数に関数を渡す関数です。
+ 例：
    ```python 
    >>> def execute(func, args):
    ...         return func(args)
    ... 
    >>> execute(max, [1,2,3])
    3
    >>> execute(list, "ABC")
    ['A', 'B', 'C']
    ```
+ python で、高階関数を書けるようになる必要はありません。
+ 「高階関数」とは何か、ということと、map(), reduce(), filter(), 関数だけ覚えてください。

### map(関数, シーケンス)
+ https://docs.python.org/ja/3.9/library/functions.html#map
+ シーケンスの各要素に関数を適用してイテレータを返す
    ```python 
    >>> def add_1(x):
    ...     return x + 1

    # イテレータオブジェクトを返す
    >>> map(add_1, range(3))
    <map object at 0x7f1c57e74310>

    # 中を確認したい場合は、list() 関数に入れるか、
    >>> list(map(add_1, range(3)))
    [1, 2, 3]

    # イテレータを nextで呼び出す
    >>> i = map(add_1, range(3))
    >>> next(i)
    1
    >>> next(i)
    2
    >>> next(i)
    3
    >>> next(i)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
    ```

### filter(関数, シーケンス)
+ https://docs.python.org/ja/3.9/library/functions.html#filter
+ シーケンスの各要素に関数を実行して、関数がTrueの要素だけのシーケンスを返します

    ```python 
    >>> def start_with_a(name):
    ...     return name.startswith("A")
    ... 

    >>> filter(start_with_a, ["Will", "James", "Avery", "Anne"])
    <filter object at 0x7f1c57efddf0>

    >>> list(filter(start_with_a, ["Will", "James", "Avery", "Anne"]))
    ['Avery', 'Anne']

    >>> s = filter(start_with_a, ["Will", "James", "Avery", "Anne"])
    >>> next(s)
    'Avery'
    >>> next(s)
    'Anne'
    >>> next(s)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration

    ```

### reduce(関数,  シーケンス)
+ reduce は、`functools` ライブラリのメソッドです。
+ シーケンスの左の要素から順に関数を適用させ、次の要素へ反映させる。
+ たとえば、左から順に掛け算していくのはこのように書けます
    ```python
    >>> from functools import reduce
    >>> def multiple(x,y):
    ...     return x * y 
    ... 
    >>> reduce(multiple, [1,2,3,4,5])
    120
    ```

## デコレータ
たとえば、`chap_04_23.md` の問題でこういうのがありました。

---

1. 引数 `obj` を一つとって，`obj` が True なら「YES」 False なら 「No」をプリントする関数 `check()` を作って下さい。ただし引数 `obj` は組み込み型オブジェクトを想定しています。
1. check関数に以下のデータを渡して，各々実行して下さい
    ```python
    s1 = "ABC"
    l1 = []
    d1 = {}
    s2 = ""
    l2 = list("ABC")
    d2 = {"name": "Zane Piet", "born": 2009, "tel": "796-824-5240"}
    ```
---

これを check 関数に渡して実行した場合、
```python 
check(s1)
check(l1)
check(d1)
check(s2)
check(l2)
check(d2)
```
出力結果として
```
YES
NO
NO
NO
YES
YES
```
こういう出力になりましたよね。これってわかりにくいですよね。渡した引数とかも一緒にプリントしてくれたらいいな、と思います。

でもそうするためには
```python 
print(s1)
check(s1)
:
:
```
みたいに、なんかめんどくさい書き方をしなくてはいけません。

そこでデコレータが登場します。デコレータは、`関数を引き取って、関数を返す関数`です。

たとえば、今の問題を解決するには、

```python 
def print_args(func): # 関数を引数に取得
    def _print(*args): # 内部に高階関数を作成
        print("引数", args) # ここで引数のプリントを行い、
        return func(args) # 引き取った関数に引数を渡して実行したものを返すという関数を作成
    return _print # 内部の高階関数を返す
```

これを、適用したい関数定義の上に `@` 付きで定義します。

```python
@print_args
def check(obj):
    if obj:
        print("YES")
    else:
        print("NO")
```
これでもう一度実行してみると
```
引数 ('ABC',)
YES
引数 ([],)
YES
引数 ({},)
YES
引数 ('',)
YES
引数 (['A', 'B', 'C'],)
YES
引数 ({'name': 'Zane Piet', 'born': 2009, 'tel': '796-824-5240'},)
YES
```
というように、引数がプリントされた形で出力されます。

高階関数とデコレータは理解するのがとても難しいと思います。
Pythonにとても慣れている人はしばしば使いますが、今の段階では読み書きできなくても大丈夫です。





