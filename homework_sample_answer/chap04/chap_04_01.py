# メソッドとは何ですか？
# pass 

# 関数とメソッドの違いを説明して下さい
# pass 

# P153 のリストのインデックスを返す関数 find_indexの定義、と、find_index() を使った例を写経して実行して下さい
# pass

# P152 のindex()メソッドを使った例、を写経して実行して下さい
# pass 

# P155 の Fig に掲載されているメソッドはそれぞれどういうメソッドなのか、下記のリストに対して実行し解答してください。（公式ドキュメントを参照して下さい）
name_list = ['Aland', 'Dari', 'Lorelle', 'Debbie', 'Jermaine', 'Royal', 'Tiena', 'Adelice', 'Vivyanne', 'Rosco']

# 要素の index 番号を返す
print(name_list.index("Royal"))

# list を後ろから並べ直す（破壊的変更で）
name_list.reverse()
print(name_list)

# list をアルファベット順にソートする（破壊的変更で）
name_list.sort()
print(name_list)

# index 番号に当たる要素を削除（破壊的変更で）
name_list.pop(0)
print(name_list)

# 要素を最後に追加（破壊的変更で）
name_list.append("Hanako")
print(name_list)

# 別のリストをつなげる
name_list.extend(["Taro", "Jiro"])
print(name_list)