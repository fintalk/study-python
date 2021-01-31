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

    # キーは変換できないものしか使えない
    # リストは変換出来る（要素をけしたり更新したりできる）のでダメ
    >>> {"A":123, ["A","B","C"]:123}
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'
    ```
+ 辞書にデータを追加
    + `辞書[キー]＝値` で追加
    ```python 
    >>> name = {
        'first_name': 'Cayla',
        'last_name': 'Camolli',
        'email': 'ccamolli0@dmoz.org',
        'gender': 'Female'
        }

    >>> name["country"] = "US" # countryキーで US を追加
    >>> name
    {'first_name': 'Cayla', 
    'last_name': 'Camolli', 
    'email': 'ccamolli0@dmoz.org', 
    'gender': 'Female', 
    'country': 'US'}
    >>>     
    ```
+ データを更新
    + `辞書[キー]＝値`で更新
    ```python 
    >>> name["country"]="JAPAN"
    >>> name
    {'first_name': 'Cayla', 
    'last_name': 'Camolli', 
    'email': 'ccamolli0@dmoz.org', 
    'gender': 'Female', 
    'country': 'JAPAN'}
    ```
+ データを削除
    + `del 辞書[キー]` 
    ```python 
    >>> del name["country"]
    >>> name
    {'first_name': 'Cayla', 
    'last_name': 'Camolli', 
    'email': 'ccamolli0@dmoz.org', 
    'gender': 'Female'}    
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
    >>> s = {'A', 'B', 'A', 'B', 'C', 'D', 'E'}
    >>> s
    {'E', 'A', 'D', 'B', 'C'}
    ```
+ 集合演算をする時に超ベンリ
    + **和集合**：複数のデータを足し合わせて重複無しのデータを取得
    + `|` （パイプ）を使う
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
    + **対象差**：ほかの集合が持っていないデータを取得
    + `^`（ハット） を使う
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
    ```python 
    >>> "C" in {"A", "B", "C"}
    True
    ```
+ リストに使える関数（max, len など)は set にも使える
    ```python
    >>> max({1,2,3,4,5})
    5
    ```
+ set()関数にリストを渡すと set を作成可
    ```python
    >>> set([1,2,3,4,5])
    {1, 2, 3, 4, 5}
    ```    

## タプルを使う
+ リストとほぼ一緒
+ `[]` ではなく `()` で囲む
+ リストとの違いは、一度作ったら変更出来ない
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
+ 変更できない＝辞書のキーとして使うことが出来る.
    ```python
    >>> {"A":123, ["A","B","C"]:123}
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

    >>> {"A":123, ("A","B","C"):123}
    {'A': 123, ('A', 'B', 'C'): 123}
    ```

## リスト、辞書、セット、タプルまとめ

型|記述方法|特徴
---|---|---
リスト|`[要素0, 要素1, 要素2, …]`|インデックスでデータを取得
辞書|`{キー1: 値, キー2: 値, キー2: 値, …}`|キーは絶対ユニーク
セット|`｛要素0, 要素1, 要素2, …｝`|要素は絶対ユニーク
タプル|`（要素0, 要素1, 要素2, …）`|一旦作ったら可変不可


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
x in y| x という要素 が y に存在する　(yは複数のデータ)
x not in y|x という要素 が y に存在しない　(yは複数のデータ)

---

## while 文でループを作る

+ 書き方
    ```python 
    while 条件式:
        # 条件がTrueの間ずっと
        実行するコード
    ```
+ 実験：インタープリタを立ち上げて以下のコードを書いて下さい
    ```python 
    i = 0
    while True: 
        i = i + 1
        print(i, "Hello")
    ```
    + だーーーーーーーーーーーーっと数字とHelloがプリントされますね。
    + これを止めるには、**Ctrl + C** (win) / **control + C** (mac) を同時に押せば止まります。
+ for 文 と while 文の違い
    ```python 
    for i in シーケンス：
        シーケンスが終わるまで繰り返す
    ```
    ```python 
    while 条件:
        条件がTrueの間はずーーっと繰り返す
    ```

## break文とcontinue文をつかったループの制御

### break 
+ **何かしらの条件に当てはまったら ループを終わらせる**
+ while でも for でも使える
+ break 文 使い方
    ```python 
    for i in シーケンス：
        if 何かしらの条件に当てはまった場合：
            break # ここでループを終わらせる
    ```

    ```python 
    while 条件:
        if 何かしらの条件に当てはまった場合：
            break # ここでループを終わらせる
    ```
    + 例：
        ```python
        # 0~9までのシーケンスをプリントするコード
        # ただし、数値が５を超えた時、ループを終わらせる
        cnt = 5
        for i in range(10):
            if i > cnt:
                break
            print(i)
        
        0
        1
        2
        3
        4
        5
        ```
        ```python
        cnt = 5
        i = 0
        while i < 10:
            if i > cnt:
                break
            print(i)
            i += 1        
        ```  

### continue 
+ **何かしらの条件に当てはまったら、何もせずに次へスキップする**
+ while でも for でも使える
+ continue 文 使い方
    ```python 
    for i in シーケンス：
        if 何かしらの条件に当てはまった場合：
            continue # 何もせずに次へスキップする
    ```

    ```python 
    while 条件:
        if 何かしらの条件に当てはまった場合：
            continue # 何もせずに次へスキップする
    ```
    + 例
        ```python 
        # 0~9の数字にたいして、3で割り切れる場合はスキップ。それ以外をプリントする。
        for i in range(10):
            if i % 3 == 0:
                continue
            print(i)
        1
        2
        4
        5
        7
        8
        ```    
        ```python 
        # 同じものを while で書く
        i = 0
        while i < 10:
            if i % 3 ==0:
                i = i + 1 # インクリメント
                continue
            print(i)
            i = i + 1 # インクリメント
        
        1
        2
        4
        5
        7
        8
        ```
        + インクリメント：データに1加えること。（1減らすことをデクリメントという）
        
+ ループの else
    + P143で説明のある ループの else ですが、私も書かないし、他の人のコードでもみたこと無いです。
    + なので教科書をよんで、ふーんくらいに思っておけばいいかなと思います

## 関数の応用
+ 関数の引数にデフォルト値を渡すことが出来るという説明は、Chapter02で消費税の関数を作った時に行った通りです。
    ```python
    def calc_with_tax(price, rate=0.1): # デフォルトで0.1
        x = price * (1 + rate) 
        x = int(x) 
        return x 

    >>> print(calc_with_tax(100))
    110
    ```
+ デフォルト引数も好きなだけ指定することができます
+ デフォルト引数の渡し方は２パターンあります
    1. 順番
    1. キーワード
+ たとえば↑の例では
    ```python
    >>> calc_with_tax(1000, 0.5)
    1500
    >>> calc_with_tax(1000, rate = 0.5)
    1500
    ```
    どちらでも構いません。順番が守られていれば、`rate =` を書く必要はありません。
+ たとえば、以下のようにデフォルト引数が２つの場合
    ```python
    def calc_with_tax_and_cost(price, rate=0.1, cost=0.01):
        x = price * (1 + rate + cost) 
        x = int(x) 
        return x 
    ```
    + この場合は、rate だけ変えたい場合は順番を守った書き方でOKですが、cost を変えたい場合はキーワード指定をしないといけません.
    ```python
    # cost を 0.02 に変えたい
    >>> calc_with_tax_and_cost(1000, , 0.02) # 3番目に引数を入れたツモリだけどエラー
    
    File "<ipython-input-6-4f58b3f3a092>", line 7
    calc_with_tax_and_cost(1000, , 0.02) 
                                 ^
    SyntaxError: invalid syntax
    ``` 
    ```python
    >>> calc_with_tax_and_cost(1000, 0.1, 0.02) 
    1120   
    >>> calc_with_tax_and_cost(1000, cost= 0.02)
    1120
    ```
    ```python
    # キーワードの場合は順番が逆でもOK
    >>> calc_with_tax_and_cost(1000, cost=0.02, rate=0.05)
    1070
    ```

## 関数とローカル変数

+ ここはP316からの名前空間の時に説明します。





        


    






