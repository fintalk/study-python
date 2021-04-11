# if を含むリスト内包表記の記法
# [式 for 繰り返し変数 in シーケンス if 条件式]
# を for 文で書き換えると
# a_list = list() # 空のリスト
# for 繰り返し変数 in シーケンス:
#     if 条件式:
#         a_list.append(繰り返し変数を渡して演算した式)
# では、
# [x * 10 for x in [1,2,3,4,5] if x > 3]
# を fot 文で書き換えるとどのようになりますか？

l1 = list()
for x in [1,2,3,4,5]:
    if x > 3:
        l1.append(x)
print(l1)

# range(10) の要素一つずつに対して, もし要素が奇数であれば100を足したリストを、for 文と リスト内包表記で書いてください。どちらの答えも
# [101, 103, 105, 107, 109]

l2 = list()
for x in range(10):
    if x % 2 != 0:
        l2.append(x+100)
print(l2)

print([x + 100 for x in range(10) if x % 2 != 0])

# 以下のリストの要素一つずつに対して Pで始まる国だけのリストを、for 文と リスト内包表記で書いてください。
# どちらの答えも
# ['Peru', 'Portugal', 'Poland']

countries = ['Peru', 'Serbia', 'Portugal', 'Finland', 'Ireland', 'Indonesia', 'Ukraine', 'Poland']
l3 = []
for country in countries:
    if country.startswith("P"):
        l3.append(country)
print(l3)

print([c for c in countries if c.startswith("P")])

# P238 の 数字以外を排除してリストを作る例、を写経して実行してください。
# pass 

# P238 の 数字以外を排除してリストを作る例、をfor文に書き換えてください。
str_speeds = "38 42 20 40 a1 39"
speeds = [int(s) for s in str_speeds.split() if s.isdigit()]
speeds_2 = list() 
for s in str_speeds.split():
    if s.isdigit():
        speeds_2.append(int(s))
print(speeds)
print(speeds_2)