c1 = {'Indonesia', 'Philippines', 'Nigeria', 'Poland', 'South Africa', 'Afghanistan', 'Ukraine', 'Portugal', 'Vietnam'}
c2 = {'Greece', 'Indonesia', 'Czech', 'France',  'China', 'Brazil', 'Republic', 'Netherlands'}

# 上記2setを使って，セットのオブジェクトメソッドと演算子のそれぞれで和集合をプリントして下さい
print(c1 | c2)
print(c1.union(c2))

# 上記2setを使って，セットのオブジェクトメソッドと演算子のそれぞれで交差をプリントして下さい
print(c1 & c2)
print(c1.intersection(c2))

# 上記2setを使って，セットのオブジェクトメソッドと演算子のそれぞれで差集合をプリントして下さい
print(c1 - c2)
print(c2 - c1)
print(c1.difference(c2))
print(c2.difference(c1))

# 上記2setを使って，セットのオブジェクトメソッドと演算子のそれぞれで対象差をプリントして下さい
print(c1^c2)
print(c1.symmetric_difference(c2))

# 上記2setを使って，c1 に c2 を追加して下さい
for country in c2:
    c1.add(country)

print(c1)

# c1からベトナムを削除して下さい
c1.remove("Vietnam")
print(c1)

# c2 にベトナムを追加して下さい
c2.add("Vietnam")
print(c2)
