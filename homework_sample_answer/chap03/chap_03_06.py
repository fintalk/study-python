# P128 setとリスト

# set と list の違いは何ですか？
# 重複するデータを持つことが出来るのがList
# 重複するデータを持つことが出来ないのが set

# set と list どちらでもできることは何ですか？
# for でループ

# P129 のリストをsetに変換する，を写経して実行して下さい
# パス

# 以下の list を set に変換して下さい
# l1 = ['A', 'A', 'B', 'C', 'D', 'E', 'E']   
l1 = ['A', 'A', 'B', 'C', 'D', 'E', 'E']   
print(set(l1))

# P130 の要素の検索とsetの比較を写経して実行して下しさい
# パス

# 以下のセットを使って下記の問題を解いてください。
set_a = {'Levey', 'Cari', 'Luis', 'Kary', 'Everett', 'Goldia', 'Amory', 'Reine', 'Daveen', 'Boot'}
set_b = {'Cari', 'Belle', 'Levey', 'Everett', 'Lanny', 'Adrea', 'Boot', 'Celka', 'Helaina', 'Daveen'}

# set_a だけにしか入っていない名前を探し"only in dict a" をプリントする
for name in set_a - set_b:
    print(name, " only in dict a")

# set_b だけにしか入っていない名前名前を探し，"only in dict b" をプリントする
for name in set_b - set_a:
    print(name, " only in dict b")

# 両方に入っている場合は，"both a and b" をプリントする
for name in set_b & set_a:
    print(name, " both a and b")
