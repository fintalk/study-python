# P235〜237を読んでください
# pass 

# P236の リスト内包表記の記法：

# [式 for 繰り返し変数 in シーケンス]
# を 通常の for 文で書くと

# a_list = list() # 空のリスト
# for 繰り返し変数 in シーケンス:
#     a_list.append(繰り返し変数を渡して演算した式) 
# a_list
# という形になります。 では、

# [x * 10 for x in [1,2,3,4,5]]
# を fot 文で書き換えるとどのようになりますか？

new_list = list()
for x in [1,2,3,4,5]:
    new_list.append(x)
print(new_list)

# range(10) の要素一つずつに対して100を足したリストを、for 文と リスト内包表記で書いてください。どちらの答えも
# [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
# になります。

# for 
l3 = list()
for x in range(10):
    l3.append(x + 100)
print(l3)
print([x + 100 for x in range(10)])

# list("ABCDE") の要素一つずつに対して "my " を付加したリストを、for 文と リスト内包表記で書いてください。どちらの答えも

# ['my A', 'my B', 'my C', 'my D', 'my E']

l4 = []
for s in list("ABCDE"):
    l4.append("my "+ s)
print(l4)

print(["my " + s for s in list("ABCDE")])

# P235 のリスト内包表記の例、を写経して実行してください。
# pass 

# P237 のリスト内包表記が返すリスト、を写経してプリントしてください。
# pass 

# P237 のリスト内包表記が返すリスト、をfor 文に書き換えてください。
monk_fish_team = [158, 157, 163, 157, 145]
mean = sum(monk_fish_team)/len(monk_fish_team)
print([(h-mean)**2 for h in monk_fish_team])

l5 = list()
for h in monk_fish_team:
    l5.append((h-mean)**2)
print(l5)



# P237 のリスト内包表記で書き換えたコード、を写経してプリントしてください。
# pass 



