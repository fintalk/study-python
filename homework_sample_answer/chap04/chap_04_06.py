# (おさらい)：オブジェクトとはなんですか？
# pass 

# (おさらい)：メソッドとはなんですか？
# pass 

# split() メソッドはどのような機能を持つメソッドですか？
# pass 

# 以下の文字列を split()メソッドを使ってリストに変換して下さい. ただし区切りはコンマです。

s1 = "Mikaela,Ashman,mashman0@auda.org.au,Female,250.94.95.131"
s2 = "Joleen,Deeny,jdeeny1@theglobeandmail.com,Female,100.31.91.185"

print(s1.split(","))
print(s2.split(","))

# (挑戦問題) 以下の文字列を、解答例と同じようなリストデータとしてプリントして下さい。ヒント：まずは改行文字 '\n' で split して、その後 for loop を使って一行ずつコンマで splitする。

names = """Emmery,253 Continental Street,Male
Lilian,95472 Sullivan Parkway,Female
Bevon,16090 Clove Alley,Male
Gaynor,41 Ronald Regan Hill,Female
Rick,5 Northland Junction,Male"""

for row in names.split("\n"):
    print(row.split(","))


# join() メソッドはどのような機能を持つメソッドですか？
# pass 

# 以下のリストを join を使って1つの文字列に変換して下さい
l = ['Emmery', '253 Continental Street', 'Male']
print("".join(l))

l = ['Emmery', '253 Continental Street', 'Male']
print(",".join(l))

# P171の余分な空白を削除する、を写経して実行して下さい
# pass 

# P171の分割してじゃら余分な空白を削除する、を写経して実行して下さい
# pass 

