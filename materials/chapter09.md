# スコープとオブジェクト

## 名前空間（ネームスペース）
変数、関数、クラスなどが定義されている場所のこと。

## スコープ
変数、関数、クラスなどが有効な範囲

## スコープのルール

![](https://i.imgur.com/xOdTeLq.jpg)

+ ビルドインスコープ
    + `+`、 `>` 、 `def` などいきなり使える python のコード
+ モジュールスコープ
    + ファイルに書く、変数や関数やクラス
    + トップレベルとも呼ぶ
    + グローバルと呼ぶひともいる
+ ローカルスコープ
    + ファイル記述された関数やクラスの「内部」のみ

+ 意識してローカルスコープを使ってください
    + 図の例でいえば、`func` 関数の中の 引数 `a` などは、**func 関数のなかでしか使えない**
    + もし、別の関数やクラスで同じ名前の引数を使っていてもローカルスコープだけで有効。    
    + これがもっとも安全（＝エラー処理が楽）な方法

## クラス、インスタンスのスコープ

クラスを学んだ時に、Resumeクラスを作りました

```python 

from datetime import date 

class Resume:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    
    def age(self): 
        # pythonの標準クラス datetime の中に定義してある today() メソッド
        today = date.today()
        # self.が保持しているデータを使う。 
        days = (today - self.birthday).days # 日数を数値で取得
        years = round(days / 365) # 365で割って年数を出す
        return years

r1 = Resume("okamoto taro", date(1911,2,26))
print(r1.age())   # 110


r2 = Resume("山田花子", date(1975,3,10))
print(r2.age()) #46

```

例えばここで間違って `r1` に `age` というアトリビュートを追加してしまったとします。

```python 
r1.age = 500
``` 
この場合 `r1` の age() 関数と同名ですので、`r1.age()` は上書きされてしまい呼び出すことはできなくなります

```python
>>> print(r1.age())  
Traceback (most recent call last):
  File "materials/chapter09_aux/classscope.py", line 24, in <module>
    print(r1.age())
TypeError: 'int' object is not callable
```

しかし、`r2.age()` は無傷です。あくまで r1 の age が上書きされただけですので、r2 には影響ありません。

これが、インスタンスのスコープです。インスタンス化してしまえば、アクセス出来るのはインスタンスのアトリビュートだけです。

### 注意

しかし、クラスのアトリビュートに直接変更を加えると、すべてのインスタンスに影響があります

```python

# 上記のResumeクラスを定義後、

r1 = Resume("okamoto taro", date(1911,2,26))
r2 = Resume("山田花子", date(1975,3,10))

Resume.age = 5000 # ←ここ！！！

r1.age() # TypeError: 'int' object is not callable
r2.age() # TypeError: 'int' object is not callable
```

このように `Resume.age` クラスのアトリビュートに直接アクセスして書き換えてしまうと、同クラスから作られたインスタンスすべてに影響します。

上記は、`r1` `r2` の インスタンスを作成したあとにもかかわらず、クラスの `age 関数`と同名のアトリビュートを数値で上書きしてしまったため、`r1.age()` `r2.age()` どちらとも `age 関数`が上書きされてしまった例です。

これはクラスのスコープは、インスタンスのスコープの下にあるために発生します。インスタンス化したあとでも親であるクラスに変更があれば子のインスタンスも影響される、そのように覚えておいてください。

ところで、実生活でこのような悪意のあることを書いている人をみたことはありませんが、初心者の間は悪意なくこういう間違いは起こしてしまいます。十分気をつけてください。



## 純粋オブジェクト指向言語としてのPython

### オブジェクト

+ オブジェクト とは、`materials/chapter04.md` の `オブジェクト指向` で学んだ以下の考え方を具現化したもの。
    ```
    * データと命令を一つにしておこうという発想
    * データじたいが、自分自身は何をすることが出来るか（メソッド）を持つ
    * オブジェクトにデータやメソッドがブラブラぶら下がる
    ```

+ 具体的には、
    + 変数
    + クラスをインスタンス化したもの（これも変数に代入するので、変数とも言える）
    + インポートしたモジュール
    ```python
    x = "shinseitaro"
    r = Resume() 
    import datetime 
    ```
    + これの `x` `r` `datetime`  がオブジェクト

### アトリビュート

+ アトリビュートとは、オブジェクトについている、データや命令（メソッド）のこと
+ オブジェクトに `.` でつなぐ
+ この `.` のことを、**紐づき**、や、**レファレンス** と呼ぶ
    ```python 
    x.upper() # SHINSEITRO
    r.name # おかもとたろう
    datetime.date(2000,1,1) # 2000/1/1 の日付オブジェクト作成
    ```
+ この、upper() メソッド, name, date()メソッドなどがアトリビュート。
+ メソッドの場合は、丸括弧 () をつけて呼び出す。引数が必要な場合は、丸括弧の中で渡す。


### dir 関数

+ オブジェクトが持つアトリビュートを取得出来る関数
    ```python 
    >>> x = "shinseitaro"
    >>> dir(x)
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    ```
+ 取得できるすべてを `.` でアクセスして利用出来る

### type 関数
+ オブジェクトの型（文字列型、数値型、などなど）を返す関数
    ```python 
    >>> type(x)
    <class 'str'>
    ```
### isinstance 関数
+ オブジェクトが、指定した型であるかを真偽値で返す関数
    ```python 
    >>> isinstance(x, str)
    True
    >>> isinstance(x, int)
    False
    ```

### issubclass 関数
+ `issubclass(a, b)` `a` クラスは `b` クラスを継承しているかどうかを真偽値で返す
    ```python 
    >>> issubclass(str, object)
    True
    >>> issubclass(int, object)
    True
    ```
+ 他の型 (float, boolean, ...) のすべて `object`型を継承
+ つまりPythonは すべての型は `object`型を継承している

### Pythonはすべてが、型を持つオブジェクト

+ 実は object 型というものがあり、python で作られるすべてのオブジェクトがこの object 型（クラス）を継承している
    ```python 
    >>> isinstance(1, object)
    True
    >>> isinstance("shinseitaro", object)
    True

    >>> import math
    >>> isinstance(math, object)
    True
    ```
+ `object` は、python の共通のルールを持っているオブジェクト、くらいに考えておけばOKです。

### オブジェクトと変数

+ オブジェクトは変数に代入して使うと便利

### オブジェクトと名前空間（スコープ）

```python 
x = "okamoto taro"
y = "shinseitaro" 

y.upper()
# SHINSEITARO
```
+ オブジェクトは、それぞれのスコープを持つ。
+ x も y も upper() メソッドは持っているのに、 y.upper() で "SHINSEITARO" と返るのは、x と y のスコープが全く独立しているから
+ オブジェクトの名前空間がキチンと守られているので、安心してコーディングが出来る

















