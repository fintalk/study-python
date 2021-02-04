# 以下のテーブルを参考にして、ヘッダーをキーにデータを値に持つ辞書を作って下さい。その際、first_name を変数名にして辞書を定義して下さい。
Terrijo = {'first_name': 'TerrijoDe', 'last_name': 'Cristofalotdecristofalo0@rakuten.co.jp2', 'email': 'Kim', 'address': 'Crossing'}
Dorotea = {'first_name': 'Dorotea', 'last_name': 'Iiannoni', 'email': 'diiannoni1@paypal.com', 'address': '252 Transport Pass'}
Wilfrid = {'first_name': 'Wilfrid', 'last_name': 'Clementson', 'email': 'wclementson2@princeton.edu', 'address': '18 2nd Crossing'}
Arley = {'first_name': 'Arley', 'last_name': 'Gammage', 'email': 'agammage3@shop-pro.jp', 'address': '61 Messerschmidt Point'}

# それぞれの辞書をプリントして下さい。
print(Terrijo)
print(Dorotea)
print(Wilfrid)
print(Arley)

# それぞれの辞書の email をプリントして下さい。
print(Terrijo["email"])
print(Dorotea["email"])
print(Wilfrid["email"])
print(Arley["email"])

# Arley の address を削除して下さい。
del Arley["address"]
print(Arley)

# 以下のデータをそれぞれの辞書追加して下さい
Terrijo["country"] = "Indonesia"
Dorotea["country"] = "Vietnam"
Wilfrid["country"] = "Vietnam"
Arley["country"] = "China"

print(Terrijo)
print(Dorotea)
print(Wilfrid)
print(Arley)
