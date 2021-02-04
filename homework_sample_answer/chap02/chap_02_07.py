# 1. 0から9の数値リストを range関数を使って作成し、変数 x に代入して print
x = list(range(10))
print(x)

# 1. 10から20の数値リストを range関数を使って作成し、変数 y に代入して print
y = list(range(10, 21))
print(y)

# 1. p82 の複利計算の例を写経する。ただし、一回毎の元本を print するコードを途中に追加すること。
# 写経はパス

# 1. 上記の複利計算の利率を、0.01から0.10まで1%ずつあげて行った場合の各利率の結果を出す。
savings = 100
rates = range(1, 11)
print(rates)
for rate in rates:
    for i in range(15):
        savings += savings*rate / 100

    print(rate/100, savings)