# クラスとオブジェクト指向開発

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

## Pythonでクラスを使う

### オブジェクトとクラス

+ オブジェクト（指向）とは `materials/chapter04.md` で学んだ通り
    + データと命令を一つにしておこうという発想
    + データじたいが、自分自身は何をすることが出来るか（メソッド）を持つ
    + データにメソッドがブラブラぶら下がる
    + 一番のメリット：**データを作ってしまえば、そのデータに対して出来ることを一つ一つコーディングする必要が無い**
+ そのオブジェクトをまとめて活用する時の仕組みを**クラス**という
+ 同じような性質を持ったオブジェクトをまとめてクラスという仕組みに突っ込んでおけば、楽だよね？！っていう考え
+ Pythonには、最初から組み込みでクラスがたくさん用意されている
    + 例：文字列クラス https://docs.python.org/ja/3/library/stdtypes.html#str
        + 文字列クラス
        + 文字列メソッド
        + ソースコードは多分[これ](https://github.com/python/cpython/blob/b6d68aa08baebb753534a26d537ac3c0d2c21c79/Lib/collections/__init__.py#L1299)
    
### クラスからオブジェクト（インスタンス）を作る
+ 設計図（型）であるクラスは、そのままでは使えない
+ 一度、実体化（インスタンス化）する必要がある
+ 組み込みクラスのインスタンス化
    1. クラスを読み込む
        ```python 
        import 組み込みクラス名
        ```
        もしくは
        ```python 
        from 組み込みクラス名 import 使いたいクラス
        ```
    1. インスタンス化する
        ```python
        c = 組み込みクラス名.使いたいクラス()
        ```
        もしくは
        ```python
        c = 使いたいクラス()
        ```
        この変数 `c` をインスタンスと呼ぶ
+ 例：
    ```python 
    import decimal
    d = decimal.Decimal(10)
    ```
    もしくは
    ```python 
    from decimal import Decimal 
    d = Decimal(10)
    ```
  
### インスタンスを利用する

+ インスタンス `d` は、Pythonで定義されている Decimal クラス内のメソッドを使うことが出来る
    + Decimal クラス https://github.com/python/cpython/blob/4e0ce820586e93cfcefb16c2a3df8eaefc54cbca/Lib/_pydecimal.py#L513
+ ソースを見るのは大変なので、 `dir()`  関数に d を渡して、どういうメソッドがあるか、確認してみましょう
    ```python 
    dir(d)
    >>> dir(d)
    ['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__complex__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',    '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'adjusted', 'as_integer_ratio', 'as_tuple', 'canonical', 'compare', 'compare_signal', 'compare_total', 'compare_total_mag', 'conjugate', 'copy_abs', 'copy_negate', 'copy_sign', 'exp', 'fma', 'from_float', 'imag', 'is_canonical', 'is_finite', 'is_infinite', 'is_nan', 'is_normal', 'is_qnan', 'is_signed', 'is_snan', 'is_subnormal', 'is_zero', 'ln', 'log10', 'logb', 'logical_and', 'logical_invert', 'logical_or', 'logical_xor', 'max', 'max_mag', 'min', 'min_mag', 'next_minus', 'next_plus', 'next_toward', 'normalize', 'number_class', 'quantize', 'radix', 'real', 'remainder_near', 'rotate', 'same_quantum', 'scaleb', 'shift', 'sqrt', 'to_eng_string', 'to_integral', 'to_integral_exact', 'to_integral_value']
    ```
    これが Decimal インスタンスである `d` が持つメソッドです。
+ `d` を使って四則演算も出来る。返り値は新しいDecimalオブジェクト
    ```python 
    >>> d + 10
    Decimal('20')
    # 実は __add__ メソッドと同じ
    >>> d.__add__(10)
    Decimal('20')

    # d を破壊的に変更などはしない
    >>> d
    Decimal('10')
    ```
+ メソッドを使う
    ```python 
    # インスタンスの平方根を出す sqrt メソッド。 () を添えないと、built-in method の sqrt ですというメッセージ（てきなもの）が返る
    >>> d.sqrt
    <built-in method sqrt of decimal.Decimal object at 0x7f8a7ecbd5e0>
    # () をつけて、メソッドを呼び出す。    
    >>> d.sqrt()
    Decimal('3.162277660168379331998893544')

    ```

### オブジェクトとインスタンス

+ 教科書の説明がわかりにくかったので、こちらを参照してください
    + [オブジェクト指向とクラス — Pythonオンライン学習サービス PyQ（パイキュー）ドキュメント](https://docs.pyq.jp/python/library/class.html#id6)
+ クラスから作られたインスタンスのこともオブジェクトと呼ぶそうです

## クラスを作る
### クラスを定義する

+ `homework/chap06/chap_06_05_2.md` で説明します

### インスタンスのアトリビュート
+ `chap_06_05_2.md` で作った Resume クラスをインスタンス化したあとで、定義していなかったデータを加えたい思った場合、インスタンスに直接データを渡すことができます。
+ 例：
    ```python 

    class Resume:
        def __init__(self, name, address, email, birthday, tel):
            self.name = name 
            self.address = address 
            self.email = email 
            self.birthday = birthday 
            self.tel = tel 
    
    taro = Resume("Taro Okamoto", "Shinjuku, Tokyo", "taro@taro.com", "1911-2-26", "11-1111-1111")
    
    # 直接データを入れる
    taro.job = "artist"
    ```
    `taro.job` を参照
    ```python 
    >>> taro.job
    'artist'
    ```
+ このように、インスタンスに変数を追加するようにデータを入れる仕組みをアトリビュートといいます。
+ `taro.job` を、「taro の job アトリビュート」と呼びます。
+ 上記は、「taro の job アトリビュートに、"artist" を代入」したということになります
+ 追加したアトリビュートは、 dir() 関数で確認できます
    ```python 
    >>> dir(taro)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'address', 'birthday', 'email', 'job', 'name', 'tel']    # job が追加されとる！
    ```
+ 実は、 `chap_06_05_2.md` で説明した、初期値もアトリビュートです。
+ もっというと、オブジェクトやインスタンスのメソッドも「アトリビュート」です。ようは、そのクラスが持つデータやメソッドはすべてそのクラスのアトリビュートです。


### メソッドの定義と初期化メソッド
+ `homework/chap06/chap_06_05_2.md` で説明します

### メソッドと第一引数 self 
+ `homework/chap06/chap_06_05_2.md` で説明します

### アトリビュートの隠蔽
`chap_06_05_2.md` で作った、`RightTriangle` クラスを使って、説明します。

```python 
class RightTriangle:
    def __init__(self, bottom, height, name, color):
        self.bottom = bottom
        self.height = height
        self.name = name 
        self.color = color 

    def area(self):
        return self.bottom * self.height * 0.5 

:
:

```
ではいったんインスタンス化します
```python 
r = RightTriangle(5, 9, "oira", "red")
print(r.area())
# >>> 22.5 
```

ここで `.area` というアトリビュートを追加してしまうとどうなるでしょう。
```python 
r.area = 10
print(r.area)
# >>> 10 
``` 
.area アトリビュートができました。というは、同名の `area()` メソッドはどうなったかというと
```python
print(r.area())
>>> Traceback (most recent call last):
    print(r.area())
TypeError: 'int' object is not callable
``` 
大事故！！！！！

このようなことが起きないように、アトリビュートの隠蔽をします。この隠遁のことをPythonではカプセル化といいます。

1. カプセル化その1： アンダーバー１つつけて名前を定義し、これはクラスの内部だけで利用するための名前ですよ、と注意喚起する方法
    ```python 
    # _ 一つつける
    class RightTriangle:
        def __init__(self, bottom, height, name, color):
            self._bottom = bottom
            self._height = height
            self._name = name 
            self._color = color 

        
        def _area(self): 
            return self._bottom * self._height * 0.5 

    ```
    + これは**注意喚起**なので、実際は書き換えることができます。
1. カプセル化その2： アンダーバー２つつけて名前を定義し、インスタンスからは呼び出せなくする方法
    ```python 
    class RightTriangle:
        def __init__(self, bottom, height, name, color):
            self.__bottom = bottom
            self.__height = height
            self.__name = name 
            self.__color = color 
            
        def __area(self): 
            return self.__bottom * self.__height * 0.5 # クラス内ではアクセス出来る

    ```
    インスタンス化して呼び出そうとすると
    ```python 
    r = RightTriangle(5, 9, "oira", "red")
    print(r.__area())
    ```
    ```python 
    Traceback (most recent call last):
        print(r.__area())
    AttributeError: 'RightTriangle' object has no attribute '__area'
    ```
    + そのようなアトリビュートはない！と怒られる。あるけど、隠遁しなくちゃ行けないのでウソついてくれる。
    + 隠遁は出来るけど、インスタンスから呼び出すことアクセスすることもできなくなる。
    + クラス定義内では、呼び出すことは出来る
    + （つまり）クラス定義内では、書き換えも出来る

+ ご利用の際はお気をつけください

### ちょっとおまけ

これまで、文字列型とかリスト型とか色々なデータ型を見てきましたが、アイツらは実は全部クラスのインスタンスです。
```python 
s = "shinseitaro" 
s.upper() # 文字列クラスのメソッド呼び出し

>>> type(s)
<class 'str'> # 文字列クラスのインスタンス


>>> isinstance(s, str) # インスタンスかどうか確認する関数
True
```

Decimal クラスのインスタンス化みたいな、インポートしてインスタンスつくって、といった作業はしていませんね。
```python
from decimal import Decimal 
d = Decimal(10)
```

どうなっているかというと、

Pythonが、ダブルクオーテーション（もしくはシングルクオーテーション）で囲まれたデータをコードの中に見つけたら、内部的に文字列型のクラスインスタンスを作って返すということを自動で行っています。

文字列やリスト、数値などは頻繁に使います。よって、開発者がわざわざクラスのインスタンス化ということをしなくても、楽にかつ直感的にコードを書けるような仕組みを後ろにもっています。

こういう機能のことを、プログラミング言語では、「シュガーシンタックス（糖衣構文）」と呼びます。

`+` や `-` といった演算子もじつはシュガーシンタックスです。


