# Python の基礎をマスターする

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


## ディクショナリ（辞書）を使う
+ 辞書とは：キーと値の組み合わせが一要素のデータで `{}` で囲まれたデータ
    ```python
    {key1: 値, key2: 値, key3: 値}
    ```
    + 辞書からデータを取得するには、キーを指定する
    + キーは絶対ユニークでなくてはいけない
    + キーは変換可能なものではダメ
    + 値はどんなデータ型でもOK
    ```python
    >>> d = {'x': 135, 'y': 225, 'z': 315}
    >>> d['x']
    135
    >>> d2 = {1:"apple", 2:"ringo"}
    >>> d2[1]
    'apple'   

    # キーはユニークでありさえすればいいので、
    # 同じ辞書内に数値のキーと文字列のキーが同居してもOK
    >>> d3 = {1:123, "A":[1,2,"a"]}
    >>> d3
    {1: 123, 'A': [1, 2, 'a']} 
    ```
+ 辞書にデータを追加
    + `辞書[キー]＝値` で追加
    ```python 
    >>> name = {'first_name': 'Cayla',
    ...     'last_name': 'Camolli',
    ...     'email': 'ccamolli0@dmoz.org',
    ...     'gender': 'Female'}

    >>> name["country"] = "US" # countryキーで US を追加
    >>> name
    {'first_name': 'Cayla', 'last_name': 'Camolli', 'email': 'ccamolli0@dmoz.org', 'gender': 'Female', 'country': 'US'}
    >>>     
    ```
+ データを更新
    + `辞書[キー]＝値`で更新
    ```python 
    >>> name["country"]="JAPAN"
    >>> name
    {'first_name': 'Cayla', 'last_name': 'Camolli', 'email': 'ccamolli0@dmoz.org', 'gender': 'Female', 'country': 'JAPAN'}
    ```
+ データを削除
    + `del 辞書[キー]` 
    ```python 
    >>> del name["country"]
    >>> name
    {'first_name': 'Cayla', 'last_name': 'Camolli', 'email': 'ccamolli0@dmoz.org', 'gender': 'Female'}    
    ```
+ キーが存在するか確認
    + `キー in 辞書`  
    ```python
    >>> "gender" in name
    True
    >>> "address" in name
    False    
    ```  
+ キーを使ったループ
    ```python 
    >>> for k in name:
    ...     print(k)
    ... 
    first_name
    last_name
    email
    gender

    >>> for k in name:
    ...     print(name[k])
    ... 
    Cayla
    Camolli
    ccamolli0@dmoz.org
    Female
    ```

## set(集合)を使う
+ 一切の重複が無いデータ
+ `{}` でくくる
+ 順番はFixされない
    ```python 
    >>> s = {'A', 'B', 'C', 'D', 'E'}
    >>> s
    {'B', 'D', 'E', 'A', 'C'}
    ```
+ 集合演算をする時に超ベンリ
    + **和集合**：複数のデータを足し合わせて重複無しのデータを取得
    + `|` を使う
        ```python 
        >>> s1 = {'A', 'B', 'C', 'D', 'E'}
        >>> s2 = {'A', 'B', 'X', 'Y', 'Z'}
        >>> s1 | s2
        {'B', 'D', 'X', 'E', 'A', 'Z', 'C', 'Y'}
        ```
    + **差集合**：集合1にはあって集合2にはないデータを取得
    +  `-` を使う
        ```python 
        >>> s1 - s2
        {'D', 'C', 'E'}
        ```  
    + **論理和**：どの集合にも入っているデータを取得
    + `&` を使う
        ```python 
        >>> s1 & s2
        {'B', 'A'}
        ```    
    + **対象差**：ほかの集合が持っていないデータを収録
    + `^` を使う
        ```python 
        >>> s1 ^ s2
        {'C', 'Z', 'X', 'E', 'D', 'Y'}
        ```    
+ 比較演算子をつかって**部分集合**かどうか確認
    ```python 
    >>> {'A', 'B'} =< {'A', 'B', 'C'}
    True
    >>> {'A', 'B'} >= {'A', 'B', 'C'}
    False
    >>> {'A', 'B', 'D'} >= {'A', 'B', 'C'}
    False
    >>> {'A', 'B', 'D'} <= {'A', 'B', 'C'}
    False
    ```
+ for で回せる
    ```python 
    >>> for x in s1 & s2:
    ...     print(x)
    ... 
    B
    A
    ```
+ in で要素を確認できる    
+ リストに使える関数（max, len など)は set にも使える
+ set()関数にリストを渡すと set を作成可
    ```python
    >>> set([1,2,3,4,5])
    {1, 2, 3, 4, 5}
    ```    

## タプルを使う
+ リストとほぼ一緒
+ 一度作ったら可変出来ない、というところが違う
    ```python 
    >>> l = [1,2,3]
    >>> l[0] = 100
    >>> l
    [100, 2, 3]

    >>> t = (1,2,3)
    >>> t[0] = 100 # 変更できない！
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    ```

## リスト、辞書、セット、タプルまとめ

型|記述方法|特徴
---|---|---
リスト|[要素0, 要素1, 要素2, …]|インデックスでデータを取得
辞書|{キー1: 値, キー2: 値, キー2: 値, …}|キーは絶対ユニーク
セット|｛要素0, 要素1, 要素2, …｝|要素は絶対ユニーク
タプル|（要素0, 要素1, 要素2, …）|一旦作ったら可変不可



## if の応用

+ `if` 文の後ろにはTrue/False（真偽値）を問うコードを書く
+ その真偽値を問うための演算子


比較演算子|意味
---|---
x == y| x と y が等しい
x != y| x と y が等しくない
x > y|  x は y よりも大きい
x < y|  x は y よりも小さい
x >= y| x は y と等しいか大きい
x <= y| x は y と等しいか小さい
x in y| x という要素 が y に存在する
x not in y|x という要素 が y に存在しない
