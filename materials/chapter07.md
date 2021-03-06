# クラスの継承と高度なオブジェクト指向機能


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

## クラスを継承する

+ `study-python/homework/chap07/chap_07_01.md` で説明します

## 特殊メソッドを利用する

+ 今回は飛ばしてOK

## 組み込み型を継承する

+ 今回は飛ばしてOK

## クラスの練習問題 

### その前におさらい

+ 辞書
    + 空の辞書を作成
    + 辞書にキーと値を入れる
    + 辞書からキーの値を取得
    + 辞書のキーだけをリストで取得
    + 辞書の値だけをリストで取得
   
### 成績表
+ 仕様： 生徒の成績をまとめて管理したい
+ メモ：これまで作った履歴書とか職務経歴書はインスタンスを作る時に、名前や住所などを初期値として渡していた。今回の成績表は、不特定多数の生徒の成績を記録していく真っ白なノートを作るイメージで作る。よってインスタンスを作る時は、データを挿入する辞書だけ内部につくって、その辞書にあとからデータを追加していく、という方法を取る
+ 作るクラス： `class RecordBook`
+ メソッド：    
    + `__init__`
        + 初期値：なし。
        + `records` 空の辞書
    + add_students(self, name)
        + 引数：name (文字列)、生徒の名前
        + records 辞書に追加する。その時すでに追加してあるかどうかを確認し、新規登録時だけ、キーワードを名前、値を空の辞書を辞書に追加する。
    + get_records(self)
        + records を返す
    + add_score(self, name, subject, score)
        + 引数：name (文字列)、subject(文字列)、 score (数値)
        + records 辞書の名前キーを探して、値として 辞書{`subject`: `score`} を追加する。
    + get_averate(self, subject)
        + 引数：subject (文字列)
        + records の中の全生徒の subjectの点数を取得し、平均を返す

+ インスタンス作成
    + RecordBook クラスのインスタンスを作成して、 `rb` に代入してください
+ データ追加
    + 以下の表の内容を rb に追加してください（平均は不要）

        Name|Math|Music|Gym|Language|平均
        ---|---:|---:|---:|---:|---:
        Cissy|81|97|69|58|76.25
        Inglebert|79|82|100|79|85
        Fred|74|67|94|62|74.25
        Ferdie|88|64|89|74|78.75
        Hermon|67|74|81|78|75


