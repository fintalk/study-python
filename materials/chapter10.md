# 例外処理

## Pythonの例外処理

+ 例外とは、システム（プログラミング）の設計では想定していない問題が発生したこと。
+ Pythonでは、ユーザーが記述したコードやデータが想定とは違っていた場合、エラーを起こし、起こされたエラーの種類によって対応する例外を返す
+ 例外を発生させることで
    1. どこでエラーが起きているのかを特定できる
    1. 例外が発生した場合、どのように対応するのかコーディングできる
+ 例： 
    ```python 
    x = 1 2 3
    
    # File "<stdin>", line 1
    # x = 1 2 3 
          ^
    # SyntaxError: invalid syntax
    ```
    1. `x = 1 2 3` という文法間違い
    2. 文法間違いの時に返す `SyntaxError` をメッセージ "invalid syntax (文法まちがっとるよ) "とともに返す
+ もちろん例外もオブジェクト
    + ということは、例外にもメソッドやデータがブラブラぶら下がっている
    + そのオブジェクトを使って、どういう対応を行うかをコーディング出来る仕組み

### 例外の捕まえ方

+ 例外が起きるたびに実行が止まってしまっては困るので、例外が起きそうな箇所には例外が起きた時に対応出来るように記述する
+ 書き方：
    + 基本
        ```python 
        try:
            コードを記述
        except:
            上記コードの中でエラーが発生し例外が発生した場合のためのコード
        ```
    + ちょっと応用：エラーの種類によって実行するコード変更する。（分岐と言ったりします）
        ```python 
        try:
            コードを記述
        except SyntaxError:
            tryの中で文法エラーが発生し SyntaxError 例外が発生した場合のためのコード
        except ValueError:
            tryの中でデータが適切では無いなどのエラーが発生し ValueError 例外が発生した場合のためのコード
        except FileNotFoundError:
            tryの中で 存在しないファイル名を与えられたなどのエラーが発生し FileNotFoundError 例外が発生した場合のためのコード
        except: 
            tryの中で、上記の例外以外の例外が発生した場合のためのコード
        ```
    + エラーが発生しようとしまいと、最後には必ずやってほしいことを書きたい場合
        ```python 
        try:
            コードを記述
        except:
            上記コードの中でエラーが発生し例外が発生した場合のためのコード
        finally:
            例外が発生してもしなくても実行するためのコード
        ```

    + 組み込み例外はこちらを参照してください。
        + [組み込み例外 — Python 3.9.2 ドキュメント](https://docs.python.org/ja/3/library/exceptions.html?highlight=valueerror#ValueError)

#### 例

+ 問題: リストのなかにゼロが含まれているかどうか確認したい。リストは複数あってその全て確認したい。
+ 解答例
    ```python 
    import random 

    def myfunc(test_list):
        try:
            for i in test_list:
                10 / i
            print("ゼロはありませんでした！", test_list)
        except ZeroDivisionError:
            print("ゼロが見つかりました！", test_list)

    # -10 から 10 の数値をランダムに10個並べたリストを作成
    myfunc(random.sample(range(-10, 10), 10))
    myfunc(random.sample(range(-10, 10), 10))
    myfunc(random.sample(range(-10, 10), 10))
    myfunc(random.sample(range(-10, 10), 10))

    ```
+ ZeroDivisionError (ゼロでは割り算できませんという例外)が起きても、全部の myfunc関数を実行してくれる。
+ (こんな簡単な例なら if でいいんだけど、ま、例としてみて下さい)
    ```python 
    if 0 in list:
        ~~~
    ```

### **トレースバック（重要）**
+ コードは、インポートしたライブラリを使用したり、他のクラスや関数を使ったりする
+ エラーが発生した場合、どこのどのポイントでエラーが発生しているのかは、使っているライブラリや関数などをたどっていく必要がある
+ Pythonでエラーが起き、例外が発生した場合、Pythonが例外が発生する原因となった箇所まで一つ一つ確認して、どのファイルの何行目に当たるところが原因になっているということを返す機能がトレースバック
+ **このトレースバック（エラーメッセージ）をちゃんと読むかどうかが、Pythonが上達するかどうかの鍵**
    + エラーはずっともだよ！
+ でも残念ながら、かなり多くの人がエラーメッセージを読まないです。理由は
    + 長いから
    + 全部英語だから
+ でも、読めば解決方法が必ず書いてありますので必ず読んでください。
+ 読まない人は上達しないし、プログラミング下手です。
+ 読むにはコツがあります
    1. 一番最後の行をまず読む
    1. 読んでも意味がわからない場合は、自分が入力したところ以外の部分をコピペしてググる

#### トレースバック例
+ `materials/chapter10_aux/traceback.py` 
+ "spam://spam.com" という存在しないURLを開こうとしてエラーになり `urllib.error.URLError` 例外が発生した例
+ Pythonが、エラーが起きた行から、一つ一つたどって、どこで例外が発生したか追っています。
    ```python 
    from urllib import request 
    request.urlopen("spam://spam.com")

    """
    $ python materials/chapter10_aux/traceback.py 
    Traceback (most recent call last):
    File "materials/chapter10_aux/traceback.py", line 2, in <module>
        request.urlopen("spam://spam.com")
    File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 222, in urlopen
        return opener.open(url, data, timeout)
    File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 525, in open
        response = self._open(req, data)
    File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 547, in _open
        return self._call_chain(self.handle_open, 'unknown',
    File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 502, in _call_chain
        result = func(*args)
    File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 1421, in unknown_open
        raise URLError('unknown url type: %s' % type)
    urllib.error.URLError: <urlopen error unknown url type: spam>
    """
    ```
+ 最終行 "urllib.error.URLError: <urlopen error unknown url type: spam>" が例外発生源
+ もし、この最終行を読んで意味がわからない場合は、自分がインプットしたと思われるデータ（ここでは spam ）を除いた箇所をググる。ここではurllib.error.URLError: <urlopen error unknown url type:
+ はっきりした答えをグーグル先生が教えてくれることは期待できないけど、他の人の解決方法が多数でてくるのでそこからヒントを得る

### raise 文

+ 簡単に例外を発生させる方法
+ 例：四桁の数字で３でも５でも割り切れるものを見つけたら即座に教えてくれるようなコードを書きたい
    ```python 
    import random

    def fizzbuzz(i):
        if i%3 == 0 and i%5==0:
            raise ValueError(f"{i} は3でも5でも割り切れるぞ")
        return i 
            
    for i in random.sample(range(1000, 10000), 99):
        print(fizzbuzz(i))
    ```
+ こんなコード全然必要じゃないけど、例えばビットコインのマイニングをしていて、とうとう見つけた！！！600万円ゲットだー（今日現在価格（BTC/JPY）: 6,037,007円)！と思っても、ストップせずに数列がどこにいったかわからん、みたいなことにならないように raise して止めといてくれると助かります。（そういう使い方？）


### with 文

+ `chap04/chap_04_34.py` で、リストの内容をファイルに書き込むという宿題をだしました。(一部割愛)
    ```python 
    lines = [
        "いでや、この世に生れては、願はしかるべき事こそ多かめれ。",
        :
        :

        ]

    f = open("yoshida.txt", "w", encoding="UTF-8")
    f.writelines(lines)
    f.close()
    ```
+ この時、`open()` 関数で開いたファイルは、`.close()` メソッドを使って必ず閉じなくてはいけません、とお伝えしたと思います。
+ これがちょっとめんどくさいし、わすれがち。
+ これを with 文を使うと少し楽になります。
    ```python 
    with open("yoshida.txt", "w", encoding="UTF-8") as f:
        f.writelines(lines)
    ```
+ with 文を使うと、 `as 変数` で変数にファイルオブジェクトを代入します。
+ もし指定されたファイルが存在しないなどの例外が発生した場合は、下のブロックは実行されません。
+ 問題なく処理が終わった場合は、自動でファイルオブジェクトをクローズしてくれます。


## よく起こる例外と処理
+ ココの部分は教科書に説明のあるとおりです。