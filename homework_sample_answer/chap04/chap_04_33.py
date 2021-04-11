# 1. 枕草子.txt を read() して変数 s に代入してプリントしてください
# ここのパスはそれぞれ皆さん違い増すので 04_32の説明に従って書いてくだい

makura_path = "study-python/data/枕草子.txt"

s = open(makura_path).read()
print(s)

# 2. 枕草子.txt を readline() して変数 t に代入してプリントしてください
t = open(makura_path).readline()
print(t)

# 3. 枕草子.txt を readline() して変数 l に代入してプリントしてください
l = open(makura_path).readlines()
print(l)

# s ,t, l ではそれぞれ何が違いますか？
# pass 

# P224 の テキストファイルを行に分割する、を 枕草子.txt で実行して下さい。（P223に、close() メソッドを呼び出さなくてもあまり問題は置きないはずです、とありますが、ファイルの大小関係なく close() メソッドは必ず書くようにして
# pass 



