# クラスの練習問題
## その前におさらい

# 辞書のおさらい
# 1. 
# 空の辞書dを作成してください
d = {}

# 2.
#  d に キーに taro 値に空の辞書を入れてください
d["taro"] = {}
# 3. 
# 続けて、d に キーに hanako 値に「空の辞書」を入れてください
d["hanako"] = {}

# 4. 
# 辞書 d をプリントしてください。このようになっているはずです。
print(d)
# >>> d
# {'taro': {}, 'hanako': {}}

# 5.
# 辞書dのキー taro の値である空の辞書に、キー "Math" 値 50 を追加してください
d["taro"]["Math"] = 50

# 6. 
# 辞書 d をプリントしてください。このようになっているはずです。
print(d)
# >>> d
# {'taro': {'Math': 50}, 'hanako': {}}

# 7.
# 辞書dのキー hanako の値である空の辞書に、キー "Math" 値 70 を追加してください
d["hanako"]["Math"] = 70
print(d)
# 8.
# 同様に、taro の "Music" を 100, hanako の "Music" を 40 を追加してください
d["taro"]["Music"] = 100
d["hanako"]["Music"] = 40

# 9.
# 今の d をプリントしてください。このようになっていれば正解です。
print(d)
# >>> d
# {'taro': {'Math': 50, 'Music': 100}, 'hanako': {'Math': 70, 'Music': 40}}


# 10. 
# 辞書の値だけをリストで取得してください。以下のようなリストが取得できれば正解です
# dict_values([{'Math': 50, 'Music': 100}, {'Math': 70, 'Music': 40}])
print(d.values())
# 11. 
# 辞書 d から、taro の Music の点数を取得してください
print(d["taro"]["Music"])
# 12.
# 以下の辞書から、"Math" の値を取得してください
x = {"Math": 30, "Music": 40, "Language": 50}
print(x["Math"])

# 13. 
# 辞書d の値だけのリストは、要素が辞書のリストでした。ではそのリストを使って、 "Math"の値だけ取得してリストで返してください。このようなリストを取得できれば正解です
# [50, 70]
d["taro"]["Math"],["hanako"]["Math"])

for i in d.values(): #aは１個ずつのMathになる
    print(i["Math"])
    
[i["Math"] for i in d.values()] 



