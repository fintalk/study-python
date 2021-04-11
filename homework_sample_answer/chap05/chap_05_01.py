# P231 のリストのメソッドを使った処理、を写経して実行してください
# pass 

# P231 の関数を使った処理、を写経して実行してください
# pass 

# P232 の Pythonの文と式、を読んで文と式の違いをメモしてください。
# pass 

# P233 の lambda 式について、まとめてメモしてください。
# pass 

# chap_04_14.md で回答した、P184の eveluate_tankdata() 関数を読み返してください
# その上で、P234 の ソート順の指定に lambda 式を使う、を写経して実行してください。
# pass 

# P234 の sorted() 関数による置き換え、を写経して実行してください
# pass 

# chap_04_14.md の test_score をlambda 式を使って平均値で降順に並べ替えてください。

test_score = [
        {'first_name': 'Carling', 'Language': 85, 'Mathematics': 20, 'Music': 48, 'Science': 6}, 
        {'first_name': 'Bengt', 'Language': 23, 'Mathematics': 46, 'Music': 26, 'Science': 50}, 
        {'first_name': 'Calla', 'Language': 63, 'Mathematics': 11, 'Music': 97, 'Science': 22}, 
        {'first_name': 'Lanie', 'Language': 23, 'Mathematics': 1, 'Music': 100, 'Science': 96}, 
        {'first_name': 'Zebulon', 'Language': 15, 'Mathematics': 68, 'Music': 35, 'Science': 68}]

test_score.sort(key=lambda d: (d["Language"]+d["Mathematics"]+d["Music"]+d["Science"]/4), reverse=True)
print(test_score)

