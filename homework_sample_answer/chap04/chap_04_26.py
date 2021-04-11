# 1. P200 の zip()関数を使う、を写経してプリントしてください
# pass 

# 2. 以下のリスト2つを使って、new_list と同じリストを作ってください.
first_names = ['Luelle', 'Kendre', 'Florry', 'Aidan', 'Desiree', 'Shawnee', 'Ernesta', 'Latrina', 'Teddi', 'Annie']
last_names = ['Shevels', 'Worts', 'Felix', 'Beetham', 'Kubacki', 'Torbett', 'Kinsley', 'Doggerell', 'McGarry', 'Gile']

#new_list = [['Luelle', 'Shevels'], ['Kendre', 'Worts'], ['Florry', 'Felix'], ['Aidan', 'Beetham'], ['Desiree', 'Kubacki'], ['Shawnee', 'Torbett'], ['Ernesta', 'Kinsley'], ['Latrina', 'Doggerell'], ['Teddi', 'McGarry'], ['Annie', 'Gile']]

# ヒント：P188の append も使いましょう

new_list = list() 
for f, n in zip(first_names, last_names):
    new_list.append([f, n])

print(new_list)