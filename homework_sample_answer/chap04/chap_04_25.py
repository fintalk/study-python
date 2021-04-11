# 1. P198-199 をよく読んで、enumerate() を使うのがなぜ良いのかまとめてください。（enumerate() はPythonでは頻発する関数です。ぜひ使い方をマスターしましょう）
# pass

# 2. P199 enumerate() を使ったコードを写経して実行してください。ただし、 seq には下記のリストを代入してください

# seq = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# メモ： enumerateは、enumerate オブジェクトを返しますので、プリントしても中身はどうなっているのはよくわかりません。

# >>> enumerate(seq)
# <enumerate object at 0x7f528438cb40>
# 中身を見たい場合は、 list() 関数に渡せば中身を確認できます。

# >>> list(enumerate(seq))
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'), (5, 'F'), (6, 'G')]

# はい、了解

# 3. 以下のリストで、奇数番目の人だけプリントしてください。
names = ['Priscilla Gunthorp', 'Jammal Penrose', 'Tabby Volett', 'Joy De Bell', 'Yule Huggard', 'Kellina Braybrooke', 'Johannes Farherty', 'Anatola Greathead', 'Ingra Guiel', 'Farrell Zelake']

for i, name in enumerate(names):
    if i % 2 != 0:
        print(name)

