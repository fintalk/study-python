# 標準ライブラリを使う

## 標準ライブラリとは

+ Pythonをインストールしたら使えるライブラリやパッケージ
    + ライブラリ、パッケージ：目的が似ているメソッドやクラスをひとまとめにしたもの
+ 今までとの違い
    + 今まで使ってきた関数
        ```python
        sum([1,2,3,4,5])
        x = list()
        ```
    + 標準ライブラリを使う ＝ `import` して使う
        ```python
        import random
        import math 

        # 1~10からランダムに整数を一つ返す
        random.randint(1,10)
        # 5

        # xのy乗を返す
        math.pow(10, 2)
        # 100.0
        ```
+ [Python 標準ライブラリ — Python 3.9.2 ドキュメント](https://docs.python.org/ja/3.9/library/index.html)を見てもわかるように大量にある
+ かつ、しっかりとテストを行ってあるので安心して使える
+ 難点：公式ドキュメントは、言葉が難しい。プログラミングのことだけでなく、コンピューターの知識が無いと理解出来ないことがおおい

### import 文の書き方

1. **import ライブラリ名**
    ```python
    # インポート
    import random
    import math

    # ライブラリ名.メソッド名() で実行
    random.randint(1,10)
    random.choice(["A", "B", "C"])
    math.pow(10, 2)
    ```
    + 利点：インポートしたライブラリに入っているメソッドを一括でインポート出来る
    + 欠点：コードが長くなる
1. **from ライブラリ名 import 使いたいメソッド**
    ```python
    # ライブラリから使いたいメソッドのみインポート
    from random import randint, choice 
    from math import pow

    # メソッド名（）で実行
    randint(1,10)
    choice(["A", "B", "C"])
    pow(10,2)

    ```
    + 利点：使いたいメソッドだけインポートすることでコードがスッキリする
    + 欠点：使いたいものを一つ一つをインポートしなくてはいけない（同じライブラリに入っている場合は、コンマでつなげれば良い）。なんのライブラリのメソッドなのか分かりづらい。同じ名前の関数を同じファイル内に作れない



## サードパーティライブラリ

+ Pythonユーザーが作ったライブラリ
+ 個人でちょこっと作ったライブラリや、Googleといった会社規模がつくったライブラリなど大量にある
+ インストールして使える
+ インストール方法はおおまかに二つ
    + [PyPI · The Python Package Index](https://pypi.org/)
    + [Anaconda.org](https://anaconda.org/)

### サードパーティライブラリをインストールする時に絶対に気をつけること
+ 必ず仮想環境を作る
+ 必ず仮想環境を作る
+ 必ず仮想環境を作る
+ 仮想環境は以下のスタイルで作ると幸せ
    1. プロジェクト毎（←コッチがオススメ）
    1. Pythonのバージョン毎
+ この章ではサードパーティライブラリは使いませんので別章で行います


# 正規表現

+ Regular Expression
+ 文字列のパターンを表現する方法
+ いつ使うの？
    + 検索や置換、特定のルールを伴う抽出
    + パスワードの条件クリア
    + メールアドレスの不正な入力値
    + などなど・・・
+ 例：**数限りなく**あります（参照：[正規表現サンプル集](https://www.megasoft.co.jp/mifes/seiki/meta.html)）

表したいパターン| 記法例（こんなのホント一部）
---| --- 
半角英数字3つ | "\w\w\w" "\w{3}" 
半角英数字1つ以上かつできるだけ少なくマッチ| "\w+?"
任意の文字１つ | "."
タブ文字 | "\t" 
ABC もしくは XYZ | "[ABC \| XYZ]" 
大文字アルファベット1文字 | "[A-Z]+"
Aを含まない|[^A]
メールアドレス | [\w.\-]+@[\w\-]+\.[\w.\-]+ 



## Pythonでの正規表現の使い方

1. まずは `re` モジュールをインポート。(re = regular expression)
1. そしていずれかの方法をとる
    1. `re.comple()`メソッドで、正規表現オブジェクトを作成して、そのメソッドを使う
    1. `re` モジュールに定義されているメソッドを使う

例：
1.  `re.comple()` オブジェクトを作成して、そのメソッドを使う方法
    ```python
    # まずは re をインポート
    import re

    # パターンをコンパイル
    # 郵便番号 (数字3文字-数字4文字) のパターンをコンパイル
    regex = re.compile(r"\d\d\d-\d\d\d\d")

    # このオブジェクトのメソッドを使う
    # .match() メソッド で引き取った文字列がパターンにマッチしているか確認

    # マッチしない場合、Noneを返す
    regex.match("shinsei-taro")
    >>> None

    # マッチした場合、 <match object> を返す
    regex.match("100-0011")
    >>> <re.Match object; span=(0, 8), match='100-0011'>
    ```
    + パターン以外のところ（ここではハイフン）はそのまま書いてよい
    + `regex` はしばしば使用される変数名

1. `re` モジュールに定義されているメソッドを使う

    
    ```python
    # まずは re をインポート
    import re

    re.match(r"\d\d\d-\d\d\d\d", "shinsei-taro")
    >>> None 
    re.match(r"\d\d\d-\d\d\d\d", "100-0011")
    >>> <re.Match object; span=(0, 8), match='100-0011'>
    ```

要は、
1. 先に正規表現パターンオブジェクトを作っておくか（`re.comile()`)
1. 正規表現を、メソッドの引数として渡すか

どっちかです。好きなほうを使ってください。

## 具体例：

### 1. `re.comple()` オブジェクトを作成して、そのメソッドを使う方法

1. 正規表現オブジェクトを作って、
1. 対象文字列を、オブジェクトが持つメソッドに渡す

```python
# re モジュールをインポート
>>> import re 

# 数字-数字 の正規表現オブジェクトを作成
>>> regex = re.compile(r"\d+-\d+")
# 対象文字列
>>> address = "1-4-1 Kabuki-cho, Shinjuku-ku Tokyo 160-8484"


#  .findall(対象文字列): 対象文字列の中でパターンにマッチする文字列を全部取得
>>> regex.findall(address)
['1-4', '160-8484']

# .split(対象文字列) : 対象文字列の中でパターンで文字列を分割
>>> regex.split(address)
['', '-1 Kabuki-cho, Shinjuku-ku Tokyo ', '']

# .sub(置換用文字列, 対象文字列): パターンにマッチした文字列を、置換用文字列に変換
>>> regex.sub("QQQQQ", address)
'QQQQQ-1 Kabuki-cho, Shinjuku-ku Tokyo QQQQQ'
```

### 2. `re` モジュールに定義されているメソッドを使う

正規表現オブジェクトを作らずに、 re モジュールが持つメソッドを使い、そのメソッドにパターンを渡す
出来ることは同じ

```python
import re

# re.findall(パターン, 対象文字列)：
>>> re.findall(r"\d+-\d+", address)
['1-4', '160-8484']

# re.split(パターン, 対象文字列): 
>>> re.split(r"\d+-\d+", address)
['', '-1 Kabuki-cho, Shinjuku-ku Tokyo ', '']

# re.sub(パターン, 置換用文字列, 対象文字列)
>>> re.sub(r"\d+-\d+", "QQQQQ", address)
'QQQQQ-1 Kabuki-cho, Shinjuku-ku Tokyo QQQQQ'
``` 

## システムパラメータを取得操作する sys

今回は飛ばしますが、いつか必要になるのでその時に行います

## ファイル、プロセスなどのOS依存の情報を取得操作する os 

### ファイルシステムとは
- [ファイルシステム - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0)
- 簡単に言ってしまうと、PCの中のデータを保存したり検索したりするためのシステム
- ディレクトリ階層構成もこのファイルシステムで管理されている
- パソコンのユーザーはグラフィカルなUIを使ってファイルやホルダをクリックすることでデータを見ることが出来るが、全く同じことをターミナル上で行うことができる
- プログラミングを行う場合はそのターミナル上での操作方法の知識が要求される。

#### ディレクトリのコマンド練習

1. vscode で terminal を開いて下さい
1. 以下のコマンドを叩いて下さい

命令内容|Windows|Max/Linux|memo
---|---|---|---
カレントディレクトリパスを表示|`cd`|`pwd`|
カレントディレクトリ内にあるファイルやディレクトリを表示|`dir`|`ls -l`|
カレントディレクトリ配下にあるディレクトリ構成を表示|`tree /F`|`tree` | Mac/linux は インストールが必要。 <br> `$ brew install tree` / `$ apt-get install tree` など
ターミナルの表示内容をクリア|`cls`|`clear`|
ディレクトリ移動|`cd 移動したいディレクトリ`|`cd 移動したいディレクトリ`|


### カレントディレクトリ（ワーキングディレクトリ）
- [カレントディレクトリ - Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%88%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA)
- `cd` / `pwd` で表示されたディレクトリ
- **現在どのディレクトリでターミナルを実行しているか** を返す
- カレントディレクトリの配下に**ある**ファイルやディレクトリにアクセスすることが出来る
- カレントディレクトリの配下に**ない**ファイルやディレクトリにアクセスする場合は、現在作業しているディレクトリからアクセスしたいファイル等がどこにあるのかを明示する必要がある。（詳細はあとで）

命令内容|Windows|Max/Linux|memo
---|---|---|---
カレントディレクトリに格納されているディレクトリへ移動|`cd ./ディレクトリパス`|`cd ./ディレクトリパス`| <font color="red">重要</font>： **`.` はカレントディレクトリを意味**
カレントディレクトリの1つ上のディレクトリへ移動|`cd ..`|`cd ..`| <font color="red">重要</font>：**`..` は1つ上のディレクトリを意味**
カレントディレクトリの2つ上のディレクトリへ移動|`cd ../..`|`cd ../..`| 

#### カレントディレクトリからの移動コマンド練習
1. ターミナルを開いて下さい
1. カレントディレクトリ内にあるファイルやディレクトリ一覧を表示して下さい
1. 表示されたディレクトリの1つに移動して下さい
1. 移動した先のファイルやディレクトリ一覧を表示して下さい
1. 2つ上のディレクトリへ移動して下さい
1. 今いる場所から3で移動したディレクトリに一気に移動して下さい
1. 今いる場所から最初（1でターミナルを開いた場所）のディレクトリへ戻って下さい

### カレントディレクトリから移動する(今日の最難関です)

現在、`misc` ディレクトリはこのような階層です。

```bash
$ tree misc/
misc/
├── data.py
├── dir_a
│   └── hoge
└── dir_b
    └── moge
        └── test.txt
```

1. まず `hoge` に移動して下さい。
1. `hoge`から`moge`へ移動するには
    - `../../dir_b/moge/`
    - **`..` はカレントディレクトリを意味**なので一旦上に上がって（dir_a）、もう一段上がって（misc）、その下の `dir_b / moge` に入るという意味です
1. カレントディレクトリパスを表示を表示して下さい
1. `moge`から`hoge`へ移動に移動して下さい
1. カレントディレクトリパスを表示を表示してhogeに入っているか確認して下さい


### ルートディレクトリ

- windows: `echo %HOMEPATH%` とコマンドを叩くと返るパス
- MacOS / Linex : `cd ~` とコマンドを叩くとルートディレクトリへ移動できる。そこで `pwd` すればよい。

### トップディレクトリ

- プロジェクトなどの一番上のディレクトリ
- この勉強会資料でいう `study-python` ディレクトリのこと

### 相対パスと絶対パス
- プログラミングでは絶対覚えなくてはいけない規則
- 絶対パス（フルパス）：ルートディレクトリからのファイルやディレクトリのパスのこと。`cd` / `pwd` で得たディレクトリパスは絶対パス
- 相対パス：現在いるホルダから見て目的のファイルやディレクトリはどこの位置あるかを示したパス
- どちらも**アクセスしたいファイル等がどこにあるのかを明示する方法**

#### 相対パスと絶対パスのコマンド練習

1. このファイル `chapter11.md` の絶対パスと相対パスをVSCodeの昨日で取得してみましょう
    - ![](https://i.imgur.com/1WzETHL.jpg)
1. 画像の方法で、`パスのコピー`（絶対パス）と、`相対パスをコピー`を取得しそれぞれメモして下さい。
1. まずは**絶対パスを使って**下記のコマンドを叩いて下さい

    命令内容|Windows|Max/Linux|memo
    ---|---|---|---
    ファイルの中身を表示|`type ＜ファイルへのパス＞`|`cat ＜ファイルへのパス＞`|

1. ターミナルの表示内容をクリアしてください
1. ターミナルで、`study-python` ディレクトリまで移動して下さい
1. `cd` / `pwd` を実行して、カレントディレクトリが`study-python` であることを確認してください。
1. そこから**相対パスをつかって**ファイルの中身を表示してください
1. ターミナルで、`chapter11.md`のファイルが存在するディレクトリまで移動して下さい
1. `dir` / `ls -l` で`chapter11.md`のファイルが存在するか確認して下さい
1. そこで ファイルの中身を表示してください。ただし、この場合は**ファイルが存在するディレクトリ＝カレントディレクトリ**ですので、**ファイルへのパスは <./ファイル名>** でOKです
1. misc/dir_a/hoge に移動して下さい
1. カレントディレクトリパスを表示を表示してhogeに入っているか確認して下さい
1. 今の状態で、`dir_b/moge/test.txt ` の 中身を表示して下さい。
 



#### 相対パス の存在理由

トップディレクトリ以下の階層構成が変わらないのであれば、トップディレクトリのを移動させたとしてもパスが変わらないから便利

### ディレクトリ、ファイル操作

- ホルダでファイルを作成、削除、Rename、コピー、コピペ出来るように、ターミナルでも出来る

#### ディレクトリ、ファイル操作練習

1. terminal で `study-python/misc` へ移動して下さい
1. 命令一覧

    命令内容|Windows|Max/Linux|memo
    ---|---|---|---
    ディレクトリ作成|`mkdir <ディレクトリパス>`|`mkdir <ディレクトリパス>`| 
    ディレクトリ削除|`rmdir <ディレクトリパス> /s`|`rm -r <ディレクトリパス>` | win：中にファイルがある場合は確認が入る
    ディレクトリRename|`move <旧ディレクトリパス> <新ディレクトリパス>` |`mv <旧ディレクトリパス> <新ディレクトリパス>` |どちらもmove
    ディレクトリ移動|`move <旧ディレクトリパス> <新ディレクトリパス>` |`mv <ディレクトリパス> <移動先ディレクトリパス>` |どちらもmove。<br>パソコンにとって移動しているのではなくてパスの変更 
    ファイル作成|`echo "" > <新規ファイルパス>`|`touch <新規ファイルパス>`|windowsには新規ファイル作成用コマンドはない。echo を利用する。
    ファイル削除|`del <ファイルパス>`|`rm <ファイルパス>`|ゴミ箱に移動するわけではない。完全削除。
    ファイルRename|`move <旧ファイルパス> <新ファイルパス>` |`mv <旧ファイルパス> <新ファイルパス>` |どちらもmove
    ファイル移動|`move <旧ファイルパス> <新ファイルパス>` |`mv <旧ファイルパス> <新ファイルパス>` |どちらもmove
    ファイルコピー|`copy <旧ファイルパス> <新ファイルパス>` |`cp <旧ファイルパス> <新ファイルパス>` |

    - `echo "" > <新規ファイル>` 空のファイルを作る（`""` は何も書かないことを意味している）
    - `echo "ほげほげ" > <新規ファイル>` 「ほげほげ」と書き込んだファイルを作る

1. `study-python/misc` で、自分の名前でディレクトリを新規作成して下さい。
1. 今作ったディレクトリを削除して下さい
1. もう一度自分の名前でディレクトリを新規作成して下さい。
1. `<自分の名前_2>` でディレクトリを新規作成して下さい。
1. `<名前_2>` を、`<名前>` の下に移動させて下さい
1. `tree` コマンドを実行して、現在のディレクトリ/ファイル構成がどのようになっているか確認して下さい。
1. `<名前_2>` の下に、`<test.txt>` を新規作成して下さい
1. `<名前_2/test.txt>` のコピーを `<名前_2/test.csv>` というパスで作成して下さい
1. `tree` コマンドを実行して、現在のディレクトリ/ファイル構成がどのようになっているか確認して下さい
1. `<名前_2/test.txt>`を、`<名前_2/hoge.txt>`にrenameしてください

### pythonを使って同じことをする os モジュール

今までやってきたファイルやディレクトリの操作は、Pythonの os モジュールを使うこと同じ操作が行えます。
ここまで見てきたように、OSによってコマンドが少しずつ違ったりしますが、その違いもPythonでは1つにまとめてくれていて便利です。

まずは ターミナルから python をよびだし、インタラクティブシェルを立ち上げます。

```python
import os 
```

命令内容|Windows|Max/Linux|python
---|---|---|---
カレントディレクトリパスを表示|`cd`|`pwd`|`os.getcwd()`
カレントディレクトリ内にあるファイルやディレクトリを表示|`dir`|`ls -l`|`os.listdir(".")` 
ディレクトリ移動|`cd 移動したいディレクトリ`|`cd 移動したいディレクトリ`|`os.chdir("移動したいディレクトリへのパス")`
ディレクトリ作成|`mkdir <ディレクトリパス>`|`mkdir <ディレクトリパス>`| `os.mkdir("<ディレクトリパス>")` <br> `os.makedirs("<ディレクトリパス>")` 複数階層可
ディレクトリ削除|`rmdir <ディレクトリパス> /s`|`rm -r <ディレクトリパス>` | `os.rmdir("<ディレクトリパス>")`  <br>  `os.removedirs("<ディレクトリパス>")` 複数階層可
ディレクトリRename|`move <旧ディレクトリパス> <新ディレクトリパス>` |`mv <旧ディレクトリパス> <新ディレクトリパス>` |`os.rename(mv <旧ディレクトリパス> <新ディレクトリパス>)`
ディレクトリ移動|`move <旧ディレクトリパス> <新ディレクトリパス>` |`mv <ディレクトリパス> <移動先ディレクトリパス>` |`os.rename(mv <旧ディレクトリパス> <新ディレクトリパス>)`
ファイル作成|`echo "" > <新規ファイルパス>`|`touch <新規ファイルパス>`|`open(<新規ファイルパス>, "w", encoding="UTF-8")` chap10 参照
ファイル削除|`del <ファイルパス>`|`rm <ファイルパス>`|`os.remove(<ファイルパス>)`
ファイルRename|`move <旧ファイルパス> <新ファイルパス>` |`mv <旧ファイルパス> <新ファイルパス>` |`os.rename( <旧ファイルパス> <新ファイルパス>)`
ファイル移動|`move <旧ファイルパス> <新ファイルパス>` |`mv <旧ファイルパス> <新ファイルパス>` |`os.rename( <旧ファイルパス> <新ファイルパス>)`
ファイルコピー|`copy <旧ファイルパス> <新ファイルパス>` |`cp <旧ファイルパス> <新ファイルパス>` |`os` モジュールではなく `shutil` モジュール。<br> `shutil.copyfile(<旧ファイルパス> <新ファイルパス>)`

#### その他のメソッドで良く使うメソッド

- ファイルが存在するか確認
    ```python
    os.path.exist("存在を確認したいファイルへのパス")
    ```
- パスを作成。OSによってパス記述方法が違うのでそれを考慮して作成してくれる。
    ```python
    os.path.join("./", "hoge", "moge") 
    ```

- パスをディレクトリ部分とファイル部分で分割する。ディレクトリパスを渡した場合は、一番下のディレクトリとそれより上のディレクトリというリストを返す
    ```python 
    os.path.split("ファイルパス")
    ```

- パスのディレクトリ部分だけ取得。ディレクトリパスを渡した場合は、1つうえのディレクトリまでのパス
    ```python 
    os.path.dirname("ファイルパス")
    ```

#### pythonを使って同じことをする os モジュール 問題

1. ターミナルで、`study-python` へ移動して下さい
1. python インタラクティブシェルを立ち上げて下さい
1. カレントディレクトリパスを表示させて下さい
1. カレントディレクトリ内にあるファイルやディレクトリを表示して下さい
1. `misc` ディレクトリ内にあるファイルやディレクトリを表示して下さい
1. `misc` ディレクトリ内の自分のディレクトリにあるファイルやディレクトリを表示して下さい
1. `misc` ディレクトリ内の自分のディレクトリに移動して下さい
1. 現在のカレントディレクトリパスを取得して下さい
1. そこで、新規ファイル "test.csv" を作成して下さい
1. "test.csv"が存在するかどうか確認して下さい
1. 現在のカレントディレクトリパスに続けて、 "text.txt" という架空のファイルパスを取得して下さい（パスを取得するだけ。実際のファイルを作るわけではない）
1. ⇑の方法と open 関数を組み合わせて、"text.txt"を作成してみてください
1. chapter11.md のフルパスを、最初に行ったVSCode の機能を使って取得し、ディレクトリ部分とファイル部分でパスを分割して下さい


## 数学関数を利用する math random

- 数学で使う、三角関数や対数演算など
- `homework/chap11/chap_11_10.md` で解説します

## インターネット上の情報を取得する urllib

- サードパーティのライブラリを使うことが多いので、実際に使うメソッドは限られている
- `homework/chap11/chap_11_11.md` で解説します



