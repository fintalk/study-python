# 変数 fruits_list に 以下のリストを代入する
# ['Boysenberry', 'Blackberry', 'Nectarine', 'Chico', 'Honeyberry', 'Apple', 'Black', 'Yuzu', 'fruit', 'Kumquat'] 
fruits_list = ['Boysenberry', 'Blackberry', 'Nectarine', 'Chico', 'Honeyberry', 'Apple', 'Black', 'Yuzu', 'fruit', 'Kumquat'] 

# fruits_list を print する
print(fruits_list)

# for 文の記法を使って fruits_list の要素を１つずつPrintする
for fruit in fruits_list:
    print(fruit)

# 変数 num_list に 0~10 の数値リストを代入する
num_list = [0,1,2,3,4,5,6,7,8,9,10]

# num_list を print する
for num in num_list:
    print(num)

# for 文の記法を使ってnum_list の要素を１つずつに、10足してPrintする
for num in num_list:
    print(num+10)

# num_listの平均をPrintする
print(sum(num_list) / len(num_list))