# P182の昇順に並べ替える、を写経してプリントして下さい
# pass 
# 下記のリストをソートして下さい。
names = ['Thomasin', 'Virginie', 'Bridie', 'Elbertine', 'Axe', 'Mandie', 'Freddie', 'Petra', 'Charlot', 'Trula']

names.sort()
print(names)

# P183の降順に並べ替える、を写経してプリントして下さい
# pass 

# １〜１０のリストをrange関数で作って降順にソートしてプリント下さい
intlist = list(range(1,11))
intlist.reverse()
print(intlist)

# 上記リスト names を降順にソートしてプリントして下さい
names.sort(reverse=True)
print(names)

# P184の、タプルのリストを作る、戦車の諸元を足して返す関数 evaluate_tankdata()、各戦車の強さを表示する、P185の戦車の強さでソートするを写経して実行して下さい
# pass 

test_score = [
    {'first_name': 'Carling', 'Language': 85, 'Mathematics': 20, 'Music': 48, 'Science': 6}, 
    {'first_name': 'Bengt', 'Language': 23, 'Mathematics': 46, 'Music': 26, 'Science': 50}, 
    {'first_name': 'Calla', 'Language': 63, 'Mathematics': 11, 'Music': 97, 'Science': 22}, 
    {'first_name': 'Lanie', 'Language': 23, 'Mathematics': 1, 'Music': 100, 'Science': 96}, 
    {'first_name': 'Zebulon', 'Language': 15, 'Mathematics': 68, 'Music': 35, 'Science': 68}]

# 辞書型の引数を1つ引き取ってテスト結果の平均値を返すget_score() を作成して下さい。
def get_score(d):
    mean = (d["Language"] + d["Mathematics"] + d["Music"] + d["Science"] ) / 4 
    # print(d["first_name"], mean) # 確認用
    return mean

# 関数 get_score を使って test_score を降順に並べ替えてください。
test_score.sort(key=get_score, reverse=True)
print(test_score)

