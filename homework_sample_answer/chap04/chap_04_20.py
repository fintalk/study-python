# 1. P191 の 組み込み関数dict()を使ってディクショナリを作る例を3つ実行して全て，{'one':1, 'two':2} が返ってくることをプリントして確認して下さい
# pass 

# 2. 同様にdict()関数を使って，以下の出力になるように3つのコードを書いて実行して下さい
#  {"first_name": "Lynnell", "last_name": "Strain", "country": "Brazil"}

print("2-1 ディクショナリのコピー")
print(dict({"first_name": "Lynnell", "last_name": "Strain", "country": "Brazil"}))

print("2-2 キーと値のシーケンス")
print(dict([
    ["first_name", "Lynnell"],
    ["last_name", "Strain"],
    ["country", "Brazil"],
]))

print("2-3 キーワード引数")
print(dict(first_name="Lynnell", last_name="Strain", country="Brazil" ))


# 3. P192 の update()メソッドによるディクショナリの連結を写経して実行して下さい
# pass 

# 4. 以下の辞書を使って問題を解いて下さい
name = {"first_name": "Ronnie", "last_name": "Fuller", "country": "China",}
data = {"code": "CN",  "wage": "$6.75"}
another = {"first_name": "Casie", "last_name": "Bradforth", }

print("4-1")
name.update(data)
print(name)

print("4-2")
print(name.keys())

print("4-3")
name.update(another)
print(name)

# 5. 今 name をプリントすると，first_name と last_name は元の name ではなくなっています．なぜですか？
# pass 

# 6. 空のリストを作って，変数 d に代入して下さい
d_list =list()

# 7. d に以下のデータを入れて下さい. ただしヘッダーがキーワードとする．
table = """Harald	Ryhorovich	Somalia	$0.33
Alice	Davenell	China	$0.13
Chanda	Maior	Philippines	$0.53
Justen	Pynn	Indonesia	$4.49
Olga	Stammer	Russia	$9.50"""

# table をリストに変換する
table_list = list()
for row in table.split("\n"):
    table_list.append(row.split("\t"))

# アンパックを使って変数に代入する
for f, l, c, w in table_list:
    d_list.append(dict(first_name=f, last_name=l, country=c, wage=w))

print(d_list)