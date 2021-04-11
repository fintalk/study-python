# break文とはどういう制御をする文法ですか？
# pass 

# continue文とはどういう制御をする文法ですか？
# pass 

# P142 のじゃんけんプログラムを写経して実行して下さい
# pass 

# じゃんけんプログラムの while True は何のために記述されているのですか？
# pass 

# P142 のじゃんけんプログラムの全体を文章で説明して下さい。
# pass 

data_list = [
    {'class': 'classC', 'first_name': 'Candice', 'gender': 'Female','score': '89'},
    {'class': 'classA', 'first_name': 'Cari', 'gender': 'Female', 'score': '45'},
    {'class': 'classA', 'first_name': 'Meggi', 'gender': 'Female', 'score': '75'},
    {'class': 'classC', 'first_name': 'Berti', 'gender': 'Female', 'score': '54'},
    {'class': 'classA', 'first_name': 'Selby', 'gender': 'Male', 'score': '36'},
    {'class': 'classB', 'first_name': 'Enrichetta','gender': 'Female','score': '5'},
    {'class': 'classA', 'first_name': 'Tamiko', 'gender': 'Female', 'score': '45'},
    {'class': 'classC', 'first_name': 'Caren', 'gender': 'Female', 'score': '23'},
    {'class': 'classC', 'first_name': 'Paulie', 'gender': 'Female', 'score': '62'},
    {'class': 'classB', 'first_name': 'Lionello', 'gender': 'Male', 'score': '45'}
    ]

# 上から順に first_nameと score をプリントしていくが、'classB' のデータが来た場合、そこでストップする
print("問題6-1", "-"*10)
for data in data_list:
    cls = data["class"]
    name = data["first_name"]
    score = data["score"]
    if cls == 'classB':
        break 
    print(name, score)

    
# 上から順に first_nameと score をプリントしていくが、'classB' のデータが来た場合、プリントをスキップして続ける
print("問題6-2", "-"*10)
for data in data_list:
    cls = data["class"]
    name = data["first_name"]
    score = data["score"]
    if cls == 'classB':
        continue
    print(name, score)

# classA と classC のスコア平均をそれぞれ出して下さい
print("問題6-3", "-"*10)

score_a = 0
count_a = 0
score_c = 0
count_c = 0


for data in data_list:
    cls = data["class"]
    score = data["score"]
    if cls == 'classA':
        score_a = score_a + int(score)
        count_a = count_a + 1 
    elif cls == 'classC':
        score_c = score_c + int(score)
        count_c = count_c + 1 
    else:
        continue

print("class A の平均は", score_a / count_a)
print("class C の平均は", score_c / count_c)


# Female と Male のスコア平均をそれぞれ出して下さい。
print("問題6-4", "-"*10)

score_male = 0
count_male = 0
score_female = 0
count_female = 0


for data in data_list:
    gender = data["gender"]
    score = data["score"]
    if gender == 'Female':
        score_female = score_female + int(score)
        count_female = count_female + 1 
    elif gender == 'Male':
        score_male = score_male + int(score)
        count_male = count_male + 1 
    else:
        continue

print("female の平均は", score_female / count_female)
print("male の平均は", score_male / count_male)

"""
閑話休題：
最後の問題は、昨今のGender問題を鑑み、今後 male/female以外の答えもありえると思い、if else ではなく elif でつなげました。ま。
"""

    