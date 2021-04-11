# モジュール

モジュールとは、自分で作った関数やクラスをひとまとめにしておく `.py ファイル` のことです。これまで作ってきた python ファイルと何ら変わりませんが、一つ違いところは 

```bash
python mycode.py 
```
といった形で実行することを「目的にはしていない」ということです。

モジュールの目的は、「他のPythonファイルにインポートしてつかう」ことを目的にしています。よって、一度作ったモジュールは、色々なファイルにインポートして使うことができ、何度も同じようなコードを書かなくてもよい仕組みを提供しています。

> Python では、一度作ったコードを使い回すことをとても奨励しています。これはPythonの哲学の一つ Don't Repeat Yourself (DRY) として脈々とPythonistaに受け継がれる文化です。


## モジュールの書き方

基本的にこれまでの python ファイルと同じですが、ネーミングにはちょっと気をつかってください。
+ 数字では始めない
+ `.py` の `.` 以外のドットはNG
+ 一般的な名前は使わない
+ 小文字だけにする
+ ダメな例：
    ```bash
    1mycode.py
    mycode.dazo.py
    str.py
    import.py 
    MyFile.py
    ```

## モジュールをインポートして使用する

### import 

chapter 02 で Python に最初からついている組み込みモジュールをインポートしてコードを書きました。

例： `homework_sample_answer/chap02/chap_02_26.py`
```python 
import os 
os.mkdir("/tmp/hoge") # 作りたいディレクトリのパスを渡す
```
その他例：
```python 
import math 
print(math.pi) # 円周率を取得
print(math.pow(2,10)) # pow(x,y) x の y乗を取得
```

同様に自分で作った py ファイルもインポートすることができます。

+ `testmodule.py ` を作成
    ```python 
    # testmodule.py 
    a = 100
    ```
+ `testmodule.py` に定義している 変数 `a` にアクセス
    ```python
    import testmodule  
    print(testmodule.a) # . でつなぐ
    # >>> 100 
    ```

このように、`モジュール名.属性` (属性とは、変数、関数名、クラス名などモジュール内で定義している名前のこと)でアクセスすることができます。

### 階層

ただし、自作のモジュールの場合は注意が必要です。

インポートしたいファイルがどこに保存されているかで、インポート文の書き方が変わります。

1. 同じディレクトリ（ホルダ）に入っている場合
1. 1つ下のディレクトリに入っている場合
1. 1つ上のディレクトリに入っている場合
1. 違うディレクトリに入っている場合


#### 用意したディレクトリ構成

+ ディレクトリ構成とは、どのような構成でファイルやディレクトリを配置しているか説明する言葉です。
+ 通常、拡張子がついていない場合はディレクトリ、ついている場合はファイルを意味します。
+ `chapter08_aux/parent` ディレクトリ構成
 
```bash
# chapter08_aux の配下
└── parent
    ├── child
    │   ├── __init__.py 
    │   ├── module_c.py
    │   ├── module_e.py
    ├── child2
    │   ├── __init__.py
    │   └── module_d.py
    ├── __init__.py
    ├── module_a.py
    ├── module_b.py

```
+ `__init__.py` の設置
    + Pythonのコードを書くためのディレクトリを作成したら、何も考えずに空の `__init__.py` を設置してください。
    + 教科書P305に説明はありますが、今はよくわからないと思うし今わかる必要もないので、設置すればいいです。
+ 自動で作成される `__pycache__` について
    + `__pycache__` ディレクトリは、一度ディレクトリをインポートすると自動で生成されます。気にせずそのままにしておいてください。

#### ① 同じディレクトリ（ホルダ）に入っている場合

```bash
parent
├── child
│   └── module_c.py
├── module_a.py # ここと
└── module_b.py # ここ
```

+ `module_a.py` を `module_b.py` で使う
+ 両ファイルとも、`parent` ディレクトリの下にある

```python
# module_a.py
def i_am_a():
    print("私はmodule a にいます")

def hello_world_from_a(name):
    print(f"{name}さん、モジュールa から、こんにちは！")
```

```python 
# module_b.py

import module_a # 同じ階層にある時はファイル名だけでOk

module_a.i_am_a()
module_a.hello_world_from_a("たろう")

```

```bash
$ python module_b.py
# 私はmodule a にいます
# たろうさん、モジュールa から、こんにちは！
```

#### ② 1つ下のディレクトリに入っている場合

```bash
parent
├── child
│   └── module_c.py # ここと
├── module_a.py
└── module_b.py # ここ
```

+ `module_b.py` から、`child/module_c.py` に書いてある関数を呼び出す
+ module_c.py は module_b.py からみたら同じ階層にある child ディレクトリの下に入っている

```python 
# child/module_c.py
def i_am_c():
    print("私はCに入っています")

def hello_world_from_c(name):
    print(f"{name}さん、モジュールCからこんにちは！")
```

```python 
# module_b.py
import child.module_c  # 同じ階層にある childから表記。/ は . で表現

child.module_c.i_am_c()
child.module_c.hello_world_from_c("たろう")
```

#### ③ 1つ上のディレクトリに入っている場合

```bash
└── parent
    ├── child
    │   ├── module_c.py
    │   ├── module_e.py # ここで呼び出す
    ├── child2
    │   └── module_d.py
    ├── module_a.py # ここの関数を
    ├── module_b.py

```

+ `module_a.py` にかいてある関数を `child/module_e.py` で呼び出す
+ これは今はまた理解する必要はありませんし、必要になった時にコピペすればいいです。

```python
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import module_a
module_a.i_am_a()
```
+ `sys.path.append(os.path.join(os.path.dirname(__file__), '..'))` の解説
```python 
sys.path.append( # 以下のファイルを使えるようにする
    os.path.join( # 下2つをつなぐ
        os.path.dirname(__file__), # ファイル自身が入っているディレクトリ名をフルパスで取得
        '..' # 一つ上の階層を意味する
        )
    )
```


#### ④ 違うディレクトリに入っている場合
```bash
└── parent
    ├── child
    │   ├── __init__.py
    │   ├── module_c.py # ココに書いてある関数を
    ├── child2
    │   ├── __init__.py
    │   └── module_d.py # ここで使いたい

```
+ `child/module_c.py` に書いてある関数を `child2/module_d.py` で使いたい

```python 
# child2/module_d.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../child'))
import module_c

module_c.i_am_c()
```

## モジュールを実行したい

`homework/chap08/chap_08_03.md` の宿題としても出しましたが、ファイルに書いたコードをテストで実行したい時などモジュールを実行したいという時があります。そういう場合のための仕組みとして、ファイルの最後に、`if __name__ == "__main__":` という if 文を書くという方法があります。

```python 
if __name__ == "__main__":
    # 実行したい関数などを筆記
```

> 細かい説明はこちらに詳しく解説されています。 [Pythonのif __name__ == "__main__" とは何ですか？への回答 - Python学習チャンネル by PyQ](https://blog.pyq.jp/entry/Python_kaiketsu_180207)







