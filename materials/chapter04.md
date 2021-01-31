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
