# Python でプログラミングを始めよう

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


## 数値を使う

演算子|説明
---| ----
+  | 加算
- |減算
* |乗算
/ |除算
// |除算の商
%  |除算の余り
** |累乗


+ この二つは案外よく使うので覚えると便利です
    ```python
    >>> 31 // 3
    10
    >>> 10 % 3
    1
    ```

## 変数を使う

+ 変数とはデータを入れる箱、という説明って案外わかりにくい
+ 変数にデータを代入しておくことで、使い勝手が上がる、と覚えてもらっていいです。
    ```python
    # 531863543 を x に代入すると、その後は 531863543 と書かなくても x に対して演算すれば良いので楽ちん

    >>> x = 531863543
    >>> x / 100
    5318635.43
    >>> x + 123
    531863666
    >>> x // 55
    9670246
    ```
### <font color="red">【注意】</font>最後に代入したデータがその変数のデータになる
+ これが案外バグ（プログラムの間違い）の原因になりやすい。何かの手違いで変数を上書きすることは非常によくあるので気をつけましょう。   
    ```python
    >>> x = 100
    >>> x + 2
    102
    # x を50で上書きする。
    >>> x = 50
    >>> x + 2
    52
    ```
### よく使うテクニック:代入した値を更新する
+ 代入されているデータを演算に使い、新しい値を代入し直す
    ```python
    >>> x = 100
    # 右辺の x はまだ100。そこに50を足したものを x に代入する
    >>> x = x + 50 
    >>> x
    150
    ```
### 複合演算子
+ 上のテクニックを使う時によく使う演算子。
+ 少しでも短くコードを書きたいと思っているオジサンたちがよく使うイメージがある。
+ （個人的には分かりづらいし、対して違わないので複合演算子は使わないです）
    ```python
    >>> x = 100
    >>> x += 50 # ここ
    >>> x
    150
    ```


複合演算子|説明
---| ----
+=  | 加算
-= |減算
*= |乗算
/= |除算


## 文字列を使う

+ 文字列は、`" ~~~~ "` もしくは `' ~~~~ '` で定義する。
+ つまりシングル/ダブルクオーテーションで囲まれていれば文字列

    ```python
    # 全部文字列
    "shinseitaro"
    "2021-01-11"
    '531'
    '*'
    "100*25"
    ```
+ 文字列の連結は `+` でできる
    ```python
    >>> me = "shinseitaro" 
    >>> you = "you" 
    >>> me + " and " + you
    'shinseitaro and you'
    ```
+ 型が違うとだめ。
    + 型とはデータの種類のこと。文字列型、数値型、などデータの型は多数。
    ```python
    >>> x = "123"
    >>> x + 100
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: can only concatenate str (not "int") to str
    ```
    + 型変換するための関数を使うとできる  
    ```python
    >>> int(x)
    123
    >>> int(x) + 100
    223
    ```    

## リストを使う
+ リスト：複数のデータをひとまとめにするデータ型
+ `[要素0, 要素1, 要素2, ..... ]` 
+ インデックス：各要素の番号（ゼロ始まり）
+ インデックスを指定することで、各要素が取り出せる
    ```python
    names = ['Oliver', 'Harry', 'George', 'Noah', 'Jack', 'Jacob', 'Leo', 'Oscar', 'Charlie', 'Muhammad']
    ```
    ```python
    >>> names 
    ['Oliver', 'Harry', 'George', 'Noah', 'Jack', 'Jacob', 'Leo', 'Oscar', 'Charlie', 'Muhammad']
    # インデックスの先頭はゼロ
    >>> names[0] 
    'Oliver'
    # インデックスを指定して要素を取得
    >>> names[2] 
    'George'
    # マイナスをつけると後ろから数えて要素を取得
    >>> names[-4] 
    'Leo'
    # 要素数以上のインデックスを渡すとエラー
    >>> names[100] 
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    ```
+ del 文を使うと、要素を削除できる。
+ もとに戻せない。（＝**破壊的変更**）
    ```python
    >>> del names[0]
    >>> names
    ['Harry', 'George', 'Noah', 'Jack', 'Jacob', 'Leo', 'Oscar', 'Charlie', 'Muhammad']
    ```    
+ スライスを使って複数の要素を取得
    + **メモ**：インデックスというのは要素の位置番号ではなく、**境目の番号**
    ```
    | Oliver | Harry | George | Noah | Jack | Jacob | Leo | Oscar | Charlie | Muhammad'
    ```
    + この `|` の番号がインデックス番号
    + インデックスが指定されたらその直後のデータを取ってくる決まりになっている。
    ```python
    # 先程破壊的変更を行ったので、もう一度データを入れ直した
    >>> names = ['Oliver', 'Harry', 'George', 'Noah', 'Jack', 'Jacob', 'Leo', 'Oscar', 'Charlie', 'Muhammad']
    # インデックス2〜6に囲まれたデータだけ取得
    >>> names[2:6]
    ['George', 'Noah', 'Jack', 'Jacob']
    # マイナスを使って指定も可
    >>> names[2:-3]
    ['George', 'Noah', 'Jack', 'Jacob', 'Leo']
    # こういう場合はエラーではなく、空のリストを返す
    >>> names[2:-10]
    []
    ```
+ 要素（リストの長さ）を数える関数
    + len関数
    ```python
    >>> len(names)
    10
    ```    
+ その他関数
    ```python
    >>> x
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> sum(x)
    45
    >>> max(x)
    9
    >>> min(x)
    0
    ```
+ 多次元も可
    ```python
    >>> girls = ['Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Isabella', 'Mia', 'Poppy', 'Ella', 'Lily']
    >>> names = [names,girls]
    >>> names
    [
        ['Oliver', 'Harry', 'George', 'Noah', 'Jack', 'Jacob', 'Leo', 'Oscar', 'Charlie', 'Muhammad'], 
        ['Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Isabella', 'Mia', 'Poppy', 'Ella', 'Lily']
    ]
    ```

## for文でループを使う
+ そもそも「**文**」とは
+ for や del のように、**引数を（）で引き取らないコード**と覚えてもらってOK
    ```python
    # 文
    del names[0]
    for x in names:
        処理を書く 

    # 関数
    print(names)
    range(20)
    ```
### ループはプログラミングで最も使うテクニック
+ ループとは同じ処理を大量に繰り返し行うこと
+ だいたいのプログラミング言語で for を使うことから、 for loop と呼ばれることも多い
+ Pythonは、並んでるデータはだいたい ループでまわせます。
+ 記述方法
    ```python
    for 変数 in シーケンス: # 最後の : が必ず必要
        繰り返す処理    # 必ずインデント（一段下げること）
    ```
+ 例：
    ```python 
    names = ['George', 'Noah', 'Jack', 'Jacob']
    for x in names:
        print(x)
    print("終わり")
    ```
    1. names を先頭から一つずつ取得してプリントしていく
    1. x に 0番目の `George` を代入、print(x)
    1. x に 1番目の `Noah` を代入、print(x)
    1. x に 2番目の `Jack` を代入、print(x)
    1. x に 3番目の `Jacob` を代入、print(x)
    1. names の最後まで終わったので for loop 終わり。
    1. 次の行を処理していく・・・
    
+ 変数のテクニック、「代入した値を更新する」を for loop でも使える

    ```python
    i = 0
    for x in [1,2,3,4,5]:
        i = i + x
    print(i)
    # 15
    ```
### range()関数
+ `range(n)`
+ 0~nのシーケンスを返す
+ たとえば、同じ言葉をｎ回繰り返してプリントしたい場合、
    ```python
    for i in range(5): # つまりこれは [0,1,2,3,4]
        print("Hello")
    # Hello
    # Hello
    # Hello
    # Hello
    # Hello
    ```
+ 繰り返し変数の `i` は使っていない。
+ このように使う必要が無い場合でも、シーケンスのデータをどこかに格納しないと for loop はまわせないので文法としておいているだけ。
+ **注意**： range() 関数はこのような使い方をするためのものではない。普通に作ったデータ（ここでは [0,1,2,3,4] ）を使って何かするために使う。

## if文で条件分岐をする

+ if 文に続く真偽値がTrueであった場合、その下のブロックを処理。Falseなら飛ばします。
+ もしくは、もし else文がかいてあったら、else文にを処理します。
    ```python
    >>> 0 == 0
    True
    >>> 0 == 1
    False

    >>> if 0 == 0: 
    ...     print("Yes")
    ... 
    Yes # if 文がTrueだったのでYesをプリントした
    >>> if 0 == 1:
    ...     print("Yes")
    ...     
        # if 文がFalseだったので何もしなかった
    >>> if 0 == 0:
    ...     print("YES")
    ... else: # false だったら else 文を処理する
    ...     print("No")
    ... 
    YES
    ```

### True / False を判断できるコード 
+ リストの中に要素があるか？
    ```python
    >>> names = ['George', 'Noah', 'Jack', 'Jacob']
    >>> "Noah" in names
    True
    >>> "taro" in names
    False
    ```    
+ リストは同値か？
    ```python
    >>> ['A', 'B', 'C'] == ['A', 'B', 'C']
    True
    >>> ['A', 'B', 'C'] == ['A', 'B', 'C', 'D']
    False
    ```
### if ~ elif ~ else
+ 条件が複数ある時は `elif` 文を使う
    ```python
    if 真偽値を問うコード:
        True なら処理する
    elif 真偽値を問うコード: ↑がFalseだった場合はココ
        True なら処理する
    elif 真偽値を問うコード: ↑がFalseだった場合はココ
        True なら処理する
        :
        :
        :
    else:
        上記の条件すべてがFalseだった場合、この処理をする
    ```
+ 注意：**上から順番に真偽値を確認し、Trueがでたらその後の処理は一切せずに飛ばす。**
    ```python
    >>> num = 10
    >>> if num > 100:
    ...     print("100以上だね")
    ... elif num > 50:
    ...     print("50以上だね")
    ... elif num > 30:
    ...     print("30以上だね")
    ... else:
    ...     print("ちっちゃいね")
    ... 
    ちっちゃいね # ずっとFalseだったので最後の else 文まで行き着いた
    ```

## 関数を使う
+ [組み込み関数 — Python 3.9.1 ドキュメント](https://docs.python.org/ja/3/library/functions.html)


## モジュールを使う