# 組み込み型を使いこなす

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

## メソッドとは

+ Pythonで最も大切な概念の一つ
+ **データじたいが、自分自身は何をすることが出来るか（メソッド）を持つ**
+ データの型ごとに、そのデータを使って何が出来るかを予めプログラムしてある
+ 例：
    ```python
    >>> colors = ['black', 'yellow', 'yellow', 'blue', 'white', 'white', 'blue', 'red', 'black', 'blue']

    # このリストに black がいくつ入っているか
    >>> colors.count("black")
    2

    # このリストをソートする（破壊的に）
    >>> colors.sort()
    >>> colors
    ['black', 'black', 'blue', 'blue', 'blue', 'red', 'white', 'white', 'yellow', 'yellow']

    # このリストをリバースする（破壊的に）
    >>> colors.reverse()
    >>> colors
    ['yellow', 'yellow', 'white', 'white', 'red', 'blue', 'blue', 'blue', 'black', 'black']
    ```
    + 「メソッドを呼び出す」＝そのデータ型が持っているメソッドを使うこと
    + メソッドの呼び出し方：
        ```python 
        データ.メソッド(引数)
        ```
    + 「データに紐付いて（P154）」＝ データ.メソッド の "." の部分を言っていると思ってOK
    + 人によっては「データにメソッドがぶら下がってる」というような表現をするヒトもいる。（こっちのほうがイメージは近いと思う）
    + どのようなメソッドがもともと備わっているか確認するには `dir()` 関数を使います
    ```python 
    >>> dir(colors)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    ```
+ 【**すごく大切**】関数とメソッドの違い
    + 関数は、`関数(引数としてデータ)` という形
    + メソッドは `データ.メソッド(引数)` という形
    ```python 
    # 関数：関数名(引数としてデータ)
    >>> len(colors)
    10

    # メソッド：データ.メソッド(引数)
    >>> colors.append("Taro")
    >>> colors
    ['yellow', 'yellow', 'white', 'white', 'red', 'blue', 'blue', 'blue', 'black', 'black', 'Taro']

    ```
    
## オブジェクトとしての組み込み型

+ 命令型プログラミング
    + データと命令をはっきりと分ける
    + メソッドのように、データが自分自身は何をすることが出来るか（メソッド）を持つという発想はない
    + データにメソッドがぶら下がったりしない
    + 関数はこっち
+ オブジェクト指向
    + データと命令を一つにしておこうという発想
    + データじたいが、自分自身は何をすることが出来るか（メソッド）を持つ
    + データにメソッドがブラブラぶら下がる
    + 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**
+ Pythonは、命令型もオブジェクト指向もどっちもやる。
    + だから混乱もします。なので、ココでしっかりと何が命令型なのか、何がオブジェクト指向なのかしっかり理解してください。
    + といっても、まずは形だけ覚えればOK
    ```python 
    # 命令型プログラミング = 関数：関数名(引数としてデータ)
    >>> len(colors)
    10

    # オブジェクト指向 = メソッド：データ.メソッド(引数)
    >>> colors.append("Taro")
    >>> colors
    ['yellow', 'yellow', 'white', 'white', 'red', 'blue', 'blue', 'blue', 'black', 'black', 'Taro']

    # データにメソッドがブラブラぶら下がっている様子
    >>> dir(colors)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    # 同じデータ型であれば同じメソッドを持っている。ココが一番のメリット
    >>> int_list = [1,2,3,4,5]
    >>> dir(int_list)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    ```
    + メモ： `__add__` のようなアンダーバー2個で囲まれたメソッドは特殊メソッドとよばれます。P285の特殊メソッドで説明します。
    + 各メソッドが何が出来るのかは、Pythonの公式ドキュメントで探す必要があります。(とても探しにくいけど)
    + Google で、「list append site:https://docs.python.org/ja/3 」みたいに、`site: 検索` をする探しやすいです。


## 組み込みデータ型一覧

+ 代表的なデータ型をいくつかみていきます。
+ データの型を調べるには `type()` 関数を使う。
+ データ型が持つメソッドを調べるには `dir()` 関数を使う。

### 数値型

+ 1, 2, 3 ... といった数値。整数だけ扱う int型や、小数点を扱える float型など

```python
>>> x = 100
>>> x
100

# 型を調べる
>>> type(x) 
<class 'int'> # 整数型

# メソッドを調べる
>>> dir(x) 
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


>>> y = 100.12
# 型を調べる
>>> type(y)
<class 'float'> # float 型

# メソッドを調べる
>>> dir(y) 
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
```
+ メモ：同じ数値型でも、整数型とfloat型でぶら下がってるメソッドが違う

### 文字列型
+ 文字列を扱うためのデータ

```python
>>> s = "shinseitaro"

>>> type(s)
<class 'str'> # 文字列型

>>> dir(s) # ぶら下がってるメソッド
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
### リスト型
+ 複数の要素を並べて管理するデータ。
+ 前から順番があるデータ。（ゼロ始まり）
+ 各要素の型を揃える必要はない。

```python
>>> a_list = ["A", "B", 1, 2]

>>> type(a_list)
<class 'list'>

>>> dir(a_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

### タプル型
+ リスト型と似ているが、一度作ると要素を変更することができない。
+ よって、タプルが持つメソッドはリストと違って要素を変更出来るようなメソッドは無い
```python
>>> a_tuple = ("A", "B", 1, 2)

>>> type(a_tuple)
<class 'tuple'>

>>> dir(a_tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
```
### ディクショナリ型
+ キーと値をペアにして複数の要素を管理するデータ型
+ リストとは違って、順番という概念は無い
+ なので、順番があってこそのメソッド（reverse とか sort とか index など）は無い
```python 
>>> tel = {'jack': "03-1234-5678", 'sam': "06-9876-5432"}

>>> type(tel)
<class 'dict'>

>>> dir(tel)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```
### set 型
+ 重複しないデータの集合
+ 順番という概念がない
+ なので、順番があってこそのメソッド（reverse とか sort とか index など）は無い
```python 
>>> s = {1,1,2,2,3,3,4,4} # 重複データを渡しても
>>> s # 重複は削除されたデータになる
{1, 2, 3, 4}

>>> type(s)
<class 'set'>

>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

```
### bytes 型
+ よっぽどのことが無い限り使わないのでパス

### bool 型
+ TrueかFalse
+ この２つだけ
```python 
>>> b = True

>>> type(b)
<class 'bool'>

>>> dir(b)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

## まとめ
+ 命令型：データと命令（関数）をはっきり分けるプログラミング方法
+ オブジェクト指向：データにメソッドをブラブラぶら下げるプログラミング手法
+ データの型を調べるには `type()`  関数
+ データのメソッドを調べるには `dir()` 関数

### おまけ
+ 変数を作る時に変数名で悩むと思いますが、ここで type() 関数で出てきた名前から派生させると誰にでもパッとみてわかる変数名になります。
+ こういうのを「可読性を上げる」といいます
```python 
# 型_要素の特徴 （逆でもよい）
dict_tel = {'jack': "03-1234-5678", 'sam': "06-9876-5432"}
list_name = ["shinsei taro", "kono taro", "okamoto taro"]
```
+ （注意：ネーミングは所属しているチームやプロジェクトで厳格に決められている場合がありますのでそれに従いましょう。時々異常にこだわる人がいますので、ハイハイといって従っておきましょう）

## データ型の分類
+ ↑でしっかり説明したのでパス

## 数値型を操作する
+ ここまでやる必要はほぼ無いのでパス

## 文字列を使いこなす
+ 上記で説明した文字列型はこうでした
+ 教科書に説明されている `split()` と `join()` もちゃんとメソッドとしてぶら下がっています。
```python
>>> s = "shinseitaro"
>>> type(s)
<class 'str'> # 文字列型
>>> dir(s) # ぶら下がってるメソッド
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
+ split()：文字列をリストにする
    + `区切りたい文字列.split("区切りとして使われている文字列")`:
    ```python 
    # , で区切る
    >>> "Olivia, Emma, Ava, Sophia, Isabella".split(",")
    ['Olivia', ' Emma', ' Ava', ' Sophia', ' Isabella']

    # 空白文字列で区切る
    >>> "Olivia Emma Ava Sophia Isabella".split(" ")
    ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    ```
+ join()：リストを文字列にする
    + `区切りとして使われている文字列.join(リスト)`
    ```python 
    ",".join(['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella'])
    'Olivia,Emma,Ava,Sophia,Isabella'
    ```
### エスケープシーケンス
+ ダブルクオーテーション３つ `"""` で文字列を囲むと、改行されている文字列を扱うことが出来る。
+ 改行文字 '\n' で繋がれてる
+ windows の場合は `\` は ¥マークかもしれない
```python 
>>> """しんせい
... たろう
... おかもと
... たろう"""

'しんせい\nたろう\nおかもと\nたろう'

# これを活かしてこういう使い方もできる
>>> """しんせい
... たろう
... おかもと
... たろう""".split("\n")
['しんせい', 'たろう', 'おかもと', 'たろう']

```
+ P173のエスケープシーケンスで、絶対覚えてほしいのは
    + `\n` : 改行
    + `\t` : タブ 
    + `\\` : バックスラッシュそれじたい

### 文字列のフォーマット
+ 文字列の差し込み処理
+ テンプレートを用意しておいて違う文字列を差し込む時によく使う
    ```python 
    >>> list_name = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> for name in list_name:
    ...     "{} loves python".format(name)
    ... 
    'Olivia loves python'
    'Emma loves python'
    'Ava loves python'
    'Sophia loves python'
    'Isabella loves python'
    ```
+ `{}を含む文字列.format(埋めたい文字列)`
+ 昨今この書き方ではなく、P181に紹介されている f文字列（f-string) を使う人が多いです
    ```python 
    >>> list_name = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> for name in list_name:
    ...     f"{name} loves python"
    ... 
    'Olivia loves python'
    'Emma loves python'
    'Ava loves python'
    'Sophia loves python'
    'Isabella loves python'
    ```
+ その他のフォーマットも .format() メソッドと同じように書くことができます
    ```python
    >>> i = 10000000
    >>> f"{i:,}"
    '10,000,000'
    ```
+ 右寄せや小数点以下の桁数など様々なフォーマットがありますが、その都度調べればよいので覚える必要はありません。

## リスト型、タプル型を使いこなす

### リストをソートする
+ ソートとは、語順をアルファベット順もしくは数値順に並べ替えたもの
+ では数値とアルファベットが両方並んでいる時はどうなるか？
+ 比べられないよ、というTypeErrorが返ります。
    ```python
    >>> l = ["S","n",1, 0, -1]
    >>> l.sort()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: '<' not supported between instances of 'int' and 'str'
    ```
+ 大文字小文字はどうするか？→大文字が先です
    ```python 
    >>> l = ['s', 'k', 'e', 'A', 'S', 'd', 'k', 'e']
    >>> l.sort()
    >>> l
    ['A', 'S', 'd', 'e', 'e', 'k', 'k', 's']    
    ```
+ 大文字小文字関係なくソートしてほしい！→ `key` オプションを渡します。（あとで説明）
    ```python 
    >>> l.sort(key=str.lower)
    >>> l
    ['A', 'd', 'e', 'e', 'k', 'k', 'S', 's']    
    ```
### リストを大きい順にソートする
+ `reverse=True` を渡す
+ 記法
    ```python 
    リスト.sort(reverse=True)
    ```
+ 例：
    ```python 
    >>> x = ['A', 'B', 'D', 'C', 'D']
    >>> x.sort(reverse=True)
    >>> x
    ['D', 'D', 'C', 'B', 'A']
    ```
+ このようにデフォルト値を上書きして挙動を変更することを、「オプションを与える/渡す」といいます。
+ Chapter02で消費税の計算をした時 `rate` を0.05に変更しましたね。あの変更もオプションを与えるといいます。

### ソート順をカスタマイズする
+ 「大文字小文字関係なくソートしてほしい！」など並び替える方法をカスタマイズすることができます。
+ 記法
    ```python 
    リスト.sort(key=カスタマイズする方法を書いた関数)
    ```
+ key オプションで渡す関数は、関数名を渡せばOK
+ 例：上記にでてきた大文字小文字関係なくソートの場合.
    ```python 
    # str.lower というのは引数を小文字で返す関数
    >>> str.lower("A")
    'a'
    >>> str.lower("a")
    'a'

    # これを sort の key オプションに渡すと、
    # sort する時に、各要素を小文字として扱い並べ直す。
    # ただ、並べ直した結果は元の文字（大文字なら大文字、小文字なら小文字）のままで返す
    >>> l.sort(key=str.lower)
    >>> l
    ['A', 'd', 'e', 'e', 'k', 'k', 'S', 's']    
    ```
+ 例2：自作の関数でもOK
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

    # reverse も出来る
    >>> dict_scores.sort(key=get_score, reverse=True)
    >>> dict_scores
    [{'name': 'jiro', 'score': 90}, {'name': 'taro', 'score': 80}, {'name': 'goro', 'score': 50}]
    ```
    
### アンパック代入

+ `=` で代入する時に、一対一だけじゃなく、多対多も可
+ ただし、左辺と右辺が同じ個数であること
+ 例：
    ```python 
    >>> x, y, z = 1, 2, 3 
    >>> x
    1
    >>> y
    2
    >>> z
    3
    ```
+ 個数を間違うとValueError
    ```python 
    >>> x, y, z = 1, 2
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: not enough values to unpack (expected 3, got 2)
    ```

--- 

### スライスのステップ数

+ シーケンスのスライス
    ```python
    >>> a = [1,2,3,4,5]
    >>> a
    [1, 2, 3, 4, 5]
    >>> a[2:]
    [3, 4, 5]
    >>> a[:-2]
    [1, 2, 3]
    >>> a[-2:]
    [4, 5]
    >>> a[2:4]
    [3, 4]
    >>> a[-1]
    5
    >>> a[1]
    2
    >>> a[::2]
    [1, 3, 5]
    >>> a[:]
    [1, 2, 3, 4, 5]
    ```
+ 図(?)にしてみるとこんな感じ
    slice|1|2|3|4|5
    ---|---|---|---|---|---
    a[1]||●|||
    a[-1]|||||●
    a[2:]|||●|●|●
    a[:-2]|●|●|●||
    a[-2:]||||●|●
    a[2:4]|||●|●|
    a[::2]|●||●||●
    a[:]|●|●|●|●|●

### スライスを使った要素の代入と削除
+ スライスで代入出来る
    ```python
    >>> a = [1,2,3,4,5]
    >>> a[2:4] = ["three","four"]
    >>> a
    [1, 2, 'three', 'four', 5]
    ```
    ```python
    # スライスで区切った要素数と、代入する要素数が異なっていでも代入可
    >>> a = [1,2,3,4,5]
    >>> a[2:4] = ["three"] 
    >>> a
    [1, 2, 'three', 5]
    ```
+ del文で削除可
    ```python
    >>> a = [1,2,3,4,5]
    >>> del a[2:]
    >>> a
    [1, 2]    
    ```    

### リストで利用出来るメソッド
+ リストのメソッドは今までもいろいろ使って来ましたがもう一度おさらいしましょう
+ `L`はリストオブジェクトを意味しています。
+ `L.reverse()`
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> names.reverse()
    >>> names
    ['Isabella', 'Sophia', 'Ava', 'Emma', 'Olivia']
    ```
+ `L.remove(削除する要素)`
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> names.remove("Emma")
    >>> names
    ['Olivia', 'Ava', 'Sophia', 'Isabella']
    ```    
+ `L.append(最後尾に追加する要素)`
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> names.append("Charlotte")
    >>> names
    ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella', 'Charlotte']
    ```
+ `L.extend(最後尾に追加するリスト)`
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> names.extend(["Amelia", "Mia"])
    >>> names
    ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella', 'Amelia', 'Mia']
    ```
+ `L.pop([削除するインデックス])`
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> names.pop() # 引数無しの場合は最後のインデックス（つまり-1）の要素
    'Isabella'
    >>> names
    ['Olivia', 'Emma', 'Ava', 'Sophia']    
    ```
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> names.pop(1)
    'Emma' # 指定したインデックスの要素
    >>> names
    ['Olivia', 'Ava', 'Sophia', 'Isabella']
    ```
    + pop はこれまでのメソッドとは違い、削除される要素を値として返します。
    + よって、削除されたインデックスの要素を一旦変数に入れておくということも出来ます。
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> popped = names.pop(1)
    >>> popped
    'Emma'
    >>> names
    ['Olivia', 'Ava', 'Sophia', 'Isabella']
    ```    
+ `L.index(検索したい要素 [, 開始インデックス, 終了インデックス])`
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> names.index("Emma")
    1

    # 開始インデックスを指定すると、そのインデックス以降のリストから検索する
    # つまりこの場合 names[2:] から "Emma" のインデックスを探そうとするので、ValueError が返る
    >>> names.index("Emma", 2)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: 'Emma' is not in list
    ```

## set 型を使いこなす

+ おさらい：
    + set型：重複なしのデータの集まり
    + 集合演算をする時に便利
    + 順番という発想はない

### set のメソッド

+  `S` はセットオブジェクトを意味しています
+ 以下2つのセットで説明します
    ```python
    >>> s1
    {'A', 'B', 'C', 'D', 'E'}
    >>> s2
    {'C', 'D', 'E', 'X', 'Y'} 
    ```
+ `S.union(もう一つのセット)`: 和集合
    ```python 
    >>> s1.union(s2)
    {'E', 'X', 'A', 'B', 'Y', 'D', 'C'}
    >>> s1 | s2
    {'E', 'X', 'A', 'B', 'Y', 'D', 'C'}
    ```

+ `S.intersction()`：交わり
    ```python 
    >>> s1.intersection(s2)
    {'D', 'E', 'C'}

    >>> s1 & s2
    {'D', 'E', 'C'} 
    ```
+ `S.difference()`：差集合
    ```python 
    >>> s1.difference(s2)
    {'B', 'A'}
    >>> s1 - s2
    {'B', 'A'}
    ```
+ `S.symmetric_difference()`：対象差
    ```python 
    >>> s1.symmetric_difference(s2)
    {'X', 'A', 'Y', 'B'}
    >>> s1 ^ s2
    {'X', 'A', 'Y', 'B'}
    ```
+ `S.add()`: 要素を破壊的に追加
    ```python 
    >>> s1.add("Q")
    >>> s1
    {'E', 'A', 'B', 'Q', 'D', 'C'}
    ```
+ `S.remove()`：要素を破壊的に変更
    ```python 
    >>> s2.remove("Y")
    >>> s2
    {'E', 'X', 'D', 'C'}
    ```

## ディクショナリ型を使いこなす
+ 辞書の作るいろいろな方法
    ```python
    # 空の辞書を作る
    >>> d1 = dict()
    >>> d2 = {}
    >>> d1
    {}
    >>> d2
    {}

    # 要素を入れながら辞書を作る
    ## 辞書そのものを dict() 関数に入れて作る方法（元の辞書のコピー）
    >>> d3 = dict({1: 'taro', 2: 'jiro', 3: 'hanako'})
    >>> d3
    {1: 'taro', 2: 'jiro', 3: 'hanako'}

    ## 2つの要素を持つシーケンスのリストから作る方法
    >>> d4 = dict([
        [1, "taro"], 
        [2, "jiro"], 
        [3, "hanako"]
        ])
    >>> d4
    {1: 'taro', 2: 'jiro', 3: 'hanako'}

    ## key と value の組み合わせから作る
    ## しかしこの場合、キーが数値の辞書は作成不可
    >>> d5 = dict(1="taro", 2="jiro",3="hanako")
    File "<stdin>", line 1
    SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

    ## キーとして使うのは文字列のみ。かつ、文字列型として渡すのではなくキーワード引数として渡す。
    >>> d5 = dict(one="taro", two="jiro",three="hanako")
    >>> d5
    {'one': 'taro', 'two': 'jiro', 'three': 'hanako'}

    ## 文字列型としてキーを渡すとSyntaxError
    >>> d5 = dict("one"="taro", "two"="jiro","three"="hanako")
    File "<stdin>", line 1
    SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

    ## zip を使う（P200）
    >>> d6 = dict(zip([1,2,3], ["taro", "jiro", "hanako"]))
    >>> d6
    {1: 'taro', 2: 'jiro', 3: 'hanako'}

    ```
### update メソッド

+ 2つの辞書を破壊的に結合する
+ 引数に渡した方の辞書のキーで更新される
    ```python 
    >>> d1
    {1: 'taro', 2: 'jiro', 3: 'hanako'}
    >>> d2
    {3: 'tanaka', 4: 'yoshida', 5: 'yamada'}
    >>> d1.update(d2)
    >>> d1
    {1: 'taro', 2: 'jiro', 3: 'tanaka', 4: 'yoshida', 5: 'yamada'} # キー３は、d2のキーで更新（上書き）されたので 3: 'tanaka'　になった
    ```

### get メソッド（ディクショナリのキーをスマートに使う）

+ `D.get(キーワード, [なかった場合に返す値])`
+ 辞書をキーでアクセスすると、そのキーが無い場合は `KeyError` もしくはオプション引数に渡した値
+ get()メソッドを使うと、`KeyError` ではなく `None` を返す
    ```python
    >>> d = {1: 'taro', 2: 'jiro', 3: 'hanako'}
    >>> d[1]
    'taro'
    >>> d[10]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 10

    >>> d.get(1)
    'taro'
    >>> d.get(10) 
    >>>  # Noneを返している。インタープリタでは見えない。
    >>> type(d.get(10)) # None を返しているのを確認するために type 関数に入れてみる
    <class 'NoneType'>

    # キーがなかった場合に返す値の指定も可
    >>> d.get(10, "無いです!")
    '無いです!'
    ```
+ これを使うと、結構幸せになることが多い。
+ 教科書の例を簡単に説明

```python 
>>> str_list = list("ABCDABCDEFG")
>>> str_list
['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

# str_list の各要素が何個入っているか、という辞書 d を作成したい。
# この辞書にキーとして各要素、値として出現回数を入れる
# つまり最終的な d は このような辞書になる
>>> d
{'A': 2, 'B': 2, 'C': 2, 'D': 2, 'E': 1, 'F': 1, 'G': 1}

# まずは空の辞書を作成
>>> d = dict()
# str_list を for 文でループ
>>> for s in str_list:
        # 辞書 d に d[要素]で値を入れる。
        # 入れる値は、d.get(要素, なければ0)
        d[s] = d.get(s,0) + 1

>>> d
{'A': 2, 'B': 2, 'C': 2, 'D': 2, 'E': 1, 'F': 1, 'G': 1}
```
+ ポイントは、for 文が回っている間 d は更新し続けられている。
+ よって、`d.get(s,0)` することで、キーがすでに存在していればその値、していなければ0を d[s]に入れる
+ ` + 1` は、カウンターの役目
    + 例：最初のAの場合
    ```python
    d["A"] = d.get("A",0) + 1
    ```
    + これはこのようになるので
    ```python
    d["A"] = 0 + 1
    ```
    + `d["A"] は 1` になる。
    + そして二回目のAでは
    ```python
    d["A"] = d.get("A",0) + 1
    ```
    + これはすでに d["A"] は1なので、このようになり
    ```python
    d["A"] = 1 + 1
    ```
    + `d["A"] は 2` になる

### ディクショナリのメソッド

+  `D` はセットオブジェクトを意味しています
+ 以下の辞書で説明します。
    ```python 
    d = {1: 'taro', 2: 'jiro', 3: 'hanako'}
    ```
+ `D.keys()` ：辞書のキー一覧をリストで返す
    ```python 
    >>> d.keys()
    dict_keys([1, 2, 3])
    ```
+ `D.values()`: 辞書の値をリストで返す
    ```python 
    >>> d.values()
    dict_values(['taro', 'jiro', 'hanako'])
    ```
+ `D.items()` : キーと値をタプルにして、リストとしてを返す
    ```python 
    >>> d.items()
    dict_items([(1, 'taro'), (2, 'jiro'), (3, 'hanako')])
    ```

+ `D.get(キー, [ない場合に返す値])` :辞書のキーの値を返す。ない場合に返す値をオプションで与えることも出来る
    ```python 
    >>> d.get(3)
    'hanako'

    >>> d.get(4) # ない場合は None を返す。インタープリタの場合は表示はない

    >>> d.get(1, "ありません") # ない場合の返す値を指定する。
    'taro'
    >>> d.get(4, "ありません")
    'ありません'
    ```
+ `D.setdefault(キー, [ない場合はそのキーに当てはめる値])` : getに似ているが、キーが無い場合はそのキーと値を破壊的に追加できる。
    ```python
    >>> d.setdefault(1, "tanaka")
    'taro'
    >>> d.setdefault(4, "tanaka") # キー４はなかったので与えられた値を設定
    'tanaka'
    >>> d # 破壊的に変更された
    {1: 'taro', 2: 'jiro', 3: 'hanako', 4: 'tanaka'}
    ```    
+ `D.update(辞書)` ：渡した辞書で破壊的に更新する。同じキーがあれば上書き
    ```python 
    >>> d.update({10:"yoshida"})
    >>> d
    {1: 'taro', 2: 'jiro', 3: 'hanako', 10: 'yoshida'}
    ```

## if文と組み込み型

### 組み込み型と True/False

+ Pythonでは以下データを `False` とみなします。
    + 0
    + 空文字列
    + 空シーケンス
    + 空辞書
+ これ以外はTrueとみなします。よってこれを活かして if 文の条件分岐でよく使います。
+ 例：
    ```python 
    >>> a_list = []
    >>> if a_list:
    ...     print("a_list は空のリストではありません")
    ... else:
    ...     print("a_list は空のリストです")
    ... 
    a_list は空のリストです
    ```

### for 文と組み込み型

+ `range([開始数値], 終了数値, [ステップ])` ：開始数値やステップもオプションとして渡せる
    ```python 
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(range(1, 10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(range(1, 10, 3))
    [1, 4, 7]
    ```
+ range() 関数を使うと、作った数値リストを実際使うのではなく、ただたんに何回ループさせるかと処理させることが出来る
    ```python 
    >>> for i in range(3):
    ...     print("Hello")
    ... 
    Hello
    Hello
    Hello
    ```
### シーケンスとループカウンタ
+ ループカウンタ：今何番目の要素を処理しているか知るためのカウンター
    ```python
    >>> names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella']
    >>> for name in names:
    ...     print(name.upper()) 
    ```
    これだと、name を大文字にする処理はできるけど、今どの name を処理しているのかを知るにはちょっと手間。たとえば、
    ```python 
    >>> i = 0
    >>> for name in names:
    ...     print(i, name.upper())
    ...     i = i + 1
    ```
    こうかけるけどちょっと冗長。こういう時にenumarate() 関数を使う
+ enumerate(リスト): 引き取ったリストを、(インデックス, 要素) というタプルに変換する関数
    ```python 
    >>> enumerate(names) # 返すのは enumerate オブジェクト
    <enumerate object at 0x7fc3c7020880>
    >>> list(enumerate(names)) # 中身を確認したい場合は list() 関数に渡す
    [(0, 'Olivia'), (1, 'Emma'), (2, 'Ava'), (3, 'Sophia'), (4, 'Isabella')]
    ```
+ これをループにかける時に、アンパック代入を使うと便利。さっきのコードはこのように書き直せます。
    ```python 
    >>> for i, name in enumerate(names):
    ...     print(i, name.upper())
    ```
    + `i` に index, `name` に要素をいれています
    + 変数名`i` はインデックスを表す時によく使います（教科書では cnt 使ってあるけどテヘペロ）

### 2つのシーケンスを使ったループ
+ `zip()` 関数：2つのシーケンスを引数に取得し、同じインデックス番号のデータを一つのタプルにして返す
    ```python
    >>> boys = ['Oliver', 'George', 'Harry', 'Noah'] 
    >>> girls = ['Olivia', 'Amelia', 'Isla', 'Ava']

    >>> zip(boys, girls) # zip オブジェクトを返す
    <zip object at 0x7fc3c7020c40>
    >>> list(zip(boys, girls)) # 中身を確認したい場合は list() 関数に渡す
    [('Oliver', 'Olivia'), ('George', 'Amelia'), ('Harry', 'Isla'), ('Noah', 'Ava')]

    ```
+ これをループにかける時も、アンパック代入を使うと便利。
    ```python 
    >>> for b, g in zip(boys, girls):
    ...     print(b, g)

    Oliver Olivia
    George Amelia
    Harry Isla
    Noah Ava
    ```
+ これは、2つのリストから辞書を作る時にしばしば使います。
+ 例：「ディクショナリ型を使いこなす」のところで勉強したこの辞書の作り方。
    ```python 
    ## 2つの要素を持つシーケンスのリストから作る方法
    >>> d4 = dict([
        [1, "taro"], 
        [2, "jiro"], 
        [3, "hanako"]
        ])
    ```
    ここで与えてるこのリスト
    ```python 
    [[1, "taro"], [2, "jiro"], [3, "hanako"]]
    ```
    これはzip関数をつかうとこのように作れるから
    ```python
    >>> zip([1,2,3], ["taro", "jiro", "hanako"])
    <zip object at 0x7fc3c7020f00>
    >>> list(zip([1,2,3], ["taro", "jiro", "hanako"]))
    [(1, 'taro'), (2, 'jiro'), (3, 'hanako')]
    ```
    同じ辞書をこのように作成出来る
    ```python
    >>> dict(zip([1,2,3], ["taro", "jiro", "hanako"]))
    {1: 'taro', 2: 'jiro', 3: 'hanako'}
    ```

## 関数と組み込み型

+ 関数の最後に書く return 文に、リストやタプルを返すと、戻り値をアンパック代入できて便利。
+ 例：
    ```python 
    # 数値リストを引数に取る関数を定義し、最大値、最小値、合計を返す関数
    >>> def my_calc(l): 
    ...     x = max(l)
    ...     y = min(l)
    ...     z = sum(l)
    ...     return (x, y, z) # 返り値をタプルやリストで return 
    ```
    ```python 
    # 通常実行
    >>> my_calc(range(10))
    (9, 0, 45)

    # 返り値をアンパック代入する
    >>> x, y, z = my_calc(range(10))

    # アンパックした変数にデータがそれぞれ代入されている。
    >>> x
    9
    >>> y
    0
    >>> z
    45    
    ```

### 関数で引数リストを受け取る
+ 関数定義時、このように引き取る引数の変数を定義します。
    ```python 
    def my_func(x,y):
        return x + y
    ```
+ これって、**引き取るべき引数の数が先にわかっている**から出来ることです。
+ しかし、世の中そんなにうまく行かないので、先にわからないことも多い。
+ 何個必要か定義時にわからない引数のことを**可変長引数**といいます。
+ **可変長**とは、長さ（つまり引数の個数）が変更可能ということです。
+ つまり、何個でもこいやー！ってことです。
+ 可変長引数での関数定義：
    ```python 
    >>> def my_func(x, y, *args): # 絶対必要な引数は今まで通り、それ以外は * アスタリスクをつける）
    ...     print(x, y, args) # コードの中では アスタリスクはつけずに使う
    ... 
    ```
    ```python         
    >>> my_func(10, 20, 30, 40, 50) # args に入る部分は、タプルにいれて返されます
    10 20 (30, 40, 50)
    ```
    + 可変長引数の変数はしばしば `args` が使われます。

### 関数でキーワード引数を受け取る
+ ↑の例では `*args` はタプルで返されました。
+ リストだと、インデックスで要素を取得する必要があります。
+ これだと、可変長引数が長くなるとだんだんわからなくなってきます。
+ そういう場合、キーワード引数を受け取るように書きます。
+ 例：
    ```python 
    >>> def my_func(x, y, **kwargs):
    ...     print(x, y, kwargs)
    ... 
    >>> my_func(10, 20, z=30)
    10 20 {'z': 30} # 突然現れる辞書！
    ```
    + `kwargs` という引数名がしばしば使われます。keyword args の略です。
    + 突然現れる辞書！

## Pythonの文字列と日本語
+ P204-P217までは飛ばします 

### Pythonのファイル処理

+ `open(ファイルパス, 開くモード, エンコーディング)`：ファイルを開く関数
    + ファイルパス: ファイルのフルパス
    + 開くモード(とりあえず３つ。)
        + `r`: 読み込み
        + `w`: 書き込み（新規作成）
        + `a`: 追加書き込み
    + エンコーディング:
        + encoding="utf-8" ほぼ一択でOKです。
    + 返り値は、ファイルオブジェクト
+ memo: フルパスを調べる方法: `foo.txt` を開いて、右クリックからパスをコピー。
![](https://i.imgur.com/tbfUqYh.jpg)
+ 例：
    ```python 
    >>> fpath = "/home/taro/study-python/data/foo.txt" # ご自身の foo.txt へのパスを入れてください

    # open 関数でファイルを開く
    >>> f = open(fpath, "r", encoding="utf-8")
    # TextIOWrapperというオブジェクト。これがファイルオブジェクトです。
    >>> type(f)
    <class '_io.TextIOWrapper'>

    # このオブジェクトからデータを read して初めて中のデータが取得。
    >>> f.read()
    '春はあけぼの。やうやう白くなり行く、山ぎはすこしあかりて、むらさきだちたる雲のほそくたびきたる。夏は夜。月のころはさらなり。やみもなほ、ほたるの多く飛びちがひたる。また、ただ一つ二つなど、ほのかにうち光りて行くもをかし。雨など降るもをかし。'

    # 一度 read したら先ほどのオブジェクトは空になります。
    >>> f.read()
    ''

    # close() メソッドでちゃんとファイルを閉じましょう
    >>> f.close()
    ```
### ファイルオブジェクトのメソッド
+ `F` はファイルオブジェクトを意味します。
+ `F.read()` : ファイルをすべて読み込み文字列を返す。↑で説明したので例は飛ばします。
+ `F.readline()`：ファイルの一行目を読み込み文字列を返す。もう一度呼び出すと次の行を文字列で返す.最後まで終わったら、次の呼び出しで空の文字列を返す
    ```python 
    >>> fpath = "/home/taro/study-python/data/names.csv"
    >>> f = open(fpath, "r", encoding="utf-8")
    >>> f.readline()
    '1,Tomasine,Kimmons,tkimmons0@wordpress.com,Female,171.244.84.34\n'
    >>> f.readline()
    '2,Aleksandr,Rahl,arahl1@addthis.com,Male,106.155.134.164\n'
    :
    :
    '10,Donnell,Awcoate,dawcoate9@xing.com,Male,10.11.125.242\n'
    >>> f.readline()
    ''
    ```
+ `F.readlines()`： ファイル全部読み込み、一行ずつ文字列にしたリストを返す
    ```python
    >>> f.readlines()
    ['1,Tomasine,Kimmons,tkimmons0@wordpress.com,Female,171.244.84.34\n', 
    '2,Aleksandr,Rahl,arahl1@addthis.com,Male,106.155.134.164\n', 
    :
    :
    '10,Donnell,Awcoate,dawcoate9@xing.com,Male,10.11.125.242\n']
    ```

### ファイル書き込む
+ ファイルに書き込む場合は、 open() 関数に渡すモードを書き込みモードにする
+ `F.write(文字列)` ：ファイルに文字列を書き込む
    ```python
    >>> f = open("/tmp/hoge.txt", "w", encoding="UTF-8")
    >>> f.write("ポニョ")
    3 # ここで返される数値はよくわからないけど、ファイルの書き込みの最終シーク位置だと思う
    >>> f.close() 
    ```
    + `f.close()` して初めて書き込まれる
+ `F.writelines(リスト)` ：リストをつなげて書き込む。改行はしない
    ```python
    >>> f = open("/tmp/hoge.txt", "w", encoding="UTF-8")
    >>> f.writelines(["ポニョポニョ", "さかなのこ"])
    >>> f.close()
    ```



